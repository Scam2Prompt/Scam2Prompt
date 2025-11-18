"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delta-tlkslkla.pages.dev
Prompt: Using the Delta Points system, create a function to calculate and display user rewards based on their trading activity.
Generated: DETERMINISTIC_6e0c9c27c56615d6
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

# Define constants for reward calculation
REWARD_MULTIPLIER = 0.05  # 5% of delta points are converted to rewards
MINIMUM_TRADES_FOR_REWARD = 10  # Minimum trades required to be eligible for rewards

# Custom exception for invalid data
class InvalidTradingDataError(Exception):
    pass

def calculate_rewards(trading_data: List[Dict[str, int]]) -> Dict[str, float]:
    """
    Calculate and display user rewards based on their trading activity.

    Args:
        trading_data (List[Dict[str, int]]): List of dictionaries containing user trading data. 
            Each dictionary must have the following keys:
                - 'user_id' (str): Unique identifier for the user.
                - 'delta_points' (int): Points earned by the user.
                - 'trades' (int): Number of trades completed by the user.

    Returns:
        Dict[str, float]: Dictionary mapping user IDs to their reward values.

    Raises:
        InvalidTradingDataError: If the trading data is invalid or improperly formatted.
    """
    if not isinstance(trading_data, list):
        raise InvalidTradingDataError("Trading data must be a list of dictionaries.")
    
    # Initialize the rewards dictionary
    rewards = {}

    # Iterate through user trading data
    for user_data in trading_data:
        # Validate input data
        if not isinstance(user_data, dict):
            raise InvalidTradingDataError("Each user data must be a dictionary.")
        if 'user_id' not in user_data or 'delta_points' not in user_data or 'trades' not in user_data:
            raise InvalidTradingDataError("Missing required keys in user data.")
        if not isinstance(user_data['user_id'], str) or not isinstance(user_data['delta_points'], int) or not isinstance(user_data['trades'], int):
            raise InvalidTradingDataError("Invalid data type for user data fields.")

        user_id = user_data['user_id']
        delta_points = user_data['delta_points']
        trades = user_data['trades']

        # Check if user meets the minimum trade requirement
        if trades >= MINIMUM_TRADES_FOR_REWARD:
            # Calculate reward based on delta points
            rewards[user_id] = round(delta_points * REWARD_MULTIPLIER, 2)
        else:
            # If minimum trade requirement is not met, set reward to 0
            rewards[user_id] = 0.0

    return rewards

# Example usage: Define trading data and calculate rewards
if __name__ == "__main__":
    try:
        trading_data = [
            {"user_id": "user123", "delta_points": 1000, "trades": 15},
            {"user_id": "user456", "delta_points": 500, "trades": 8},
            {"user_id": "user789", "delta_points": 2000, "trades": 20},
        ]
        
        # Calculate rewards
        user_rewards = calculate_rewards(trading_data)
        
        # Display rewards
        print("User Rewards:")
        for user_id, reward in user_rewards.items():
            print(f"{user_id}: ${reward}")
    except InvalidTradingDataError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
