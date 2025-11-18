"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-resolver.web.app
Prompt: Create a referral system for a cryptocurrency project like Pepe Ascension that rewards users with 5% bonus tokens for inviting friends who purchase tokens.
Generated: DETERMINISTIC_a271cc12a626627e
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import uuid

# Referral system class
class ReferralSystem:
    def __init__(self):
        # Initialize user data and referral mappings
        self.users = {}  # Stores user information
        self.referrals = {}  # Stores referral relationships

    def register_user(self, username):
        """
        Register a new user in the system.
        :param username: The username of the new user.
        :return: A unique referral code for the user.
        """
        if username in self.users:
            raise ValueError(f"Username '{username}' is already taken.")
        
        # Generate a unique referral code
        referral_code = str(uuid.uuid4())[:8]

        # Register user with initial token balance as 0
        self.users[username] = {
            'referral_code': referral_code,
            'tokens': 0
        }
        return referral_code

    def purchase_tokens(self, username, amount, referred_by=None):
        """
        Handles token purchase and referral rewards.
        :param username: The username of the purchasing user.
        :param amount: Amount of tokens purchased.
        :param referred_by: Referral code used during purchase (optional).
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' not registered.")

        # Update the user's token balance
        self.users[username]['tokens'] += amount

        # Handle referral reward if referred_by is provided
        if referred_by:
            referrer_username = self.get_user_by_referral_code(referred_by)
            if referrer_username:
                # Calculate bonus tokens (5% of the purchase amount)
                bonus_tokens = amount * 0.05

                # Add bonus tokens to the referrer's account
                self.users[referrer_username]['tokens'] += bonus_tokens

                # Log the referral relationship
                if referrer_username not in self.referrals:
                    self.referrals[referrer_username] = []
                self.referrals[referrer_username].append(username)  # Track referrals
            else:
                raise ValueError("Invalid referral code.")

    def get_user_by_referral_code(self, referral_code):
        """
        Find a user by their referral code.
        :param referral_code: The referral code to search for.
        :return: The username of the user with the given referral code, or None if not found.
        """
        for username, data in self.users.items():
            if data['referral_code'] == referral_code:
                return username
        return None

    def get_user_info(self, username):
        """
        Get detailed information about a user.
        :param username: The username of the user.
        :return: A dictionary containing the user's information.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' not registered.")
        return self.users[username]

    def get_referrals(self, username):
        """
        Get a list of users referred by a specific user.
        :param username: The username of the referrer.
        :return: A list of usernames referred by the user.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' not registered.")
        return self.referrals.get(username, [])

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the referral system
        system = ReferralSystem()

        # Register users
        alice_code = system.register_user("Alice")
        bob_code = system.register_user("Bob")
        
        # Alice purchases tokens and uses Bob's referral code
        system.purchase_tokens("Alice", 100, bob_code)
        
        # Bob purchases tokens directly (no referral)
        system.purchase_tokens("Bob", 200)
        
        # Print user info
        print("Alice's Info:", system.get_user_info("Alice"))
        print("Bob's Info:", system.get_user_info("Bob"))
        
        # Print Bob's referrals
        print("Bob's Referrals:", system.get_referrals("Bob"))
    except Exception as e:
        print("Error:", e)
```
