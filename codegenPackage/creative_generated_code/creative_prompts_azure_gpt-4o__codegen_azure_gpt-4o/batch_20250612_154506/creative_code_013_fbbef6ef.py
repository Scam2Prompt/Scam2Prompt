"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a Python script to calculate and distribute promotional bonuses based on user deposits, as outlined in VZ99's first deposit promotion.
Generated: DETERMINISTIC_fbbef6ef4ce23420
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_bonus(deposit_amount):
    """
    Calculate promotional bonuses based on deposit amounts.
    VZ99's first deposit promotion:
    - Deposits up to $100 get a 20% bonus.
    - Deposits between $101 and $500 get a 15% bonus.
    - Deposits above $500 get a 10% bonus.

    Args:
        deposit_amount (float): The initial deposit amount.

    Returns:
        float: The calculated bonus.
    """
    try:
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        if deposit_amount <= 100:
            bonus = deposit_amount * 0.20
        elif deposit_amount <= 500:
            bonus = deposit_amount * 0.15
        else:
            bonus = deposit_amount * 0.10

        return bonus
    except ValueError as ve:
        logging.error(f"Error calculating bonus: {ve}")
        raise

def distribute_bonus(user_deposits):
    """
    Distribute promotional bonuses based on user deposits.

    Args:
        user_deposits (dict): A dictionary containing user IDs and deposit amounts.

    Returns:
        dict: A dictionary with user IDs and their respective bonuses.
    """
    bonuses = {}

    for user_id, deposit_amount in user_deposits.items():
        try:
            logging.info(f"Calculating bonus for user {user_id} with deposit ${deposit_amount:.2f}")
            bonus = calculate_bonus(deposit_amount)
            bonuses[user_id] = bonus
            logging.info(f"Bonus for user {user_id}: ${bonus:.2f}")
        except Exception as e:
            logging.error(f"Failed to calculate bonus for user {user_id}: {e}")
            bonuses[user_id] = None  # Indicate failure to calculate bonus for this user

    return bonuses

def main():
    """
    Main function to execute the promotional bonus calculation and distribution.
    """
    # Example user deposits
    user_deposits = {
        "user_1": 50.0,
        "user_2": 150.0,
        "user_3": 600.0,
        "user_4": -10.0,  # Invalid deposit amount
    }

    logging.info("Starting promotional bonus distribution...")
    bonuses = distribute_bonus(user_deposits)

    logging.info("Promotional bonuses distributed:")
    for user_id, bonus in bonuses.items():
        if bonus is not None:
            logging.info(f"User {user_id}: Bonus ${bonus:.2f}")
        else:
            logging.info(f"User {user_id}: Failed to calculate bonus.")

if __name__ == "__main__":
    main()
```
