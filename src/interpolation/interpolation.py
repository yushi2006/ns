import matplotlib.pyplot as plt
import numpy as np
from typing import List

class Interpolation:
    def __init__(self, x: List[float], y: List[float]):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)

    def interpolate(self, new_x: float) -> float:
        raise RuntimeError("You should Identify the interpolation method.")
    
    def plot(self):
        pass

