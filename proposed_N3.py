import numpy as np
from computeDHT_IVmatrix import compute_DHT_IV_matrix

def proposed_N3():
    h = compute_DHT_IV_matrix(3)[0]
    a, b = h[2], h[1]
    S = {
        "S_0": a,
        "S_1": b,
    }

    matrix0 = np.array([
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
    ])
    matrix1 = np.array([
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ])

    matrix2 = np.diag([S["S_0"], S["S_1"], 1, 1, 1])

    matrix3 = np.array([
        [1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])

    matrix4 = np.diag([
        2,
        1,
        1,
        1,
        1
    ])

    matrix5 = np.array([
        [0, 1, 0],
        [1,-1, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])


    result = matrix0 @ matrix1 @ matrix2 @ matrix3 @ matrix4 @ matrix5

    return result