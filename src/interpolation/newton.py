from src.interpolation.interpolation import Interpolation
import numpy as np
import matplotlib.pyplot as plt
from typing import List

class Newton(Interpolation):
    def __init__(self, x: List[int], y: List[int]):
        self.x = x
        self.y = y
        prev_space = x[1] - x[0]
        for i in range(2, len(x)):
            if x[i] - x[i-1] != prev_space:
                raise RuntimeError("Points must be evenly spaced in newton interpolation.")
            
    def _compute_divided_differences(self) -> np.array:
        num_points = len(self.x)
        coef = np.zeros((num_points, num_points))
        coef[:, 0] = self.y  # First column is just the y values

        for j in range(1, num_points):
            for i in range(num_points - j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (self.x[i+j] - self.x[i])
        return coef
    
    def interpolate(self, new_x: float) -> float:
        num_points = len(self.x)
        coef = self._compute_divided_differences()
        interpolated_y = coef[0, 0]
        product_term = 1.0

        for i in range(1, num_points):
            product_term *= (new_x - self.x[i-1])
            interpolated_y += coef[0, i] * product_term

        return interpolated_y

    def plot(self):
        x_smooth = np.linspace(min(self.x), max(self.x), 1000)
        y_smooth = [self.interpolate(x) for x in x_smooth]

        # Plot original points
        plt.scatter(self.x, self.y, color='red', marker='o', edgecolors='black', label="Original Points")

        # Plot interpolated curve
        plt.plot(x_smooth, y_smooth, color='blue', linestyle='-', linewidth=2, label="Newton Interpolation")

        # Labels and grid
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Newton's Polynomial Interpolation")
        plt.legend()
        plt.grid(True)
        plt.show()


