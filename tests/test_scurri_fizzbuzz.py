import unittest
from scurrifizzbuzz import scurri_fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(scurri_fizzbuzz.fizzbuzz(2), 2)
        self.assertEqual(scurri_fizzbuzz.fizzbuzz(3), "Three")
        self.assertEqual(scurri_fizzbuzz.fizzbuzz(5), "Five")
        self.assertEqual(scurri_fizzbuzz.fizzbuzz(15), "ThreeFive")







if __name__ == '__main__':
    unittest.main()
