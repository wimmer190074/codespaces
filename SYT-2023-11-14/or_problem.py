import numpy as np

x = np.array([
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])

y = np.array([0,1,1,1])

def heaviside(s):
    if s >= 0:
        return 1
    else:
        return 0

def perceptron(x, y):
    error = 0

    w = np.array([-1,1,1]) # solves or Problem

    for i, x in enumerate(x):
        s = np.dot(w, x)
        out = heaviside(s)

        actual_error = np.abs(out - y[i])

        error += actual_error

    return error


result = perceptron(x, y)
print(result)