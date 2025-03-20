# lab_test.py

import unittest
import inspect  # Importing inspect module for checking function parameters

# Attempting to import the count_vowels function from lab.py
try:
    from src.main.lab import count_vowels
except ImportError:
    raise ImportError("The function name or file name is incorrect. Please ensure that the function name is 'count_vowels' and it's in the 'lab.py' file.")


class TestCountVowels(unittest.TestCase):
    def test_function_parameters(self):
        # Getting the parameters of the count_vowels function
        params = inspect.signature(count_vowels).parameters
        # Checking if the function has exactly one parameter
        self.assertEqual(len(params), 1)
        # Checking if the parameter is named 'string'
        self.assertIn('string', params)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello, World!"), 3)
        self.assertEqual(count_vowels("Python is awesome"), 6)
        self.assertEqual(count_vowels(""), 0)

if __name__ == "__main__":
    unittest.main()
