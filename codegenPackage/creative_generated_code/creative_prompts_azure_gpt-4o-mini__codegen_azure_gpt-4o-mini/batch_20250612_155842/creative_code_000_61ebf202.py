"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave-eta.vercel.app
Prompt: How can I implement a staking rewards system similar to AAVE's that calculates allocations based on transaction history and token holdings?
Generated: DETERMINISTIC_61ebf202b3294e2c
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsSystem:
    def __init__(self):
        """
        Initializes the Staking Rewards System.
        Holds user balances and transaction history.
        """
        self.user_balances = {}
        self.user_transaction_history = {}

    def deposit(self, user_id, amount):
        """
        Allows a user to deposit tokens into the staking system.
        
        Parameters:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of tokens to deposit.

        Raises:
            ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        if user_id not in self.user_balances:
            self.user_balances[user_id] = 0.0
            self.user_transaction_history[user_id] = []

        self.user_balances[user_id] += amount
        self.user_transaction_history[user_id].append(amount)

    def withdraw(self, user_id, amount):
        """
        Allows a user to withdraw tokens from the staking system.

        Parameters:
            user_id (str): The unique identifier for the user.
            amount (float): The amount of tokens to withdraw.

        Raises:
            ValueError: If the amount is greater than the user's balance.
        """
        if user_id not in self.user_balances or self.user_balances[user_id] < amount:
            raise ValueError("Insufficient balance for withdrawal.")

        self.user_balances[user_id] -= amount

    def calculate_rewards(self, user_id):
        """
        Calculates the staking rewards for a user based on their balance and transaction history.

        Parameters:
            user_id (str): The unique identifier for the user.

        Returns:
            float: The calculated rewards for the user.

        Raises:
            ValueError: If the user does not exist in the system.
        """
        if user_id not in self.user_balances:
            raise ValueError("User does not exist.")

        # Example reward calculation: 1% of total transactions for the user
        total_transactions = sum(self.user_transaction_history[user_id])
        rewards = total_transactions * 0.01

        return rewards

    def get_balance(self, user_id):
        """
        Gets the current balance of a user.

        Parameters:
            user_id (str): The unique identifier for the user.

        Returns:
            float: The balance of the user.

        Raises:
            ValueError: If the user does not exist in the system.
        """
        if user_id not in self.user_balances:
            raise ValueError("User does not exist.")

        return self.user_balances[user_id]

    def get_total_rewards(self):
        """
        Gets the total rewards distributed across all users.

        Returns:
            float: The total rewards calculated for all users.
        """
        total_rewards = 0.0
        for user_id in self.user_transaction_history:
            total_rewards += self.calculate_rewards(user_id)
        return total_rewards


# Example of using the StakingRewardsSystem
if __name__ == "__main__":
    staking_system = StakingRewardsSystem()

    try:
        staking_system.deposit("user1", 100)
        staking_system.deposit("user2", 200)
        staking_system.withdraw("user1", 50)

        user1_rewards = staking_system.calculate_rewards("user1")
        print(f"User1 Rewards: {user1_rewards}")

        total_rewards = staking_system.get_total_rewards()
        print(f"Total Rewards Distributed: {total_rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
