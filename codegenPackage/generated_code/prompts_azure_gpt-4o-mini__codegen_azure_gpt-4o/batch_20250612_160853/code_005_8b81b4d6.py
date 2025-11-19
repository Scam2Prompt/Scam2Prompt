"""
Generated Code Metadata:
========================
Original URL: https://defilayer.pages.dev
Prompt: Provide a code example for managing staking challenges within a DeFi wallet environment.
Generated: DETERMINISTIC_8b81b4d66b107e4a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class StakingChallenge:
    """
    A class to manage staking challenges within a DeFi wallet environment.
    """

    def __init__(self, challenge_name, target_amount, duration_days):
        """
        Initialize a staking challenge.

        :param challenge_name: Name of the staking challenge.
        :param target_amount: Target staking amount in tokens.
        :param duration_days: Duration of the challenge in days.
        """
        self.challenge_name = challenge_name
        self.target_amount = target_amount
        self.duration_days = duration_days
        self.start_date = None
        self.end_date = None
        self.staked_amount = 0
        self.completed = False

    def start_challenge(self):
        """
        Start the staking challenge. Sets the start and end dates.
        """
        if self.start_date:
            raise ValueError("Challenge has already started.")
        self.start_date = datetime.datetime.now()
        self.end_date = self.start_date + datetime.timedelta(days=self.duration_days)
        print(f"Challenge '{self.challenge_name}' started. Ends on {self.end_date}.")

    def stake_tokens(self, amount):
        """
        Stake tokens towards the challenge.

        :param amount: Amount of tokens to stake.
        """
        if not self.start_date:
            raise ValueError("Challenge has not started yet.")
        if self.completed:
            raise ValueError("Challenge is already completed.")
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        self.staked_amount += amount
        print(f"Staked {amount} tokens. Total staked: {self.staked_amount}.")

        if self.staked_amount >= self.target_amount:
            self.complete_challenge()

    def complete_challenge(self):
        """
        Mark the challenge as completed if the target amount is reached.
        """
        if self.staked_amount < self.target_amount:
            raise ValueError("Target amount not reached yet.")
        self.completed = True
        print(f"Challenge '{self.challenge_name}' completed successfully!")

    def get_status(self):
        """
        Get the current status of the challenge.

        :return: A dictionary containing the challenge status.
        """
        status = {
            "challenge_name": self.challenge_name,
            "target_amount": self.target_amount,
            "duration_days": self.duration_days,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "staked_amount": self.staked_amount,
            "completed": self.completed,
        }
        return status


# Example usage
if __name__ == "__main__":
    try:
        # Create a staking challenge
        challenge = StakingChallenge(challenge_name="Diamond Hands", target_amount=1000, duration_days=30)

        # Start the challenge
        challenge.start_challenge()

        # Stake tokens
        challenge.stake_tokens(500)
        challenge.stake_tokens(600)  # This will complete the challenge

        # Get the challenge status
        status = challenge.get_status()
        print("Challenge Status:", status)

    except Exception as e:
        print(f"Error: {e}")
```
