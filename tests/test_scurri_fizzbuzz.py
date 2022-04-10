import unittest
from scurrifizzbuzz import scurri_fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    """Unit tests for scurri_fizzbuzz.py """

    def test_three_multiples(self):
        for i in [3, 12, 33, 51, 81]:
            self.assertEqual(scurri_fizzbuzz.fizzbuzz(i), "Three")


    def test_five_multiples(self):
        for i in [5, 25, 55, 70, 95]:
            self.assertEqual(scurri_fizzbuzz.fizzbuzz(i), "Five")


    def test_fifteen_multiples(self):
        for i in [15, 45, 60, 75, 90]:
            self.assertEqual(scurri_fizzbuzz.fizzbuzz(i), "ThreeFive")

    def test_non_threefive_multiples(self):
        for i in [1, 4, 43, 67, 82]:
            self.assertEqual(scurri_fizzbuzz.fizzbuzz(i), i)

if __name__ == '__main__':
    unittest.main()
