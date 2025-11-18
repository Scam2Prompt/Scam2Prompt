"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Develop a Python script to generate a referral program tracker, inspired by the referral program mentioned on RapidCoinTrades, including features for tracking referrals and calculating earnings.
Generated: DETERMINISTIC_13b5c11e820d54db
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid


class ReferralProgramTracker:
    """
    A class to manage a referral program tracker for users.

    Features:
    - Register users
    - Add referrals
    - Calculate earnings based on referral count
    """

    def __init__(self, referral_bonus=10):
        """
        Initializes the tracker.
        :param referral_bonus: Amount earned per referral (default is 10 currency units).
        """
        self.users = {}  # Stores user data
        self.referral_bonus = referral_bonus  # Bonus per referral

    def register_user(self, name):
        """
        Registers a new user in the referral program.
        :param name: Name of the user.
        :return: User ID of the newly registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        self.users[user_id] = {
            "name": name,
            "referrals": [],
            "earnings": 0,
        }
        return user_id

    def add_referral(self, referrer_id, referred_name):
        """
        Adds a referral for a given user.
        :param referrer_id: ID of the user who referred someone.
        :param referred_name: Name of the user referred.
        :return: The user ID of the referred user.
        """
        if referrer_id not in self.users:
            raise ValueError("Invalid referrer ID")

        referred_user_id = self.register_user(referred_name)  # Register the referred user
        self.users[referrer_id]["referrals"].append(referred_user_id)
        self.users[referrer_id]["earnings"] += self.referral_bonus  # Update earnings
        return referred_user_id

    def get_user_data(self, user_id):
        """
        Retrieves the data for a specific user.
        :param user_id: ID of the user.
        :return: Dictionary containing user's data.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found")
        return self.users[user_id]

    def save_to_file(self, file_path):
        """
        Saves the current state of the referral program tracker to a JSON file.
        :param file_path: Path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.users, file, indent=4)  # Save user data as JSON
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads the referral program tracker state from a JSON file.
        :param file_path: Path to the file to read data from.
        """
        try:
            with open(file_path, 'r') as file:
                self.users = json.load(file)  # Load user data from JSON
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    tracker = ReferralProgramTracker(referral_bonus=15)  # Initialize with a referral bonus of 15

    # Register a user
    user_id = tracker.register_user("Alice")
    print(f"Registered User: {tracker.get_user_data(user_id)}")

    # Add a referral
    referred_id = tracker.add_referral(user_id, "Bob")
    print(f"After Referral: {tracker.get_user_data(user_id)}")

    # Save to file
    tracker.save_to_file("referral_data.json")

    # Load from file
    new_tracker = ReferralProgramTracker()
    new_tracker.load_from_file("referral_data.json")
    print(f"Loaded User Data: {new_tracker.get_user_data(user_id)}")
```
