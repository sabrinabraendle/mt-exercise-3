#! /bin/bash

scripts=`dirname "$0"`
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools
samples=$base/samples

mkdir -p $samples

num_threads=4
device=""

(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python3 generate.py \
        --data $data/pride \
        --words 100 \
        --checkpoint $models/model_00.pt \
        --outf $samples/sample_00 \
        --input "you are astonished"
)
