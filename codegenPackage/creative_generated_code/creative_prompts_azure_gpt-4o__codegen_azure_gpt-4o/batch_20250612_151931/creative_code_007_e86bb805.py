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
from datetime import datetime, timedelta

class ClaimRestriction:
    def __init__(self):
        """
        Initializes the ClaimRestriction instance.
        Keeps track of the last claim time for each user.
        """
        self.last_claim_times = {}  # Dictionary to store the last claim time for each user

    def can_claim(self, user_id):
        """
        Checks if the user is eligible to claim rewards based on the 24-hour restriction.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            bool: True if the user can claim, False otherwise.
        """
        last_claim_time = self.last_claim_times.get(user_id, None)
        if last_claim_time is None:
            # User has not claimed before, so they can claim
            return True
        # Check if 24 hours have passed since the last claim
        return datetime.now() >= last_claim_time + timedelta(hours=24)

    def claim_reward(self, user_id):
        """
        Allows a user to claim rewards if eligible and updates their last claim time.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: A message indicating the status of the claim.
        """
        try:
            if self.can_claim(user_id):
                # User is eligible to claim
                self.last_claim_times[user_id] = datetime.now()
                return f"Success! $BANANA reward claimed for user {user_id}."
            else:
                # User cannot claim yet
                remaining_time = (self.last_claim_times[user_id] + timedelta(hours=24)) - datetime.now()
                return f"Error: User {user_id} cannot claim yet. Try again in {remaining_time}."
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An unexpected error occurred: {e}"

# Example usage:
if __name__ == "__main__":
    claim_restriction = ClaimRestriction()

    user_id = "user123"
    print(claim_restriction.claim_reward(user_id))  # First attempt - should succeed
    print(claim_restriction.claim_reward(user_id))  # Second attempt - should fail
```
