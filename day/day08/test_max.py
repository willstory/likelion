# test_sum.py
from max import add
from max import find_max
from max import Calculator

def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) == 2


def test_find_max():
    assert find_max([1,2,3,4,5]) == 5
    assert find_max([-1, -5, -3, -4]) == -1

# tests/test_calculator.py 추가 테스트 케이스


# tests/test_calculator.py

import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
