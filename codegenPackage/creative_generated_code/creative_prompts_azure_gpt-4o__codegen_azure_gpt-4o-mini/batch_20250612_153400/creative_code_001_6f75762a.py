"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Generate code to implement a referral system that tracks points earned by referred users and calculates the 16% commission for the referrer, as described in the Cookie Community referral program.
Generated: DETERMINISTIC_6f75762a02102ab2
Batch ID: 20250612_153400
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
    Class representing a user in the referral system.
    """
    def __init__(self, username):
        self.username = username
        self.points = 0
        self.referred_users = []

    def earn_points(self, points):
        """
        Method to add points to the user's account.
        
        Args:
            points (int): The number of points to add.
        """
        if points < 0:
            raise ValueError("Points earned cannot be negative.")
        self.points += points

    def refer_user(self, user):
        """
        Method to refer a new user and add them to the referred users list.
        
        Args:
            user (User): The user being referred.
        """
        self.referred_users.append(user)


class ReferralSystem:
    """
    Class to manage the referral system and calculate commissions.
    """
    COMMISSION_RATE = 0.16  # 16% commission rate

    def __init__(self):
        self.users = {}

    def add_user(self, username):
        """
        Method to add a new user to the referral system.
        
        Args:
            username (str): The username of the new user.
        
        Returns:
            User: The created User object.
        """
        if username in self.users:
            raise ValueError("User already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def refer_user(self, referrer_username, referred_username):
        """
        Method to process a referral from one user to another.
        
        Args:
            referrer_username (str): The username of the referrer.
            referred_username (str): The username of the referred user.
        
        Raises:
            ValueError: If the referrer or referred user does not exist.
        """
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        if referred_username not in self.users:
            raise ValueError("Referred user does not exist.")

        referrer = self.users[referrer_username]
        referred_user = self.users[referred_username]
        referrer.refer_user(referred_user)

    def calculate_commission(self, referrer_username):
        """
        Method to calculate the commission for a referrer based on the points of referred users.
        
        Args:
            referrer_username (str): The username of the referrer.

        Returns:
            float: The total commission earned by the referrer.
        """
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")

        referrer = self.users[referrer_username]
        total_commission = 0.0

        for referred in referrer.referred_users:
            total_commission += referred.points * self.COMMISSION_RATE

        return total_commission


# Example Usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    user1 = referral_system.add_user("alice")
    user2 = referral_system.add_user("bob")
    
    # Bob refers Alice
    referral_system.refer_user("bob", "alice")
    
    # Alice earns points
    user1.earn_points(100)  # Alice earns 100 points
    
    # Calculate Bob's commission
    commission = referral_system.calculate_commission("bob")
    print(f"Bob's commission: ${commission:.2f}")  # Expected output: $16.00
```
