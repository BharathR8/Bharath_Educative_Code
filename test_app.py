import unittest
from app import kebab_to_str

class TestKebabToStr(unittest.TestCase):
    def test_basic_kebab(self):
        self.assertEqual(kebab_to_str('hello-world'), 'Hello World')

    def test_single_word(self):
        self.assertEqual(kebab_to_str('python'), 'Python')

    def test_multiple_words(self):
        self.assertEqual(kebab_to_str('this-is-a-test'), 'This Is A Test')

    def test_empty_string(self):
        self.assertEqual(kebab_to_str(''), '')

    def test_trailing_dash(self):
        self.assertEqual(kebab_to_str('end-'), 'End ')

    def test_leading_dash(self):
        self.assertEqual(kebab_to_str('-start'), ' Start')

    def test_multiple_consecutive_dashes(self):
        self.assertEqual(kebab_to_str('a--b'), 'A  B')

    def test_all_uppercase(self):
        self.assertEqual(kebab_to_str('HELLO-WORLD'), 'Hello World')

import unittest
from app import kebab_to_str

class TestKebabToStr(unittest.TestCase):
    """Unit tests for kebab_to_str utility function."""

    def test_basic_kebab(self):
        """Should convert a simple kebab-case string to capitalized words."""
        self.assertEqual(kebab_to_str('hello-world'), 'Hello World')

    def test_single_word(self):
        """Should capitalize a single word."""
        self.assertEqual(kebab_to_str('python'), 'Python')

    def test_multiple_words(self):
        """Should handle multiple words in kebab-case."""
        self.assertEqual(kebab_to_str('this-is-a-test'), 'This Is A Test')

    def test_empty_string(self):
        """Should return empty string for empty input."""
        self.assertEqual(kebab_to_str(''), '')

    def test_trailing_dash(self):
        """Should translate trailing dash to trailing space."""
        self.assertEqual(kebab_to_str('end-'), 'End ')

    def test_leading_dash(self):
        """Should translate leading dash to leading space."""
        self.assertEqual(kebab_to_str('-start'), ' Start')

    def test_multiple_consecutive_dashes(self):
        """Should translate consecutive dashes to consecutive spaces."""
        self.assertEqual(kebab_to_str('a--b'), 'A  B')

    def test_all_uppercase(self):
        """Should handle all-uppercase input and capitalize properly."""
        self.assertEqual(kebab_to_str('HELLO-WORLD'), 'Hello World')

    def test_numbers_and_symbols(self):
        """Should retain numbers and symbols in the string."""
        self.assertEqual(kebab_to_str('test-123-case'), 'Test 123 Case')
        self.assertEqual(kebab_to_str('hello-@-world'), 'Hello @ World')

    def test_non_ascii_characters(self):
        """Should retain non-ASCII characters in conversion."""
        self.assertEqual(kebab_to_str('café-münsterländer'), 'Café Münsterländer')

if __name__ == '__main__':
    unittest.main()