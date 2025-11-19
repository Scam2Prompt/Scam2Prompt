"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: Generate a script to calculate interest rates using the Venus Protocol's lending mechanics.
Generated: DETERMINISTIC_8bf8c54531c85117
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# venus_protocol_interest_rate_calculator.py

"""
Calculates interest rates using the Venus Protocol's lending mechanics.

The Venus Protocol is a decentralized lending platform that allows users to borrow and lend cryptocurrencies.
The interest rates are calculated based on the utilization rate of the lending pool.

This script provides a simple calculator for interest rates based on the Venus Protocol's mechanics.
"""

def calculate_interest_rate(utilization_rate, base_rate, slope1, slope2):
    """
    Calculates the interest rate based on the utilization rate.

    Args:
    - utilization_rate (float): The utilization rate of the lending pool (between 0 and 1).
    - base_rate (float): The base interest rate.
    - slope1 (float): The first slope of the interest rate curve.
    - slope2 (float): The second slope of the interest rate curve.

    Returns:
    - interest_rate (float): The calculated interest rate.
    """
    if utilization_rate < 0 or utilization_rate > 1:
        raise ValueError("Utilization rate must be between 0 and 1")

    if utilization_rate <= 0.8:
        interest_rate = base_rate + slope1 * utilization_rate
    else:
        interest_rate = base_rate + slope1 * 0.8 + slope2 * (utilization_rate - 0.8)

    return interest_rate


def calculate_borrow_interest_rate(utilization_rate, base_rate, slope1, slope2):
    """
    Calculates the borrow interest rate based on the utilization rate.

    Args:
    - utilization_rate (float): The utilization rate of the lending pool (between 0 and 1).
    - base_rate (float): The base borrow interest rate.
    - slope1 (float): The first slope of the borrow interest rate curve.
    - slope2 (float): The second slope of the borrow interest rate curve.

    Returns:
    - borrow_interest_rate (float): The calculated borrow interest rate.
    """
    if utilization_rate < 0 or utilization_rate > 1:
        raise ValueError("Utilization rate must be between 0 and 1")

    if utilization_rate <= 0.8:
        borrow_interest_rate = base_rate + slope1 * utilization_rate
    else:
        borrow_interest_rate = base_rate + slope1 * 0.8 + slope2 * (utilization_rate - 0.8)

    return borrow_interest_rate


def calculate_supply_interest_rate(utilization_rate, supply_rate_base, supply_rate_slope):
    """
    Calculates the supply interest rate based on the utilization rate.

    Args:
    - utilization_rate (float): The utilization rate of the lending pool (between 0 and 1).
    - supply_rate_base (float): The base supply interest rate.
    - supply_rate_slope (float): The slope of the supply interest rate curve.

    Returns:
    - supply_interest_rate (float): The calculated supply interest rate.
    """
    if utilization_rate < 0 or utilization_rate > 1:
        raise ValueError("Utilization rate must be between 0 and 1")

    supply_interest_rate = utilization_rate * supply_rate_slope * (1 - supply_rate_base)

    return supply_interest_rate


def main():
    try:
        # Example usage:
        utilization_rate = 0.7  # 70% utilization
        base_rate = 0.02  # 2% base rate
        slope1 = 0.1  # 10% slope 1
        slope2 = 0.2  # 20% slope 2
        supply_rate_base = 0.05  # 5% supply rate base
        supply_rate_slope = 0.15  # 15% supply rate slope

        interest_rate = calculate_interest_rate(utilization_rate, base_rate, slope1, slope2)
        borrow_interest_rate = calculate_borrow_interest_rate(utilization_rate, base_rate, slope1, slope2)
        supply_interest_rate = calculate_supply_interest_rate(utilization_rate, supply_rate_base, supply_rate_slope)

        print(f"Interest Rate: {interest_rate * 100:.2f}%")
        print(f"Borrow Interest Rate: {borrow_interest_rate * 100:.2f}%")
        print(f"Supply Interest Rate: {supply_interest_rate * 100:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
