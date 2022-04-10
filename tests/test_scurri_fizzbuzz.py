import unittest
from scurrifizzbuzz import scurri_fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_fizzbuzz(self):
        scurri_fizzbuzz.fizzbuzz()



if __name__ == '__main__':
    unittest.main()
