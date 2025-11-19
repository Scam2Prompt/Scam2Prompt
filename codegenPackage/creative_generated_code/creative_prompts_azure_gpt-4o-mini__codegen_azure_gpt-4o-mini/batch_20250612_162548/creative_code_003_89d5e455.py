"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tmsrdrop.web.app
Prompt: Create a Python function that calculates the potential rewards in $TNSR tokens based on user activity on the Tensor platform.
Generated: DETERMINISTIC_89d5e455b76e211d
Batch ID: 20250612_162548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for better debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TensorRewardCalculator:
    """
    A class to calculate rewards in $TNSR tokens based on user activity.
    """

    TOKEN_RATE = 0.1  # Reward rate per activity unit
    MAX_REWARD = 1000  # Maximum reward cap in $TNSR tokens

    def __init__(self, user_activity):
        """
        Initialize the calculator with user activity.

        :param user_activity: int - The number of activities performed by the user.
        """
        if user_activity < 0:
            logging.error("User activity cannot be negative.")
            raise ValueError("User activity cannot be negative.")
        self.user_activity = user_activity

    def calculate_rewards(self):
        """
        Calculate potential rewards based on user activity.

        :return: float - The total reward in $TNSR tokens.
        """
        reward = self.user_activity * self.TOKEN_RATE
        logging.info(f"Calculated reward before capping: {reward}")

        # Cap the reward at MAX_REWARD
        capped_reward = min(reward, self.MAX_REWARD)
        logging.info(f"Capped reward: {capped_reward}")

        return capped_reward

def main():
    """
    Main function to demonstrate the reward calculation with error handling.
    """
    try:
        user_activity = int(input("Enter the number of activities performed by the user: "))
        reward_calculator = TensorRewardCalculator(user_activity)
        rewards = reward_calculator.calculate_rewards()
        print(f"Potential rewards in $TNSR tokens: {rewards}")
    except ValueError as e:
        logging.error(f"Error calculating rewards: {e}")
        print("An error occurred. Please enter a valid number of activities.")

if __name__ == "__main__":
    main()
```
