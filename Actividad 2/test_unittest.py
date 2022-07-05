import unittest

class testUnittest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(4,4)

    def test_notequal(self):
        self.assertNotEqual(4,6)

    def test_in(self):
        self.assertIn(9,[0,4,9,8,7])

    def test_notin(self):
        self.assertNotIn(6,[0,4,9,8,7])

    def test_lessequal(self):
        self.assertLessEqual(3,6)
