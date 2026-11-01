import numpy as np


def compute_DHT_IV_matrix(N):
    C = np.zeros((N, N))
    for k  in range(0, N):
        for n in range(0, N):
            C[k,n] = (1 / np.sqrt(N)) * (np.cos((np.pi * (2 * k  + 1) * (2 * n + 1)) / (2 * N)) + np.sin((np.pi * (2 * k+ 1) * (2 * n + 1)) / (2 * N)))
    return C
