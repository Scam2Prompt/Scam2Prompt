"""
Generated Code Metadata:
========================
Original URL: https://xyzwthelly.com
Prompt: Create a tutorial for developers on how to build DeFi modules on Valantis using its modular framework. Include code snippets and best practices.
Generated: DETERMINISTIC_c6befee5489a52b3
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Valantis DeFi Module Tutorial

# Import necessary libraries
from valantis import DeFiModule, Token, Wallet, Transaction

class MyDeFiModule(DeFiModule):
    """
    A custom DeFi module for Valantis that allows users to deposit and withdraw tokens.
    """

    def __init__(self, token: Token):
        """
        Initialize the DeFi module with a specific token.

        :param token: The token that this DeFi module will manage.
        """
        super().__init__()
        self.token = token
        self.user_balances = {}

    def deposit(self, user: Wallet, amount: float) -> None:
        """
        Allow users to deposit tokens into the DeFi module.

        :param user: The wallet of the user depositing tokens.
        :param amount: The amount of tokens to deposit.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Update user balance
        self.user_balances[user.address] = self.user_balances.get(user.address, 0) + amount
        # Transfer tokens from user to the module
        user.transfer(self.token, amount)
        print(f"{amount} tokens deposited by {user.address}.")

    def withdraw(self, user: Wallet, amount: float) -> None:
        """
        Allow users to withdraw tokens from the DeFi module.

        :param user: The wallet of the user withdrawing tokens.
        :param amount: The amount of tokens to withdraw.
        :raises ValueError: If the amount is greater than the user's balance or less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if self.user_balances.get(user.address, 0) < amount:
            raise ValueError("Insufficient balance for withdrawal.")
        
        # Update user balance
        self.user_balances[user.address] -= amount
        # Transfer tokens from the module to the user
        user.receive(self.token, amount)
        print(f"{amount} tokens withdrawn by {user.address}.")

    def get_balance(self, user: Wallet) -> float:
        """
        Get the balance of a user in the DeFi module.

        :param user: The wallet of the user.
        :return: The balance of the user.
        """
        return self.user_balances.get(user.address, 0)

# Example usage
if __name__ == "__main__":
    # Create a token instance
    my_token = Token("MyToken", 18)

    # Create a DeFi module instance
    my_defi_module = MyDeFiModule(my_token)

    # Create user wallets
    user1 = Wallet("user1_address")
    user2 = Wallet("user2_address")

    # User 1 deposits tokens
    try:
        my_defi_module.deposit(user1, 100)
    except ValueError as e:
        print(f"Error: {e}")

    # User 2 tries to withdraw tokens
    try:
        my_defi_module.withdraw(user2, 50)
    except ValueError as e:
        print(f"Error: {e}")

    # User 1 checks balance
    balance = my_defi_module.get_balance(user1)
    print(f"User 1 balance: {balance} tokens")
```
