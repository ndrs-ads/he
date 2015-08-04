'''
Created on Jul 21, 2015

@author: ndrs-jry
'''

class Mytest(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def test_add(self, a, b):
        return a+ba
    
    def test_sub(self, a, b):
        return a-b
    
    def test_multi(self, a, b):
        return a*b
    
    def test_divine(self, a, b):
        if(b!=0):
            ret_val = float(a)/float(b)
        else:
            ret_val = 'ERROR'
        return ret_val
    
    
