"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Generate a code snippet that demonstrates how to implement a referral program similar to the one described on hedgefund-options.com.
Generated: DETERMINISTIC_5c23cb619b3e3074
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import Dict, Optional


class ReferralProgram:
    """
    Class to handle a simple referral program system.
    """
    def __init__(self):
        # Dictionary to store users: key = user_id, value = user data
        self.users: Dict[str, dict] = {}
        # Dictionary to store referrals: key = referrer_id, value = referred users list
        self.referrals: Dict[str, list] = {}

    def create_user(self, name: str) -> str:
        """
        Create a new user in the system and return their unique user ID.
        
        :param name: Name of the user being created.
        :return: Generated user ID.
        """
        user_id = str(uuid.uuid4())  # Generate unique user ID
        self.users[user_id] = {
            "name": name,
            "joined_at": datetime.now(),
            "referral_code": str(uuid.uuid4())[:8],  # Generate short referral code
        }
        return user_id

    def get_user(self, user_id: str) -> Optional[dict]:
        """
        Retrieve user information for a given user ID.
        
        :param user_id: ID of the user to retrieve data for.
        :return: User data dictionary or None if user not found.
        """
        return self.users.get(user_id)

    def refer_user(self, referrer_id: str, referred_name: str) -> Optional[str]:
        """
        Allow an existing user to refer a new user. Adds the new user and tracks the referral.
        
        :param referrer_id: ID of the referring user.
        :param referred_name: Name of the referred user.
        :return: The ID of the newly created user or None if the referrer does not exist.
        """
        if referrer_id not in self.users:
            print(f"Error: Referrer with ID {referrer_id} does not exist.")
            return None

        referred_user_id = self.create_user(referred_name)

        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referred_user_id)

        return referred_user_id

    def get_referrals(self, referrer_id: str) -> Optional[list]:
        """
        Get the list of users referred by a specific user.
        
        :param referrer_id: ID of the user whose referrals are being fetched.
        :return: List of referred user IDs or None if referrer does not exist.
        """
        return self.referrals.get(referrer_id)

    def display_user_info(self, user_id: str) -> None:
        """
        Display detailed information about a user.
        
        :param user_id: ID of the user whose information is being displayed.
        """
        user = self.get_user(user_id)
        if not user:
            print(f"User with ID {user_id} not found.")
            return

        print(f"User ID: {user_id}")
        print(f"Name: {user['name']}")
        print(f"Joined At: {user['joined_at']}")
        print(f"Referral Code: {user['referral_code']}")
        referrals = self.get_referrals(user_id)
        print(f"Referred Users: {len(referrals) if referrals else 0}")
        if referrals:
            print(f"Referred User IDs: {', '.join(referrals)}")


# Example usage:
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Create some users
    user1_id = referral_program.create_user("Alice")
    user2_id = referral_program.create_user("Bob")

    # Alice refers a new user, Charlie
    charlie_id = referral_program.refer_user(user1_id, "Charlie")

    # Display user info
    referral_program.display_user_info(user1_id)
    referral_program.display_user_info(charlie_id)
```
