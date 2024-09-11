#!/usr/bin/env python3

class Neuron:
    def __init__(self, nx):
        if not isistance(nx, int):
            raise TypeError ("nx must be an integer")
            if nx <1 :
                raise TypeError("nx must be a positive integer")
