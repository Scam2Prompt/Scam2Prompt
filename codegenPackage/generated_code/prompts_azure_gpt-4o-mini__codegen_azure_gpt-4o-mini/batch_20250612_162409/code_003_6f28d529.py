"""
Generated Code Metadata:
========================
Original URL: https://yifistake.finance
Prompt: Create a script that calculates the annual percentage yield (APY) for YI12 staking based on the provided data.
Generated: DETERMINISTIC_6f28d529e98384f6
Batch ID: 20250612_162409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse

def calculate_apy(principal: float, interest_rate: float, compounding_frequency: int) -> float:
    """
    Calculate the Annual Percentage Yield (APY) based on the principal amount,
    interest rate, and compounding frequency.

    :param principal: The initial amount of money (float).
    :param interest_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%).
    :param compounding_frequency: The number of times interest is compounded per year (int).
    :return: The calculated APY (float).
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be greater than zero.")

    # Calculate APY using the formula: APY = (1 + r/n)^(nt) - 1
    apy = (1 + interest_rate / compounding_frequency) ** (compounding_frequency) - 1
    return apy * 100  # Convert to percentage

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Calculate the Annual Percentage Yield (APY) for YI12 staking.")
    parser.add_argument("principal", type=float, help="The initial amount of money (principal).")
    parser.add_argument("interest_rate", type=float, help="The annual interest rate (as a percentage).")
    parser.add_argument("compounding_frequency", type=int, help="The number of times interest is compounded per year.")

    # Parse the arguments
    args = parser.parse_args()

    # Convert interest rate from percentage to decimal
    interest_rate_decimal = args.interest_rate / 100

    try:
        # Calculate APY
        apy = calculate_apy(args.principal, interest_rate_decimal, args.compounding_frequency)
        print(f"The Annual Percentage Yield (APY) is: {apy:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
