# DHT-IV — fast algorithms

Factorizations of the type-IV discrete Hartley transform (DHT-IV) matrix for sizes N = 3…8, with correctness tests.

## Structure

| File | Description |
|------|-------------|
| `computeDHT_IVmatrix.py` | `compute_DHT_IV_matrix(N)` — DHT-IV matrix computed directly from the definition |
| `proposed_N3.py` … `proposed_N8.py` | `proposed_NX()` — proposed factorization of the DHT-IV matrix for N = X as a product of sparse matrices |
| `tests.py` | Tests comparing each factorization with the reference matrix |

Each `proposed_NX()` function derives its coefficients from the first row of `compute_DHT_IV_matrix(N)` and stores them in a dictionary `S` (`S_0`, `S_1`, …), which is used to build the diagonal matrix.

## Requirements

- Python
- NumPy

## Running the tests

```bash
python -m unittest tests
```

Each factorization is compared with the reference matrix using an absolute tolerance of `EPS = 1e-12`.
