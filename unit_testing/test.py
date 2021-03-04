import unittest

class ChseckNumbers(unittest.TestCase):
	def test_int_float(self):
		# Will fail if evaluate to false
		self.assertEqual(1, '1.0')


def averate(seq):
	return sum(seq) / len(seq)

class TestAverage(unittest.TestCase):
	def test_zero(self):
		self.assertRaises(ZeroDivisionError, average)

def test_with_zero(self):
	with self.assertRaises(zeroDivisionError):
		average([])


if __name__ == "__main__":
	unittest.main()

if __name__ == "__main__":
	unittest.main()
