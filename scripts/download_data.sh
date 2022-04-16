#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data

# mkdir -p $data

tools=$base/tools

# TODO: link default training data for easier access

mkdir -p $data/wikitext-2

for corpus in train valid test; do
    absolute_path=$(realpath $tools/pytorch-examples/word_language_model/data/wikitext-2/$corpus.txt)
    ln -snf $absolute_path $data/wikitext-2/$corpus.txt
done

# TODO: download a different interesting data set!

mkdir -p $data/pride

mkdir -p $data/pride/raw

# wget https://www.gutenberg.org/files/52521/52521-0.txt
wget https://www.gutenberg.org/files/1342/1342-0.txt
mv 1342-0.txt $data/pride/raw/text.txt

# TODO: preprocess slightly

cat $data/pride/raw/text.txt | python $base/scripts/preprocess_raw.py > $data/pride/raw/text.cleaned.txt

# TODO: tokenize, fix vocabulary upper bound

cat $data/pride/raw/text.cleaned.txt | python $base/scripts/preprocess.py --vocab-size 5000 --tokenize --lang "en" --sent-tokenize > \
    $data/pride/raw/text.preprocessed.txt

# TODO: split into train, valid and test

# head -n 440 $data/grimm/raw/tales.preprocessed.txt | tail -n 400 > $data/grimm/valid.txt
# head -n 840 $data/grimm/raw/tales.preprocessed.txt | tail -n 400 > $data/grimm/test.txt
# tail -n 3075 $data/grimm/raw/tales.preprocessed.txt | head -n 2955 > $data/grimm/train.txt

head -n 750 $data/pride/raw/text.preprocessed.txt | tail -n 700 > $data/pride/valid.txt
head -n 1400 $data/pride/raw/text.preprocessed.txt | tail -n 700 > $data/pride/test.txt
tail -n 7000 $data/pride/raw/text.preprocessed.txt | head -n 6000 > $data/pride/train.txt
