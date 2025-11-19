"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.live
Prompt: Develop a function to calculate cashback rewards for users based on their betting activity, inspired by the loyalty programs at BaxBet.
Generated: DETERMINISTIC_10968bd49680a076
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# cashback_rewards.py

# Import necessary module for type hinting
from typing import List, Dict

def calculate_cashback(betting_data: List[Dict[str, float]], cashback_rate: float) -> Dict[str, float]:
    """
    Calculate cashback rewards for users based on their betting activity.
    
    Args:
        betting_data (List[Dict[str, float]]): A list of dictionaries containing user betting data.
            Each dictionary must have the keys:
                - 'user_id' (str): Unique identifier for the user.
                - 'bet_amount' (float): Total amount bet by the user.
        cashback_rate (float): The percentage cashback rate (e.g., 0.05 for 5% cashback).
    
    Returns:
        Dict[str, float]: A dictionary where keys are user IDs and values are cashback rewards.
    
    Raises:
        ValueError: If `cashback_rate` is negative or exceeds 1 (invalid percentage).
        ValueError: If any bet amount is negative.
    """
    # Validate the cashback rate
    if cashback_rate < 0 or cashback_rate > 1:
        raise ValueError("Cashback rate must be between 0 and 1.")
    
    # Initialize the cashback rewards dictionary
    cashback_rewards = {}

    for entry in betting_data:
        user_id = entry.get('user_id')
        bet_amount = entry.get('bet_amount')

        # Check if both user_id and bet_amount are present
        if user_id is None or bet_amount is None:
            raise ValueError("Each entry must contain 'user_id' and 'bet_amount' keys.")

        # Validate the bet amount
        if bet_amount < 0:
            raise ValueError(f"Bet amount cannot be negative for user '{user_id}'.")

        # Calculate cashback reward
        reward = bet_amount * cashback_rate

        # Add the reward to the dictionary
        cashback_rewards[user_id] = reward
    
    return cashback_rewards

# Example usage of the function
if __name__ == "__main__":
    try:
        # Example betting data
        betting_data = [
            {"user_id": "user123", "bet_amount": 500.0},
            {"user_id": "user456", "bet_amount": 300.0},
            {"user_id": "user789", "bet_amount": 100.0},
        ]
        cashback_rate = 0.05  # 5% cashback
        
        # Calculate cashback rewards
        rewards = calculate_cashback(betting_data, cashback_rate)
        
        # Display results
        for user_id, reward in rewards.items():
            print(f"User '{user_id}' cashback reward: ${reward:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
