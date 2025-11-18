"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appwienerclaim.pages.dev
Prompt: Generate code to implement a staking mechanism for $WAI tokens, ensuring rewards calculation based on the provided APY of 177%.
Generated: DETERMINISTIC_153c6232f3812370
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import math

class TokenStaking:
    """
    Implements a staking mechanism for $WAI tokens with rewards calculated
    based on an Annual Percentage Yield (APY) of 177%.
    """

    def __init__(self, apy=177):
        """
        Initializes the staking system with a specified APY.

        :param apy: Annual Percentage Yield for rewards calculation (default: 177%)
        """
        self.apy = apy
        self.stakers = {}  # Records staking information for each user

    def stake_tokens(self, user_id, amount):
        """
        Stake tokens for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        if user_id not in self.stakers:
            self.stakers[user_id] = {
                "amount": 0,
                "start_time": None,
                "last_updated": None
            }

        # Add to the staked amount and update the timestamps
        self.stakers[user_id]["amount"] += amount
        self.stakers[user_id]["start_time"] = self.stakers[user_id]["start_time"] or datetime.now()
        self.stakers[user_id]["last_updated"] = datetime.now()

    def unstake_tokens(self, user_id):
        """
        Unstake tokens for a user and calculate the rewards.

        :param user_id: Unique identifier for the user.
        :return: Tuple containing (staked_amount, rewards).
        """
        if user_id not in self.stakers or self.stakers[user_id]["amount"] <= 0:
            raise ValueError("No tokens staked for the user.")

        staked_data = self.stakers[user_id]
        staked_amount = staked_data["amount"]
        start_time = staked_data["start_time"]

        # Calculate rewards based on APY and staking duration
        duration_in_days = (datetime.now() - start_time).days
        rewards = self.calculate_rewards(staked_amount, duration_in_days)

        # Clear staking data after unstaking
        self.stakers[user_id] = {
            "amount": 0,
            "start_time": None,
            "last_updated": None
        }

        return staked_amount, rewards

    def calculate_rewards(self, staked_amount, duration_in_days):
        """
        Calculate rewards based on the APY and duration.

        :param staked_amount: Amount of tokens staked.
        :param duration_in_days: Duration for which tokens were staked.
        :return: Calculated rewards.
        """
        if duration_in_days <= 0:
            return 0

        # APY is annual, so we calculate daily rate
        daily_rate = self.apy / 100 / 365
        total_rewards = staked_amount * (math.pow(1 + daily_rate, duration_in_days) - 1)
        return total_rewards

    def get_staking_info(self, user_id):
        """
        Retrieve staking information for a specific user.

        :param user_id: Unique identifier for the user.
        :return: Dictionary containing staking details.
        """
        if user_id not in self.stakers:
            return None

        return self.stakers[user_id]


# Example usage of the TokenStaking class
if __name__ == "__main__":
    staking_system = TokenStaking(apy=177)

    try:
        # User stakes tokens
        staking_system.stake_tokens(user_id="user1", amount=1000)
        print("User1 staking info:", staking_system.get_staking_info("user1"))

        # Simulate passing time (example: 30 days later)
        staking_system.stakers["user1"]["start_time"] -= timedelta(days=30)

        # User unstakes tokens and receives rewards
        staked_amount, rewards = staking_system.unstake_tokens(user_id="user1")
        print(f"User1 unstaked {staked_amount} tokens with rewards: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
