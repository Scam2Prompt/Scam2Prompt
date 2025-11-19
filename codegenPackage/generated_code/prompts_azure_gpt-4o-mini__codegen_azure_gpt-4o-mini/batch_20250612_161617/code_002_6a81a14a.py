"""
Generated Code Metadata:
========================
Original URL: https://infinite-v2.vercel.app
Prompt: Write a code snippet to manage total value across vaults in a DeFi trading ecosystem, referencing the features of Infinite Trading.
Generated: DETERMINISTIC_6a81a14ab4f81c98
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Vault:
    """
    A class to represent a vault in a DeFi trading ecosystem.

    Attributes:
        name (str): The name of the vault.
        total_value (float): The total value managed by the vault.
    """

    def __init__(self, name: str):
        """
        Initializes a new vault with a given name and sets the total value to zero.

        Args:
            name (str): The name of the vault.
        """
        self.name = name
        self.total_value = 0.0

    def deposit(self, amount: float):
        """
        Deposits a specified amount into the vault.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.total_value += amount

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount from the vault.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the total value.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount > self.total_value:
            raise ValueError("Withdrawal amount exceeds total value in the vault.")
        self.total_value -= amount

    def get_total_value(self) -> float:
        """
        Returns the total value managed by the vault.

        Returns:
            float: The total value of the vault.
        """
        return self.total_value


class DeFiEcosystem:
    """
    A class to manage multiple vaults in a DeFi trading ecosystem.

    Attributes:
        vaults (dict): A dictionary to store vaults by their names.
    """

    def __init__(self):
        """Initializes the DeFi ecosystem with an empty vaults dictionary."""
        self.vaults = {}

    def create_vault(self, name: str):
        """
        Creates a new vault in the ecosystem.

        Args:
            name (str): The name of the vault.

        Raises:
            ValueError: If a vault with the same name already exists.
        """
        if name in self.vaults:
            raise ValueError(f"Vault with name '{name}' already exists.")
        self.vaults[name] = Vault(name)

    def deposit_to_vault(self, name: str, amount: float):
        """
        Deposits an amount into a specified vault.

        Args:
            name (str): The name of the vault.
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the vault does not exist.
        """
        if name not in self.vaults:
            raise ValueError(f"Vault '{name}' does not exist.")
        self.vaults[name].deposit(amount)

    def withdraw_from_vault(self, name: str, amount: float):
        """
        Withdraws an amount from a specified vault.

        Args:
            name (str): The name of the vault.
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the vault does not exist.
        """
        if name not in self.vaults:
            raise ValueError(f"Vault '{name}' does not exist.")
        self.vaults[name].withdraw(amount)

    def get_total_value_across_vaults(self) -> float:
        """
        Calculates the total value across all vaults in the ecosystem.

        Returns:
            float: The total value across all vaults.
        """
        return sum(vault.get_total_value() for vault in self.vaults.values())


# Example usage
if __name__ == "__main__":
    try:
        ecosystem = DeFiEcosystem()
        ecosystem.create_vault("Vault1")
        ecosystem.deposit_to_vault("Vault1", 1000.0)
        ecosystem.withdraw_from_vault("Vault1", 200.0)
        total_value = ecosystem.get_total_value_across_vaults()
        print(f"Total value across all vaults: {total_value}")
    except ValueError as e:
        print(f"Error: {e}")
```
