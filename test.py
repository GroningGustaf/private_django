import unittest
from ci_cd.simple_functions import *
class testAddition(unittest.TestCase):
    def testAdditionSuccess(self):
        actual = addition(3, 8)
        expected = 11
        self.assertEqual(actual, expected)

    def testAdditionFailed(self):
        actual = addition(3, 9)
        expected = 12
        self.assertEqual(actual, expected)

    def testSimpleTest(self):
        a = 4
        b = 7
        self.assertEqual(11, (a + b))

# To run unittests - python3 -m unittest simple_functions.py