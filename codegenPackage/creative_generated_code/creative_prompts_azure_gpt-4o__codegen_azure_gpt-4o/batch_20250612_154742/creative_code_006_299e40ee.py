"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfxinvestment.com
Prompt: Write code to implement a bonus system for users, similar to the user commission structure described by Perfx Investment.
Generated: DETERMINISTIC_299e40ee6308443a
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BonusSystem:
    """
    A class to implement a bonus system for users. 
    This system calculates bonuses based on a tiered structure.
    """

    def __init__(self):
        # Initialize the user bonuses dictionary
        self.user_bonuses = {}

    def add_user(self, user_id):
        """
        Adds a new user to the bonus system.

        :param user_id: Unique identifier of the user
        """
        if user_id in self.user_bonuses:
            print(f"User {user_id} already exists in the system.")
        else:
            self.user_bonuses[user_id] = {
                "total_bonus": 0.0,
                "bonus_transactions": []
            }

    def calculate_bonus(self, amount):
        """
        Calculates the bonus based on the given tiered structure.

        :param amount: The amount for which the bonus is calculated
        :return: Bonus amount
        """
        if amount <= 0:
            raise ValueError("Amount should be greater than 0.")

        # Define the tiered structure for bonuses
        if amount < 500:
            return amount * 0.05  # 5% bonus for amounts below $500
        elif amount < 1000:
            return amount * 0.07  # 7% bonus for amounts between $500 and $1000
        else:
            return amount * 0.10  # 10% bonus for amounts above $1000

    def add_bonus_transaction(self, user_id, amount):
        """
        Adds a bonus transaction for a user.

        :param user_id: Unique identifier of the user
        :param amount: The amount for which the bonus is calculated
        """
        if user_id not in self.user_bonuses:
            raise ValueError(f"User {user_id} does not exist in the system.")

        bonus = self.calculate_bonus(amount)
        transaction = {
            "amount": amount,
            "bonus": bonus,
            "timestamp": datetime.datetime.now()
        }

        self.user_bonuses[user_id]["total_bonus"] += bonus
        self.user_bonuses[user_id]["bonus_transactions"].append(transaction)

    def get_user_bonus(self, user_id):
        """
        Retrieves the total bonus and bonus transactions for a user.

        :param user_id: Unique identifier of the user
        :return: A dictionary containing total bonus and transactions
        """
        if user_id not in self.user_bonuses:
            raise ValueError(f"User {user_id} does not exist in the system.")

        return self.user_bonuses[user_id]

    def display_user_bonus(self, user_id):
        """
        Displays the total bonus and transactions for a user.

        :param user_id: Unique identifier of the user
        """
        try:
            user_bonus = self.get_user_bonus(user_id)
            print(f"User ID: {user_id}")
            print(f"Total Bonus: {user_bonus['total_bonus']:.2f}")
            print("Transactions:")
            for transaction in user_bonus["bonus_transactions"]:
                print(f"  - Amount: {transaction['amount']:.2f}, Bonus: {transaction['bonus']:.2f}, Timestamp: {transaction['timestamp']}")
        except ValueError as e:
            print(e)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the bonus system
    system = BonusSystem()

    # Add users
    system.add_user("user123")
    system.add_user("user456")

    # Add transactions and calculate bonuses
    system.add_bonus_transaction("user123", 300)
    system.add_bonus_transaction("user123", 700)
    system.add_bonus_transaction("user456", 1200)

    # Display user bonuses
    system.display_user_bonus("user123")
    system.display_user_bonus("user456")
```
