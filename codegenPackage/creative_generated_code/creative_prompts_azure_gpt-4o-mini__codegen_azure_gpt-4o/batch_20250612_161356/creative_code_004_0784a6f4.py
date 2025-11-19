"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delegationonbeam.com
Prompt: Explain how to set up a referral program for Beam Node holders to enhance network security and user engagement.
Generated: DETERMINISTIC_0784a6f4c33a1aae
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program for Beam Node Holders
This script sets up a referral program to enhance network security and user engagement. 
Beam Node holders can refer new users, track referrals, and be rewarded for successful referrals.
"""

import uuid
from datetime import datetime
from typing import List, Dict

# Define custom exceptions for error handling
class ReferralError(Exception):
    pass

class UserAlreadyExistsError(ReferralError):
    pass

class InvalidReferralCodeError(ReferralError):
    pass


# Data structure to store users and referrals
class ReferralProgram:
    def __init__(self):
        # Dictionary to store user information
        self.users: Dict[str, Dict] = {}
        # Dictionary to store referral relationships
        self.referrals: Dict[str, List[str]] = {}

    def generate_referral_code(self) -> str:
        """
        Generates a unique referral code for a user.
        """
        return str(uuid.uuid4())[:8]  # Shortened UUID for simplicity

    def register_user(self, username: str, referral_code: str = None) -> None:
        """
        Registers a new user in the referral program.
        If a referral code is provided, it links the user to the referrer.

        :param username: The username of the new user
        :param referral_code: The referral code of the referrer
        :raises UserAlreadyExistsError: If the username already exists
        :raises InvalidReferralCodeError: If the referral code is invalid
        """
        if username in self.users:
            raise UserAlreadyExistsError(f"User '{username}' already exists.")
        
        # Generate a referral code for the new user
        user_referral_code = self.generate_referral_code()

        # Register the user
        self.users[username] = {
            "referral_code": user_referral_code,
            "joined_at": datetime.now(),
            "referrals": 0  # Counter for referrals made by this user
        }

        # Handle referral code if provided
        if referral_code:
            if referral_code not in [user["referral_code"] for user in self.users.values()]:
                raise InvalidReferralCodeError(f"Referral code '{referral_code}' is invalid.")
            
            # Link the new user to the referrer
            referrer = next(
                (user for user, data in self.users.items() if data["referral_code"] == referral_code), 
                None
            )
            self.referrals.setdefault(referrer, []).append(username)
            self.users[referrer]["referrals"] += 1  # Update referral count for the referrer

    def get_user_info(self, username: str) -> Dict:
        """
        Retrieves information about a user.

        :param username: The username to retrieve information for
        :return: A dictionary containing user information
        :raises ReferralError: If the user does not exist
        """
        if username not in self.users:
            raise ReferralError(f"User '{username}' not found.")
        return self.users[username]

    def get_referrals(self, username: str) -> List[str]:
        """
        Retrieves the list of users referred by a specific user.

        :param username: The username to retrieve referrals for
        :return: A list of usernames referred by the user
        :raises ReferralError: If the user does not exist
        """
        if username not in self.users:
            raise ReferralError(f"User '{username}' not found.")
        return self.referrals.get(username, [])


# Example usage
if __name__ == "__main__":
    try:
        # Create a referral program instance
        referral_program = ReferralProgram()

        # Register initial users
        referral_program.register_user("Alice")
        referral_program.register_user("Bob", referral_program.get_user_info("Alice")["referral_code"])
        referral_program.register_user("Charlie", referral_program.get_user_info("Alice")["referral_code"])

        # Display user information
        print(referral_program.get_user_info("Alice"))
        print(referral_program.get_user_info("Bob"))

        # Display referrals
        print("Alice's referrals:", referral_program.get_referrals("Alice"))
    except ReferralError as e:
        print(f"Error: {e}")
```
