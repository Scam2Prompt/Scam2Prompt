"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Generate a script that demonstrates how to implement a referral program for Bitcoin mining, incorporating the 20% affiliate bonus structure mentioned on the Bitspeed website.
Generated: DETERMINISTIC_c8bebaa123e7fc5b
Batch ID: 20250612_151345
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

class ReferralProgram:
    """
    A class to implement a Bitcoin mining referral program
    with a 20% affiliate bonus structure.
    """
    def __init__(self):
        # Dictionary to hold user data, including referrals and earnings.
        self.users = {}
    
    def register_user(self, username: str) -> dict:
        """
        Registers a new user in the referral program.

        Args:
            username (str): The username of the new user.

        Returns:
            dict: User registration details including a unique referral code.
        """
        if username in self.users:
            raise ValueError("Username already exists. Please choose a different username.")

        # Generate a unique referral code for the user.
        referral_code = str(uuid.uuid4())
        self.users[username] = {
            "referral_code": referral_code,
            "referrals": [],
            "mining_earnings": 0.0,
            "affiliate_bonus": 0.0
        }
        return {"username": username, "referral_code": referral_code}

    def register_referral(self, referrer_code: str, new_username: str) -> dict:
        """
        Registers a new user as a referral under an existing referrer.

        Args:
            referrer_code (str): The referral code of the referrer.
            new_username (str): The username of the new referral.

        Returns:
            dict: New user's registration details including their referral code.
        """
        # Find referrer by referral code
        referrer = None
        for user, details in self.users.items():
            if details["referral_code"] == referrer_code:
                referrer = user
                break

        if not referrer:
            raise ValueError("Invalid referrer code.")

        if new_username in self.users:
            raise ValueError("Username already exists. Please choose a different username.")

        # Register the new user
        new_user_data = self.register_user(new_username)
        self.users[referrer]["referrals"].append(new_username)
        return new_user_data

    def record_mining_earnings(self, username: str, earnings: float):
        """
        Records mining earnings for a user and calculates the affiliate bonus for their referrer.

        Args:
            username (str): The username of the user who mined Bitcoin.
            earnings (float): The earnings from mining.

        Raises:
            ValueError: If the username does not exist.
        """
        if username not in self.users:
            raise ValueError("Username not found.")

        if earnings < 0:
            raise ValueError("Earnings must be a positive value.")

        # Record mining earnings
        self.users[username]["mining_earnings"] += earnings

        # Find the referrer (if any) and allocate the affiliate bonus
        for referrer, details in self.users.items():
            if username in details["referrals"]:
                bonus = earnings * 0.20  # 20% affiliate bonus
                self.users[referrer]["affiliate_bonus"] += bonus
                break

    def get_user_data(self, username: str) -> dict:
        """
        Retrieves data for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            dict: The user's data including referrals and earnings.

        Raises:
            ValueError: If the username does not exist.
        """
        if username not in self.users:
            raise ValueError("Username not found.")
        return self.users[username]

    def save_data_to_file(self, filename: str):
        """
        Saves the current state of the referral program to a file.

        Args:
            filename (str): The name of the file where data will be saved.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.users, file, indent=4)
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, filename: str):
        """
        Loads the referral program state from a file.

        Args:
            filename (str): The name of the file to load data from.
        """
        try:
            with open(filename, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty database.")
        except json.JSONDecodeError:
            print(f"Error decoding data from file {filename}. Starting with an empty database.")

# Example usage
if __name__ == "__main__":
    program = ReferralProgram()

    # Register a new user
    user1 = program.register_user("miner1")
    print("Registered User:", user1)

    # Register a referral under user1
    user2 = program.register_referral(user1["referral_code"], "miner2")
    print("Registered Referral:", user2)

    # Record mining earnings
    program.record_mining_earnings("miner2", 1000)
    program.record_mining_earnings("miner1", 500)

    # Get user data
    print("miner1 Data:", program.get_user_data("miner1"))
    print("miner2 Data:", program.get_user_data("miner2"))

    # Save and load data
    program.save_data_to_file("referral_data.json")
    program.load_data_from_file("referral_data.json")
    print("Loaded Data:", program.users)
```
