import unittest

from source.rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class TestRectangleFunctions(unittest.TestCase):
    
    def test_area_positive_integer(self):
        self.assertEqual(rectangle_area(8, 12), 96)
        self.assertEqual(rectangle_area(15, 20), 300)

    def test_area_positive_float(self):
        self.assertAlmostEqual(rectangle_area(3.5, 2.8), 9.8, places=7)
        self.assertAlmostEqual(rectangle_area(4.25, 6.5), 27.625, places=7)
        self.assertAlmostEqual(rectangle_area(7.8, 3.2), 24.96, places=7)
    
    def test_area_large_numbers(self):
        self.assertEqual(rectangle_area(1500000000, 2000000000), 3000000000000000000)
        self.assertEqual(rectangle_area(250000000, 1800000000), 450000000000000000)

    def test_area_zero_sides(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(4, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_area_negative_sides(self):
        with self.assertRaises(ValueError):
            rectangle_area(-4, 7)
        with self.assertRaises(ValueError):
            rectangle_area(4, -7)
        with self.assertRaises(ValueError):
            rectangle_area(-3, -5)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle_area("length", 5)
        with self.assertRaises(TypeError):
            rectangle_area(5, "width")
    

    #perimeter
    def test_perimeter_positive_integer(self):
        self.assertEqual(rectangle_perimeter(4, 7), 22)
        self.assertEqual(rectangle_perimeter(15, 20), 70)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(rectangle_perimeter(3.5, 2.8), 12.6, places=7)
        self.assertAlmostEqual(rectangle_perimeter(4.25, 6.5), 21.5, places=7)
        self.assertAlmostEqual(rectangle_perimeter(7.8, 3.2), 22.0, places=7)

    def test_perimeter_zero_sides(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(4, 0), 8)
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_perimeter_large_numbers(self):
        self.assertEqual(rectangle_perimeter(1500000000, 2000000000), 7000000000)
        self.assertEqual(rectangle_perimeter(250000000, 1800000000), 4100000000)
        
    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter(-4, 7)
        with self.assertRaises(ValueError):
            rectangle_perimeter(4, -7)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-3, -5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter("length", 5)
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "width")
