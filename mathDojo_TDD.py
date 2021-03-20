import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in nums:
            num += i
        self.result += num  
        return self
    def subtract(self, num, *nums):
        for i in nums:
            num += i
        self.result -= num
        return self

class addTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(self.md.add(1,2).add(3,4,5).result, 15)
    def testTwo(self):
        self.assertEqual(self.md.add(1,2,3).add(4,5,6).result, 21)
    def testThree(self):
        self.assertEqual(self.md.add(1,2,3,4).add(5,6,7,8).result, 36)
    def setUp(self):
        self.md = MathDojo()
    def tearDown(self):
        print('running teardown tasks')

class subtractTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(self.md.add(50).subtract(1,2).result, 47)
    def testTwo(self):
        self.assertEqual(self.md.add(50).subtract(1,2).subtract(3,4,5).result, 35)
    def testThree(self):
        self.assertEqual(self.md.add(50).subtract(1,2).subtract(3,4,5).subtract(6,7,8).result, 14)
    def setUp(self):
        self.md = MathDojo()
    def tearDown(self):
        print('running teardown tasks')

if __name__ == '__main__':
    unittest.main()