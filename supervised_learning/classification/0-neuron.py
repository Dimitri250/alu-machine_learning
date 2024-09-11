#!/usr/bin/env python3
""" Neuron class """

import numpy as np

"""
A class is a neuron for binary classification
"""


class Neuron:
    """
    Initialise the class and its attribute nx

    """
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
