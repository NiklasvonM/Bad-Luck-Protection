import numpy as np
import scipy.stats as stats


def negative_binomial_cdf(x, expected_value: float, alpha: float) -> np.ndarray:
    """
    Calculates the CDF of a negative binomial distribution that is parameterized in a non-standard
    way.

    Args:
        x: Array-like input values where the CDF is evaluated.
        expected_value: The desired expected value of the distribution.
        alpha: A scaling factor to control the variance (alpha > 0). At alpha = 1, the
            distribution is equal to the geometric distribution.
            For alpha > 1, the variance is increased compared to the geometric distribution.
            For alpha < 1, the variance is decreased.

    Returns:
        Array of CDF values corresponding to the input x values.
    """
    assert alpha > 0
    assert expected_value > 0

    p = 1 / (expected_value * alpha)
    r = p * expected_value / (1 - p)
    return stats.nbinom.cdf(x, r, p)
