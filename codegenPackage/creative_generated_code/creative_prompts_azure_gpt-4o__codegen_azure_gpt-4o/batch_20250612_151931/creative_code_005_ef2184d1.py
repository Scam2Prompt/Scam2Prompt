"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Create a system that tracks reward forfeiture when a user sells or transfers more than 300 $BANANA tokens during an epoch, redistributing forfeited rewards among other holders.
Generated: DETERMINISTIC_ef2184d103ef70a7
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from collections import defaultdict

class BananaRewardTracker:
    """
    A system to track reward forfeiture when users sell or transfer 
    more than 300 $BANANA tokens during an epoch. 
    Forfeited rewards are redistributed among other holders.
    """

    def __init__(self, epoch_duration_seconds=86400):
        """
        Initializes the reward tracker system.
        
        :param epoch_duration_seconds: Duration of an epoch in seconds (default: 1 day).
        """
        self.epoch_duration = epoch_duration_seconds
        self.current_epoch_start = time.time()
        self.user_balances = defaultdict(int)  # Tracks $BANANA token balances for each user
        self.user_rewards = defaultdict(float)  # Tracks rewards for each user
        self.forfeited_rewards_pool = 0  # Pool for redistributed forfeited rewards
        self.transaction_log = defaultdict(int)  # Tracks token transfers for each user in the current epoch

    def transfer_tokens(self, sender, recipient, amount):
        """
        Handles token transfers between users.

        :param sender: The user sending the tokens.
        :param recipient: The user receiving the tokens.
        :param amount: The amount of tokens being transferred.
        :raises ValueError: If the sender does not have enough tokens.
        """
        if self.user_balances[sender] < amount:
            raise ValueError("Insufficient balance for transfer.")

        self._check_epoch_reset()

        # Update balances
        self.user_balances[sender] -= amount
        self.user_balances[recipient] += amount

        # Track sender's transaction volume within the current epoch
        self.transaction_log[sender] += amount

        # Check if sender exceeds the transfer threshold (300 tokens in the epoch)
        if self.transaction_log[sender] > 300:
            self._forfeit_rewards(sender)

    def _forfeit_rewards(self, user):
        """
        Forfeits the user's rewards and adds them to the forfeited rewards pool.

        :param user: The user forfeiting their rewards.
        """
        forfeited_rewards = self.user_rewards[user]
        self.user_rewards[user] = 0  # Reset the user's rewards
        self.forfeited_rewards_pool += forfeited_rewards

    def _redistribute_rewards(self):
        """
        Redistributes forfeited rewards among all eligible users 
        based on their current token holdings.
        """
        total_tokens = sum(self.user_balances.values())
        if total_tokens == 0:
            return  # Avoid division by zero if no tokens are held

        for user, balance in self.user_balances.items():
            # Distribute rewards proportionally to token holdings
            self.user_rewards[user] += (
                self.forfeited_rewards_pool * (balance / total_tokens)
            )

        # Reset the forfeited rewards pool after redistribution
        self.forfeited_rewards_pool = 0

    def _check_epoch_reset(self):
        """
        Resets the epoch if the current epoch has ended.
        """
        current_time = time.time()
        if current_time - self.current_epoch_start >= self.epoch_duration:
            # Reset epoch-specific data
            self.transaction_log = defaultdict(int)
            self.current_epoch_start = current_time

            # Redistribute forfeited rewards to eligible users
            self._redistribute_rewards()

    def add_tokens(self, user, amount):
        """
        Adds tokens to a user's balance.

        :param user: The user receiving the tokens.
        :param amount: The amount of tokens to add.
        """
        self.user_balances[user] += amount

    def add_rewards(self, user, amount):
        """
        Adds rewards to a user's account.

        :param user: The user receiving the rewards.
        :param amount: The amount of rewards to add.
        """
        self.user_rewards[user] += amount

    def get_user_balance(self, user):
        """
        Returns the token balance of a user.

        :param user: The user whose balance is being queried.
        :return: The user's token balance.
        """
        return self.user_balances[user]

    def get_user_rewards(self, user):
        """
        Returns the reward balance of a user.

        :param user: The user whose reward balance is being queried.
        :return: The user's reward balance.
        """
        return self.user_rewards[user]

    def get_forfeited_rewards_pool(self):
        """
        Returns the total forfeited rewards pool.

        :return: The forfeited rewards pool.
        """
        return self.forfeited_rewards_pool


# Example usage
if __name__ == "__main__":
    tracker = BananaRewardTracker(epoch_duration_seconds=86400)  # 1 day epochs

    # Adding initial balances and rewards
    tracker.add_tokens("Alice", 500)
    tracker.add_tokens("Bob", 300)
    tracker.add_rewards("Alice", 50)
    tracker.add_rewards("Bob", 30)

    # Simulating transfers
    tracker.transfer_tokens("Alice", "Bob", 350)  # Alice exceeds the 300-token threshold
    tracker.transfer_tokens("Bob", "Alice", 150)

    # Querying balances and rewards
    print("Alice's balance:", tracker.get_user_balance("Alice"))
    print("Bob's balance:", tracker.get_user_balance("Bob"))
    print("Alice's rewards:", tracker.get_user_rewards("Alice"))
    print("Bob's rewards:", tracker.get_user_rewards("Bob"))
    print("Forfeited rewards pool:", tracker.get_forfeited_rewards_pool())
```
