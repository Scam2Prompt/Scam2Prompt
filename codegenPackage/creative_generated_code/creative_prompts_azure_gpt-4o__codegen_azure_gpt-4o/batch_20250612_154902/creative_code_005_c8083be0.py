"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cotidashboard.com
Prompt: Generate a Python script to calculate rewards for a user depositing $COTI in the COTI Treasury, factoring in both Base APY and Boost APY.
Generated: DETERMINISTIC_c8083be0177c3a22
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_rewards(deposit_amount, base_apy, boost_apy, days_deposited):
    """
    Calculate rewards for a user depositing $COTI in the COTI Treasury.

    Parameters:
        deposit_amount (float): The amount of $COTI deposited.
        base_apy (float): Base Annual Percentage Yield (APY) in percentage (e.g., 5 for 5%).
        boost_apy (float): Boost Annual Percentage Yield (APY) in percentage (e.g., 2 for 2%).
        days_deposited (int): Number of days the deposit is held.

    Returns:
        float: Total rewards accumulated over the given period.
    """
    try:
        # Validate inputs
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        if base_apy < 0 or boost_apy < 0:
            raise ValueError("APY values must be non-negative.")
        if days_deposited <= 0:
            raise ValueError("Days deposited must be greater than 0.")

        # Calculate total APY (Base APY + Boost APY)
        total_apy = base_apy + boost_apy

        # Convert APY to daily rate (percentage -> decimal)
        daily_rate = total_apy / 100 / 365

        # Calculate rewards
        rewards = deposit_amount * daily_rate * days_deposited

        return rewards
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    try:
        # User input for deposit details
        deposit_amount = float(input("Enter deposit amount ($COTI): "))
        base_apy = float(input("Enter Base APY (%): "))
        boost_apy = float(input("Enter Boost APY (%): "))
        days_deposited = int(input("Enter number of days deposited: "))

        # Calculate rewards
        rewards = calculate_rewards(deposit_amount, base_apy, boost_apy, days_deposited)

        if rewards is not None:
            print(f"Total rewards for depositing ${deposit_amount} $COTI over {days_deposited} days: {rewards:.2f} $COTI")
        else:
            print("Unable to calculate rewards due to invalid inputs.")
    except Exception as e:
        logging.error(f"Error during user input or calculation: {e}")
```
