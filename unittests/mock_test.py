import sys
import unittest
from unittest import mock
from src.backend.algorithms import Algorithms


class MyTestCase(unittest.TestCase):
    x = 0.5
    y = 7
    z = 10
    branches = ["cos(x)", "exp(x)", "sqr(x)"]
    alg = Algorithms()

    def test_linear(self):
        with mock.patch.object(self.alg, 'linear_algoritm', return_value=2.2023596274535873) as mock_linear:
            self.assertEqual(self.alg.linear_algoritm(self.x, self.y, self.y), 2.2023596274535873)
            mock_linear.assert_called_once_with(self.x, self.y, self.y)

    def test_branch_first(self):
        with mock.patch.object(self.alg, 'branching_algorithm', return_value=1.5403023058681398) as mock_branch:
            self.assertEqual(self.alg.branching_algorithm(self.x, self.y, self.branches[0]), 1.5403023058681398)
            mock_branch.assert_called_once_with(self.x, self.y, self.branches[0])

    def test_branch_second(self):
        with mock.patch.object(self.alg, 'branching_algorithm', return_value=5.436563656918091) as mock_branch:
            self.assertEqual(self.alg.branching_algorithm(self.x, self.y, self.branches[1]), 5.436563656918091)
            mock_branch.assert_called_once_with(self.x, self.y, self.branches[1])

    def test_branch_third(self):
        with mock.patch.object(self.alg, 'branching_algorithm', return_value=0.125) as mock_branch:
            self.assertEqual(self.alg.branching_algorithm(self.x, self.y, self.branches[2]), 0.125)
            mock_branch.assert_called_once_with(self.x, self.y, self.branches[2])


if __name__ == '__main__':
    unittest.main()
