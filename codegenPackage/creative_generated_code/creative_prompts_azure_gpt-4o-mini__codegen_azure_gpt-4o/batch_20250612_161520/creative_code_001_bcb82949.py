"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: How can I implement a staking mechanism for $MGLS tokens that rewards users based on their share of the staking pool?
Generated: DETERMINISTIC_bcb82949f85c0dcf
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class StakingPool:
    """
    A class that represents a staking pool for $MGLS tokens.
    Users can stake tokens and earn rewards proportional to their share of the pool.
    """
    def __init__(self, reward_rate_per_second: float):
        """
        Initializes the staking pool.

        Args:
            reward_rate_per_second (float): Rate at which rewards are distributed 
                                            per second for the entire pool.
        """
        self.total_staked = 0.0  # Total tokens staked in the pool
        self.reward_rate_per_second = reward_rate_per_second  # Reward rate per second for the pool
        self.users = {}  # Tracks user stakes, rewards, and last update time
    
    def stake(self, user: str, amount: float):
        """
        Allows a user to stake tokens into the pool.

        Args:
            user (str): The user's identifier (e.g. wallet address, username).
            amount (float): The number of $MGLS tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Update rewards before changing the user's stake
        self._update_rewards(user)

        # Update total staked tokens and user's staked amount
        self.total_staked += amount
        if user not in self.users:
            self.users[user] = {'staked': 0.0, 'rewards': 0.0, 'last_update': datetime.now()}
        self.users[user]['staked'] += amount
        self.users[user]['last_update'] = datetime.now()

    def withdraw(self, user: str, amount: float):
        """
        Allows a user to withdraw their staked tokens and rewards.

        Args:
            user (str): The user's identifier.
            amount (float): The number of $MGLS tokens to withdraw.
        """
        if user not in self.users or self.users[user]['staked'] <= 0:
            raise ValueError("No staked tokens found for user.")
        if amount <= 0 or amount > self.users[user]['staked']:
            raise ValueError("Invalid withdrawal amount.")

        # Update rewards before changing the user's stake
        self._update_rewards(user)

        # Update total staked tokens and user's staked amount
        self.total_staked -= amount
        self.users[user]['staked'] -= amount

        # Simulate transfer of staked tokens and rewards to the user
        withdrawn_rewards = self.users[user]['rewards']
        self.users[user]['rewards'] = 0.0
        self.users[user]['last_update'] = datetime.now()

        return {
            'withdrawn_tokens': amount,
            'rewards': withdrawn_rewards
        }

    def claim_rewards(self, user: str):
        """
        Allows a user to claim their accumulated rewards.

        Args:
            user (str): The user's identifier.
        """
        if user not in self.users:
            raise ValueError("No rewards found for user.")

        # Update rewards before claiming
        self._update_rewards(user)

        claimed_rewards = self.users[user]['rewards']
        self.users[user]['rewards'] = 0.0
        self.users[user]['last_update'] = datetime.now()

        return claimed_rewards

    def _update_rewards(self, user: str):
        """
        Updates the user's rewards based on the time elapsed and their pool share.

        Args:
            user (str): The user's identifier.
        """
        if user not in self.users:
            return

        user_data = self.users[user]
        if user_data['staked'] == 0:
            return
        
        # Calculate time elapsed since last update
        now = datetime.now()
        elapsed_time = (now - user_data['last_update']).total_seconds()

        # Calculate user's share of the rewards
        pool_share = user_data['staked'] / self.total_staked if self.total_staked > 0 else 0
        rewards = elapsed_time * self.reward_rate_per_second * pool_share
        user_data['rewards'] += rewards
        user_data['last_update'] = now

    def get_user_info(self, user: str):
        """
        Retrieves the user's staking information.

        Args:
            user (str): The user's identifier.

        Returns:
            dict: A dictionary containing the user's staked tokens, rewards, and last update time.
        """
        if user not in self.users:
            return {"staked": 0.0, "rewards": 0.0, "last_update": None}
        
        self._update_rewards(user)
        return self.users[user]


# Example usage:
if __name__ == "__main__":
    pool = StakingPool(reward_rate_per_second=0.01)  # 0.01 $MGLS rewards per second for the pool

    # User staking
    pool.stake("user1", 100)
    pool.stake("user2", 200)

    # Simulate time passing
    import time
    time.sleep(5)  # Wait for 5 seconds

    # User information
    print(pool.get_user_info("user1"))
    print(pool.get_user_info("user2"))

    # Claim rewards
    print(pool.claim_rewards("user1"))

    # Withdraw staked tokens
    print(pool.withdraw("user2", 50))
```
