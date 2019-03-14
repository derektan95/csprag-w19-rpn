import unittest
import rpn                      # something like #include in c++


class TestBasics(unittest.TestCase):        #class definition using unit test framework

    def test_plus(self):                     # test 1
        result = rpn.calculate(1, 1, '+')     # no need to define 'result'?
        self.assertEqual(2,result)          # check if 2 == result

    def test_minus(self):                     # test 1
        result = rpn.calculate(1, 1, '-')     # no need to define 'result'?
        self.assertEqual(0,result)          # check if 0 == result

    def test_minus(self):                     # test 1
        result = rpn.calculate(3, 1, '-')     # no need to define 'result'?
        self.assertEqual(-2,result)          # check if 0 == result

    def test_prev_calc(self):                # test 1
        result = rpn.calculate(2, 3, '+')     # no need to define 'result'?
        self.assertEqual(5,result)          # check if 0 == result

    def test_exponentiation(self):                     # test 1
        result = rpn.calculate(2, 7, '^')     # no need to define 'result'?
        self.assertEqual(14,result)          # check if 0 == result



#TestBasics tb;
#tb.test_add() ==> TestBasics.test_add(test)

