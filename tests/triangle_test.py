import unittest

from source.triangle import area as triangle_area, perimeter as triangle_perimeter

class TestTriangleFunctions(unittest.TestCase):
    
    #area
    def test_area_positive_integer(self):
        self.assertEqual(triangle_area(6, 4), 12)
        self.assertEqual(triangle_area(8, 5), 20)
        self.assertEqual(triangle_area(12, 7), 42)

    def test_area_positive_float(self):
        self.assertAlmostEqual(triangle_area(5.5, 3.2), 8.8, places=7)
        self.assertAlmostEqual(triangle_area(7.8, 4.5), 17.55, places=7)
        self.assertAlmostEqual(triangle_area(3.2, 6.4), 10.24, places=7)

    def test_area_large_numbers(self):
        self.assertEqual(triangle_area(1200000000, 800000000), 480000000000000000)
        self.assertEqual(triangle_area(2500000000, 1500000000), 1875000000000000000)

    def test_area_zero_values(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(6, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)

    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            triangle_area(-6, 4)
        with self.assertRaises(ValueError):
            triangle_area(6, -4)
        with self.assertRaises(ValueError):
            triangle_area(-3, -5)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle_area("base", 4)
        with self.assertRaises(TypeError):
            triangle_area(6, "height")

    

    #perimeter
    def test_perimeter_positive_integer(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(8, 10, 12), 30)
        self.assertEqual(triangle_perimeter(7, 8, 9), 24)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(triangle_perimeter(2.5, 3.5, 4.5), 10.5, places=7)
        self.assertAlmostEqual(triangle_perimeter(3.2, 4.8, 5.6), 13.6, places=7)
        self.assertAlmostEqual(triangle_perimeter(1.5, 2.5, 3.5), 7.5, places=7)

    def test_perimeter_equilateral_triangle(self):
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)
        self.assertEqual(triangle_perimeter(7, 7, 7), 21)
    
    def test_perimeter_large_numbers(self):
        self.assertEqual(triangle_perimeter(1000000000, 1500000000, 1200000000), 3700000000)
        self.assertEqual(triangle_perimeter(2000000000, 2500000000, 3000000000), 7500000000)

    def test_perimeter_zero_values(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, 0, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, -4, 0)

    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, -4, -5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            triangle_perimeter("side", 4, 5)
        with self.assertRaises(TypeError):
            triangle_perimeter(3, "side", 5)

    def test_perimeter_impossible_triangle(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(1, 2, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(10, 2, 3)
        with self.assertRaises(ValueError):
            triangle_perimeter(5, 8, 15)

    def test_perimeter_degenerate_triangle(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(2, 3, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(7, 8, 15)
        with self.assertRaises(ValueError):
            triangle_perimeter(9, 4, 5)