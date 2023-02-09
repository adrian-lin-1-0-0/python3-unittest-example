import unittest
from context import utils

class UtilsTest(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(utils.Say_hello("Adrian"), "Hello Adrian")
        self.assertEqual(utils.Say_hello("Zoey"), "Hello Zoey")


if __name__ == '__main__':
    unittest.main()