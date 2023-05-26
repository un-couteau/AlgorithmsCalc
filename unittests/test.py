import sys

sys.path.append('../')
import unittest
from src.backend.algorithms import Algorithms


class MyTestCase(unittest.TestCase):
    x = 0.5
    y = 7
    z = 10
    branches = ["cos(x)", "exp(x)", "sqr(x)"]
    alg = Algorithms()

    def test_linear(self):
        self.assertEqual(self.alg.linear_algoritm(self.x, self.y, self.y), 2.2023596274535873)

    def test_branch_first(self):
        self.assertEqual(self.alg.branching_algorithm(self.x, self.y, self.branches[0]), 1.5403023058681398)

    def test_branch_second(self):
        self.assertEqual(self.alg.branching_algorithm(self.x, self.y, self.branches[1]), 5.436563656918091)

    def test_branch_third(self):
        self.assertEqual(self.alg.branching_algorithm(self.x, self.y, self.branches[2]), 0.125)


if __name__ == '__main__':
    unittest.main()
