"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Write a Python script to simulate a payment system for "Slot Dana" deposits, incorporating features like cashback and bonus saldo as described on the website.
Generated: DETERMINISTIC_38396e79e34b6a42
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SlotDanaPaymentSystem:
    """
    A class to simulate the payment system for Slot Dana deposits.
    Features include cashback and bonus saldo.
    """

    def __init__(self):
        # Simulated database for users and their balances
        self.users = {
            "user1": {"saldo": 100000},  # Example user with initial saldo
            "user2": {"saldo": 50000},
        }

    def deposit(self, username, amount):
        """
        Process a deposit for the given user and apply cashback and bonus saldo.

        Parameters:
        username (str): The username of the user making the deposit.
        amount (int): The deposit amount.

        Returns:
        dict: A detailed transaction summary including cashback and bonus.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist in the system.")

        # Validate deposit amount
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Calculate cashback (e.g., 5% cashback)
        cashback_rate = 0.05
        cashback = int(amount * cashback_rate)

        # Calculate bonus saldo based on deposit tiers
        bonus = self.calculate_bonus(amount)

        # Update user's saldo
        total_credit = amount + cashback + bonus
        self.users[username]["saldo"] += total_credit

        # Return transaction summary
        return {
            "username": username,
            "deposit_amount": amount,
            "cashback": cashback,
            "bonus": bonus,
            "total_credit": total_credit,
            "updated_saldo": self.users[username]["saldo"],
        }

    @staticmethod
    def calculate_bonus(amount):
        """
        Calculate bonus saldo based on deposit tiers.

        Parameters:
        amount (int): The deposit amount.

        Returns:
        int: The calculated bonus amount.
        """
        if amount >= 100000:
            return 20000  # Bonus for deposits >= 100,000
        elif amount >= 50000:
            return 10000  # Bonus for deposits >= 50,000
        elif amount >= 20000:
            return 5000  # Bonus for deposits >= 20,000
        return 0  # No bonus for deposits < 20,000

    def get_user_saldo(self, username):
        """
        Retrieve the current saldo for a given user.

        Parameters:
        username (str): The username of the user.

        Returns:
        int: The user's current saldo.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist in the system.")

        return self.users[username]["saldo"]


# Example usage of the payment system
if __name__ == "__main__":
    system = SlotDanaPaymentSystem()

    try:
        # Simulate a deposit
        username = "user1"
        deposit_amount = 75000
        print(f"Processing deposit of {deposit_amount} for {username}...\n")

        transaction = system.deposit(username, deposit_amount)
        print("Transaction Summary:")
        for key, value in transaction.items():
            print(f"{key.capitalize()}: {value}")

        # Retrieve updated saldo
        saldo = system.get_user_saldo(username)
        print(f"\nUpdated Saldo for {username}: {saldo}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
