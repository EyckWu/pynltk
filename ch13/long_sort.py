#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from nltk.book import *

V = set(text1)
long_words = [w for w in V if len(w) > 15]

print(long_words)

sorted(long_words)

print(long_words)