# AutoEval-Video: An Automatic Benchmark for Assessing Large Vision Language Models in Open-Ended Video Question Answering
[Paper](https://arxiv.org/abs/2311.14906), [Leaderboard](https://huggingface.co/spaces/khhuiyh/AutoEval-Video_LeaderBoard)

AutoEval-Video is a comprehensive and challenging benchmark to assess the capabilities of large vision-language models. The highlights of AutoEval-Video include:
- AutoEval-Video constructs open-ended video-questions across 9 skill dimensions, addressing capabilities of perception, comprehension, and generation.
- AutoEval-Video contains newly collected videos from YouTube that cover over 40 distinct themes.
- Unique evaluation rules are annotated for every instance in AutoEval-Video, enabling accurate assessments by an LLM-based automatic evaluator.
<p align="center">
  <b><em>Examples of AutoEval-Video.</em></b>
  <img src="https://github.com/Xiuyuan-Chen/AutoEval-Video/blob/main/figs/cases.png"/>
</p>
<br>
<p align="center">
  <b><em>Automatic Evaluation Process in AutoEval-Video.</em></b>
  <br>
  <img src="https://github.com/Xiuyuan-Chen/AutoEval-Video/blob/main/figs/overview.png"/>
</p>
<p align="center">
  <b><em>Statistics of AutoEval-Video.</em></b>
</p>
<p align="center">
  <em> The distribution of the skill dimensions and the video themes in AutoEval-Video.</em>
  <img src="https://github.com/Xiuyuan-Chen/AutoEval-Video/blob/main/figs/distribution.png"/>
</p>
<p align="center">
  <em> Statistical information of the video and annotations.</em>
  <img src="https://github.com/Xiuyuan-Chen/AutoEval-Video/blob/main/figs/statistics_table.png"/>
</p>

Please refer to our [paper](https://arxiv.org/abs/2311.14906) for more details about AutoEval-Video.
## News
**[2023.11.28]** [AutoEval-Video Leaderboard](https://huggingface.co/spaces/khhuiyh/AutoEval-Video_LeaderBoard) is released! Welcome to submit your model's results.

**[2023.11.25]** AutoEval-Video is released! Data and evaluation code is available now.

## Leaderboard Submission

Welcome to submit your model results to [AutoEval-Video Leaderboard](https://huggingface.co/spaces/khhuiyh/AutoEval-Video_LeaderBoard). If you discover a case where our rules have resulted in inaccurate evaluation, feel free to raise an issue here to inform us. Any changes in the rules will be reactivated on the leaderboard.

## Run Evaluation

Utilize our evaluation code, [eval.py](https://github.com/Xiuyuan-Chen/AutoEval-Video/eval.py), to generate output.json, which contains your model's evaluation results. Please ensure your model results are prepared in JSON format, similar to [sample.json](https://github.com/Xiuyuan-Chen/AutoEval-Video/blob/main/sample.json). Execute the following evaluation script:

```shell
python3 eval.py --rule_path AutoEval-Video.json --pre_path <path_to_your_model_output> --output_dir ./results --ak <your_api_key>
```

The output.json file contains the accuracy of each instance, while the acc.txt file documents the overall accuracy score. If you discover that any evaluation rules are not comprehensive, please feel free to submit an issue to us. We will refine the rules if there are identified problems. Additionally, the results on the leaderboard will be updated to reflect these changes.


## License
AutoEval-Video is released under Apache License Version 2.0.


## Declaration
All videos of AutoEval-Video are collected from YouTube(https://www.youtube.com), following the Creative Commons License (https://support.google.com/youtube/answer/2797468).

<!-- ## Citation
If you find AutoEval-Video useful for your research and applications, please cite using this BibTeX:
```bibtex

``` -->
