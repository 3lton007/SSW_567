import unittest

from classify_triangle import classify_triangle

class TestList(unittest.TestCase):

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right Triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right Triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(8, 6, 10), 'Right Triangle')

    def testEquilateralTriangleA(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral Triangle')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classify_triangle(10,10,10),'Equilateral Triangle')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classify_triangle(3, 3, 2),'Isoceles Triangle')
    
    def testIsocelesTriangleB(self):     
        self.assertEqual(classify_triangle(4, 6, 6),'Isoceles Triangle')
    
    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(10, 15, 12),'Scalene Triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classify_triangle(4, 6, 5),'Scalene Triangle')

    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(-1, -1, -1),'Invalid Triangle')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle("200", "0", "0"),'Invalid Triangle')


if __name__ == "__main__":
    unittest.main()