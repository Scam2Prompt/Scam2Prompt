"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Create a function that simulates the compounding rewards for Sidus staking over a specified lock term on SidusPad.
Generated: DETERMINISTIC_d54d00850cd6af42
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_staking_rewards(initial_amount, annual_percentage_rate, term_in_days):
    """
    Simulates compounding staking rewards over a specified lock term.

    :param initial_amount: float - Initial staked amount in SIDUS tokens.
    :param annual_percentage_rate: float - Annual Percentage Rate (APR) in percentage (e.g., 15 for 15% APR).
    :param term_in_days: int - Number of days tokens are staked/locked.
    :return: dict - A dictionary containing final staked amount and total earned rewards.
    """
    try:
        # Validate input
        if initial_amount <= 0:
            raise ValueError("Initial staking amount must be greater than 0.")
        if annual_percentage_rate <= 0:
            raise ValueError("Annual Percentage Rate (APR) must be greater than 0.")
        if term_in_days <= 0:
            raise ValueError("Staking term must be greater than 0 days.")

        # Constants
        DAYS_IN_YEAR = 365

        # Convert APR to daily rate (percentage to decimal)
        daily_rate = annual_percentage_rate / 100 / DAYS_IN_YEAR

        # Calculate final amount using compound interest formula
        # A = P * (1 + r)^t
        final_amount = initial_amount * math.pow((1 + daily_rate), term_in_days)

        # Calculate total rewards earned
        total_rewards = final_amount - initial_amount

        # Return results in a dictionary
        return {
            "initial_amount": round(initial_amount, 2),
            "final_amount": round(final_amount, 2),
            "total_rewards": round(total_rewards, 2)
        }
    except ValueError as ve:
        # Handle invalid input errors
        return {"error": f"Invalid input: {str(ve)}"}
    except Exception as e:
        # Catch any unforeseen errors
        return {"error": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    staking_result = calculate_staking_rewards(
        initial_amount=1000, 
        annual_percentage_rate=15, 
        term_in_days=90
    )
    print(staking_result)
```
