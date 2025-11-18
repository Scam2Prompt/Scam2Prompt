"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdwon.com
Prompt: Create a function to track and display the total claimed rewards and active participants in a cryptocurrency reward program, similar to usdwon.com.
Generated: DETERMINISTIC_5e5b6298d4e4ff3c
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardProgram:
    def __init__(self):
        """
        Initialize the RewardProgram with zero total rewards and no active participants.
        """
        self.total_claimed_rewards = 0.0
        self.active_participants = set()

    def claim_reward(self, participant_id, amount):
        """
        Function to allow a participant to claim a reward.

        Parameters:
        - participant_id: Unique identifier for the participant (str).
        - amount: Amount of rewards to be claimed (float).

        Raises:
        - ValueError: If the amount is negative or participant_id is empty.
        """
        if amount < 0:
            raise ValueError("Claimed amount must be a non-negative value.")
        if not participant_id:
            raise ValueError("Participant ID cannot be empty.")

        # Add the participant to active participants
        self.active_participants.add(participant_id)
        
        # Update the total claimed rewards
        self.total_claimed_rewards += amount

    def display_summary(self):
        """
        Display the total claimed rewards and the number of active participants.
        """
        print(f"Total Claimed Rewards: ${self.total_claimed_rewards:.2f}")
        print(f"Active Participants: {len(self.active_participants)}")

# Example usage
if __name__ == "__main__":
    # Create an instance of RewardProgram
    reward_program = RewardProgram()

    # Participants claim rewards
    try:
        reward_program.claim_reward("user123", 50.0)
        reward_program.claim_reward("user456", 25.0)
        reward_program.claim_reward("user123", 10.0)  # user123 claims again
        reward_program.claim_reward("user789", -5.0)   # This will raise an exception
    except ValueError as e:
        print(f"Error occurred: {e}")

    # Display the summary of rewards and participants
    reward_program.display_summary()
```
