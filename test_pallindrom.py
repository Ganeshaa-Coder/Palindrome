import unittest
from Pallindrom import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        """Test with a simple palindrome."""
        self.assertTrue(is_palindrome("madam"))

    def test_mixed_case_punctuation_palindrome(self):
        """Test with mixed case and punctuation."""
        self.assertTrue(is_palindrome("Race car!"))

    def test_non_palindrome(self):
        """Test with a non-palindrome word."""
        self.assertFalse(is_palindrome("world"))

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertTrue(is_palindrome(""))

    def test_non_alphanumeric(self):
        """Test with only non-alphanumeric characters."""
        self.assertTrue(is_palindrome("!@#$%"))

    def test_single_character(self):
        """Test with a single character."""
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main()
