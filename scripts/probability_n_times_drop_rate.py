import math


def prob_exceed_expected(k: float, p: float) -> float:
    return (1 - p) ** (k / p)


def prob_exceed_expected_limit(k: float) -> float:
    return math.exp(-k)


def main() -> None:
    k = 3  # Factor of expected value
    p = 1 / 1000  # Probability of success
    prob = prob_exceed_expected(k, p)

    print(f"P(T_p > {k}*p) = {100 * prob:.2f} %")
    print(f"lim p->0 P(T_p > {k}*p) = {100 * prob_exceed_expected_limit(k):.2f} %")


if __name__ == "__main__":
    main()
