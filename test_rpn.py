import unittest
import rpn                      # something like #include in c++


class TestBasics(unittest.TestCase):        #class definition using unit test framework
    def test_add(self):                     # test 1
        result = rpn.calculate('1 1 +')     # no need to define 'result'?
        self.assertEqual(2,result)          # check if 2 == result

#TestBasics tb;
#tb.test_add() ==> TestBasics.test_add(test)

