import unittest
import math

from source.circle import area as circle_area, perimeter as circle_perimeter

class TestCircleFunctions(unittest.TestCase):
    
    #area
    def test_area_positive_integer(self):
        self.assertEqual(circle_area(4), math.pi * 16)
        self.assertEqual(circle_area(7), math.pi * 49)
        self.assertEqual(circle_area(12), math.pi * 144)

    def test_area_positive_float(self):
        self.assertAlmostEqual(circle_area(3.5), math.pi * 12.25, places=7)
        self.assertAlmostEqual(circle_area(2.8), math.pi * 7.84, places=7)
        self.assertAlmostEqual(circle_area(5.25), math.pi * 27.5625, places=7)

    def test_area_large_numbers(self):
        self.assertAlmostEqual(circle_area(18000000), math.pi * 18000000 ** 2, places=0)
        self.assertAlmostEqual(circle_area(2500000000), math.pi * 2500000000 ** 2, places=0)

    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_area(-8)
        with self.assertRaises(ValueError):
            circle_area(-15)
        with self.assertRaises(ValueError):
            circle_area(-3.5)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            circle_area("radius")
        with self.assertRaises(TypeError):
            circle_area([5])
    
    #perimeter
    def test_perimeter_positive_integer(self):
        self.assertEqual(circle_perimeter(4), 2 * math.pi * 4)
        self.assertEqual(circle_perimeter(9), 2 * math.pi * 9)
        self.assertEqual(circle_perimeter(15), 2 * math.pi * 15)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(circle_perimeter(3.5), 2 * math.pi * 3.5, places=7)
        self.assertAlmostEqual(circle_perimeter(2.8), 2 * math.pi * 2.8, places=7)
        self.assertAlmostEqual(circle_perimeter(6.75), 2 * math.pi * 6.75, places=7)

    def test_perimeter_large_numbers(self):
        self.assertEqual(circle_perimeter(3800000000), 2 * math.pi * 3800000000)
        self.assertEqual(circle_perimeter(42000000000), 2 * math.pi * 42000000000)

    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-6)
        with self.assertRaises(ValueError):
            circle_perimeter(-12)
        with self.assertRaises(ValueError):
            circle_perimeter(-2.5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            circle_perimeter("diameter")
        with self.assertRaises(TypeError):
            circle_perimeter({"r": 5})