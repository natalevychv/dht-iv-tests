import unittest
from proposed_N3 import proposed_N3
from proposed_N4 import proposed_N4
from proposed_N5 import proposed_N5
from proposed_N6 import proposed_N6
from proposed_N7 import proposed_N7
from proposed_N8 import proposed_N8
from computeDHT_IVmatrix import compute_DHT_IV_matrix
import numpy as np

EPS = 1e-12

class Tests(unittest.TestCase):

    def test_n3(self):
        result = np.array(proposed_N3(), dtype=np.float64)
        expected = np.array(compute_DHT_IV_matrix(3), dtype=np.float64)
        np.testing.assert_allclose(result, expected, atol=EPS)

    def test_n4(self):
        result = np.array(proposed_N4(), dtype=np.float64)
        expected = np.array(compute_DHT_IV_matrix(4), dtype=np.float64)
        np.testing.assert_allclose(result, expected, atol=EPS)

    def test_n5(self):
        result = np.array(proposed_N5(), dtype=np.float64)
        expected = np.array(compute_DHT_IV_matrix(5), dtype=np.float64)
        np.testing.assert_allclose(result, expected, atol=EPS)

    def test_n6(self):
        result = np.array(proposed_N6(), dtype=np.float64)
        expected = np.array(compute_DHT_IV_matrix(6), dtype=np.float64)
        np.testing.assert_allclose(result, expected, atol=EPS)

    def test_n7(self):
        result = np.array(proposed_N7(), dtype=np.float64)
        expected = np.array(compute_DHT_IV_matrix(7), dtype=np.float64)
        np.testing.assert_allclose(result, expected, atol=EPS)

    def test_n8(self):
        result = np.array(proposed_N8(), dtype=np.float64)
        expected = np.array(compute_DHT_IV_matrix(8), dtype=np.float64)
        np.testing.assert_allclose(result, expected, atol=EPS)


if __name__ == '__main__':
    unittest.main()
