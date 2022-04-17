# MT Exercise 3: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model).

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/emmavdbold/mt-exercise-3
    cd mt-exercise-3

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:
* Make sure to first delete the 'data' folder again in order to reproduce the steps we took for downloading


    ./scripts/download_data.sh

Train the models:
* The command `mkdir -p $models` is already commented out, so you can start the training directly and do not need to change this section of the script
* In order to obtain all 5 models, change the settings the following way:
  * --dropout 0; --save $models/model_00.pt
  * --dropout 0.3; --save $models/model_03.pt
  * --dropout 0.5; --save $models/model_05.pt
  * --dropout 0.7; --save $models/model_07.pt
  * --dropout 1; --save $models/model_10.pt


    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

In order to create the tables and the charts, cd into the `scripts` directory and run `python3 table_chart_creator.py`.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh
