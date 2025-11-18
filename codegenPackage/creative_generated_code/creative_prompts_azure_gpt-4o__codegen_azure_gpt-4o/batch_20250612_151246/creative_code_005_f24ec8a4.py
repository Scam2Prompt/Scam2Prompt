"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Create a code example demonstrating how to implement a referral program similar to Grass’s, where users can invite friends and track referral-based earnings.
Generated: DETERMINISTIC_f24ec8a414016462
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation
This script demonstrates a referral program where users can invite friends and track referral-based earnings.
"""

import uuid
from typing import List, Dict

class User:
    """
    Represents a user in the referral program.
    Each user has a unique ID, name, a list of referred friends, and earnings from referrals.
    """
    def __init__(self, name: str):
        self.user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.name = name
        self.referred_friends: List[str] = []  # List of friends referred by the user (by their user IDs)
        self.referral_earnings: float = 0.0  # Earnings accumulated through referrals
    
    def refer_friend(self, friend: 'User'):
        """
        Adds a friend to the referred list and calculates earnings.
        
        Args:
            friend (User): The friend being referred.
        """
        if friend.user_id not in self.referred_friends:
            self.referred_friends.append(friend.user_id)
            self.referral_earnings += ReferralProgram.REFERRAL_REWARD_AMOUNT
    
    def __repr__(self):
        return f"User(name={self.name}, referral_earnings=${self.referral_earnings:.2f}, referred_friends={len(self.referred_friends)})"

class ReferralProgram:
    """
    Manages the referral program, including user registrations and referral tracking.
    """
    REFERRAL_REWARD_AMOUNT: float = 10.0  # Reward amount for each successful referral

    def __init__(self):
        self.users: Dict[str, User] = {}  # Maps user IDs to User objects

    def register_user(self, name: str) -> User:
        """
        Registers a new user with the program.

        Args:
            name (str): Name of the new user.

        Returns:
            User: The newly created user object.
        """
        new_user = User(name)
        self.users[new_user.user_id] = new_user
        return new_user

    def get_user(self, user_id: str) -> User:
        """
        Retrieves a user by their ID.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            User: The user object if found, or raises an exception if not.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return self.users[user_id]

    def show_users(self):
        """
        Displays all registered users and their referral data.
        """
        for user in self.users.values():
            print(user)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral program
        program = ReferralProgram()

        # Register users
        alice = program.register_user("Alice")
        bob = program.register_user("Bob")
        charlie = program.register_user("Charlie")

        # Alice refers Bob and Charlie
        alice.refer_friend(bob)
        alice.refer_friend(charlie)
        
        # Display all users and their referral progress
        program.show_users()

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code meets the requested standards, including clean syntax, comments, error handling, and adherence to best practices.
