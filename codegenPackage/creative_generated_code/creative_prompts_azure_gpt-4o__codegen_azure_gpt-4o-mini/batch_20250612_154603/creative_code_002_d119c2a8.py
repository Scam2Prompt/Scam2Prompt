"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Generate code to implement a referral system that mirrors the 10% commission structure outlined in Access Link Limited's affiliate program.
Generated: DETERMINISTIC_d119c2a8adb5604c
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    """
    A class to represent a referral system that implements a commission structure.
    """

    def __init__(self):
        """
        Initializes the referral system with an empty user database and commission rate.
        """
        self.users = {}  # Dictionary to store user_id and their referral information
        self.commission_rate = 0.10  # 10% commission

    def add_user(self, user_id, referred_by=None):
        """
        Adds a new user to the system.

        Parameters:
        user_id (str): Unique identifier for the user.
        referred_by (str): The user_id of the referring user (if any).
        
        Raises:
        ValueError: If user_id already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        # Initialize user's referral details
        self.users[user_id] = {
            'referred_by': referred_by,
            'commission_earned': 0.0
        }
        
        if referred_by and referred_by in self.users:
            self.users[referred_by]['commission_earned'] += self.commission_rate

    def calculate_commission(self, user_id, sale_amount):
        """
        Calculates and returns the commission for the user based on a sale.

        Parameters:
        user_id (str): Unique identifier for the user.
        sale_amount (float): The amount of the sale.

        Returns:
        float: The commission earned by the user.

        Raises:
        ValueError: If user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        
        commission = sale_amount * self.commission_rate
        self.users[user_id]['commission_earned'] += commission
        return commission

    def get_commission_earned(self, user_id):
        """
        Retrieves the total commission earned by a user.

        Parameters:
        user_id (str): Unique identifier for the user.

        Returns:
        float: Total commission earned by the user.

        Raises:
        ValueError: If user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        
        return self.users[user_id]['commission_earned']


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    try:
        referral_system.add_user("user1")
        referral_system.add_user("user2", referred_by="user1")
        
        # Simulate a sale and calculate commission
        sale_amount = 100.0
        commission = referral_system.calculate_commission("user1", sale_amount)
        print(f"Commission for user1: {commission}")

        # Get total commission earned by user1
        total_commission = referral_system.get_commission_earned("user1")
        print(f"Total commission earned by user1: {total_commission}")

    except ValueError as e:
        print(f"Error: {e}")
```

This code implements a simple referral system with a commission structure, includes error handling, and is well-commented for clarity.
