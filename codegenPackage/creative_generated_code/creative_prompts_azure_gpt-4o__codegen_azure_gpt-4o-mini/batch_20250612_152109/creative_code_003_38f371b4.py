"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pufferr.pages.dev
Prompt: Write a script to calculate staking multipliers and double Puffer Points for registered users in Chapter 3, based on the rules described on the Puffer.fi website.
Generated: DETERMINISTIC_38f371b43a836426
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    def __init__(self, user_id: str, registered: bool, staked_amount: float):
        """
        Initialize a User object.

        :param user_id: Unique identifier for the user.
        :param registered: Boolean indicating if the user is registered.
        :param staked_amount: Amount of tokens staked by the user.
        """
        self.user_id = user_id
        self.registered = registered
        self.staked_amount = staked_amount

def calculate_staking_multiplier(user: User) -> float:
    """
    Calculate the staking multiplier based on the staked amount.

    :param user: User object containing user's staking information.
    :return: Staking multiplier for the user.
    """
    # Define the multiplier rules (example values)
    if user.staked_amount < 100:
        return 1.0
    elif user.staked_amount < 1000:
        return 1.5
    else:
        return 2.0

def calculate_puffer_points(users: List[User]) -> Dict[str, float]:
    """
    Calculate double Puffer Points for all registered users based on their staking multiplier.

    :param users: List of User objects.
    :return: Dictionary mapping user IDs to their calculated Puffer Points.
    """
    puffer_points = {}
    
    for user in users:
        # Check if the user is registered
        if not user.registered:
            logging.warning(f"User {user.user_id} is not registered. Skipping calculation.")
            continue
        
        try:
            multiplier = calculate_staking_multiplier(user)
            points = user.staked_amount * multiplier * 2  # Double the points
            puffer_points[user.user_id] = points
            logging.info(f"Calculated {points} Puffer Points for user {user.user_id} with multiplier {multiplier}.")
        except Exception as e:
            logging.error(f"Error calculating Puffer Points for user {user.user_id}: {e}")
    
    return puffer_points

if __name__ == "__main__":
    # Sample user data
    users = [
        User("user1", True, 50),
        User("user2", True, 150),
        User("user3", False, 200),
        User("user4", True, 1200)
    ]

    # Calculate Puffer Points
    results = calculate_puffer_points(users)
    
    # Output results
    for user_id, points in results.items():
        print(f"User: {user_id}, Puffer Points: {points}")
```
