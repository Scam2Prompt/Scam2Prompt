"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogegovlive.com
Prompt: Write a program to simulate the staking and unstaking of DOGEGOV memecoins based on the community-driven token mechanics described on the site.
Generated: DETERMINISTIC_9edfcdeb2e2d04b3
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DogeGovStaking:
    def __init__(self):
        # Initialize the staking dictionary to keep track of user stakes
        self.stakes = {}
        # Set a minimum staking amount
        self.MIN_STAKE = 100

    def stake(self, user_id, amount):
        """
        Allows a user to stake an amount of DOGEGOV memecoins.
        
        :param user_id: The unique identifier for the user
        :param amount: The amount of DOGEGOV memecoins to stake
        :raises ValueError: If the stake amount is below the minimum
        :raises ValueError: If the user tries to stake a negative amount
        """
        if amount < self.MIN_STAKE:
            raise ValueError(f"Minimum stake amount is {self.MIN_STAKE}.")
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        # Update the user's stake
        if user_id in self.stakes:
            self.stakes[user_id] += amount
        else:
            self.stakes[user_id] = amount
        
        print(f"User {user_id} staked {amount} DOGEGOV. Total stake: {self.stakes[user_id]} DOGEGOV.")

    def unstake(self, user_id, amount):
        """
        Allows a user to unstake an amount of DOGEGOV memecoins.
        
        :param user_id: The unique identifier for the user
        :param amount: The amount of DOGEGOV memecoins to unstake
        :raises ValueError: If the user does not have enough staked
        :raises ValueError: If the unstake amount is negative
        """
        if user_id not in self.stakes:
            raise ValueError("User has no stakes.")
        if amount <= 0:
            raise ValueError("Unstake amount must be positive.")
        if amount > self.stakes[user_id]:
            raise ValueError("Insufficient stake to unstake.")

        # Update the user's stake
        self.stakes[user_id] -= amount
        
        # Remove user from stakes if their balance is zero
        if self.stakes[user_id] == 0:
            del self.stakes[user_id]
        
        print(f"User {user_id} unstaked {amount} DOGEGOV. Remaining stake: {self.stakes.get(user_id, 0)} DOGEGOV.")

    def get_stake(self, user_id):
        """
        Retrieves the current stake of a user.
        
        :param user_id: The unique identifier for the user
        :return: The amount of DOGEGOV memecoins staked by the user
        """
        return self.stakes.get(user_id, 0)

    def total_staked(self):
        """
        Calculates the total amount of DOGEGOV memecoins staked across all users.
        
        :return: The total amount staked
        """
        return sum(self.stakes.values())

# Example usage
if __name__ == "__main__":
    staking_system = DogeGovStaking()

    try:
        staking_system.stake('user1', 200)
        staking_system.stake('user2', 150)
        staking_system.unstake('user1', 50)
        print(f"Total staked: {staking_system.total_staked()} DOGEGOV")
    except ValueError as e:
        print(f"Error: {e}")
```
