def calculate_psi(expected, actual):
    import numpy as np
    expected = np.array(expected)
    actual = np.array(actual)
    return float(np.abs(expected - actual).mean())
