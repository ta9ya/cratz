#!/usr/bin/env python
# -*- encoding:utf-8 -*-


from cratz import Cratz

first_word = '本田未央'
second_word = '高垣　楓'

c = Cratz(first_word, second_word)
print(c.levenshtein_distance(normalized=True))
