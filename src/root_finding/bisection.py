import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from src.root_finding.root_finder import RootFinder

class Bisection:
    def __init__(self, func_str):
        x = symbols('x')
        expr = eval(func_str.replace("^", "**"), {"x": x})  # Convert string to sympy expression
        self.func = lambdify(x, expr)  # Convert to a callable function
    
    def find(self, interval, tolerance=1e-3):
        a, b = interval

        if np.sign(self.func(a)) == np.sign(self.func(b)):
            raise ValueError("Scalars a and b don't bound a root.")

        while (b - a) / 2 > tolerance:
            m = (a + b) / 2
            f_m = self.func(m)

            if np.abs(f_m) < tolerance:
                return m
            elif np.sign(f_m) == np.sign(self.func(a)):
                a = m
            else:
                b = m

        return (a + b) / 2  # Final estimate of root

# Example usage
x = symbols('x')
func_str = input("\nEnter an equation with respect to x: ")  # Example: "x**2 - 4"

solver = Bisection(func_str)
root = solver.find(interval=(-1, 1), tolerance=0.01)
print(f"Root found: {root}")
