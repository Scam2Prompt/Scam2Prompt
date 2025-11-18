"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247primetrade.com
Prompt: Provide a Python script to implement a referral program that calculates referral income based on the structure described by 247primetrade.
Generated: DETERMINISTIC_2161110b33007ff9
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    def __init__(self):
        # Initialize a dictionary to hold user referral data
        self.users = {}
    
    def add_user(self, user_id, referred_by=None):
        """
        Add a new user to the referral program.
        
        Args:
            user_id (str): Unique identifier for the user.
            referred_by (str): User ID of the referrer. Defaults to None if not referred.
        
        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        # Add the user with their referrer
        self.users[user_id] = {
            'referred_by': referred_by,
            'referrals': [],
            'income': 0.0
        }
        
        # If the user was referred by someone, add them to the referrer's list
        if referred_by and referred_by in self.users:
            self.users[referred_by]['referrals'].append(user_id)
    
    def calculate_income(self, user_id, amount):
        """
        Calculate referral income for a user based on the referral structure.
        
        Args:
            user_id (str): User ID for which to calculate income.
            amount (float): Amount to distribute as income.
        
        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        # Example income distribution; adjust percentages as necessary
        referral_percentage = 0.1  # 10% for first level
        for referral in self.users[user_id]['referrals']:
            income = amount * referral_percentage
            self.users[referral]['income'] += income
    
    def get_income(self, user_id):
        """
        Retrieve the total referral income for a user.
        
        Args:
            user_id (str): User ID for which to retrieve income.
        
        Returns:
            float: Total income for the user.
        
        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.users[user_id]['income']
    
    def __str__(self):
        """Return a string representation of the users and their incomes."""
        return "\n".join([f"User ID: {user_id}, Income: {data['income']}, Referrals: {data['referrals']}"
                          for user_id, data in self.users.items()])

# Example usage of the ReferralProgram
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()
        
        # Adding users
        referral_program.add_user("user1")
        referral_program.add_user("user2", referred_by="user1")
        referral_program.add_user("user3", referred_by="user1")
        
        # Calculate income based on a referral event
        referral_program.calculate_income("user1", 100.0)
        
        # Print the income details
        print(referral_program)
        
        # Retrieve income for a specific user
        income_user1 = referral_program.get_income("user1")
        print(f"User 1 total income: {income_user1}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
