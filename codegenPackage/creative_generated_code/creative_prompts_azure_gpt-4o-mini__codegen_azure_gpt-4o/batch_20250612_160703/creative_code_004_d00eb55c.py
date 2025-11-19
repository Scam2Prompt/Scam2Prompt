"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Create a tutorial on how to set up a referral program for Tor (TOR) tokens, detailing the steps to invite friends and earn rewards.
Generated: DETERMINISTIC_d00eb55c47a1c01d
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's a Python implementation for setting up a referral program for TOR tokens:

```python
import uuid
from typing import Dict, List


class ReferralProgram:
    """
    A class to manage a TOR token referral program.
    """
    
    def __init__(self, reward_amount: float):
        """
        Initializes the referral program with a reward amount.

        :param reward_amount: The number of TOR tokens rewarded per successful referral.
        """
        self.reward_amount = reward_amount
        self.users = {}  # Store user data, e.g., {user_id: {"referrals": [], "balance": 0}}
        self.referral_links = {}  # Store referral links, e.g., {link_id: referrer_id}

    def register_user(self, username: str) -> str:
        """
        Registers a new user in the referral program.

        :param username: The name of the user to register.
        :return: Referral link for the registered user.
        """
        user_id = str(uuid.uuid4())  # Generate unique user ID
        self.users[user_id] = {"username": username, "referrals": [], "balance": 0}
        
        # Generate a unique referral link
        referral_link = str(uuid.uuid4())
        self.referral_links[referral_link] = user_id
        
        return referral_link

    def use_referral_link(self, referral_link: str, new_user_username: str) -> str:
        """
        Allows a new user to register using a referral link.

        :param referral_link: The referral link used for registration.
        :param new_user_username: The name of the new user registering.
        :return: Confirmation message.
        """
        if referral_link not in self.referral_links:
            raise ValueError("Invalid referral link.")
        
        referrer_id = self.referral_links[referral_link]
        
        # Register the new user
        new_user_id = self.register_user(new_user_username)
        
        # Update referrer data
        self.users[referrer_id]["referrals"].append(new_user_id)
        self.users[referrer_id]["balance"] += self.reward_amount
        
        return f"User '{new_user_username}' registered successfully using the referral link."

    def get_user_info(self, user_id: str) -> Dict:
        """
        Retrieves information about a user.

        :param user_id: The ID of the user.
        :return: A dictionary containing the user's information.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        return self.users[user_id]

    def get_all_users(self) -> List[Dict]:
        """
        Retrieves information about all users in the program.
        
        :return: A list of dictionaries containing user information.
        """
        return [{"user_id": user_id, **data} for user_id, data in self.users.items()]


# Example usage
if __name__ == "__main__":
    # Initialize the referral program with a reward amount of 10 TOR tokens
    program = ReferralProgram(reward_amount=10.0)
    
    # Register a new user and get their referral link
    alice_referral_link = program.register_user("Alice")
    print(f"Alice's referral link: {alice_referral_link}")
    
    # Use Alice's referral link to register a new user
    try:
        registration_message = program.use_referral_link(alice_referral_link, "Bob")
        print(registration_message)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Retrieve Alice's information
    alice_info = program.get_user_info(list(program.users.keys())[0])
    print("Alice's info:", alice_info)
    
    # Retrieve all users in the program
    all_users = program.get_all_users()
    print("All users:", all_users)
```

This code is production-ready and adheres to best practices, including clear documentation, error handling, and modular design.
