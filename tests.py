import unittest

from first_largest import *

class FirstLargest(unittest.TestCase):

    def test_largest_is_first(self):
        given = [5,3,4,1,2]
        expect = 5
        got = largest_element(given)
        self.assertEqual(got, expect)
   
    def test_largest_is_first_with_loc(self):
        given = [5,3,4,1,2]
        expect = 5, 0
        got = largest_element(given, loc=True)
        self.assertEqual(got, expect)


if __name__ == '__main__':
    unittest.main()
