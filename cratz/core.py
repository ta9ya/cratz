# Insert your code here. 


class Cratz:

	def __init__(self, first_word, second_word):
		"""
		:param first_word: str
		:param second_word: str

		:return
		"""

		self.first_word = first_word
		self.second_word = second_word

	def is_perfect_match(self):
		"""

		:return: bool
		"""

		return self.first_word == self.second_word

	def is_contained(self, reverse=False):
		"""
		:param reverse : bool
			The default case is "first is contained second."
			Reverse param is True,

		:return: bool
		"""

		if not reverse:
			return self.first_word in self.second_word
		else:
			return self.second_word in self.first_word

	def levenshtein_distance(self, normalized=False):
		"""
		calculate the levenshtein distance.

		:param normalized : bool

		:return : int
			Case of normalized=False, the distance is returned as a int.
		:return : float
			Case of normalized=True, the distance is returned as a float.
			(0 <= distance <= 1)
		"""

		s1 = self.first_word
		s2 = self.second_word

		if len(s1) > len(s2):
			s1, s2 = s2, s1

		distances = range(len(s1) + 1)

		for index2, char2 in enumerate(s2):
			newDistances = [index2 + 1]

			for index1, char1 in enumerate(s1):

				if char1 == char2:
					newDistances.append(distances[index1])
				else:
					newDistances.append(1 + min((distances[index1],
					                             distances[index1 + 1],
					                             newDistances[-1])))
			distances = newDistances

		if normalized:
			return distances[-1] / len(s2)
		else:
			return distances[-1]
