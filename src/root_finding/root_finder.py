import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional

class RootFinder:
    def __init__(self):
        super(RootFinder, self).__init__()
    
    def find(self, point: Optional[float], inetrval: Optional[Tuple[float, float]]):
        raise NotImplemented("You must define the root finding algorithm to use.")