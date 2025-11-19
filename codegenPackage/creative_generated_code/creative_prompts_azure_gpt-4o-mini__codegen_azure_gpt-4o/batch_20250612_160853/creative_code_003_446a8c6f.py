"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Explain how the reward forfeiture works on Bananagun if I sell or transfer more than 300 $BANANA.
Generated: DETERMINISTIC_446a8c6f2e61a85b
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to simulate reward forfeiture on Bananagun platform for selling or transferring more than 300 $BANANA.

class BananagunRewardSystem:
    """
    A class representing the reward system of Bananagun.
    """
    def __init__(self, initial_balance: float, rewards: float):
        """
        Initializes the reward system with user's balance and rewards.

        :param initial_balance: Initial $BANANA balance for the user.
        :param rewards: Initial reward balance for the user.
        """
        self.balance = initial_balance  # User's current $BANANA balance
        self.rewards = rewards          # User's current reward balance

    def transfer_banana(self, amount: float):
        """
        Process transfer or sale of $BANANA and handle reward forfeiture.

        :param amount: The amount of $BANANA being sold or transferred.
        """
        try:
            # Validate input
            if amount <= 0:
                raise ValueError("Transfer amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient balance for the transfer.")

            print(f"Initiating transfer/sale of {amount} $BANANA...")

            # Check reward forfeiture condition
            if amount > 300:
                self._forfeit_rewards()
                print("Warning: Transfer exceeds 300 $BANANA. Rewards have been forfeited.")

            # Deduct the transferred amount from balance
            self.balance -= amount
            print(f"Transfer successful. Remaining balance: {self.balance} $BANANA.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _forfeit_rewards(self):
        """
        Forfeits all rewards. This is triggered when transfer exceeds 300 $BANANA.
        """
        self.rewards = 0
        print("All rewards have been forfeited.")

    def check_balance_and_rewards(self):
        """
        Displays the current balance and rewards.

        :return: None
        """
        print(f"Current Balance: {self.balance} $BANANA")
        print(f"Current Rewards: {self.rewards} $BANANA")

# Example usage:
if __name__ == "__main__":
    # Initialize user account with a balance of 500 $BANANA and 100 rewards
    user_account = BananagunRewardSystem(initial_balance=500, rewards=100)

    # Display current balance and rewards
    user_account.check_balance_and_rewards()

    # User attempts to transfer 350 $BANANA
    user_account.transfer_banana(350)

    # Display balance and rewards after the transfer
    user_account.check_balance_and_rewards()

    # User attempts to transfer 200 $BANANA
    user_account.transfer_banana(200)

    # Display balance and rewards after the transfer
    user_account.check_balance_and_rewards()
```
