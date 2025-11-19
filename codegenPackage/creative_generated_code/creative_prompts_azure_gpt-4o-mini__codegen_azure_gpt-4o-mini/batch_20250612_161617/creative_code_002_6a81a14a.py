"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinite-v2.vercel.app
Prompt: Write a code snippet to manage total value across vaults in a DeFi trading ecosystem, referencing the features of Infinite Trading.
Generated: DETERMINISTIC_6a81a14ab4f81c98
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Vault:
    """
    A class to represent a vault in the DeFi trading ecosystem.

    Attributes:
        name (str): The name of the vault.
        balance (float): The total value held in the vault.
    """

    def __init__(self, name: str, initial_balance: float = 0.0):
        """
        Initialize the vault with a name and an optional initial balance.

        Args:
            name (str): The name of the vault.
            initial_balance (float): The initial balance of the vault (default is 0.0).
        """
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount: float):
        """
        Deposit an amount into the vault.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Withdraw an amount from the vault.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Get the current balance of the vault.

        Returns:
            float: The current balance of the vault.
        """
        return self.balance


class DeFiEcosystem:
    """
    A class to manage multiple vaults in a DeFi trading ecosystem.

    Attributes:
        vaults (dict): A dictionary storing vault instances by their names.
    """

    def __init__(self):
        """Initialize the DeFi ecosystem with an empty vault dictionary."""
        self.vaults = {}

    def create_vault(self, name: str, initial_balance: float = 0.0):
        """
        Create a new vault in the ecosystem.

        Args:
            name (str): The name of the new vault.
            initial_balance (float): The initial balance of the vault (default is 0.0).

        Raises:
            ValueError: If a vault with the given name already exists.
        """
        if name in self.vaults:
            raise ValueError(f"Vault '{name}' already exists.")
        self.vaults[name] = Vault(name, initial_balance)

    def deposit_to_vault(self, name: str, amount: float):
        """
        Deposit an amount into a specific vault.

        Args:
            name (str): The name of the vault.
            amount (float): The amount to deposit.

        Raises:
            KeyError: If the vault does not exist.
        """
        if name not in self.vaults:
            raise KeyError(f"Vault '{name}' does not exist.")
        self.vaults[name].deposit(amount)

    def withdraw_from_vault(self, name: str, amount: float):
        """
        Withdraw an amount from a specific vault.

        Args:
            name (str): The name of the vault.
            amount (float): The amount to withdraw.

        Raises:
            KeyError: If the vault does not exist.
        """
        if name not in self.vaults:
            raise KeyError(f"Vault '{name}' does not exist.")
        self.vaults[name].withdraw(amount)

    def get_total_value(self) -> float:
        """
        Calculate the total value across all vaults.

        Returns:
            float: The total value held across all vaults.
        """
        return sum(vault.get_balance() for vault in self.vaults.values())


# Example Usage
if __name__ == "__main__":
    try:
        ecosystem = DeFiEcosystem()
        ecosystem.create_vault("Vault1", 1000.0)
        ecosystem.create_vault("Vault2", 500.0)

        ecosystem.deposit_to_vault("Vault1", 200.0)
        ecosystem.withdraw_from_vault("Vault2", 100.0)

        total_value = ecosystem.get_total_value()
        print(f"Total value across all vaults: {total_value}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
