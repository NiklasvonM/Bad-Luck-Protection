import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import scipy.stats as stats

from blp.negative_binomial_cdf import negative_binomial_cdf


def main() -> None:
    expected_value: float = 100.0
    x = range(0, round(3 * expected_value) + 1)
    alphas: list[float] = [1.0, 0.5, 0.2]

    plt.figure(figsize=(10, 6))

    # Negative Binomials
    for alpha in alphas:
        cdf = negative_binomial_cdf(x, expected_value, alpha)
        plt.plot(x, cdf * 100, label=f"Negative Binomial (α={alpha})")

    # Geometric
    geom_cdf = stats.geom.cdf(x, 1 / (expected_value + 1))
    plt.plot(x, geom_cdf * 100, label="Geometric", color="black", linestyle="--")
    plt.axhline(y=95, color="r", linestyle="dashed", linewidth=0.8)  # Horizontal line at 95 %

    plt.xlabel("Number of Rolls Until Success")
    plt.ylabel("Cumulative Probability (%)")
    plt.title(
        f"CDFs of Geometric and Negative Binomial Distributions (Expected Value = {expected_value})"
    )
    plt.ylim(0, 101)
    plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter())
    plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(5))
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
