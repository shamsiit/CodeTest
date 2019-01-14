import unittest
from leaset_common_ancestor import lca_driver

class TestLeastCommonAncestor(unittest.TestCase):

    def test_empty(self):
        self.assertAlmostEqual(lca_driver(None, None, None), None)

    def test_bad_data_with_string(self):
        with self.assertRaises(ValueError):
            lca_driver("", "", "")

    def test_bad_data_with_int(self):
        with self.assertRaises(ValueError):
            lca_driver(12, 22, 33)        

    

if __name__ == '__main__':
    unittest.main()  