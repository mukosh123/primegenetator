import unittest
from primeg import primeGenerator
class PrimeTest(unittest.TestCase):
    def test_arg_is_neg(self):
        self.assertEqual("wrong arg",primeGenerator(-1))

    def test_output(self):

        self.assertEqual([1,2,3,5],primeGenerator(5))

    def test_output1(self):
        self.assertEqual([1,2,3,5,7],primeGenerator(10))
    
    def test_output2(self):
        self.assertEqual([1,2,3,5,7,11,13,17,19],primeGenerator(20))

    def test_output3(self):
        self.assertEqual([1,2,3,5,7,11,13,17,19,23,29],primeGenerator(30))

    def test_arg_is_string(self):
        self.assertEqual("wrong arg",primeGenerator('ert'))

    def test_arg_is_list(self):
        self.assertEqual("wrong arg",primeGenerator([]))

    def test_arg_is_float(self):
        self.assertEqual("wrong arg",primeGenerator(8.9))

    def test_arg_is_dict(self):
        self.assertEqual("wrong arg",primeGenerator({1:'e'}))

    def test_arg_is_set(self):
        self.assertEqual("wrong arg",primeGenerator(set()))
