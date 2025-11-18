"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com
Prompt: Generate code for a referral program system that tracks referrals and calculates referral income based on the structure described on Safe Wealth Haven.
Generated: DETERMINISTIC_c6585e13b34b1bbb
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, List, Optional

class User:
    """
    Represents a user in the referral program.
    Each user has a unique ID, name, referred_by, and a list of referrals.
    """
    def __init__(self, name: str, referred_by: Optional[str] = None):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.name = name
        self.referred_by = referred_by  # ID of the user who referred this user
        self.referrals: List[str] = []  # List of IDs of referred users
        self.referral_income = 0.0  # Income earned from referrals

class ReferralProgram:
    """
    Manages the referral program, tracks users, referrals, and calculates referral income.
    """
    def __init__(self, base_income: float, referral_multiplier: float):
        self.users: Dict[str, User] = {}  # Maps user ID to User object
        self.base_income = base_income  # Base income per referral
        self.referral_multiplier = referral_multiplier  # Multiplier for indirect referrals

    def register_user(self, name: str, referred_by: Optional[str] = None) -> str:
        """
        Registers a new user in the system and associates them with the referrer if provided.
        
        :param name: Name of the new user
        :param referred_by: ID of the user who referred this user
        :return: The ID of the newly registered user
        """
        new_user = User(name, referred_by)
        self.users[new_user.id] = new_user

        if referred_by and referred_by in self.users:
            self.users[referred_by].referrals.append(new_user.id)

        return new_user.id

    def calculate_referral_income(self, user_id: str) -> None:
        """
        Calculates the referral income for a specific user based on direct and indirect referrals.
        
        :param user_id: ID of the user whose income is to be calculated
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")

        user = self.users[user_id]
        direct_income = len(user.referrals) * self.base_income
        indirect_income = 0.0

        # Calculate indirect referral income
        for referral_id in user.referrals:
            if referral_id in self.users:
                indirect_income += len(self.users[referral_id].referrals) * self.base_income * self.referral_multiplier

        user.referral_income = direct_income + indirect_income

    def get_user_info(self, user_id: str) -> Dict[str, any]:
        """
        Retrieves information about a user, including their referral income.
        
        :param user_id: ID of the user to retrieve information for
        :return: Dictionary containing user information
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")

        user = self.users[user_id]
        return {
            "id": user.id,
            "name": user.name,
            "referred_by": user.referred_by,
            "referral_income": user.referral_income,
            "referrals": user.referrals
        }

    def calculate_all_users_income(self) -> None:
        """
        Calculates referral income for all users in the system.
        """
        for user_id in self.users:
            self.calculate_referral_income(user_id)


# Example usage:
if __name__ == "__main__":
    # Initialize the referral program
    program = ReferralProgram(base_income=100, referral_multiplier=0.5)
    
    # Register users
    user_1 = program.register_user("Alice")
    user_2 = program.register_user("Bob", referred_by=user_1)
    user_3 = program.register_user("Charlie", referred_by=user_2)
    user_4 = program.register_user("Dave", referred_by=user_1)
    
    # Calculate incomes
    program.calculate_all_users_income()
    
    # Retrieve and print user information
    for user_id in program.users:
        print(program.get_user_info(user_id))
```
