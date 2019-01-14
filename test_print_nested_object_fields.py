import unittest
from print_nested_object_fields import convert_obj_values_in_dict

class TestNestedObjectFields(unittest.TestCase):

    def test_bad_data_with_string(self):
        with self.assertRaises(ValueError):
            convert_obj_values_in_dict("")

    def test_bad_data_with_int(self):
        with self.assertRaises(ValueError):
            convert_obj_values_in_dict(12)        

    

if __name__ == '__main__':
    unittest.main()  