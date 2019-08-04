import unittest
from Babysitter import Babysitter

class BabysitterTest(unittest.TestCase):

    def test_class_creation(self):
        babysitter = Babysitter()
        self.assertNotEqual(babysitter, None)

    def test_charges_for_familyA_without_rate_change(self):
        babysitter = Babysitter()
        self.assertEqual(babysitter.calculate(17, 22), 75)

if __name__ == '__main__':
    unittest.main()
