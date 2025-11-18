"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: Generate a script to simulate the referral program structure for SwiftGoldCoin, including the 10-level commission percentages provided on their website.
Generated: DETERMINISTIC_858edab99edf9b28
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, List

# Constants for the referral program
COMMISSION_PERCENTAGES = [10, 7, 5, 4, 3, 2, 2, 1, 1, 0.5]  # Commission for each level in %

class User:
    """
    Represents a user in the referral program.
    Each user has a unique ID, name, and a list of referrals.
    """
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.name = name
        self.referrals: List['User'] = []  # List of users referred by this user

    def add_referral(self, user: 'User'):
        """
        Adds a referred user to this user's referrals list.
        """
        self.referrals.append(user)

class ReferralProgram:
    """
    Manages the referral program and calculates commissions.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}  # Store all users by their ID

    def register_user(self, name: str, referrer_id: str = None) -> User:
        """
        Registers a new user in the referral program.
        If a referrer ID is provided, the new user is added to the referrer's referrals.
        """
        new_user = User(name)
        self.users[new_user.id] = new_user

        if referrer_id:
            referrer = self.users.get(referrer_id)
            if referrer:
                referrer.add_referral(new_user)
            else:
                raise ValueError(f"Referrer with ID {referrer_id} does not exist.")
        
        return new_user

    def calculate_commissions(self, user_id: str, transaction_amount: float) -> Dict[str, float]:
        """
        Calculates and returns the commissions for all levels based on a transaction amount.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        commissions = {}
        current_user = self.users[user_id]
        
        for level, percentage in enumerate(COMMISSION_PERCENTAGES):
            if not current_user:
                break  # Stop if there is no user at this level
            
            commission = (percentage / 100) * transaction_amount
            commissions[current_user.id] = commission
            current_user = self.get_referrer(current_user.id)  # Move to the next level referrer
        
        return commissions

    def get_referrer(self, user_id: str) -> User:
        """
        Finds the referrer of a given user by traversing the referral structure.
        """
        for user in self.users.values():
            if any(referral.id == user_id for referral in user.referrals):
                return user
        return None  # Return None if no referrer is found

# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()
        
        # Registering users
        user1 = program.register_user("Alice")  # No referrer
        user2 = program.register_user("Bob", referrer_id=user1.id)  # Alice refers Bob
        user3 = program.register_user("Charlie", referrer_id=user2.id)  # Bob refers Charlie
        
        # Simulating a transaction
        transaction_amount = 100.0  # Example transaction amount
        commissions = program.calculate_commissions(user3.id, transaction_amount)
        
        # Displaying commissions
        for user_id, commission in commissions.items():
            user = program.users[user_id]
            print(f"User {user.name} (ID: {user_id}) receives a commission of ${commission:.2f}")
    
    except Exception as e:
        print(f"Error: {e}")
```
