"""Test file for testing the functions in main.py file"""


import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)
from main import count_vowels  # nopep8 pylint: disable=wrong-import-position


class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def test_count_vowels_empty_string(self):
        """Tests count_vowels with an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """Tests count_vowels with a string that contains no vowels."""
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_all_vowels(self):
        """Tests count_vowels with a string that contains all vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_count_vowels_mixed_case(self):
        """Tests count_vowels with a string that contains mixed case letters."""
        self.assertEqual(count_vowels("AbCdeFG"), 2)

    def test_count_vowels_with_numbers(self):
        """Tests count_vowels with a string that contains numbers."""
        self.assertEqual(count_vowels("hello123"), 2)

    def test_count_vowels_with_special_characters(self):
        """Tests count_vowels with a string that contains special characters."""
        self.assertEqual(count_vowels("hello!@#"), 2)


if __name__ == "__main__":
    unittest.main()
