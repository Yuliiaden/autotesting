import unittest
import boxer

class TestBoxer(unittest.TestCase):
    def test_age(self):
        self.assertGreater(boxer.PitWilder.age, 18, "The boxer is too young.")
        self.assertGreater(boxer.RobeGrant.age, 18, "The boxer is too young.")
        self.assertGreater(boxer.TomyHurd.age, 18, "The boxer is too young.")

    def test_weight(self):
        self.assertGreaterEqual(boxer.PitWilder.weight, 69, "It`s another weight category")
        self.assertLessEqual(boxer.PitWilder.weight, 75, "It`s another weight category")
        self.assertGreaterEqual(boxer.RobeGrant.weight, 69, "It`s another weight category")
        self.assertLessEqual(boxer.RobeGrant.weight, 75, "It`s another weight category")
        self.assertGreaterEqual(boxer.TomyHurd.weight, 69, "It`s another weight category")
        self.assertLessEqual(boxer.PitWilder.weight, 75, "It`s another weight category")

    def test_height(self):
        self.assertGreaterEqual(boxer.PitWilder.height, 180)
        self.assertGreaterEqual(boxer.TomyHurd.height, 180)
        self.assertGreaterEqual(boxer.RobeGrant.height, 180)

unittest.main()