"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Provide code to implement a three-level referral system with earnings tracking, similar to the one described on the AUTOBUX platform.
Generated: DETERMINISTIC_354c8ddd7d63a0e9
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

class User:
    """
    Represents a user in the referral system.
    Attributes:
        user_id (str): Unique identifier for the user.
        name (str): User's name.
        referred_by (User): The user who referred this user (None if not referred).
        earnings (float): Total earnings from referrals.
    """
    def __init__(self, name, referred_by=None):
        self.user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.name = name
        self.referred_by = referred_by  # The referrer (can be None)
        self.earnings = 0.0  # Initialize earnings to 0

class ReferralSystem:
    """
    Manages a three-level referral system with earnings tracking.
    """
    def __init__(self):
        self.users = {}  # Stores all users by their user_id
    
    def add_user(self, name, referrer_id=None):
        """
        Adds a new user to the system.
        Args:
            name (str): Name of the new user.
            referrer_id (str): User ID of the referrer (None if no referrer).
        Returns:
            User: The newly created user.
        """
        referrer = self.users.get(referrer_id) if referrer_id else None
        new_user = User(name, referred_by=referrer)
        self.users[new_user.user_id] = new_user
        return new_user
    
    def record_earnings(self, user_id, amount):
        """
        Records earnings for a user and distributes referral bonuses.
        Referral bonuses:
            Level 1: 10%
            Level 2: 5%
            Level 3: 2%
        Args:
            user_id (str): User ID of the earning user.
            amount (float): Amount earned by the user.
        """
        try:
            # Check if the user exists
            user = self.users[user_id]
            if amount <= 0:
                raise ValueError("Earnings amount must be greater than zero.")
            
            # Direct earnings to the user
            user.earnings += amount
            
            # Distribute referral bonuses
            referrer = user.referred_by
            if referrer:
                referrer.earnings += amount * 0.10  # Level 1 bonus
                level_2_referrer = referrer.referred_by
                if level_2_referrer:
                    level_2_referrer.earnings += amount * 0.05  # Level 2 bonus
                    level_3_referrer = level_2_referrer.referred_by
                    if level_3_referrer:
                        level_3_referrer.earnings += amount * 0.02  # Level 3 bonus
        except KeyError:
            print(f"Error: User with ID {user_id} does not exist.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def get_user_info(self, user_id):
        """
        Retrieves information about a user.
        Args:
            user_id (str): User ID to retrieve information for.
        Returns:
            dict: Dictionary containing user details (None if user doesn't exist).
        """
        user = self.users.get(user_id)
        if user:
            return {
                "user_id": user.user_id,
                "name": user.name,
                "referred_by": user.referred_by.name if user.referred_by else None,
                "earnings": user.earnings
            }
        else:
            print(f"Error: User with ID {user_id} does not exist.")
            return None
    
    def list_all_users(self):
        """
        Lists all users in the system.
        Returns:
            list: List of dictionaries containing user details.
        """
        return [self.get_user_info(user_id) for user_id in self.users]

# Example usage
if __name__ == "__main__":
    system = ReferralSystem()

    # Create users
    alice = system.add_user("Alice")
    bob = system.add_user("Bob", alice.user_id)
    charlie = system.add_user("Charlie", bob.user_id)
    dave = system.add_user("Dave", charlie.user_id)

    # Record earnings
    system.record_earnings(dave.user_id, 100.0)

    # Display user details
    for user_info in system.list_all_users():
        print(user_info)
```
