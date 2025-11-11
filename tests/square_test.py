import unittest

from source.square import area as square_area, perimeter as square_perimeter

class TestSquareFunctions(unittest.TestCase):
    
    #area
    def test_area_positive_integer(self):
        self.assertEqual(square_area(1), 1) 
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(9), 81)
        self.assertEqual(square_area(12), 144)

    def test_area_positive_float(self):
        self.assertAlmostEqual(square_area(3.5), 12.25, places=7)
        self.assertAlmostEqual(square_area(2.8), 7.84, places=7)
        self.assertAlmostEqual(square_area(5.25), 27.5625, places=7)

    def test_area_large_numbers(self):
        self.assertEqual(square_area(1800000000), 3240000000000000000)
        self.assertEqual(square_area(25000000000), 625000000000000000000)

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            square_area(-6)
        with self.assertRaises(ValueError):
            square_area(-11)
        with self.assertRaises(ValueError):
            square_area(-3.5)

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            square_area("side")
        with self.assertRaises(TypeError):
            square_area([4])

    

    #perimeter
    def test_perimeter_positive_integer(self):
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(4), 16)
        self.assertEqual(square_perimeter(9), 36)
        self.assertEqual(square_perimeter(12), 48)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(square_perimeter(3.5), 14.0, places=7)
        self.assertAlmostEqual(square_perimeter(2.8), 11.2, places=7)
        self.assertAlmostEqual(square_perimeter(5.25), 21.0, places=7)

    def test_perimeter_large_numbers(self):
        self.assertEqual(square_perimeter(2200000000), 8800000000)
        self.assertEqual(square_perimeter(35000000000), 140000000000)
        
    def test_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square_perimeter(-7)
        with self.assertRaises(ValueError):
            square_perimeter(-14)
        with self.assertRaises(ValueError):
            square_perimeter(-2.5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            square_perimeter("side")
        with self.assertRaises(TypeError):
            square_perimeter({"s": 4})
