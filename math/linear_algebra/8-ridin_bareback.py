#!/usr/bin/env python3
'''
This script has a function def mat_mul(mat1, mat2)
that performs matrix multiplication.
'''

def mat_mul(mat1, mat2):
    '''
    The function def mat_mul(mat1, mat2)
    performs matrix multiplication.
    '''
    # Check if number of columns in mat1 is equal to number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Perform matrix multiplication
    result = [
        [
            sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0])))
            for j in range(len(mat2[0]))
        ]
        for i in range(len(mat1))
    ]

    return result
