import unittest
from babysitter import Babysitter

class BabysitterTest(unittest.TestCase):

    def setUp(self):
        self.babysitter = Babysitter()

    def test_class_creation(self):
        self.assertNotEqual(self.babysitter, None)

    def test_charges_for_family_A_without_rate_change(self):
        self.assertEqual(self.babysitter.calculate(17, 22, "A"), 75)

    def test_charges_for_family_A_with_rate_change_before_midnight(self):
        self.assertEqual(self.babysitter.calculate(17, 24, "A"), 110)

    def test_charges_for_family_A_with_shift_going_beyond_midnight(self):
        self.assertEqual(self.babysitter.calculate(17, 1, "A"), 130)

    def test_charges_for_family_B_without_rate_change(self):
        self.assertEqual(self.babysitter.calculate(17, 21, "B"), 48)

    def test_charges_for_family_B_with_rate_change_before_midnight(self):
        self.assertEqual(self.babysitter.calculate(18, 24, "B"), 64)

if __name__ == '__main__':
    unittest.main()
