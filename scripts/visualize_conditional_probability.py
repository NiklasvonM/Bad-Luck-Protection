import matplotlib.pyplot as plt

from blp.conditional_probability_from_cdf import conditional_probability_from_cdf
from blp.negative_binomial_cdf import negative_binomial_cdf


def main() -> None:
    expected_value: float = 100.0
    x = range(0, round(3 * expected_value) + 1)
    alphas: list[float] = [1.0, 0.5, 0.2]
    plt.figure(figsize=(10, 6))
    for alpha in alphas:
        conditional_probability = conditional_probability_from_cdf(
            cdf=lambda k: negative_binomial_cdf(k, expected_value, alpha=alpha)  # noqa
        )
        plt.plot(
            x,
            [conditional_probability(value) for value in x],
            label=f"Negative Binomial (α={alpha})",
        )
    plt.xlabel("Number of Rolls")
    plt.ylabel("Probability of Success for this Roll")
    plt.title("Probability of Success for Different Parameters")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
