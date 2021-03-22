# ADAPET #

This repository contains the official code for the paper: "Improving and Simplifying Pattern Exploiting Training" (link coming soon).

The model improves and simplifies [PET](https://arxiv.org/abs/2009.07118) with a decoupled label objective and label-conditioned MLM objective. 


## Model ## 

<img src="img/ADAPET_update.png" width="400" height="300"/> <img src="img/LCMLM_update.png" width="420" height="300"/>
                       **Decoupled Label Loss                                                Label Conditioned Masked Language Modelling**

## Setup ##

Setup environment by running `source bin/init.sh`. This will 

- Download the [FewGLUE](https://github.com/timoschick/fewglue) and [SuperGLUE](https://super.gluebenchmark.com/tasks) datasets in `data/fewglue/{task}` and `data/superglue/{task}` respectively. 
- Install and setup environment with correct dependencies.

## Training  ##

First, create a config JSON file with the necessary hyperparameters. For reference, please see `config/BoolQ.json`.

Then, to train the model, run the following commands:
```
sh bin/setup.sh
sh bin/train.sh {config_file}
```

The output will be in the experiment directory `exp_out/fewglue/{task_name}/albert-xxlarge-v2/{timestamp}/`. Once the model has been trained, the following files can be found in the directory:
```
exp_out/fewglue/{task_name}/albert-xxlarge-v2/{timestamp}/
    |
    |__ best_model.pt
    |__ dev_scores.json
    |__ config.json
    |__ dev_logits.npy
    |__ src
```

To aid reproducibility, we provide the JSON files to replicate the paper's results at `config/{task_name}.json`.

## Evaluation ## 

To evaluate the model on the SuperGLUE dev set, run the following command:
```
sh bin/dev.sh exp_out/fewglue/{task_name}/albert-xxlarge-v2/{timestamp}/
```
The dev scores can be found in `exp_out/fewglue/{task_name}/albert-xxlarge-v2/{timestamp}/dev_scores.json`.


To evaluate the model on the SuperGLUE test set, run the following command.
```
sh bin/test.sh exp_out/fewglue/{task_name}/albert-xxlarge-v2/{timestamp}/
```
The generated predictions can be found in `exp_out/fewglue/{task_name}/albert-xxlarge-v2/{timestamp}/test.json`.

## Contact ##

For any doubts or questions regarding the work, please contact Derek ([dtredsox@cs.unc.edu](mailto:dtredsox+adapet@cs.unc.edu)) or Rakesh ([rrmenon@cs.unc.edu](mailto:rrmenon+adapet@cs.unc.edu)). For any bug or issues with the code, feel free to open a GitHub issue or pull request.
