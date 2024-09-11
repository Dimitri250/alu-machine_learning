import numpy as np

class Neuron:
    def __init__(self, nx):
        if not isistance(nx, int):
            raise TypeError ("nx must be an integer")
            if nx <1 :
                raise TypeError("nx must be a positive integer")

            self.W = np.random.randn(1, nx)  # weights initialized with a random normal distribution
            self.b = 0  # bias initialized to 0
            self.A = 0  # activated output initialized to 0