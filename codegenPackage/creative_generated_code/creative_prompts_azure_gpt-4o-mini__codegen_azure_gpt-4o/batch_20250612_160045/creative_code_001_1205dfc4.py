"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.live
Prompt: Write a function that calculates cashback rewards for users based on their betting losses, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_1205dfc43f688e2e
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict

def calculate_cashback(losses: Dict[str, float], cashback_rate: float) -> Dict[str, float]:
    """
    Calculate cashback rewards for users based on their betting losses.
    
    Args:
        losses (Dict[str, float]): A dictionary where the keys are user IDs (str) and the values are their betting losses (float).
        cashback_rate (float): The percentage of cashback rewards to return, expressed as a decimal (e.g., 0.10 for 10%).
        
    Returns:
        Dict[str, float]: A dictionary where the keys are user IDs and the values are their cashback rewards.
    """
    # Validate input parameters
    if not isinstance(losses, dict):
        raise ValueError("Losses must be provided as a dictionary with user IDs as keys and losses as values.")
    if not isinstance(cashback_rate, (float, int)) or cashback_rate < 0 or cashback_rate > 1:
        raise ValueError("Cashback rate must be a number between 0 and 1 (inclusive).")

    # Initialize the result dictionary
    cashback_rewards = {}
    
    # Iterate over the losses dictionary to calculate cashback rewards
    for user_id, loss in losses.items():
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string.")
        if not isinstance(loss, (float, int)) or loss < 0:
            raise ValueError(f"Loss amount for user {user_id} must be a non-negative number.")
        
        # Calculate cashback reward for each user
        cashback_rewards[user_id] = round(loss * cashback_rate, 2)  # Round to 2 decimal places for monetary values
    
    return cashback_rewards

# Example usage:
if __name__ == "__main__":
    # Sample user losses
    user_losses = {
        "user123": 500.0,
        "user456": 1200.75,
        "user789": 300.50,
    }
    
    # Define a cashback rate (e.g., 10%)
    rate = 0.10
    
    try:
        # Calculate cashback rewards
        rewards = calculate_cashback(user_losses, rate)
        
        # Print the results
        for user, reward in rewards.items():
            print(f"User {user} receives a cashback reward of ${reward:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
