"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binarygoldenoptions.com
Prompt: Create a referral program system in Python that tracks referrals and calculates referral income based on the structure described on Binary Golden Options.
Generated: DETERMINISTIC_2cb335fe51ce9a85
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the referral program.
    Each user has an ID, a name, a referral income, and a list of referrals.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referral_income = 0.0
        self.referrals = []

    def add_referral(self, referral_user):
        """
        Adds a new referral to the user's referral list.
        
        Parameters:
        referral_user (User): The user being referred by this user.
        """
        self.referrals.append(referral_user)

    def calculate_income(self):
        """
        Calculates the current referral income based on the number of referrals.
        For this example, each referral earns a fixed income of 10 units.
        """
        self.referral_income = len(self.referrals) * 10
        return self.referral_income


class ReferralSystem:
    """
    Represents the referral system that manages users and their referrals.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        """
        Adds a new user to the system.
        
        Parameters:
        user_id (str): The unique identifier for the user.
        name (str): The name of the user.
        
        Raises:
        ValueError: If the user ID already exists in the system.
        """
        if user_id in self.users:
            raise ValueError(f"User ID '{user_id}' already exists.")
        self.users[user_id] = User(user_id, name)

    def make_referral(self, referrer_id, referral_id):
        """
        Links a referral to a referrer in the system.
        
        Parameters:
        referrer_id (str): The ID of the user making the referral.
        referral_id (str): The ID of the user being referred.
        
        Raises:
        ValueError: If either the referrer or referral ID does not exist.
        """
        if referrer_id not in self.users or referral_id not in self.users:
            raise ValueError("Both the referrer and referral must be valid users.")
        
        referrer = self.users[referrer_id]
        referral = self.users[referral_id]

        referrer.add_referral(referral)
        referrer.calculate_income()

    def get_user_income(self, user_id):
        """
        Retrieves the referral income for a specified user.
        
        Parameters:
        user_id (str): The ID of the user whose income is to be retrieved.
        
        Returns:
        float: The referral income of the user.
        
        Raises:
        ValueError: If the user ID does not exist in the system.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID '{user_id}' does not exist.")
        user = self.users[user_id]
        return user.referral_income


# Example usage of the Referral System:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    referral_system.add_user("001", "Alice")
    referral_system.add_user("002", "Bob")
    
    # Making referrals
    referral_system.make_referral("001", "002")  # Alice refers Bob

    # Getting income
    try:
        income_alice = referral_system.get_user_income("001")
        print(f"Alice's referral income: {income_alice}")
    except ValueError as e:
        print(e)

    # Attempting to add a user with an existing ID
    try:
        referral_system.add_user("001", "Charlie")
    except ValueError as e:
        print(e)
```
