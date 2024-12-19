import unittest
import sys
import math

sys.path.append("../")
from geometric_lib.circle import area as circle_area
from geometric_lib.circle import perimeter as circle_perimeter
from geometric_lib.rectangle import area as rectangle_area
from geometric_lib.rectangle import perimeter as rectangle_perimeter
from geometric_lib.square import area as square_area
from geometric_lib.square import perimeter as square_perimeter
from geometric_lib.triangle import area as triangle_area
from geometric_lib.triangle import perimeter as triangle_perimeter

'''class CircleTestCase(unittest.TestCase):
    def test_normal_integer_area(self):
        answer = circle_area(3)
        self.assertEqual(answer, (9 * math.pi))

    def test_normal_float_area(self):
        answer = circle_area(2.2)
        self.assertEqual(answer, (4.84 * math.pi))

    def test_null_area(self):
        answer = circle_area(0)
        self.assertEqual(answer, 0)

    def test_fraction_area(self):
        answer = circle_area(5/7)
        self.assertEqual(answer, (25/49 * math.pi))

    def test_large_integer_area(self):
        answer = circle_area(1348189472847109241092)
        self.assertEqual(answer,
                         (1817614854695766305665882433191464181352464 *
                          math.pi))

    def test_small_float_area(self):
        answer = circle_area(0.0000000000000000000000000032)
        self.assertEqual(answer, (0.00000000000000000000000000000000000000000000000000001024
                                  * math.pi))

    def test_normal_integer_perimeter(self):
        answer = circle_perimeter(3)
        self.assertEqual(answer, (6 * math.pi))

    def test_normal_float_perimeter(self):
        answer = circle_perimeter(2.2)
        self.assertEqual(answer, (4.4 * math.pi))

    def test_null_perimeter(self):
        answer = circle_perimeter(0)
        self.assertEqual(answer, 0)

    def test_fraction_perimeter(self):
        answer = circle_perimeter(5/7)
        self.assertEqual(answer, (10/7 * math.pi))

    def test_large_integer_perimeter(self):
        answer = circle_perimeter(1348189472847109241092312834129085702)
        self.assertEqual(answer, (2696378945694218482184625668258171404 * math.pi))

    def test_small_float_perimeter(self):
        answer = circle_perimeter(0.00000000000000000000000000000000000000000000000000000013)
        self.assertEqual(answer, (0.00000000000000000000000000000000000000000000000000000026
                                  * math.pi))

class RectangleTestCase(unittest.TestCase):
    def test_normal_integer_area(self):
        answer = rectangle_area(3, 4)
        self.assertEqual(answer, 12)

    def test_normal_float_area(self):
        answer = rectangle_area(2.2, 1.5)
        self.assertEqual(answer, 3.3)

    def test_null_integer_area(self):
        answer = rectangle_area(0, 1776)
        self.assertEqual(answer, 0)

    def test_integer_null_area(self):
        answer = rectangle_area(492, 0)
        self.assertEqual(answer, 0)

    def test_null_null_area(self):
        answer = rectangle_area(0, 0)
        self.assertEqual(answer, 0)

    def test_float_integer_area(self):
        answer = rectangle_area(2, 2.1)
        self.assertEqual(answer, 4.2)

    def test_fractions_area(self):
        answer = rectangle_area((2/3), (1/3))
        self.assertEqual(answer, (2/9))

    def test_large_integer_area(self):
        answer = rectangle_area(1348189472847109241092, 183904257034882)
        self.assertEqual(answer, 247937783346196844772710993191771144)

    def test_small_float_area(self):
        answer = rectangle_area(0.0000000000000000123, 0.00000000000000000013333)
        self.assertEqual(answer, 0.000000000000000000000000000000000001639959)

    def test_normal_integer_perimeter(self):
        answer = rectangle_perimeter(3, 4)
        self.assertEqual(answer, 14)

    def test_normal_float_perimeter(self):
        answer = rectangle_perimeter(2.2, 1.5)
        self.assertEqual(answer, 7.4)

    def test_null_integer_perimeter(self):
        answer = rectangle_perimeter(0, 1776)
        self.assertEqual(answer, 3552)

    def test_integer_null_perimeter(self):
        answer = rectangle_perimeter(492, 0)
        self.assertEqual(answer, 984)

    def test_null_null_perimeter(self):
        answer = rectangle_area(0, 0)
        self.assertEqual(answer, 0)

    def test_float_integer_perimeter(self):
        answer = rectangle_perimeter(2, 2.1)
        self.assertEqual(answer, 8.2)

    def test_fractions_perimeter(self):
        answer = rectangle_perimeter((1/7), (1/6))
        self.assertEqual(answer, (13/21))

    def test_large_integer_perimeter(self):
        answer = rectangle_perimeter(1348189472847109241092, 183904257034882)
        self.assertEqual(answer, 2696379313502732551948)

    def test_small_float_perimeter(self):
        answer = rectangle_perimeter(0.0000000000000000123, 0.00000000000000000013333)
        self.assertEqual(answer, 0.00000000000000002486666)

class SquareTestCase(unittest.TestCase):
    def test_normal_integer_area(self):
        answer = square_area(3)
        self.assertEqual(answer, 9)

    def test_normal_float_area(self):
        answer = square_area(2.2)
        self.assertEqual(answer, 4.84)

    def test_null_area(self):
        answer = square_area(0)
        self.assertEqual(answer, 0)

    def test_fraction_area(self):
        answer = square_area(5/7)
        self.assertEqual(answer, 25/49)

    def test_large_integer_area(self):
        answer = square_area(1348189472847109241092)
        self.assertEqual(answer, 1817614854695766305665882433191464181352464)

    def test_small_float_area(self):
        answer = square_area(0.0000000000000000000000000032)
        self.assertEqual(answer, 0.00000000000000000000000000000000000000000000000000001024)

    def test_normal_integer_perimeter(self):
        answer = square_perimeter(3)
        self.assertEqual(answer, 12)

    def test_normal_float_perimeter(self):
        answer = square_perimeter(2.2)
        self.assertEqual(answer, 8.8)

    def test_null_perimeter(self):
        answer = square_perimeter(0)
        self.assertEqual(answer, 0)

    def test_fraction_perimeter(self):
        answer = square_perimeter(5/7)
        self.assertEqual(answer, 20/7)

    def test_large_integer_perimeter(self):
        answer = square_perimeter(1348189472847109241092312834129085702)
        self.assertEqual(answer, 5392757891388436964369251336516342808)

    def test_small_float_perimeter(self):
        answer = square_perimeter(0.00000000000000000000000000000000000000000000000000000013)
        self.assertEqual(answer, 0.00000000000000000000000000000000000000000000000000000052)
'''
class TriangleTestCase(unittest.TestCase):
    def test_normal_integer_area(self):
        answer = triangle_area(3, 4)
        self.assertEqual(answer, 6)

