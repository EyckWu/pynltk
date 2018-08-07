#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from nltk.book import *

print(sent7)

print([w for w in sent7 if len(w) < 4])

print([w for w in sent7 if len(w) <= 4])

print([w for w in sent7 if len(w) == 4])

print([w for w in sent7 if len(w) != 4])