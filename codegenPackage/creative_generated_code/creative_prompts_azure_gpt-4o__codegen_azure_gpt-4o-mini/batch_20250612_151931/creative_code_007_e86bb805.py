"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Write a function that enforces the 24-hour claim restriction for $BANANA rewards, ensuring users cannot claim more frequently than allowed.
Generated: DETERMINISTIC_e86bb805e4265dc1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class RewardClaimError(Exception):
    """Custom exception for reward claim violations."""
    pass

class BananaRewardSystem:
    def __init__(self):
        # Dictionary to track the last claim time for each user
        self.user_claim_times = {}

    def can_claim_reward(self, user_id):
        """
        Check if a user is eligible to claim the reward.

        Args:
            user_id (str): The ID of the user.

        Returns:
            bool: True if the user can claim the reward, False otherwise.
        """
        current_time = datetime.now()

        # Get the last claim time for the user, defaulting to None if not found
        last_claim_time = self.user_claim_times.get(user_id)

        if last_claim_time is None:
            # User has never claimed before
            return True
        
        # Calculate the time difference since the last claim
        time_difference = current_time - last_claim_time
        
        # Check if 24 hours have passed
        return time_difference >= timedelta(hours=24)

    def claim_reward(self, user_id):
        """
        Allow a user to claim their reward if eligible.

        Args:
            user_id (str): The ID of the user.

        Raises:
            RewardClaimError: If the user has claimed the reward within 24 hours.
        """
        if not self.can_claim_reward(user_id):
            raise RewardClaimError("You can only claim your $BANANA reward once every 24 hours.")

        # Process the reward claim (e.g., add to user balance)
        self.process_reward(user_id)

        # Update the last claim time for the user
        self.user_claim_times[user_id] = datetime.now()

    def process_reward(self, user_id):
        """
        Simulate processing the reward for a user.

        Args:
            user_id (str): The ID of the user.
        """
        # Here you would add the reward logic, e.g., updating user balance
        print(f"Reward for user {user_id} has been successfully claimed.")

# Example usage
if __name__ == "__main__":
    reward_system = BananaRewardSystem()
    user_id = "user123"

    try:
        reward_system.claim_reward(user_id)  # First claim should succeed
        time.sleep(1)  # Simulating a short wait
        reward_system.claim_reward(user_id)  # This should raise an error
    except RewardClaimError as e:
        print(e)
```
