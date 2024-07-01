import random
from functools import cache

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from tqdm import tqdm

from blp.conditional_probability_from_cdf import conditional_probability_from_cdf
from blp.negative_binomial_cdf import negative_binomial_cdf


def simulate_number_of_trials_naive(
    expected_value: float, number_simulations: int = 10000
) -> list[int]:
    assert expected_value >= 1
    p = 1 / expected_value
    trials_to_success: list[int] = []
    for _ in tqdm(range(number_simulations)):
        number_trials = 0
        while True:
            number_trials += 1
            if random.uniform(0, 1) < p:
                trials_to_success.append(number_trials)
                break
    return trials_to_success


def simulate_number_of_trials_bad_luck_protection(
    expected_value: float, number_simulations: int = 10000, alpha: float = 0.5
) -> list[int]:
    assert expected_value >= 1
    conditional_probability = cache(
        conditional_probability_from_cdf(
            cdf=lambda k: negative_binomial_cdf(k, expected_value, alpha=alpha)
        )
    )
    trials_to_success: list[int] = []
    for _ in tqdm(range(number_simulations)):
        number_trials = 0
        while True:
            number_trials += 1
            if random.uniform(0, 1) < conditional_probability(number_trials):
                trials_to_success.append(number_trials)
                break
    return trials_to_success


def main_cdf() -> None:
    expected_value: float = 100.0
    n_simulations = 10000
    alpha_values: list[float] = [0.5, 0.2]

    trials_to_success_naive = simulate_number_of_trials_naive(
        expected_value=expected_value, number_simulations=n_simulations
    )
    values_naive, base_naive = np.histogram(
        trials_to_success_naive,
        bins=100,
        range=(0, round(expected_value * 5) + 1),
        density=True,
    )
    cumulative_naive = np.cumsum(values_naive / np.sum(values_naive)) * 100

    plt.figure(figsize=(10, 6))
    plt.plot(base_naive[:-1], cumulative_naive, label="CDF Naive")
    for alpha in alpha_values:
        trials_to_success_blp = simulate_number_of_trials_bad_luck_protection(
            expected_value=expected_value, number_simulations=n_simulations, alpha=alpha
        )
        values_blp, base_blp = np.histogram(
            trials_to_success_blp,
            bins=100,
            range=(0, round(expected_value * 5) + 1),
            density=True,
        )
        cumulative_blp = np.cumsum(values_blp / np.sum(values_blp)) * 100
        plt.plot(base_blp[:-1], cumulative_blp, label=f"CDF Bad Luck Protection (α={alpha})")
    plt.axhline(y=95, color="r", linestyle="dashed", linewidth=0.8)  # Horizontal line at 95%
    plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter())
    plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(5))
    plt.xlabel("Number of Rolls Until Success")
    plt.ylabel("Cumulative Probability")
    plt.title("Simulated Cumulative Distribution of Number of Rolls Until Success")
    plt.legend()
    plt.show()


def main_pdf() -> None:
    expected_value: float = 100.0
    n_simulations = 1000000
    alpha_values: list[float] = [0.5, 0.2]
    trials_to_success_naive = simulate_number_of_trials_naive(
        expected_value=expected_value, number_simulations=n_simulations
    )

    values_naive, base_naive = np.histogram(
        trials_to_success_naive,
        bins=100,
        range=(0, round(expected_value * 5) + 1),
        density=True,
    )

    plt.figure(figsize=(10, 6))
    plt.plot(base_naive[:-1], values_naive, label="PDF Naive")
    for alpha in alpha_values:
        trials_to_success_blp = simulate_number_of_trials_bad_luck_protection(
            expected_value=expected_value, number_simulations=n_simulations, alpha=alpha
        )
        values_blp, base_blp = np.histogram(
            trials_to_success_blp,
            bins=100,
            range=(0, round(expected_value * 5) + 1),
            density=True,
        )
        plt.plot(base_blp[:-1], values_blp, label=f"PDF Bad Luck Protection (α={alpha})")
    plt.xlabel("Number of Rolls Until Success")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.title("Simulated Distribution of Number of Rolls Until Success")
    plt.show()


if __name__ == "__main__":
    main_pdf()
