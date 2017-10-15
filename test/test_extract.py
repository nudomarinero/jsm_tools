from __future__ import print_function
import sys
import unittest
#import traceback
#import os

# Append the path of the module to the syspath
sys.path.append('..')
from jsm import extract

class TestExtract(unittest.TestCase):
    """
    Tests for the extract module
    """
    def test_parser(self):
        """
        See https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module
        """
        parsed = extract.parse_args(["image.fits"])
        self.assertEqual(parsed.img, "image.fits")


if __name__ == '__main__':
    unittest.main()
