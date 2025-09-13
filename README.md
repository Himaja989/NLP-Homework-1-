CS5760 NLP Homework 1

Student: Himaja Arabati ( 700772489 )

Description

This repository contains Python solutions for Homework 1 of CS5760 (Natural Language Processing), covering:

Q1 – Regex: ZIP codes, non-capitalized words, numbers, email variants, interjections, and lines ending with ?.
Q2 – Tokenization: Naïve, manual, and spaCy tokenization; multiword expressions (MWEs).
Q3 – BPE: Manual merges and mini-BPE learner on a toy corpus; subword segmentation.
Q4 – Edit Distance: Minimum edit distance between Sunday → Saturday under different cost models.

Files
File	Description
regex_test.py	Q1 – Regex tasks
tokenization_q2.py	Q2 – Tokenization
bpe_q3.py	Q3 – BPE tasks
edit_distance_q4.py	Q4 – Edit Distance
homework1_nlp.py	Optional combined file for all questions
Dependencies
python3 -m pip install spacy numpy
python3 -m spacy download en_core_web_sm

Usage

Run each question separately:

python3 regex_test.py
python3 tokenization_q2.py
python3 bpe_q3.py
python3 edit_distance_q4.py


Or run all together:

python3 homework1_nlp.py

Highlights

Regex handles token boundaries, optional parts, and disjunctions.

Tokenization handles punctuation, clitics, and MWEs.

BPE reduces OOV problems and captures meaningful subwords.

Edit Distance demonstrates effects of different operation costs.
