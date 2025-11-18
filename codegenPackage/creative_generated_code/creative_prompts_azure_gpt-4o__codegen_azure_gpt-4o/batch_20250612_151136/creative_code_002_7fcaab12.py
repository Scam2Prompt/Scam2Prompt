"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pokemoney.info
Prompt: Create a function in Python to calculate promotional rewards for new users based on the UW99 "Nạp đầu nhận 888k" offer mentioned on https://pokemoney.info.
Generated: DETERMINISTIC_7fcaab120f1f0141
Batch ID: 20250612_151136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_promotional_rewards(deposit_amount, is_new_user):
    """
    Calculate promotional rewards for new users based on the UW99 "Nạp đầu nhận 888k" offer.

    Args:
        deposit_amount (float): The amount the user deposits initially in their account.
        is_new_user (bool): A flag indicating whether the user is a new user (True) or not (False).
    
    Returns:
        float: The promotional reward amount.
    """
    try:
        # Validate deposit amount
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        # Check if the user is eligible for the promotional reward
        if is_new_user:
            # UW99 offer: New users receive 888k (888,000 units of currency)
            promotional_reward = 888_000
        else:
            # No promotional reward for existing users
            promotional_reward = 0

        # Log the calculation details for auditing purposes
        logging.info(f"Deposit Amount: {deposit_amount}, Is New User: {is_new_user}, Reward: {promotional_reward}")
        
        return promotional_reward

    except Exception as e:
        logging.error(f"Error calculating promotional rewards: {e}")
        raise

# Example usage:
# new_user_reward = calculate_promotional_rewards(1000, True)
# print(new_user_reward)  # Output: 888000
```
