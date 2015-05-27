import unittest
from grab import Patent


class PatentTest(unittest.TestCase):
    """Test the retrieval of patent characteristics."""
    def setUp(self):
        self.num = '7654321'

    def test_patent_response(self):
        patent = Patent(self.num)

        # Test returned Title
        expected = "Formation fluid sampling apparatus and methods"
        self.assertEqual(patent.get_title(), expected)
