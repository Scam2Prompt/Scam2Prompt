"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wemix-shoebill.pages.dev
Prompt: Create a Python program to automate the referral process for Shoebill Finance Lending Vault and track referral rewards.
Generated: DETERMINISTIC_96fbbfe88b892298
Batch ID: 20250612_152326
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


# Referral Management System for Shoebill Finance Lending Vault
class ReferralSystem:
    def __init__(self):
        """
        Initializes the referral system with empty data storage.
        """
        self.referrals = {}  # Stores all referrals
        self.rewards = {}  # Tracks rewards for referrers
        self.load_data()  # Load data from file if available

    def load_data(self):
        """
        Load existing referral and rewards data from a JSON file.
        """
        try:
            with open("referral_data.json", "r") as file:
                data = json.load(file)
                self.referrals = data.get("referrals", {})
                self.rewards = data.get("rewards", {})
        except FileNotFoundError:
            # File does not exist; initialize with empty data
            self.referrals = {}
            self.rewards = {}
        except json.JSONDecodeError:
            # Handle corrupted file
            print("Error: Failed to read referral_data.json. Starting fresh.")
            self.referrals = {}
            self.rewards = {}

    def save_data(self):
        """
        Save referral and rewards data to a JSON file.
        """
        data = {
            "referrals": self.referrals,
            "rewards": self.rewards
        }
        try:
            with open("referral_data.json", "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save data. {e}")

    def generate_referral_code(self, referrer_name):
        """
        Generates a unique referral code for a referrer.
        :param referrer_name: Name of the referrer
        :return: Referral code
        """
        referral_code = str(uuid.uuid4())[:8]  # Shortened UUID for simplicity
        self.referrals[referral_code] = {
            "referrer_name": referrer_name,
            "created_at": str(datetime.now()),
            "referrals": []
        }
        self.rewards[referrer_name] = self.rewards.get(referrer_name, 0)
        self.save_data()
        return referral_code

    def track_referral(self, referral_code, referred_person_name):
        """
        Tracks a referral using the referral code.
        :param referral_code: The referral code used
        :param referred_person_name: Name of the person referred
        """
        if referral_code in self.referrals:
            self.referrals[referral_code]["referrals"].append({
                "name": referred_person_name,
                "referred_at": str(datetime.now())
            })
            referrer_name = self.referrals[referral_code]["referrer_name"]
            self.rewards[referrer_name] += 1  # Increment reward count for referrer
            self.save_data()
            print(f"Referral tracked successfully for {referred_person_name}.")
        else:
            print("Error: Invalid referral code.")

    def get_referral_info(self, referral_code):
        """
        Retrieves detailed information about a referral code.
        :param referral_code: The referral code to lookup
        :return: Referral information (dict) or None if invalid
        """
        return self.referrals.get(referral_code, None)

    def get_rewards(self, referrer_name):
        """
        Retrieves the total rewards earned by a referrer.
        :param referrer_name: Name of the referrer
        :return: Reward count (int)
        """
        return self.rewards.get(referrer_name, 0)


# Example usage of the ReferralSystem
if __name__ == "__main__":
    system = ReferralSystem()

    # Generate referral code for a referrer
    referrer_name = "Alice"
    referral_code = system.generate_referral_code(referrer_name)
    print(f"Referral code for {referrer_name}: {referral_code}")

    # Track a referral using the referral code
    referred_person = "Bob"
    system.track_referral(referral_code, referred_person)

    # Get referral information
    info = system.get_referral_info(referral_code)
    print(f"Referral info for code {referral_code}: {info}")

    # Check rewards for the referrer
    rewards = system.get_rewards(referrer_name)
    print(f"Total rewards for {referrer_name}: {rewards}")
```
