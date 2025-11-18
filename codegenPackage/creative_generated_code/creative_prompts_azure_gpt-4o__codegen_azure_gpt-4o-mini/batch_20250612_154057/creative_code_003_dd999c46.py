"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sosphon.xyz
Prompt: Write a program that automates the process of claiming SOPH rewards and ensures the user qualifies for Bronze, Silver, or Gold Staker status based on their staking percentage and duration.
Generated: DETERMINISTIC_dd999c4691e12ff2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class Staker:
    STATUS_LEVELS = {
        'Bronze': (0.01, 30),  # Minimum staking percentage and duration (in days)
        'Silver': (0.05, 60),
        'Gold': (0.1, 90)
    }

    def __init__(self, user_id, staking_percentage, staking_duration):
        self.user_id = user_id
        self.staking_percentage = staking_percentage
        self.staking_duration = staking_duration  # in days
        self.reward_claimed = False

    def check_status(self):
        """
        Check the user's staker status based on staking percentage and duration.
        
        Returns:
            str: The staker status (Bronze, Silver, Gold, or None)
        """
        for status, (min_percentage, min_duration) in self.STATUS_LEVELS.items():
            if (self.staking_percentage >= min_percentage and
                self.staking_duration >= min_duration):
                return status
        return None

    def claim_rewards(self):
        """
        Claim the rewards for the user based on their staker status.
        
        Raises:
            RuntimeError: If rewards have already been claimed or the user does not qualify.
        
        Returns:
            str: Confirmation message with the staker status.
        """
        if self.reward_claimed:
            raise RuntimeError("Rewards have already been claimed.")
        
        status = self.check_status()
        if not status:
            raise RuntimeError("User does not qualify for any rewards.")

        # Simulating reward claiming process
        time.sleep(1)  # Simulate network delay
        self.reward_claimed = True
        return f"Rewards claimed successfully for {self.user_id}. Status: {status}"

def main():
    try:
        # Sample user data - in a real scenario, this would come from a database or API
        user_id = 'user123'
        staking_percentage = 0.07  # Example staking percentage
        staking_duration = 45  # Example staking duration in days

        # Create a Staker instance
        staker = Staker(user_id, staking_percentage, staking_duration)

        # Claim rewards
        result = staker.claim_rewards()
        print(result)
        
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
