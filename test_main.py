import os
import tempfile
import unittest
from main import (
    count_words_bruteforce,
    count_words_optimized,
    most_frequent_word
)

class TestWordCount(unittest.TestCase):
    SAMPLE = "Hello, hello! WORLD world."

    def setUp(self):
        # create a temporary file with SAMPLE
        self.tmp_file = tempfile.NamedTemporaryFile(
            mode='w+', delete=False, encoding='utf-8'
        )
        self.tmp_file.write(self.SAMPLE)
        self.tmp_file.flush()
        # save the path for use in tests
        self.file_path = self.tmp_file.name

    def tearDown(self):
        # clean up
        self.tmp_file.close()
        os.unlink(self.file_path)

    def test_null_input(self):
        # calling with None should raise TypeError
        with self.assertRaises(TypeError):
            count_words_bruteforce(None)
        with self.assertRaises(TypeError):
            count_words_optimized(None)

    def test_empty_file(self):
        # overwrite with empty content
        with open(self.file_path, 'w', encoding='utf-8'):
            pass
        self.assertEqual(count_words_bruteforce(self.file_path), {})
        self.assertEqual(count_words_optimized(self.file_path), {})

    def test_invalid_path(self):
        # a non-existent filename
        with self.assertRaises(FileNotFoundError):
            count_words_bruteforce("does_not_exist.txt")
        with self.assertRaises(FileNotFoundError):
            count_words_optimized("does_not_exist.txt")

    def test_valid_counts(self):
        # we wrote "Hello, hello! WORLD world." → hello:2, world:2
        expected = {'hello': 2, 'world': 2}
        bf = count_words_bruteforce(self.file_path)
        opt = count_words_optimized(self.file_path)
        self.assertEqual(bf, expected)
        self.assertEqual(opt, expected)

    def test_most_frequent(self):
        counts = {'a': 3, 'b': 5, 'c': 2}
        self.assertEqual(most_frequent_word(counts), ('b', 5))
        # empty dict should return (None, 0)
        self.assertEqual(most_frequent_word({}), (None, 0))

if __name__ == '__main__':
    unittest.main()
