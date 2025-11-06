'''MATH 5001 Lab 3 Quinlin Neuhaus'''
import numpy as np

def matrixmult():
    '''Returns matrix product of given matrices A and B'''
    A = np.array([[3, -1, 4], [1, 5, -9]])
    B = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return np.dot(A, B)

def matrixpower():
    '''Returns resulting matrix from given polynomial expression'''
    A = np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    return (-1) * np.dot(np.dot(A, A), A) + 9 * np.dot(A, A) + (-15) * A

def matrixcreate():
    '''Returns ABA matrix product'''
    A = np.triu(np.ones((7,7)))
    B = np.tril(np.full((7,7), -6)) + 5
    return np.dot(np.dot(A, B), A).astype(np.int64)

def matrixpositive(A):
    '''Returns input matrix with 0s for negative values'''
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i, j] < 0:
                A[i, j] = 0
    return A

def matrixstack():
    '''Returns stacked matrices from given specifications'''
    A = np.arange(6).reshape((3,2)).T
    B = np.tril(np.full((3,3), 3))
    C = (-2) * np.eye(3)
    column1 = np.vstack((np.zeros((3,3)), A, B))
    column2 = np.vstack((A.T, np.zeros((2,2)), np.zeros((3,2))))
    column3 = np.vstack((np.eye(3), np.zeros((2,3)), C))
    return np.hstack((column1, column2, column3))

def rowstochastic(A):
    '''Returns row-stochastic matrix of input matrix'''
    return A / A.sum(axis=1).reshape((-1,1))

def maxof4():
    '''Returns largest product of 4 consecutive entries in the 20x20 grid file'''
    grid = np.load("grid.npy")
    numrows = grid.shape[0]
    numcols = grid.shape[1]
    maxr = np.max(grid[:, :-3] * grid[:, 1:-2] * grid[:, 2:-1] * grid[:, 3:])
    maxc = np.max(grid[:-3, :] * grid[1:-2, :] * grid[2:-1, :] * grid[3:, :])
    maxx = np.max(grid[3:, :-3] * grid[2:-1, 1:-2] * grid[1:-2, 2:-1] * grid[:-3, 3:])
    maxy = np.max(grid[:-3, :-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:])
    truemax = max(maxr, maxc, maxx, maxy)
    return truemax
