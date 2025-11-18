"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Generate a script to calculate cashback bonuses for users based on the Vavada platform's bonus program, including variables for deposit amounts and activity levels.
Generated: DETERMINISTIC_f324a4a458973952
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate cashback bonuses for users based on the Vavada platform's bonus program.
The cashback percentage is determined by deposit amounts and activity levels.
"""

# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for cashback calculation
CASHBACK_RATES = {
    "low_activity": 0.01,  # 1% cashback
    "medium_activity": 0.03,  # 3% cashback
    "high_activity": 0.05  # 5% cashback
}

# Thresholds for deposit amounts
DEPOSIT_THRESHOLDS = {
    "low_activity": 1000,  # Minimum deposit for low activity level
    "medium_activity": 5000,  # Minimum deposit for medium activity level
    "high_activity": 10000  # Minimum deposit for high activity level
}

def calculate_cashback(deposit_amount, activity_level):
    """
    Calculate the cashback bonus for a user.

    Args:
        deposit_amount (float): The amount of deposit made by the user.
        activity_level (str): The activity level of the user ('low_activity', 'medium_activity', or 'high_activity').

    Returns:
        float: The cashback bonus amount.
    """
    try:
        if activity_level not in CASHBACK_RATES:
            raise ValueError(f"Invalid activity level: {activity_level}")

        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")

        # Determine cashback rate based on activity level
        cashback_rate = CASHBACK_RATES[activity_level]

        # Ensure deposit meets the threshold for the given activity level
        if deposit_amount < DEPOSIT_THRESHOLDS[activity_level]:
            logging.warning(f"Deposit amount ${deposit_amount} does not meet the threshold for {activity_level}. Cashback will not be applied.")
            return 0.0

        # Calculate cashback bonus
        cashback_bonus = deposit_amount * cashback_rate
        logging.info(f"Cashback calculated: ${cashback_bonus:.2f} for deposit ${deposit_amount} at activity level {activity_level}.")
        return cashback_bonus

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return 0.0
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 0.0

# Example usage of the script
if __name__ == "__main__":
    # User deposit and activity level
    user_deposit = 7000  # Example deposit amount
    user_activity = "medium_activity"  # Example activity level

    # Calculate cashback bonus for the user
    cashback = calculate_cashback(user_deposit, user_activity)
    print(f"Cashback Bonus: ${cashback:.2f}")
```
