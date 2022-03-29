import unittest
from main import get_doc_shelf, get_doc_shelf, add_new_doc
from unittest.mock import patch


class TestFunctions(unittest.TestCase):

    @patch('builtins.input', return_value="10006")
    def test_get_doc_shelf(self, mock_input):
        result = get_doc_shelf()
        self.assertEqual(result, "2")

    @unittest.expectedFailure
    @patch('builtins.input', return_value="100061")
    def test_get_doc_shelf_2(self, mock_input):
        result = get_doc_shelf()
        self.assertEqual(result, "2")

    def test_add_new_doc(self):
        result = add_new_doc(101, "passport", "pom-pom", 2)
        self.assertEqual(result, 2)

    def test_add_new_doc2(self):
        result = add_new_doc(101, "passport", "pom-pom", 'a')
        self.assertEqual(result, 'a')


if __name__ == '__main__':
    unittest.main()
