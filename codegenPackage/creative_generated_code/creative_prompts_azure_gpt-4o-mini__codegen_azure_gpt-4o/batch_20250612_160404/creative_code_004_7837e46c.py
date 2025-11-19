"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainecotrust.cc
Prompt: Illustrate how to implement a referral commission tracking system in Python, inspired by the 10% referral commission structure mentioned on mainecotrust.cc.
Generated: DETERMINISTIC_7837e46c294c9658
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class User:
    """
    Represents a user in the referral system.
    Each user has a unique ID, name, balance, and a referrer (optional).
    """
    def __init__(self, name, referrer=None):
        self.user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.name = name
        self.balance = 0.0  # Initial balance
        self.referrer = referrer  # Referrer User object (if any)

    def __str__(self):
        return f"User(name={self.name}, balance={self.balance:.2f}, referrer={self.referrer.name if self.referrer else None})"


class ReferralSystem:
    """
    Manages users and referral commissions in the system.
    Allows adding users, processing transactions, and tracking commissions.
    """
    def __init__(self):
        self.users = {}  # Dictionary to store users by their user ID

    def add_user(self, name, referrer_id=None):
        """
        Adds a new user to the system. If referrer_id is provided,
        links the new user to the referring user.

        :param name: Name of the new user
        :param referrer_id: ID of the referring user (optional)
        :return: The newly created User object
        """
        referrer = self.users.get(referrer_id)  # Get the referrer User object (if exists)
        new_user = User(name, referrer)
        self.users[new_user.user_id] = new_user  # Add new user to the system
        return new_user

    def process_transaction(self, user_id, transaction_amount):
        """
        Processes a transaction for the specified user and calculates
        referral commission for the referrer.

        :param user_id: ID of the user making the transaction
        :param transaction_amount: The transaction amount (positive float)
        :return: None
        """
        try:
            user = self.users[user_id]
            if transaction_amount <= 0:
                raise ValueError("Transaction amount must be positive.")

            # Add transaction amount to user's balance
            user.balance += transaction_amount

            # Calculate and distribute referral commission (10%)
            if user.referrer:
                commission = transaction_amount * 0.10  # 10% commission
                user.referrer.balance += commission  # Add commission to referrer's balance

        except KeyError:
            print(f"Error: User with ID {user_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def display_users(self):
        """
        Displays all users in the system along with their details.

        :return: None
        """
        for user in self.users.values():
            print(user)


# Example usage of the referral system
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Add users
    user1 = referral_system.add_user("Alice")
    user2 = referral_system.add_user("Bob", referrer_id=user1.user_id)
    user3 = referral_system.add_user("Charlie", referrer_id=user2.user_id)

    # Process transactions
    referral_system.process_transaction(user2.user_id, 100.0)  # Bob makes a transaction of $100
    referral_system.process_transaction(user3.user_id, 50.0)   # Charlie makes a transaction of $50

    # Display all users and their balances
    referral_system.display_users()
```

This code implements a referral commission tracking system in Python based on a 10% referral structure. It follows best practices, includes error handling, and is well-documented with comments.
