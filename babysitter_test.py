import unittest
from Babysitter import Babysitter

class BabysitterTest(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_class_creation(self):
        self.assertNotEqual(self.babysitter, None)

    def test_charges_for_familyA_without_rate_change(self):
        self.assertEqual(self.babysitter.calculate(17, 22), 75)

    def test_charges_for_familyA_with_rate_change(self):
        self.assertEqual(self.babysitter.calculate(17, 24), 110)
if __name__ == '__main__':
    unittest.main()
