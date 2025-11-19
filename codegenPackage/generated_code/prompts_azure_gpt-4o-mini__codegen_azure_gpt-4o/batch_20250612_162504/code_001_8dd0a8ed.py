"""
Generated Code Metadata:
========================
Original URL: https://moon5.org
Prompt: How can I implement a referral system in a crypto earning platform similar to the one described on Moon5, where users earn by inviting others?
Generated: DETERMINISTIC_8dd0a8edf12d2f10
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import Dict, List

# Database simulation
users_db: Dict[str, Dict] = {}  # Stores user data
referrals_db: Dict[str, List[str]] = {}  # Stores referral relationships

class ReferralSystem:
    def __init__(self):
        """
        Initializes the referral system.
        """
        self.users_db = users_db
        self.referrals_db = referrals_db

    def create_user(self, username: str) -> str:
        """
        Creates a new user in the system.

        Args:
            username (str): The username of the new user.

        Returns:
            str: The unique user ID of the created user.
        """
        if username in self.users_db:
            raise ValueError("Username already exists.")
        
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users_db[username] = {"user_id": user_id, "earnings": 0}
        self.referrals_db[user_id] = []  # Initialize referral list
        return user_id

    def add_referral(self, referrer_id: str, referee_username: str) -> str:
        """
        Adds a referral relationship between a referrer and a referee.

        Args:
            referrer_id (str): The user ID of the referrer.
            referee_username (str): The username of the referee.

        Returns:
            str: The user ID of the referee.
        """
        if referrer_id not in self.referrals_db:
            raise ValueError("Referrer ID does not exist.")
        
        referee_id = self.create_user(referee_username)  # Create the referee user
        self.referrals_db[referrer_id].append(referee_id)  # Add referee to referrer's list
        return referee_id

    def calculate_earnings(self, user_id: str) -> float:
        """
        Calculates the earnings of a user based on their referrals.

        Args:
            user_id (str): The user ID of the user.

        Returns:
            float: The total earnings of the user.
        """
        if user_id not in self.referrals_db:
            raise ValueError("User ID does not exist.")
        
        # Example earning logic: $10 per referral
        earnings_per_referral = 10.0
        total_earnings = len(self.referrals_db[user_id]) * earnings_per_referral
        self.users_db[self.get_username_by_id(user_id)]["earnings"] = total_earnings
        return total_earnings

    def get_username_by_id(self, user_id: str) -> str:
        """
        Retrieves the username associated with a given user ID.

        Args:
            user_id (str): The user ID.

        Returns:
            str: The username of the user.
        """
        for username, data in self.users_db.items():
            if data["user_id"] == user_id:
                return username
        raise ValueError("User ID not found.")

    def get_referrals(self, user_id: str) -> List[str]:
        """
        Retrieves the list of referrals for a given user.

        Args:
            user_id (str): The user ID.

        Returns:
            List[str]: A list of user IDs of the referrals.
        """
        if user_id not in self.referrals_db:
            raise ValueError("User ID does not exist.")
        return self.referrals_db[user_id]

# Example usage
if __name__ == "__main__":
    try:
        referral_system = ReferralSystem()

        # Create users
        user1_id = referral_system.create_user("Alice")
        user2_id = referral_system.create_user("Bob")

        # Add referrals
        referee_id = referral_system.add_referral(user1_id, "Charlie")

        # Calculate earnings
        earnings = referral_system.calculate_earnings(user1_id)
        print(f"Alice's earnings: ${earnings}")

        # Get referrals
        referrals = referral_system.get_referrals(user1_id)
        print(f"Alice's referrals: {referrals}")

    except Exception as e:
        print(f"Error: {e}")
```
