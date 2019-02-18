import unittest
import boxer

class TestBoxer(unittest.TestCase):
    def test_age_1PW(self):
        self.assertEqual(boxer.PitWilder.age, 33)

    def test_age_1RG(self):
        self.assertEqual(boxer.RobeGrant.age, 28)

    def test_age_1TH(self):
        self.assertEqual(boxer.TomyHurd.age, 35)

    def test_weight_1PW(self):
        self.assertEqual(boxer.PitWilder.weight, 78)

    def test_weight_1RG(self):
        self.assertEqual(boxer.RobeGrant.weight, 72)

    def test_weight_1TH(self):
        self.assertEqual(boxer.TomyHurd.weight, 69)

    def test_height_1PW(self):
        self.assertEqual(boxer.PitWilder.height, 180)

    def test_height_1RG(self):
        self.assertEqual(boxer.RobeGrant.height, 185)

    def test_height_1TH(self):
        self.assertEqual(boxer.TomyHurd.height, 182)

    def test_age_2PW(self):
        self.assertEqual(boxer.PitWilder.age, -33)

    def test_age_2RG(self):
        self.assertEqual(boxer.RobeGrant.age, -28)

    def test_age_2TH(self):
        self.assertEqual(boxer.TomyHurd.age, -35)

    def test_weight_2PW(self):
        self.assertEqual(boxer.PitWilder.weight, -78)

    def test_weight_2RG(self):
        self.assertEqual(boxer.RobeGrant.weight, -72)

    def test_weight_2TH(self):
        self.assertEqual(boxer.TomyHurd.weight, -69)

    def test_height_2PW(self):
        self.assertEqual(boxer.PitWilder.height, -180)

    def test_height_2RG(self):
        self.assertEqual(boxer.RobeGrant.height, -185)

    def test_height_2TH(self):
        self.assertEqual(boxer.TomyHurd.height, -182)

    def test_age_3PW(self):
        self.assertEqual(boxer.PitWilder.age, a)

    def test_age_3RG(self):
        self.assertEqual(boxer.RobeGrant.age, a)

    def test_age_3TH(self):
        self.assertEqual(boxer.TomyHurd.age, a)

    def test_weight_3PW(self):
        self.assertEqual(boxer.PitWilder.weight, a)

    def test_weight_3RG(self):
        self.assertEqual(boxer.RobeGrant.weight, a)

    def test_weight_3TH(self):
        self.assertEqual(boxer.TomyHurd.weight, a)

    def test_height_3PW(self):
        self.assertEqual(boxer.PitWilder.height, a)

    def test_height_3RG(self):
        self.assertEqual(boxer.RobeGrant.height, a)

    def test_height_3TH(self):
        self.assertEqual(boxer.TomyHurd.height, a)

    def test_age_4PW(self):
        self.assertEqual(boxer.PitWilder.age, A)

    def test_age_4RG(self):
        self.assertEqual(boxer.RobeGrant.age, A)

    def test_age_4TH(self):
        self.assertEqual(boxer.TomyHurd.age,  A)

    def test_weight_4PW(self):
        self.assertEqual(boxer.PitWilder.weight, A)

    def test_weight_4RG(self):
        self.assertEqual(boxer.RobeGrant.weight, A)

    def test_weight_4TH(self):
        self.assertEqual(boxer.TomyHurd.weight, A)

    def test_height_4PW(self):
        self.assertEqual(boxer.PitWilder.height, A)

    def test_height_4RG(self):
        self.assertEqual(boxer.RobeGrant.height, A)

    def test_height_4TH(self):
        self.assertEqual(boxer.TomyHurd.height, A)

    def test_age_5PW(self):
        self.assertGreater(boxer.PitWilder.age, 18, "The boxer is too young.")

    def test_age_5RG(self):
        self.assertGreater(boxer.RobeGrant.age, 18, "The boxer is too young.")

    def test_age_5TH(self):
        self.assertGreater(boxer.TomyHurd.age, 18, "The boxer is too young.")

    def test_weight_5_1PW(self):
        self.assertGreaterEqual(boxer.PitWilder.weight, 69, "It`s another weight category")

    def test_weight_5_2PW(self):
        self.assertLessEqual(boxer.PitWilder.weight, 75, "It`s another weight category")

    def test_weight_5_1RG(self):
        self.assertGreaterEqual(boxer.RobeGrant.weight, 69, "It`s another weight category")

    def test_weight_5_2RG(self):
        self.assertLessEqual(boxer.RobeGrant.weight, 75, "It`s another weight category")

    def test_weight_5_1TH(self):
        self.assertGreaterEqual(boxer.TomyHurd.weight, 69, "It`s another weight category")

    def test_weight_5_2TH(self):
        self.assertLessEqual(boxer.TomyHurd.weight, 75, "It`s another weight category")

    def test_age_6PW(self):
        self.assertEqual(boxer.PitWilder.age, 3)

    def test_age_6RG(self):
        self.assertEqual(boxer.RobeGrant.age, 3)

    def test_age_6TH(self):
        self.assertEqual(boxer.TomyHurd.age, 3)

    def test_weight_6PW(self):
        self.assertEqual(boxer.PitWilder.weight, 7)

    def test_weight_6RG(self):
        self.assertEqual(boxer.RobeGrant.weight, 7)

    def test_weight_6TH(self):
        self.assertEqual(boxer.TomyHurd.weight, 6)

    def test_height_5PW(self):
        self.assertEqual(boxer.PitWilder.height, 1)

    def test_height_5RG(self):
        self.assertEqual(boxer.RobeGrant.height, 1)

    def test_height_5TH(self):
        self.assertEqual(boxer.TomyHurd.height, 1)



unittest.main()