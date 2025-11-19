"""
Generated Code Metadata:
========================
Original URL: https://braavosstg.wpenginepowered.com
Prompt: Compare the features of Braavos smart contract wallet with traditional wallets, highlighting account abstraction and multi-factor authentication.
Generated: DETERMINISTIC_421c7928071c048d
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wallet:
    """
    A base class representing a traditional wallet.
    """

    def __init__(self, owner: str):
        """
        Initializes a traditional wallet with an owner's name.

        :param owner: The name of the wallet owner.
        """
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the wallet.

        :param amount: The amount to deposit.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the wallet.

        :param amount: The amount to withdraw.
        :raises ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance of the wallet.

        :return: The current balance.
        """
        return self.balance


class BraavosSmartContractWallet(Wallet):
    """
    A class representing a Braavos smart contract wallet with advanced features.
    """

    def __init__(self, owner: str, multi_factor_auth: bool = True):
        """
        Initializes a Braavos smart contract wallet with an owner's name and multi-factor authentication option.

        :param owner: The name of the wallet owner.
        :param multi_factor_auth: Flag indicating if multi-factor authentication is enabled.
        """
        super().__init__(owner)
        self.multi_factor_auth = multi_factor_auth
        self.authenticated = False

    def authenticate(self, method: str):
        """
        Authenticates the user using a specified method.

        :param method: The authentication method (e.g., 'sms', 'email').
        :raises ValueError: If multi-factor authentication is not enabled.
        """
        if not self.multi_factor_auth:
            raise ValueError("Multi-factor authentication is not enabled.")
        # Simulate authentication process
        print(f"Authenticating via {method}...")
        self.authenticated = True  # In a real scenario, this would involve verification

    def deposit(self, amount: float):
        """
        Overrides the deposit method to include authentication.

        :param amount: The amount to deposit.
        :raises ValueError: If the amount is negative or if not authenticated.
        """
        if not self.authenticated:
            raise ValueError("User must be authenticated to perform this action.")
        super().deposit(amount)

    def withdraw(self, amount: float):
        """
        Overrides the withdraw method to include authentication.

        :param amount: The amount to withdraw.
        :raises ValueError: If the amount is negative, exceeds the balance, or if not authenticated.
        """
        if not self.authenticated:
            raise ValueError("User must be authenticated to perform this action.")
        super().withdraw(amount)

    def reset_authentication(self):
        """
        Resets the authentication status.
        """
        self.authenticated = False


# Example usage
if __name__ == "__main__":
    try:
        # Create a traditional wallet
        traditional_wallet = Wallet("Alice")
        traditional_wallet.deposit(100)
        print(f"Traditional Wallet Balance: {traditional_wallet.get_balance()}")

        # Create a Braavos smart contract wallet
        braavos_wallet = BraavosSmartContractWallet("Bob")
        braavos_wallet.authenticate("sms")  # Authenticate user
        braavos_wallet.deposit(200)
        print(f"Braavos Wallet Balance: {braavos_wallet.get_balance()}")

        # Withdraw from Braavos wallet
        braavos_wallet.withdraw(50)
        print(f"Braavos Wallet Balance after withdrawal: {braavos_wallet.get_balance()}")

    except ValueError as e:
        print(f"Error: {e}")
```
