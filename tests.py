import unittest
from internal.counter import Counter

class TestCounter(unittest.TestCase):
    def test_empty_string(self):
        counter = Counter("")
        self.assertEqual(counter.count(), 0)
    
    def test_single_word(self):
        counter = Counter("hello")
        self.assertEqual(counter.count(), 1)
    
    def test_multiple_words(self):
        counter = Counter("hello world")
        self.assertEqual(counter.count(), 2)
    
    def test_multiple_spaces(self):
        counter = Counter("hello    world")
        self.assertEqual(counter.count(), 2)
    
    def test_leading_trailing_spaces(self):
        counter = Counter("   hello world   ")
        self.assertEqual(counter.count(), 2)
    
    def test_tabs_and_newlines(self):
        counter = Counter("hello\tworld\n\ntest")
        self.assertEqual(counter.count(), 3)
    
    def test_special_characters(self):
        counter = Counter("hello-world! What's up?")
        self.assertEqual(counter.count(), 4)
    
    def test_unicode_characters(self):
        counter = Counter("こんにちは world")
        self.assertEqual(counter.count(), 2)

if __name__ == '__main__':
    unittest.main()