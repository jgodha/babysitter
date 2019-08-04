import unittest
from Babysitter import Babysitter

class BabysitterTest(unittest.TestCase):

    def test_hello_world(self):
        babysitter = Babysitter()
        self.assertNotEqual(babysitter, None)

if __name__ == '__main__':
    unittest.main()
