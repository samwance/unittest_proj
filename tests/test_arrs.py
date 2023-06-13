import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_get_out_of_bounds(self):
        self.assertEqual(arrs.get([1, 2, 3], 10, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_my_slice_out_of_bounds(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 10), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -10, 2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, 2), [])
        self.assertEqual(arrs.my_slice([], -10, 2), [])
