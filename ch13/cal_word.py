#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from nltk.book import *

a = [len(w) for w in text1]
# for a in text1:
#     print(a)
fdist = FreqDist(a)
print(fdist)

keys = fdist.keys()

print(keys)

print(fdist.items())

print(fdist.max())

print(fdist[3])

print(fdist.freq(3))

fdist.plot()
fdist.plot(cumulative = True)
# print(a)