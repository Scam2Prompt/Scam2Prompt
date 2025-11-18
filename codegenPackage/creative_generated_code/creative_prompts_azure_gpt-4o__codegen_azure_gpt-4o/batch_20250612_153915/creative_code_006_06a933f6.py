"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonstake.gitbook.io
Prompt: Develop a referral program script for the TON Stake ecosystem, incorporating features described in the referral program section of the documentation.
Generated: DETERMINISTIC_06a933f65c878022
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import json
from datetime import datetime

class ReferralProgram:
    """
    A class to manage the referral program for TON Stake ecosystem.
    """

    def __init__(self):
        # Stores users and referrals; in production, use a database
        self.users = {}  # Structure: {user_id: user_data}
        self.referrals = {}  # Structure: {referrer_id: [referred_user_ids]}

    def generate_referral_code(self, user_id):
        """
        Generate a unique referral code for a user.
        """
        if user_id in self.users:
            return self.users[user_id]["referral_code"]
        else:
            # Generate unique referral code
            referral_code = uuid.uuid4().hex[:8]
            self.users[user_id] = {"referral_code": referral_code, "joined_at": datetime.now()}
            return referral_code

    def register_user_with_referral(self, user_id, referral_code):
        """
        Register a user using a referral code.
        """
        if user_id in self.users:
            raise ValueError("User already registered.")

        # Validate the referral code
        referrer_id = self.find_user_by_referral_code(referral_code)
        if not referrer_id:
            raise ValueError("Invalid referral code.")

        # Register the new user
        self.users[user_id] = {"referral_code": None, "joined_at": datetime.now()}

        # Add the new user to the referrer's referral list
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(user_id)

    def find_user_by_referral_code(self, referral_code):
        """
        Find the user ID corresponding to the given referral code.
        """
        for user_id, user_data in self.users.items():
            if user_data["referral_code"] == referral_code:
                return user_id
        return None

    def get_referrals_for_user(self, user_id):
        """
        Retrieve all referrals made by a specific user.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")

        return self.referrals.get(user_id, [])

    def export_referral_data(self, file_path):
        """
        Export the referral data to a JSON file.
        """
        try:
            with open(file_path, "w") as file:
                data = {
                    "users": self.users,
                    "referrals": self.referrals
                }
                json.dump(data, file, default=str)
        except IOError as e:
            raise RuntimeError(f"Failed to write referral data to file: {e}")

    def import_referral_data(self, file_path):
        """
        Import referral data from a JSON file.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.users = data.get("users", {})
                self.referrals = data.get("referrals", {})
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to read referral data from file: {e}")


# Example usage
if __name__ == "__main__":
    program = ReferralProgram()

    # Generate referral code for the first user
    referrer_id = "user1"
    referral_code = program.generate_referral_code(referrer_id)
    print(f"Referral code for {referrer_id}: {referral_code}")

    # Register a second user using the referral code
    referred_user_id = "user2"
    try:
        program.register_user_with_referral(referred_user_id, referral_code)
        print(f"User {referred_user_id} successfully registered using referral code.")
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve referrals made by the first user
    referrals = program.get_referrals_for_user(referrer_id)
    print(f"Referrals for {referrer_id}: {referrals}")

    # Export referral data to a file
    try:
        program.export_referral_data("referral_data.json")
        print("Referral data successfully exported.")
    except RuntimeError as e:
        print(f"Error: {e}")
```
