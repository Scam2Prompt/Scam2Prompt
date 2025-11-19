"""
Generated Code Metadata:
========================
Original URL: https://paalofficial.vercel.app
Prompt: Design a staking system that allows users to lock up a portion of their cryptocurrency for a period of time, earning rewards in the form of additional coins or tokens.
Generated: DETERMINISTIC_d5f1d287708c4cab
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import hashlib

class StakingSystem:
    def __init__(self):
        # Initialize an empty dictionary to store user staking information
        self.staking_info = {}

    def stake(self, user_id, amount, duration):
        """
        Stake a portion of cryptocurrency for a period of time.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of cryptocurrency to stake.
            duration (int): Duration of staking in days.

        Returns:
            bool: True if staking is successful, False otherwise.
        """
        # Check if user already has an active stake
        if user_id in self.staking_info:
            return False

        # Calculate the end time of staking
        end_time = datetime.datetime.now() + datetime.timedelta(days=duration)

        # Create a staking info dictionary
        staking_info = {
            'amount': amount,
            'start_time': datetime.datetime.now(),
            'end_time': end_time,
            'reward': self.calculate_reward(amount, duration)
        }

        # Store the staking info
        self.staking_info[user_id] = staking_info

        return True

    def calculate_reward(self, amount, duration):
        """
        Calculate the reward based on the staked amount and duration.

        Args:
            amount (float): Amount of cryptocurrency staked.
            duration (int): Duration of staking in days.

        Returns:
            float: Reward amount.
        """
        # For simplicity, assume a fixed reward rate of 5% per day
        reward_rate = 0.05
        return amount * reward_rate * duration

    def unstake(self, user_id):
        """
        Unstake cryptocurrency before the end time.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            bool: True if unstaking is successful, False otherwise.
        """
        # Check if user has an active stake
        if user_id not in self.staking_info:
            return False

        # Check if the staking period has ended
        if datetime.datetime.now() < self.staking_info[user_id]['end_time']:
            # Calculate the penalty for early unstaking (e.g., 10% of staked amount)
            penalty = self.staking_info[user_id]['amount'] * 0.1
            self.staking_info[user_id]['amount'] -= penalty

        # Remove the staking info
        del self.staking_info[user_id]

        return True

    def claim_reward(self, user_id):
        """
        Claim the reward after the staking period has ended.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            bool: True if claiming is successful, False otherwise.
        """
        # Check if user has an active stake
        if user_id not in self.staking_info:
            return False

        # Check if the staking period has ended
        if datetime.datetime.now() < self.staking_info[user_id]['end_time']:
            return False

        # Claim the reward
        reward = self.staking_info[user_id]['reward']
        del self.staking_info[user_id]

        return reward

    def get_staking_info(self, user_id):
        """
        Get the staking information for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: Staking information, or None if user has no active stake.
        """
        return self.staking_info.get(user_id)


def hash_transaction(transaction):
    """
    Hash a transaction using SHA-256.

    Args:
        transaction (dict): Transaction data.

    Returns:
        str: Hashed transaction.
    """
    transaction_str = str(transaction).encode('utf-8')
    return hashlib.sha256(transaction_str).hexdigest()


def main():
    staking_system = StakingSystem()

    # Example usage:
    user_id = "user123"
    amount = 100.0
    duration = 30  # days

    # Stake
    if staking_system.stake(user_id, amount, duration):
        print(f"Staking successful for user {user_id}")
    else:
        print(f"Staking failed for user {user_id}")

    # Get staking info
    staking_info = staking_system.get_staking_info(user_id)
    if staking_info:
        print(f"Staking info for user {user_id}: {staking_info}")
    else:
        print(f"No staking info found for user {user_id}")

    # Claim reward
    reward = staking_system.claim_reward(user_id)
    if reward:
        print(f"Reward claimed: {reward}")
    else:
        print(f"Failed to claim reward")

    # Unstake
    if staking_system.unstake(user_id):
        print(f"Unstaking successful for user {user_id}")
    else:
        print(f"Unstaking failed for user {user_id}")


if __name__ == "__main__":
    main()
```
