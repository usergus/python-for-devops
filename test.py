import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.53, places=2)

    def test_calculate_bmr(self):
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, 'male'), 1724.05, places=2)
        self.assertAlmostEqual(calculate_bmr(160, 50, 30, 'female'), 1275.72, places=2)


if __name__ == '__main__':
    unittest.main()