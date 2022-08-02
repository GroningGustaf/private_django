# ---- Description ---- #
# This file is meant to contain very simple functions and unitTests that assert based on those functions.
# Nothing here is complicated, the point it to be able to use the test cases in a Github Action
# as a part of our CI/CD workflow.

import unittest

def hello():
    print("Hello world!")

def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

class testAddition(unittest.TestCase):
    def testAdditionSuccess(self):
        actual = addition(3, 8)
        expected = 11
        self.assertEqual(actual, expected)

    def testAdditionFailed(self):
        actual = addition(3, 8)
        expected = 13 # incorrect
        self.assertEqual(actual, expected)

# To run unittests - python3 -m unittest simple_functions.py