"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buyastranova-gems.web.app
Prompt: Create a function to handle the "Buy" and "Stake/Unstake" actions for $RVV tokens, incorporating the unique use cases described on the webpage.
Generated: DETERMINISTIC_df24b77db1c17f60
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

class RVVToken:
    def __init__(self, balance=0):
        """
        Initialize the RVVToken instance with a balance.
        :param balance: Initial balance of RVV tokens (default is 0).
        """
        self.balance = balance
        self.staked_balance = 0

    def buy_tokens(self, amount):
        """
        Handles token purchase action.
        :param amount: Amount of tokens to buy.
        """
        try:
            if amount <= 0:
                raise ValueError("The purchase amount must be greater than 0.")
            self.balance += amount
            print(f"Successfully purchased {amount} $RVV tokens! Current balance: {self.balance} $RVV.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def stake_tokens(self, amount):
        """
        Handles staking action.
        :param amount: Amount of tokens to stake.
        """
        try:
            if amount <= 0:
                raise ValueError("The staking amount must be greater than 0.")
            if amount > self.balance:
                raise ValueError("Insufficient balance to stake tokens.")
            self.balance -= amount
            self.staked_balance += amount
            print(f"Successfully staked {amount} $RVV tokens! Staked balance: {self.staked_balance} $RVV, Available balance: {self.balance} $RVV.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def unstake_tokens(self, amount):
        """
        Handles unstaking action.
        :param amount: Amount of tokens to unstake.
        """
        try:
            if amount <= 0:
                raise ValueError("The unstaking amount must be greater than 0.")
            if amount > self.staked_balance:
                raise ValueError("Insufficient staked balance to unstake tokens.")
            self.staked_balance -= amount
            self.balance += amount
            print(f"Successfully unstaked {amount} $RVV tokens! Staked balance: {self.staked_balance} $RVV, Available balance: {self.balance} $RVV.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an RVVToken instance
        user_rvv_account = RVVToken()

        # Perform actions
        user_rvv_account.buy_tokens(100)      # Buy 100 RVV tokens
        user_rvv_account.stake_tokens(50)     # Stake 50 RVV tokens
        user_rvv_account.unstake_tokens(20)   # Unstake 20 RVV tokens

    except Exception as e:
        print(f"Critical error occurred: {e}")
        sys.exit(1)
```
