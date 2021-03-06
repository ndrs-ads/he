'''
Created on Jul 23, 2015

@author: ndrs-ads
'''
import unittest
import test


class Test_v2(unittest.TestCase):


    def setUp(self):
        self.test = test.Mytest()
        pass


    def tearDown(self):
        pass


    def testAdd(self):
        val_in = self.test.test_add(12, 3)
        val_out = 15
        self.assertEqual(val_in, val_out)
        pass
    
    def testSub(self):
        val_in = self.test.test_sub(13, 2)
        val_out = 10
        self.assertEqual(val_in, val_out)
        pass
    
    def testMulti(self):
        val_in = self.test.test_multi(12, 2)
        val_out = 24
        self.assertEqual(val_in, val_out)
        pass
    
    def testDivine(self):
        val_in = self.test.test_divine(12, 2)
        val_out = 6.0
        self.assertEqual(val_in, val_out)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()