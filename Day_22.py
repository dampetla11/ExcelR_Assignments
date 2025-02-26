# -*- coding: utf-8 -*-
"""Day-22

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17bZTixFsnpoNNVzbjha9v2T4FalaGYoG
"""
#Write a Python script to perform part-of-speech tagging on the sentence: 'NLP is amazing and fun to learn.' using SpaCy.

import spacy

nlp = spacy.load("en_core_web_sm")
e
sentence = "NLP is amazing and fun to learn."

doc = nlp(sentence)

print(f"{'Token':<10}{'POS':<10}{'Tag'}")
print("-" * 30)
for token in doc:
    print(f"{token.text:<10}{token.pos_:<10}{token.tag_}")