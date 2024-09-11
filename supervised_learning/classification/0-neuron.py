#!/usr/bin/env python3

""" import numpy"""
import numpy as np

"""
A class is a neuron for binary classification
"""

class Neuron:
    """
    Initialise the class and its attribute nx

    """
    def __init__(self, nx):
        if not isistance(nx, int):
            raise TypeError ("nx must be an integer")
            if nx <1 :
                raise TypeError("nx must be a positive integer")
        
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0