'''    def test_normal_float_area(self):
        answer = triangle_area(2.2, 1.5)
        self.assertEqual(answer, 1.65)

    def test_null_integer_area(self):
        answer = triangle_area(0, 1776)
        self.assertEqual(answer, 0)

    def test_integer_null_area(self):
        answer = triangle_area(492, 0)
        self.assertEqual(answer, 0)

    def test_null_null_area(self):
        answer = triangle_area(0, 0)
        self.assertEqual(answer, 0)

    def test_float_integer_area(self):
        answer = triangle_area(2, 2.1)
        self.assertEqual(answer, 2.1)

    def test_fractions_area(self):
        answer = triangle_area((2/3), (1/3))
        self.assertEqual(answer, (1/9))

    def test_large_integer_area(self):
        answer = triangle_area(1348189472847109241092, 183904257034882)
        self.assertEqual(answer, 123968891673098422386355496595885572)

    def test_small_float_area(self):
        answer = triangle_area(0.0000000000000000123, 0.00000000000000000013333)
        self.assertEqual(answer, 0.0000000000000000000000000000000000008199795)

    def test_normal_integer_perimeter(self):
        answer = triangle_perimeter(3, 4, 5)
        self.assertEqual(answer, 12)

    def test_normal_float_perimeter(self):
        answer = triangle_perimeter(2.2, 1.5, 1.1)
        self.assertEqual(answer, 4.8)

    def test_null_integer_integer_perimeter(self):
        answer = triangle_perimeter(0, 1776, 203)
        self.assertEqual(answer, 1979)

    def test_null_null_integer_perimeter(self):
        answer = triangle_perimeter(0, 0, 203)
        self.assertEqual(answer, 203)

    def test_null_null_perimeter(self):
        answer = triangle_perimeter(0, 0, 0)
        self.assertEqual(answer, 0)

    def test_float_integer_perimeter(self):
        answer = triangle_perimeter(2, 2.1, 124)
        self.assertEqual(answer, 128.1)

    def test_fractions_perimeter(self):
        answer = triangle_perimeter((1/7), (1/6), (7/8))
        self.assertEqual(answer, (199/168))

    def test_large_integer_perimeter(self):
        answer = triangle_perimeter(1348189472847109241092,
                                    183904257034882,
                                    1723567123461923571439157824369524)
        self.assertEqual(answer, 1723567123463271761095909190645498)

    def test_small_float_perimeter(self):
        answer = triangle_perimeter(0.0000000000000000123,
                                    0.00000000000000000013333,
                                    0.0000000000000000000000000000001)
        self.assertEqual(answer, 0.0000000000000000124333300000001)'''
