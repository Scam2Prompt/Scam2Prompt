"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Provide code to implement a staking mechanism for CRUDO tokens, allowing token holders to earn passive income, as described in the Crudo Protocol roadmap.
Generated: DETERMINISTIC_e7ab90dcffd6a0b4
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_mechanism.py

from datetime import datetime, timedelta

class TokenStaking:
    """
    A class to implement a staking mechanism for CRUDO tokens
    where token holders can earn passive income.
    """

    def __init__(self, annual_interest_rate: float):
        """
        Initializes the staking mechanism.

        :param annual_interest_rate: Annual interest rate for staking in percentage (e.g., 5.0 for 5% APR).
        """
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be greater than 0.")
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.stakers = {}  # Dictionary to store staking information for each user

    def stake_tokens(self, user_id: str, amount: float):
        """
        Allows a user to stake CRUDO tokens.

        :param user_id: Unique identifier for the user (e.g., username or wallet address).
        :param amount: Number of CRUDO tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be greater than 0.")
        current_time = datetime.now()

        # Add or update the user's staking information
        if user_id in self.stakers:
            self.stakers[user_id]["amount"] += amount
            self.stakers[user_id]["last_stake_time"] = current_time
        else:
            self.stakers[user_id] = {
                "amount": amount,
                "last_stake_time": current_time,
                "rewards": 0.0
            }

    def calculate_rewards(self, user_id: str):
        """
        Calculates the rewards for a specific user based on their staking duration.

        :param user_id: Unique identifier for the user.
        :return: The calculated rewards.
        """
        if user_id not in self.stakers:
            raise ValueError(f"No staking information found for user: {user_id}")

        staking_info = self.stakers[user_id]
        staked_amount = staking_info["amount"]
        last_stake_time = staking_info["last_stake_time"]

        # Calculate the staking duration in days
        current_time = datetime.now()
        staking_duration_days = (current_time - last_stake_time).days

        if staking_duration_days <= 0:
            return 0.0

        # Formula: Rewards = Staked Amount * (APR / 365) * Staking Duration (in days)
        rewards = staked_amount * (self.annual_interest_rate / 365) * staking_duration_days
        return rewards

    def claim_rewards(self, user_id: str):
        """
        Allows the user to claim their rewards.

        :param user_id: Unique identifier for the user.
        :return: The claimed rewards amount.
        """
        if user_id not in self.stakers:
            raise ValueError(f"No staking information found for user: {user_id}")

        # Calculate rewards and reset last stake time
        rewards = self.calculate_rewards(user_id)
        self.stakers[user_id]["rewards"] += rewards
        self.stakers[user_id]["last_stake_time"] = datetime.now()

        return rewards

    def unstake_tokens(self, user_id: str):
        """
        Allows a user to unstake their tokens, including any pending rewards.

        :param user_id: Unique identifier for the user.
        :return: The total amount returned to the user (staked amount + rewards).
        """
        if user_id not in self.stakers:
            raise ValueError(f"No staking information found for user: {user_id}")

        staking_info = self.stakers[user_id]
        staked_amount = staking_info["amount"]
        pending_rewards = self.calculate_rewards(user_id)

        # Total amount returned to the user
        total_return = staked_amount + pending_rewards + staking_info["rewards"]

        # Remove user from staking records
        del self.stakers[user_id]

        return total_return

    def get_staking_info(self, user_id: str):
        """
        Fetches staking information for a specific user.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing staking details.
        """
        if user_id not in self.stakers:
            raise ValueError(f"No staking information found for user: {user_id}")

        return self.stakers[user_id]


# Example usage
if __name__ == "__main__":
    try:
        staking = TokenStaking(5.0)  # Initialize staking with 5% APR

        # User stakes tokens
        staking.stake_tokens("user1", 1000)
        print("Staking info:", staking.get_staking_info("user1"))

        # Simulate passage of time
        print("Rewards after 30 days:", staking.calculate_rewards("user1"))

        # User claims rewards
        claimed_rewards = staking.claim_rewards("user1")
        print("Claimed Rewards:", claimed_rewards)
        print("Updated Staking info:", staking.get_staking_info("user1"))

        # User unstakes tokens
        total_return = staking.unstake_tokens("user1")
        print("Total return after unstaking:", total_return)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
