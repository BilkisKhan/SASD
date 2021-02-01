

import unittest
# import sys
# print(sys.path)

from src.roman_numeral_converter import RomanNumeralConverter


class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.my_converter = RomanNumeralConverter()

    def test_converts_one(self):
        self.assertEqual(self.my_converter.convert(1), "I")

    def test_converts_two(self):
        self.assertEqual(self.my_converter.convert(2), "II")

    def test_converts_three(self):
        self.assertEqual(self.my_converter.convert(3), "III")

    def test_converts_ten(self):
        self.assertEqual(self.my_converter.convert(10), "X")

    def test_converts_twenty(self):
        self.assertEqual(self.my_converter.convert(20), "XX")

    def test_converts_twentyTwohundred(self):
        self.assertEqual(self.my_converter.convert(2200), "MMCC")

    def test_converts_twentyTwohundred13(self):
        self.assertEqual(self.my_converter.convert(2213), "MMCCXIII")

    def test_converts_thirthundred(self):
        self.assertEqual(self.my_converter.convert(3000), "MMM")


if __name__ == '__main__':
    unittest.main()
