import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import scipy.stats as stats


def main() -> None:
    expected_value: float = 100.0
    x = range(0, round(3 * expected_value) + 1)

    plt.figure(figsize=(10, 6))
    geom_cdf = stats.geom.cdf(x, 1 / (expected_value + 1))

    # Plotting with percentage formatting
    plt.plot(x, geom_cdf * 100, label="Geometric")
    plt.axhline(y=95, color="r", linestyle="dashed", linewidth=0.8)  # Horizontal line at 95%

    plt.xlabel("Number of Rolls Until Success")
    plt.ylabel("Cumulative Probability (Share of Players that get the Drop)")
    plt.title(f"CDF of a Geometric Distribution (Expected Value = {expected_value})")

    # Formatting the y-axis ticks
    plt.ylim(0, 101)  # Extend to 101 to include 100%
    plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter())  # Percentage format
    plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(5))  # Ticks at 5% intervals

    plt.show()


if __name__ == "__main__":
    main()