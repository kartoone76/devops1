'''Defines some geometric functions'''
import unittest

def square(a_n):
    '''Takes in a number n, returns the square of n'''
    return a_n*a_n

class Test(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
  