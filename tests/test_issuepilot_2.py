import unittest

from textkit import truncate


class TestTruncateWidth(unittest.TestCase):
    def test_truncated_text_fits_width_with_suffix(self):
        self.assertEqual(truncate("Hello, open source!", 10), "Hello, ...")
