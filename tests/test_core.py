#!/usr/bin/env python3
# coding:utf8


import unittest

from cratz import Cratz


class TestCratz(unittest.TestCase):

	def test_is_perfect_match(self):

		first_word = '今日は17000円したAir podsの調子が悪い'
		second_word = first_word

		cratz_instance = Cratz(first_word, second_word)

		self.assertTrue(cratz_instance.is_perfect_match())

	def test_is_is_contained(self):

		first_word = '焼肉'
		second_word = '焼肉定食が食べたい'

		cratz_instance = Cratz(first_word, second_word,)

		self.assertTrue(cratz_instance.is_contained())