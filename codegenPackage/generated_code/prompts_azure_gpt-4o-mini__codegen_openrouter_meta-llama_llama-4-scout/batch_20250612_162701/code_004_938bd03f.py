"""
Generated Code Metadata:
========================
Original URL: https://assets-maple.finance
Prompt: Create a function that calculates potential yields for BTC holders using Maple's BTC Yield Product, considering the target APY of 5%.
Generated: DETERMINISTIC_938bd03f8221faf9
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_potential_yields(principal: float, days: int, target_apy: float = 0.05) -> Dict[str, float]:
    """
    Calculate potential yields for BTC holders using Maple's BTC Yield Product.

    Args:
    - principal (float): The initial amount of BTC.
    - days (int): The number of days to calculate the yield for.
    - target_apy (float, optional): The target annual percentage yield. Defaults to 0.05 (5%).

    Returns:
    - Dict[str, float]: A dictionary containing the principal, interest, and total amount.
    """

    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if days < 0:
        raise ValueError("Days cannot be negative.")
    if target_apy < 0 or target_apy > 1:
        raise ValueError("Target APY must be between 0 and 1.")

    # Calculate the daily interest rate
    daily_interest_rate = (target_apy / 365)

    # Calculate the total amount using the formula for compound interest
    total_amount = principal * (1 + daily_interest_rate) ** days

    # Calculate the interest earned
    interest = total_amount - principal

    # Return the results as a dictionary
    return {
        "principal": principal,
        "interest": interest,
        "total_amount": total_amount,
    }


def main():
    try:
        principal = 1.0  # 1 BTC
        days = 365  # 1 year
        target_apy = 0.05  # 5%

        result = calculate_potential_yields(principal, days, target_apy)

        print("Potential Yields:")
        print(f"Principal: {result['principal']:.8f} BTC")
        print(f"Interest: {result['interest']:.8f} BTC")
        print(f"Total Amount: {result['total_amount']:.8f} BTC")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
