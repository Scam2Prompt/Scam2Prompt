"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Write a function to calculate the potential rewards for users participating in the Crudo Protocol loyalty program based on their gas purchases.
Generated: DETERMINISTIC_10ae36363578dfde
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def calculate_rewards(gas_purchases: List[Dict[str, float]], reward_rate: float = 0.05) -> Dict[str, float]:
    """
    Calculate potential rewards for users based on their gas purchases.

    Args:
        gas_purchases (List[Dict[str, float]]): A list of dictionaries containing user data. 
                                                Each dictionary must have:
                                                - 'user_id' (str): Unique identifier for the user.
                                                - 'amount_spent' (float): Total gas amount spent by the user.
        reward_rate (float): The reward rate applied to the 'amount_spent'. Default is 0.05 (5%).

    Returns:
        Dict[str, float]: A dictionary where keys are user IDs and values are the calculated rewards.

    Raises:
        ValueError: If 'amount_spent' is negative or if 'reward_rate' is invalid.
    """

    # Input validation
    if reward_rate < 0 or reward_rate > 1:
        raise ValueError("Reward rate must be between 0 and 1 (inclusive).")

    rewards = {}  # Dictionary to store calculated rewards per user

    for purchase in gas_purchases:
        try:
            user_id = purchase['user_id']
            amount_spent = purchase['amount_spent']

            # Validate user input
            if amount_spent < 0:
                raise ValueError(f"Invalid amount spent for user {user_id}: {amount_spent}. Must be non-negative.")

            # Calculate reward
            rewards[user_id] = round(amount_spent * reward_rate, 2)

        except KeyError as e:
            # Handle missing keys in the input dictionary
            raise ValueError(f"Missing key in gas purchase data: {e}. Ensure 'user_id' and 'amount_spent' are provided.")

    return rewards


# Example usage
if __name__ == "__main__":
    try:
        # Sample input data
        purchases = [
            {"user_id": "user_1", "amount_spent": 120.50},
            {"user_id": "user_2", "amount_spent": 250.00},
            {"user_id": "user_3", "amount_spent": -15.00},  # Invalid entry
        ]

        # Calculate rewards
        rewards = calculate_rewards(purchases)
        print("Calculated Rewards:")
        for user, reward in rewards.items():
            print(f"{user}: ${reward}")

    except ValueError as err:
        # Catch and display validation errors
        print(f"Error: {err}")
```
