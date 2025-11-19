"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Create a function that calculates potential earnings from staking $SCORP tokens based on the number of tokens held.
Generated: DETERMINISTIC_9173d302f0db4146
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_staking_earnings(tokens_held: int, annual_percentage_rate: float, days_staked: int) -> Union[float, str]:
    """
    Calculate potential earnings from staking $SCORP tokens.

    Args:
        tokens_held (int): The number of $SCORP tokens a user holds.
        annual_percentage_rate (float): The annual percentage rate (APR) of staking rewards (in percentage).
        days_staked (int): The number of days the tokens are staked.

    Returns:
        Union[float, str]: Potential earnings from staking. Returns an error message if input is invalid.
    """
    try:
        # Input validation
        if tokens_held <= 0:
            return "Error: tokens_held must be greater than 0."
        if annual_percentage_rate <= 0:
            return "Error: annual_percentage_rate must be greater than 0."
        if days_staked <= 0:
            return "Error: days_staked must be greater than 0."

        # Calculate daily rate from APR
        daily_rate = annual_percentage_rate / 100 / 365  # Convert APR to daily percentage

        # Calculate earnings
        earnings = tokens_held * daily_rate * days_staked

        return round(earnings, 2)  # Return earnings rounded to two decimal places for clarity

    except Exception as e:
        # Catch any unforeseen errors and return a descriptive message
        return f"An unexpected error occurred: {e}"


# Example usage (optional, remove in production):
if __name__ == "__main__":
    tokens = 1000
    apr = 12.5  # Example APR: 12.5%
    days = 30   # Example staking period: 30 days

    potential_earnings = calculate_staking_earnings(tokens, apr, days)
    print(f"Potential earnings from staking: ${potential_earnings}")
```
