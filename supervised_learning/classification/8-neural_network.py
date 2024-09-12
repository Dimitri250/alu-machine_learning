#!/usr/bin/env python3
'''Comment'''

import numpy as np


class NeuralNetwork:
   """
Public instance attributes:
    W1 (ndarray): The weights vector for the hidden layer.
        - Initialized using a random normal distribution upon instantiation.
    b1 (ndarray): The bias for the hidden layer.
        - Initialized to 0 upon instantiation.
    A1 (ndarray): The activated output of the hidden layer.
        - Initialized to 0 upon instantiation.
    W2 (ndarray): The weights vector for the output neuron.
        - Initialized using a random normal distribution upon instantiation.
    b2 (ndarray): The bias for the output neuron.
        - Initialized to 0 upon instantiation.
    A2 (ndarray): The activated output of the output neuron (prediction).
        - Initialized to 0 upon instantiation.
"""

    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')

        self.nx = nx
        self.nodes = nodes
        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
