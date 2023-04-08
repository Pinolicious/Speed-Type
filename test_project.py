import project
from project import load_text
import unittest
from unittest.mock import patch
from random import Random


class test_project(unittest.TestCase):

    def test_esc(self):
        assert project.esc(chr(27)) == True
        assert project.esc("KEY_BACKSPACE") == False


    @patch('project.random')
    def test_load_text(self, random):
        self.random = Random(666)
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(load_text(), "Why do Java programmers have to wear glasses? Because they don't C#.")

        self.random = Random(661)
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(load_text(), "One man's crappy software is another man's full-time job.")

        self.random = Random(662)
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(load_text(), "To understand what recursion is, you must first understand recursion.")


    def test_wpm_test(self):
        ...


if __name__ == "__main__":
    unittest.main()