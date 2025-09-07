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

if __name__ == '__main__':
    unittest.main()