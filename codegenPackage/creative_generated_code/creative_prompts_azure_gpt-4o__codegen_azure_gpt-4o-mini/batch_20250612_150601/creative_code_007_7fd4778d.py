"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ed-boxes.web.app
Prompt: Write a function to calculate and display rewards for users based on their activity level on a Solana-based NFT marketplace.
Generated: DETERMINISTIC_7fd4778dea386288
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """
    Represents a user in the NFT marketplace.
    
    Attributes:
        username (str): The username of the user.
        activity_level (int): The activity level of the user, representing the number of transactions.
    """
    def __init__(self, username: str, activity_level: int):
        self.username = username
        self.activity_level = activity_level

    def __str__(self):
        return f"User(username={self.username}, activity_level={self.activity_level})"

def calculate_rewards(activity_level: int) -> float:
    """
    Calculate rewards based on user activity level.

    Args:
        activity_level (int): The user's activity level.

    Returns:
        float: The calculated rewards.
    
    Raises:
        ValueError: If activity_level is negative.
    """
    if activity_level < 0:
        logging.error("Activity level cannot be negative")
        raise ValueError("Activity level cannot be negative")

    # Define a reward structure based on activity level
    reward_per_transaction = 0.05  # Reward amount per transaction
    rewards = activity_level * reward_per_transaction
    logging.info(f"Calculated rewards: {rewards} for activity level: {activity_level}")
    return rewards

def display_rewards(user: User) -> None:
    """
    Display the rewards for a given user based on their activity level.

    Args:
        user (User): The user for whom to display rewards.
    """
    try:
        rewards = calculate_rewards(user.activity_level)
        print(f"{user.username} has earned {rewards:.2f} SOL in rewards.")
    except ValueError as e:
        print(f"Error calculating rewards for {user.username}: {e}")

# Example usage
if __name__ == "__main__":
    # Create a user with an activity level
    user1 = User(username="NFTCollector123", activity_level=20)
    
    # Display rewards for the user
    display_rewards(user1)

    # Uncomment the following line to see error handling for a negative activity level
    # user_invalid = User(username="InvalidUser", activity_level=-5)
    # display_rewards(user_invalid)
```
