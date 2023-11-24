# AutoEval-Video: An Automatic Benchmark for Assessing Large Vision Language Models in Open-Ended Video Question Answering
[Paper](), [Project Page](https://github.com/Xiuyuan-Chen/AutoEval-Video), [Leaderboard]()

<p align="center">
  <img src="https://github.com/Xiuyuan-Chen/AutoEval-Video-try/blob/main/overview.png" />
</p>
 
  AutoEval-Video comprises 327 complex open-ended video-question instances that span across nine skill dimensions, which address video-specific perception, comprehension, and generation skills. Please refer to our [paper]() for more details.
## News
**[2023.11.25]** [AutoEval-Video Leaderboard]() is released! You can now utilize GPT-4 to automatically evaluate your own model.

**[2023.11.25]** AutoEval-Video is released! Data and evaluation code is available now.

### Leaderboard Submission

You can submit your model results in [AutoEval-Video Leaderboard]() now. If you discover a case where our rules have resulted in inaccurate evaluation, feel free to raise an issue here to inform us. Any changes in the rules will be reactivated on the leaderboard.

## Offline Evaluation

The evaluation script is provided in [eval.py](https://github.com/Xiuyuan-Chen/AutoEval-Video/eval.py). In order to conform to the script input format, you need to format your model output as JSON format, like [sample.json](). You can use the evaluation script as follows:

```shell
python3 eval.py --rule_path AutoEval-Video.json --pre_path prediction.json --output_dir ./results --ak <your_api_key>
```

After the evaluation is finished, you can obtain the accuracy of each evaluation dimension in 'acc.txt' and also 'output.json' in 'results' folder. And, 'output.json' can be directly submitted to [AutoEval-Video Leaderboard]().


## License
AutoEval-Video is released under Apache License Version 2.0.


## Declaration
All videos of AutoEval-Video are collected from YouTube(https://www.youtube.com), following the Creative Commons License (https://support.google.com/youtube/answer/2797468).

<!-- ## Citation
If you find AutoEval-Video useful for your research and applications, please cite using this BibTeX:
```bibtex

``` -->