import numpy as np

def square(x):
    """ calculate the square.

    Parameter
    ---------
    x : ndarray

    Returns
    -------
    energy : float

    """
    return np.sum(x*x)
