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

		cratz_instance = Cratz(first_word, second_word)
		self.assertTrue(cratz_instance.is_contained())

		cratz_instance = Cratz(second_word, first_word)
		self.assertFalse(cratz_instance.is_contained())

	def test_levenshtein_distance(self):

		first_word = '今日はいい天気だ'
		second_word = '今日いい天気だ'

		c = Cratz(first_word, second_word)
		self.assertEqual(c.levenshtein_distance(), 1)

	def test_norm_levenshtein_distance(self):

		first_word = '今日はいい天気だよね'
		second_word = '今日いい天気だよね'

		c = Cratz(first_word, second_word)
		self.assertEqual(c.levenshtein_distance(normalized=True), 0.1)

