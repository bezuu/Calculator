import temp
import unittest

class TestCalc(unittest.TestCase, temp.Kalkulator):

    def test_add(self):
        #given
        a = 5
        b = 11
        sign = "+"
        expected = 16
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,result, msg)
        
    def test_min(self):
        #given
        a = 123
        b = 54
        sign = "-"
        expected = 69
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,result, msg)
        
    def test_multiply(self):
        #given
        a = 23
        b = 5
        sign = "*"
        expected = 115
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,result, msg)
    def test_divide(self):
        #given
        a = 42
        b = 7
        sign = "/"
        expected = 6
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,result, msg)
    def test_date_type_add(self):
        #given
        a = 42
        b = 7
        sign = "+"
        expected = int
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,type(result), msg)
    def test_date_type_min(self):
        #given
        a = 42
        b = 7
        sign = "-"
        expected = int
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,type(result), msg)
    def test_date_type_multiply(self):
        #given
        a = 42
        b = 7
        sign = "*"
        expected = int
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,type(result), msg)
    def test_date_type_divide(self):
        #given
        a = 42
        b = 7
        sign = "/"
        expected = float
        msg = "Wrong"
        #when
        result = temp.Kalkulator.calc(self, a, b, sign)
        #then
        self.assertEqual(expected,type(result), msg)
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    