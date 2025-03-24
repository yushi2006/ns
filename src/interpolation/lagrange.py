from src.interpolation.interpolation import Interpolation
import matplotlib.pyplot as plt
import numpy as np

class Lagrange(Interpolation):
    def interpolate(self, new_x: float) -> float:
        n = len(self.x)
        y_interpolated = 0

        for k in range(n):
            L_k = 1
            for i in range(n):
                if i != k:
                    L_k *= (new_x - self.x[i]) / (self.x[k] - self.x[i])

            y_interpolated += self.y[k] * L_k

        return y_interpolated


    def plot(self):
        x_smooth = np.linspace(min(self.x), max(self.x), 1000)
        y_smooth = [self.interpolate(x) for x in x_smooth]

        plt.scatter(self.x, self.y, color='red', marker='o', edgecolors='black', label="Original Points")

        plt.plot(x_smooth, y_smooth, color='blue', linestyle='-', linewidth=2, label="Lagrange Interpolation")

        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Lagrange Polynomial Interpolation")
        plt.legend()
        plt.grid(True)
        plt.show()

