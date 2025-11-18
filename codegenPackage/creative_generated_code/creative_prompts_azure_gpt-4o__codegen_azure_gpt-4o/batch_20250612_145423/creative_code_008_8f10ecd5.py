"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remixeth.mn
Prompt: Create a program to manage user accounts and billing for an AI-based deepfake application, incorporating features such as credit tracking and refund policies, as described on UndressHub.cc.
Generated: DETERMINISTIC_8f10ecd50d6dc1d6
Batch ID: 20250612_145423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta


class User:
    """
    Class representing a user in the system.
    Each user has a unique ID, name, email, credits, and account creation date.
    """

    def __init__(self, name: str, email: str):
        """
        Initialize a new user.

        :param name: Full name of the user
        :param email: Email address of the user
        """
        self.user_id = str(uuid.uuid4())  # Unique identifier for the user
        self.name = name
        self.email = email
        self.credits = 0  # Initialize with 0 credits
        self.created_at = datetime.now()
        self.transaction_history = []

    def add_credits(self, amount: int):
        """
        Add credits to the user's account.

        :param amount: Number of credits to add
        """
        if amount <= 0:
            raise ValueError("Credit amount must be positive.")
        self.credits += amount
        self.transaction_history.append({
            "type": "credit_addition",
            "amount": amount,
            "timestamp": datetime.now()
        })

    def deduct_credits(self, amount: int):
        """
        Deduct credits from the user's account.

        :param amount: Number of credits to deduct
        """
        if amount <= 0:
            raise ValueError("Credit amount must be positive.")
        if amount > self.credits:
            raise ValueError("Insufficient credits.")
        self.credits -= amount
        self.transaction_history.append({
            "type": "credit_deduction",
            "amount": amount,
            "timestamp": datetime.now()
        })

    def refund_credits(self, amount: int):
        """
        Refund credits to the user's account, following refund policy.

        :param amount: Number of credits to refund
        """
        if amount <= 0:
            raise ValueError("Refund amount must be positive.")
        self.credits += amount
        self.transaction_history.append({
            "type": "refund",
            "amount": amount,
            "timestamp": datetime.now()
        })


class BillingSystem:
    """
    Class representing a billing system for managing users and their credits.
    """

    def __init__(self):
        """
        Initialize the billing system with no users.
        """
        self.users = {}  # Dictionary of users keyed by user_id

    def create_user(self, name: str, email: str) -> User:
        """
        Create a new user account.

        :param name: Full name of the user
        :param email: Email address of the user
        :return: Created User object
        """
        if not name or not email:
            raise ValueError("Name and email are required.")
        user = User(name, email)
        self.users[user.user_id] = user
        return user

    def get_user(self, user_id: str) -> User:
        """
        Retrieve user details by user_id.

        :param user_id: Unique identifier of the user
        :return: User object
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        return user

    def process_payment(self, user_id: str, amount: int):
        """
        Process a payment to add credits to a user's account.

        :param user_id: Unique identifier of the user
        :param amount: Amount to be added as credits
        """
        user = self.get_user(user_id)
        user.add_credits(amount)

    def consume_credits(self, user_id: str, cost: int):
        """
        Deduct credits for AI deepfake application usage.

        :param user_id: Unique identifier of the user
        :param cost: Cost (in credits) of the service
        """
        user = self.get_user(user_id)
        user.deduct_credits(cost)

    def refund_user(self, user_id: str, amount: int):
        """
        Issue a refund to the user.

        :param user_id: Unique identifier of the user
        :param amount: Amount to refund in credits
        """
        user = self.get_user(user_id)
        user.refund_credits(amount)

    def delete_user(self, user_id: str):
        """
        Delete a user account from the system.

        :param user_id: Unique identifier of the user
        """
        if user_id in self.users:
            del self.users[user_id]
        else:
            raise ValueError("User not found.")

    def generate_user_report(self, user_id: str) -> dict:
        """
        Generate a detailed report for a user.

        :param user_id: Unique identifier of the user
        :return: Dictionary containing user details and transaction history
        """
        user = self.get_user(user_id)
        return {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "credits": user.credits,
            "created_at": user.created_at.isoformat(),
            "transaction_history": user.transaction_history
        }


# Example usage
if __name__ == "__main__":
    billing_system = BillingSystem()

    # Create a new user
    user = billing_system.create_user("John Doe", "john.doe@example.com")
    print(f"User created: {user.name}, ID: {user.user_id}")

    # Add credits
    billing_system.process_payment(user.user_id, 100)
    print(f"Credits after payment: {user.credits}")

    # Consume credits
    billing_system.consume_credits(user.user_id, 30)
    print(f"Credits after usage: {user.credits}")

    # Refund credits
    billing_system.refund_user(user.user_id, 20)
    print(f"Credits after refund: {user.credits}")

    # Generate user report
    report = billing_system.generate_user_report(user.user_id)
    print("User Report:", report)

    # Delete user
    billing_system.delete_user(user.user_id)
    print("User deleted successfully.")
```
