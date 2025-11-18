"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-virtuswap.pages.dev
Prompt: Write code to simulate a staking mechanism for a DeFi application, inspired by the Virtuswap staking functionality.
Generated: DETERMINISTIC_94bfced884177923
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class StakingContract:
    """
    A simple staking contract class for a DeFi application.
    Users can stake tokens to earn rewards based on the staking duration.
    """

    def __init__(self, reward_rate_per_day: float):
        """
        Initializes the staking contract with a reward rate.

        :param reward_rate_per_day: The daily reward rate (percentage of staked amount).
        """
        if reward_rate_per_day <= 0:
            raise ValueError("Reward rate must be a positive value")
        
        self.reward_rate_per_day = reward_rate_per_day  # Daily reward rate in percentage
        self.stakers = {}  # Dictionary to track staking details for each user

    def stake_tokens(self, user: str, amount: float):
        """
        Allows a user to stake tokens.

        :param user: The user ID.
        :param amount: The amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero")

        current_time = datetime.now()
        if user in self.stakers:
            # If the user already staked, add to their existing stake
            self._update_rewards(user)
            self.stakers[user]['amount'] += amount
            self.stakers[user]['start_time'] = current_time
        else:
            # Create a new staking entry for the user
            self.stakers[user] = {
                'amount': amount,
                'start_time': current_time,
                'pending_rewards': 0.0,
            }

    def unstake_tokens(self, user: str):
        """
        Allows a user to unstake their tokens and claim rewards.

        :param user: The user ID.
        :return: A tuple containing the unstaked amount and the reward earned.
        """
        if user not in self.stakers:
            raise ValueError("User has no tokens staked")

        self._update_rewards(user)
        staked_data = self.stakers.pop(user)
        amount = staked_data['amount']
        rewards = staked_data['pending_rewards']

        return amount, rewards

    def _update_rewards(self, user: str):
        """
        Internal method to update the pending rewards for a user.

        :param user: The user ID.
        """
        if user not in self.stakers:
            raise ValueError("User has no tokens staked")

        current_time = datetime.now()
        staked_data = self.stakers[user]
        staking_duration = (current_time - staked_data['start_time']).total_seconds() / 86400  # Convert seconds to days
        rewards = staked_data['amount'] * self.reward_rate_per_day * staking_duration / 100
        staked_data['pending_rewards'] += rewards
        staked_data['start_time'] = current_time  # Reset start time for future rewards

    def get_staking_info(self, user: str):
        """
        Retrieves the staking information for a user.

        :param user: The user ID.
        :return: A dictionary containing the staking details.
        """
        if user not in self.stakers:
            raise ValueError("User has no tokens staked")

        self._update_rewards(user)
        return self.stakers[user]

    def calculate_rewards(self, user: str):
        """
        Calculates the rewards for a user without unstaking.

        :param user: The user ID.
        :return: The pending reward amount.
        """
        if user not in self.stakers:
            raise ValueError("User has no tokens staked")

        self._update_rewards(user)
        return self.stakers[user]['pending_rewards']


# Example usage
if __name__ == "__main__":
    try:
        staking_contract = StakingContract(reward_rate_per_day=1.0)

        # User stakes tokens
        staking_contract.stake_tokens(user="Alice", amount=100.0)
        print("Staking info after staking:", staking_contract.get_staking_info("Alice"))

        # Simulate time passing (for demonstration purposes)
        import time
        time.sleep(2)  # Wait for 2 seconds

        # User checks rewards
        print("Rewards for Alice:", staking_contract.calculate_rewards("Alice"))

        # User unstakes tokens
        unstaked_amount, reward = staking_contract.unstake_tokens(user="Alice")
        print(f"Alice unstaked {unstaked_amount} tokens and earned {reward} rewards.")

    except Exception as e:
        print(f"Error: {e}")
```
