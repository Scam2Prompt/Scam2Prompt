"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Write a Python script that calculates the actual interest from DeFi yield rates, considering the nuances of APY as discussed in the article.
Generated: DETERMINISTIC_63ac86ff1cb36fc3
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DeFi Yield Rate Calculator

Calculates the actual interest from DeFi yield rates, considering the nuances of APY.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_defi_yield(principal: float, apy: float, compounding_frequency: int, time_in_years: float) -> float:
    """
    Calculate the actual interest from DeFi yield rates.

    Args:
    - principal (float): The initial investment amount.
    - apy (float): The annual percentage yield (APY) as a decimal.
    - compounding_frequency (int): The number of times interest is compounded per year.
    - time_in_years (float): The time the money is invested for, in years.

    Returns:
    - float: The final amount after interest has been applied.

    Raises:
    - ValueError: If principal, apy, or time_in_years is negative.
    - ValueError: If compounding_frequency is not a positive integer.
    """

    # Validate inputs
    if principal < 0 or apy < 0 or time_in_years < 0:
        raise ValueError("Principal, APY, and time in years must be non-negative.")
    if compounding_frequency <= 0 or not isinstance(compounding_frequency, int):
        raise ValueError("Compounding frequency must be a positive integer.")

    # Calculate the final amount using the formula for compound interest
    final_amount = principal * (1 + apy / compounding_frequency) ** (compounding_frequency * time_in_years)

    return final_amount


def calculate_actual_interest(principal: float, apy: float, compounding_frequency: int, time_in_years: float) -> float:
    """
    Calculate the actual interest earned.

    Args:
    - principal (float): The initial investment amount.
    - apy (float): The annual percentage yield (APY) as a decimal.
    - compounding_frequency (int): The number of times interest is compounded per year.
    - time_in_years (float): The time the money is invested for, in years.

    Returns:
    - float: The actual interest earned.

    Raises:
    - ValueError: If principal, apy, or time_in_years is negative.
    - ValueError: If compounding_frequency is not a positive integer.
    """

    final_amount = calculate_defi_yield(principal, apy, compounding_frequency, time_in_years)
    actual_interest = final_amount - principal

    return actual_interest


def main():
    try:
        principal = 1000.0  # Initial investment of $1000
        apy = 0.20  # 20% APY
        compounding_frequency = 365  # Compounded daily
        time_in_years = 1.0  # 1 year

        final_amount = calculate_defi_yield(principal, apy, compounding_frequency, time_in_years)
        actual_interest = calculate_actual_interest(principal, apy, compounding_frequency, time_in_years)

        print(f"Final Amount: ${final_amount:.2f}")
        print(f"Actual Interest: ${actual_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
