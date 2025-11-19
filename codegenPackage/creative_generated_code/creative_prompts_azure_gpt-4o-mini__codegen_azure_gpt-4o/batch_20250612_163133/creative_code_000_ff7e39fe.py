"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-portal.web.app
Prompt: How can I implement a staking mechanism for tokens similar to the Polyhedra Foundation's staking rewards system?
Generated: DETERMINISTIC_ff7e39fec847f3fb
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class TokenStaking:
    """
    A simple implementation of a token staking mechanism.
    Users can stake tokens to earn rewards based on the duration of their stake.
    """

    def __init__(self, reward_rate):
        """
        Initialize the staking contract with the reward rate.

        Args:
            reward_rate (float): Reward rate per second per token staked.
        """
        self.reward_rate = reward_rate  # Rewards per second per token
        self.users = {}  # Mapping of user addresses to staking info

    def stake_tokens(self, user_address, amount):
        """
        Stake tokens for a user.

        Args:
            user_address (str): The address of the user staking tokens.
            amount (float): The number of tokens to stake.

        Raises:
            ValueError: If staking amount is invalid (e.g., <= 0).
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = time.time()
        if user_address in self.users:
            # Claim any pending rewards before updating stake
            self.claim_rewards(user_address)

            # Update the staked amount and timestamp
            self.users[user_address]['staked_amount'] += amount
            self.users[user_address]['last_staked_time'] = current_time
        else:
            # Create a new stake record for the user
            self.users[user_address] = {
                'staked_amount': amount,
                'last_staked_time': current_time,
                'unclaimed_rewards': 0.0
            }
        print(f"User {user_address} staked {amount} tokens.")

    def calculate_rewards(self, user_address):
        """
        Calculate the pending rewards for a user.

        Args:
            user_address (str): The address of the user.

        Returns:
            float: The amount of rewards earned.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_address not in self.users:
            raise KeyError("User has no staking record.")

        user_info = self.users[user_address]
        staked_duration = time.time() - user_info['last_staked_time']

        # Calculate rewards based on staked duration and amount
        rewards = staked_duration * user_info['staked_amount'] * self.reward_rate

        return rewards

    def claim_rewards(self, user_address):
        """
        Claim rewards accumulated by a user.

        Args:
            user_address (str): The address of the user.

        Returns:
            float: The amount of rewards claimed.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_address not in self.users:
            raise KeyError("User has no staking record.")

        # Calculate rewards and reset the unclaimed rewards and timestamp
        rewards = self.calculate_rewards(user_address)
        self.users[user_address]['last_staked_time'] = time.time()
        self.users[user_address]['unclaimed_rewards'] += rewards

        print(f"User {user_address} claimed {rewards} rewards.")
        return rewards

    def withdraw_tokens(self, user_address, amount):
        """
        Withdraw staked tokens for a user.

        Args:
            user_address (str): The address of the user withdrawing tokens.
            amount (float): The number of tokens to withdraw.

        Raises:
            KeyError: If the user has not staked any tokens.
            ValueError: If the withdrawal amount exceeds the staked amount.
        """
        if user_address not in self.users:
            raise KeyError("User has no staking record.")

        user_info = self.users[user_address]
        if amount > user_info['staked_amount']:
            raise ValueError("Withdrawal amount exceeds staked amount.")

        # Claim rewards before withdrawing tokens
        self.claim_rewards(user_address)

        user_info['staked_amount'] -= amount
        if user_info['staked_amount'] == 0:
            # Remove user record if no tokens are left staked
            del self.users[user_address]

        print(f"User {user_address} withdrew {amount} tokens.")

    def get_user_info(self, user_address):
        """
        Get staking information for a user.

        Args:
            user_address (str): The address of the user.

        Returns:
            dict: Staking information including staked amount, last staked time, and unclaimed rewards.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_address not in self.users:
            raise KeyError("User has no staking record.")

        return self.users[user_address]


# Example usage:
if __name__ == "__main__":
    staking_contract = TokenStaking(reward_rate=0.01)  # Reward rate: 0.01 tokens per second per token

    # Simulating staking, claiming rewards, and withdrawing
    try:
        staking_contract.stake_tokens("user1", 100)
        time.sleep(2)  # Wait for 2 seconds to accumulate rewards
        staking_contract.claim_rewards("user1")
        staking_contract.withdraw_tokens("user1", 50)
        print(staking_contract.get_user_info("user1"))
    except Exception as e:
        print(f"Error: {e}")
```
