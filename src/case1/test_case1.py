#!/usr/bin/env python

import unittest
from case1 import hello

# TestCase1 is a class that inherits from unittest.TestCase
class TestCase1(unittest.TestCase):
    def test_hello(self):
        assert hello("hello") == "hello"


if __name__ == "__main__":
    unittest.main()
