import unittest
from solution import is_valid_parentheses

class TestValidParentheses(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_simple_invalid(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_nested_valid(self):
        self.assertTrue(is_valid_parentheses("{[()]}"))

if __name__ == "__main__":
    unittest.main()
