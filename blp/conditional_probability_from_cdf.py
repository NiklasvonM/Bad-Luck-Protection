from collections.abc import Callable


def conditional_probability_from_cdf(cdf: Callable[[int], float]) -> Callable[[int], float]:
    def conditional_probability(k: int) -> float:
        if cdf(k - 1) >= 1.0:
            return 1.0
        return (cdf(k) - cdf(k - 1)) / (1 - cdf(k - 1))

    return conditional_probability
