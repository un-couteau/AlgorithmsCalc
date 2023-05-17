import math
class Algorithms():

    def linear_algoritm(self, x, y, z) -> float:
        return (5 * math.atan(x)) - ((1/4 * math.acos(x)) * ((x + 3 * abs(x - y) + x**2) / (abs(x - y) * z + x**2)))

    def f(self, func: str, x: float) -> float:
        if func == "cos(x)":
            return math.cos(x)
        elif func == "exp(x)":
            return math.exp(x)
        elif func == "sqr(x)":
            return x**2
        elif func == None:
            return 6

    def branching_algorithm(self, x: float, y: float, func: str) -> float:
        if x * y > 5 and x * y < 0.5:
            return math.e**self.f(func, x) - abs(y)
        elif x * y > 0.5 and x * y < 0.1:
            return abs(self.f(func, x) + y)**0.5
        else:
            return 2 * self.f(func, x)**2

if __name__ == "__main__":
    res = Algorithms()
    print(res.linear_algoritm(1, 2, 3))