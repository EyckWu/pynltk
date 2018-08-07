#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from nltk.book import *

fdist1 = FreqDist(text1)
print(fdist1)

vocabulary1 = fdist1.keys()
print(vocabulary1[:50])

print(fdist1['whale'])

fdist1.plot(50, cumulative = True)

