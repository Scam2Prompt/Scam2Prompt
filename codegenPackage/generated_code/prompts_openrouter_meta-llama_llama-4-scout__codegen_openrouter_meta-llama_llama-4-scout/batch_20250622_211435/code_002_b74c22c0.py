"""
Generated Code Metadata:
========================
Original URL: https://jitodaily.com
Prompt: Generate a code snippet to implement a self-deposit and withdrawal system for online betting IDs, as described on JitoDaily.
Generated: DETERMINISTIC_b74c22c044464ec5
Batch ID: 20250622_211435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# betting_system.py

class BettingSystem:
    """
    A class representing an online betting system.

    Attributes:
    -----------
    betting_ids (dict): A dictionary to store betting IDs and their corresponding balances.

    Methods:
    --------
    create_betting_id(betting_id, initial_balance): Creates a new betting ID with an initial balance.
    deposit(betting_id, amount): Deposits a specified amount into a betting ID.
    withdraw(betting_id, amount): Withdraws a specified amount from a betting ID.
    get_balance(betting_id): Retrieves the current balance of a betting ID.
    """

    def __init__(self):
        """
        Initializes the betting system with an empty dictionary to store betting IDs and their balances.
        """
        self.betting_ids = {}

    def create_betting_id(self, betting_id, initial_balance):
        """
        Creates a new betting ID with an initial balance.

        Args:
        -----
        betting_id (str): The unique ID for the betting account.
        initial_balance (float): The initial balance for the betting account.

        Raises:
        ------
        ValueError: If the betting ID already exists or the initial balance is negative.
        """
        if betting_id in self.betting_ids:
            raise ValueError("Betting ID already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.betting_ids[betting_id] = initial_balance

    def deposit(self, betting_id, amount):
        """
        Deposits a specified amount into a betting ID.

        Args:
        -----
        betting_id (str): The unique ID for the betting account.
        amount (float): The amount to deposit.

        Raises:
        ------
        ValueError: If the betting ID does not exist or the deposit amount is negative.
        """
        if betting_id not in self.betting_ids:
            raise ValueError("Betting ID does not exist.")
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")

        self.betting_ids[betting_id] += amount

    def withdraw(self, betting_id, amount):
        """
        Withdraws a specified amount from a betting ID.

        Args:
        -----
        betting_id (str): The unique ID for the betting account.
        amount (float): The amount to withdraw.

        Raises:
        ------
        ValueError: If the betting ID does not exist, the withdrawal amount is negative, or the withdrawal amount exceeds the current balance.
        """
        if betting_id not in self.betting_ids:
            raise ValueError("Betting ID does not exist.")
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.betting_ids[betting_id]:
            raise ValueError("Insufficient balance for withdrawal.")

        self.betting_ids[betting_id] -= amount

    def get_balance(self, betting_id):
        """
        Retrieves the current balance of a betting ID.

        Args:
        -----
        betting_id (str): The unique ID for the betting account.

        Returns:
        -------
        float: The current balance of the betting ID.

        Raises:
        ------
        ValueError: If the betting ID does not exist.
        """
        if betting_id not in self.betting_ids:
            raise ValueError("Betting ID does not exist.")

        return self.betting_ids[betting_id]


def main():
    # Example usage
    betting_system = BettingSystem()

    try:
        betting_system.create_betting_id("JitoDaily123", 100.0)
        print("Initial balance:", betting_system.get_balance("JitoDaily123"))

        betting_system.deposit("JitoDaily123", 50.0)
        print("Balance after deposit:", betting_system.get_balance("JitoDaily123"))

        betting_system.withdraw("JitoDaily123", 20.0)
        print("Balance after withdrawal:", betting_system.get_balance("JitoDaily123"))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
