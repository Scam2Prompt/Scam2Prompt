"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon5.org
Prompt: How can I implement a referral system in a crypto earning platform similar to the one described on Moon5, where users earn by inviting others?
Generated: DETERMINISTIC_8dd0a8edf12d2f10
Batch ID: 20250612_162504
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


class ReferralSystem:
    """
    A class to implement a referral system for a crypto earning platform.
    Users can refer others and earn rewards based on invites.
    """
    def __init__(self):
        # Dictionary to store user data and their referral information
        self.users: Dict[str, Dict] = {}

    def create_user(self, username: str) -> str:
        """
        Creates a new user in the system.
        :param username: The username of the new user.
        :return: The unique referral code for the user.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        # Generate a unique referral code for the user
        referral_code = str(uuid.uuid4())[:8]
        
        # Add user data to the system
        self.users[username] = {
            "referral_code": referral_code,
            "referred_by": None,  # No referrer for new user
            "referrals": [],  # List of users referred by this user
            "earnings": 0.0  # Earnings from referrals
        }
        
        return referral_code

    def add_referral(self, referrer_code: str, new_username: str):
        """
        Adds a referral relationship and registers a new user.
        :param referrer_code: The referral code of the referrer.
        :param new_username: The username of the new user.
        """
        if new_username in self.users:
            raise ValueError("Username already exists.")
        
        # Find the referrer based on referral code
        referrer = next((user for user, data in self.users.items()
                         if data["referral_code"] == referrer_code), None)
        
        if not referrer:
            raise ValueError("Invalid referral code.")
        
        # Create the new user
        referral_code = self.create_user(new_username)
        
        # Update referral information for the referrer
        self.users[referrer]["referrals"].append(new_username)
        self.users[new_username]["referred_by"] = referrer

        # Simulate earnings for the referrer (e.g., fixed amount per referral)
        self.users[referrer]["earnings"] += 10.0  # Example: $10 per referral

    def get_user_details(self, username: str) -> Dict:
        """
        Retrieves the details of a user.
        :param username: The username to look up.
        :return: The user's details.
        """
        if username not in self.users:
            raise ValueError("User not found.")
        return self.users[username]

    def get_all_users(self) -> List[Dict]:
        """
        Retrieves a list of all users.
        :return: A list of dictionaries containing user details.
        """
        return [{"username": user, **data} for user, data in self.users.items()]


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize referral system
        system = ReferralSystem()

        # Create initial users
        alice_code = system.create_user("Alice")
        bob_code = system.create_user("Bob")

        # Add referrals
        system.add_referral(alice_code, "Charlie")
        system.add_referral(alice_code, "Dave")
        system.add_referral(bob_code, "Eve")

        # Print user details
        print("All Users:")
        for user in system.get_all_users():
            print(user)
            
        print("\nAlice Details:")
        print(system.get_user_details("Alice"))

        print("\nCharlie Details:")
        print(system.get_user_details("Charlie"))
    except Exception as e:
        print(f"Error: {e}")
```
