import numpy as np
from computeDHT_IVmatrix import compute_DHT_IV_matrix

def proposed_N4():
    h = compute_DHT_IV_matrix(4)[0]
    a, b = h[0], h[2]
    S = {
        "S_0": a - b,
        "S_1": -a - b,
        "S_2": b,
        "S_3": a - b,
        "S_4": -a - b,
        "S_5": b,
    }

    matrix0 = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0,-1]
    ])

    matrix1 = np.array([
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0,-1, 0],
        [0, 1, 0,-1]
    ])
    matrix2 = np.array([
        [1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1]
    ])

    matrix3 = np.diag([
        S["S_0"],
        S["S_1"],
        S["S_2"],
        S["S_3"],
        S["S_4"],
        S["S_5"]
    ])

    matrix4 = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1]
    ])

    matrix5 = matrix0


    result = matrix0 @ matrix1 @ matrix2 @ matrix3 @ matrix4 @ matrix5

    return result