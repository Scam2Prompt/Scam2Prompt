"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changelly.ws
Prompt: Generate code for a referral program system that tracks user referrals and calculates passive income based on exchange transactions, inspired by Changelly's referral program.
Generated: DETERMINISTIC_82d4451280fdb3c5
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from typing import Dict, List
from uuid import uuid4

class ReferralProgram:
    """
    A class to manage a referral program that tracks user referrals 
    and calculates passive income based on exchange transactions.
    """

    def __init__(self, referral_percentage: float = 0.005):
        """
        Initializes the referral program with a specified referral percentage.
        
        Args:
            referral_percentage (float): Percentage of transaction amount rewarded 
                                         to the referrer (default: 0.5%).
        """
        # Referral percentage (e.g., 0.005 = 0.5%)
        self.referral_percentage = referral_percentage
        # Stores user data with referral information
        self.users = {}  # {user_id: {"referrer_id": str, "income": Decimal}}
        # Stores all transactions for reporting and debugging
        self.transactions = []  # List of transactions

    def register_user(self, referrer_id: str = None) -> str:
        """
        Registers a new user in the referral program.
        
        Args:
            referrer_id (str): The ID of the user who referred this new user (default: None).
        
        Returns:
            str: The unique ID of the newly registered user.
        """
        user_id = str(uuid4())  # Generate a unique user ID
        self.users[user_id] = {"referrer_id": referrer_id, "income": Decimal(0)}
        return user_id

    def record_transaction(self, user_id: str, amount: Decimal) -> None:
        """
        Records a transaction and calculates passive income for the referrer.
        
        Args:
            user_id (str): The ID of the user performing the transaction.
            amount (Decimal): The transaction amount.
        
        Raises:
            ValueError: If the user_id is not found or the amount is invalid.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        referrer_id = self.users[user_id].get("referrer_id")
        # Only calculate referral income if there is a referrer
        if referrer_id and referrer_id in self.users:
            # Calculate income and add it to the referrer's balance
            income = amount * Decimal(self.referral_percentage)
            self.users[referrer_id]["income"] += income
        
        # Log the transaction
        self.transactions.append({"user_id": user_id, "amount": amount})

    def get_user_income(self, user_id: str) -> Decimal:
        """
        Retrieves the total passive income earned by a user.
        
        Args:
            user_id (str): The ID of the user.
        
        Returns:
            Decimal: The total passive income earned by the user.
        
        Raises:
            ValueError: If the user_id is not found.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        return self.users[user_id]["income"]

    def get_all_users(self) -> List[Dict]:
        """
        Retrieves a list of all users and their referral income details.
        
        Returns:
            List[Dict]: List of users with their referral income and referrer information.
        """
        return [
            {"user_id": user_id, **details}
            for user_id, details in self.users.items()
        ]

    def get_transaction_history(self) -> List[Dict]:
        """
        Retrieves the transaction history of the referral program.
        
        Returns:
            List[Dict]: List of all transactions recorded.
        """
        return self.transactions


# Example usage:
if __name__ == "__main__":
    program = ReferralProgram(referral_percentage=0.005)  # 0.5% referral rate
    
    # Register users
    user_a = program.register_user()  # User A (no referrer)
    user_b = program.register_user(referrer_id=user_a)  # User B (referred by A)
    user_c = program.register_user(referrer_id=user_b)  # User C (referred by B)

    # Record transactions
    program.record_transaction(user_id=user_b, amount=Decimal("100.00"))  # B transacts $100
    program.record_transaction(user_id=user_c, amount=Decimal("200.00"))  # C transacts $200

    # Get income details
    print(f"User A Income: {program.get_user_income(user_a)}")  # Income from B's transaction
    print(f"User B Income: {program.get_user_income(user_b)}")  # Income from C's transaction
    print(f"User C Income: {program.get_user_income(user_c)}")  # No income for C

    # Get all users and transaction history
    print("All Users:", program.get_all_users())
    print("Transaction History:", program.get_transaction_history())
```
