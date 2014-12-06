#!/usr/bin/env python
# -*- coding: utf_8 -*-

"""
Dan O'Day
Robert Hinh
Upasita Jain
Sangmi Shin
Penghao Wang

Purdue University
CNIT499 Natural Language Technologies

Simple count features.
"""

__author__ = "Dan O'Day, Sangmi Shin, Robert Hinh"
__copyright__ = "Copyright 2014, Dan O'Day, Purdue University"
__credits__ = ["Dan O'Day", "Robert Hinh", "Upasita Jain", "Sangmi Shin", "Penghao Wang", "Julia Taylor"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Dan O'Day"
__email__ = "doday@purdue.edu"
__status__ = "Development"


from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'ms', 'prof', 'inc'])


def clean_up(sentences):
    i = 0
    indexes_to_concatenate = []
    cleaned_up_sentence_list = []

    for s in sentences:
        if s.endswith('e.g.') or s.endswith('i.e.') or s.endswith('viz.'):
            indexes_to_concatenate.append(i)
        i += 1

    if len(indexes_to_concatenate) > 0:
        pass
    else:
        return sentences

    return cleaned_up_sentence_list


def count_sentences(email):
    return len(prepare_email(email))


def create_text_from_body(email):
    text = ""
    for line in email.enumerate_lines():
        text += line + ' '
    return text


def prepare_email(email):
    text = create_text_from_body(email)
    sentence_list = split_sentences(text)
    return sentence_list


def split_sentences(text):
    sentence_splitter = PunktSentenceTokenizer(punkt_param)
    sentences = sentence_splitter.tokenize(text)
    cleaned_up_sentences = clean_up(sentences)
    return cleaned_up_sentences