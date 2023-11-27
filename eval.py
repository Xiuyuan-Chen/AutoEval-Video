import argparse
import time
from tqdm import tqdm
import random
import json
import os
from openai import OpenAI

def get_response(prompt: str, ak: str) -> str:
    '''
    This is an example reference function for invoking GPT-4. Please modify it according to the actual circumstances.
    '''
    client = OpenAI(api_key=ak)

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def check_judge(answer: str) -> str:

    assert len(answer.split('\n')[0])>=1 , "Answer has no analysis."
    assert answer.split('\n')[-1] in ['0', '1'], "Judge output is not 0 or 1." + answer.split('\n')[-1]
    assert not (answer.split('\n')[0] in ['0', '1']), "Answer has no analysis."

    return answer.split('\n')[-1]


def judge(rule: str, answer: str, ak: str):
    return get_response(rule.replace("[Answer to be judged]:", "[Answer to be judged]: " + answer + '\n'), ak)

def alternate_judge(rule, answer, ak):
    maxtry = 10
    while True:
        try:
            out = judge(rule, answer, ak)
            bitout = check_judge(out)
            return out, bitout
        except Exception as e:
            if maxtry <= 0:
                return None, "0"
            if not isinstance(e, KeyError):
                maxtry -= 1
                print(e)
            else:
                print("Request Error: " + str(e))
            print("Retrying...")
            time.sleep(random.uniform(1, 2))
            continue

def count_lines(file_path: str):
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rule_path', type=str, help='The path of rule file of AutoEval-Video')
    parser.add_argument('--pre_path', type=str, help='The path of output from your model. Please ensure the format is correct.')
    parser.add_argument('--output_dir', type=str, help='The path to save output')
    parser.add_argument('--ak', type=str, help='The apikey for OpenAI API')
    args = parser.parse_args()
    file_path = args.pre_path
    gt_file_path = args.rule_path
    output_path = args.output_dir
    ak = args.ak
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    acc_file_path = os.path.join(output_path, 'acc.txt')
    output_json_path = os.path.join(output_path, 'output.json')

    total_lines = count_lines(file_path)
    overall_acc = []
    output = []
    dimension_correct, dimension_total = dict(), dict()

    id2dimension, id2rule = dict(), dict()
    with open(gt_file_path, 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            id_num = int(data.get('ID'))
            rule = data.get('Rule')
            dimension = data.get('Dimension')
            id2rule[id_num] = rule
            id2dimension[id_num] = dimension
            if dimension not in dimension_correct:
                dimension_correct[dimension] = 0
            if dimension not in dimension_total:
                dimension_total[dimension] = 0
        f.close()

    assert len(dimension_correct) == 9

    if total_lines != count_lines(gt_file_path):
        print("The number of prediction lines is not equal to the number of ground truth lines, which may cause error.")

    with open(file_path, 'r') as f:
        for line in tqdm(f, total=total_lines, unit="lines"):
            data = json.loads(line.strip())
            id_num = int(data.get('ID'))
            rule = id2rule[id_num]
            answer = data.get('prediction')
            dimension = id2dimension[id_num]

            out, bitout = alternate_judge(rule, answer, ak)
            outputdict = {'ID': id_num,
             'prediction': answer, 
             'Dimension': dimension, 
             'Rule': rule, 
             'judge': bitout,
             'reason':out}
            output.append(outputdict)
            if out is not None:
                overall_acc.append(int(bitout))
                dimension_correct[dimension] += int(bitout)
                dimension_total[dimension] += 1
            else:
                print(f"Instance {id_num} judge failed.")
            if len(output) > 10:
                break
        f.close()

    acclines = [f"Overall Accuracy: {round(sum(overall_acc) / max(len(overall_acc), 1) * 100, 1)}%"] + [f"{k}: {round(v / max(1, dimension_total[k]) * 100, 1)}%" for k, v in dimension_correct.items()]
    with open(acc_file_path, 'w') as f:
        f.write('\n'.join(acclines))
    with open(output_json_path, 'w') as f:
        for dict_item in output:
            json_str = json.dumps(dict_item, ensure_ascii=False)
            f.write(json_str + '\n')
    print("Output saved to: ", output_path)

if __name__ == '__main__':
    main()