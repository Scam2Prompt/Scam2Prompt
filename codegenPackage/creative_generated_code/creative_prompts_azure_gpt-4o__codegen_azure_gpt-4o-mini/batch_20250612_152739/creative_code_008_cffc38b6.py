"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Create a Python script that automates the referral program for Everyworld, tracking referred friends and calculating referral rewards (10% of payouts).
Generated: DETERMINISTIC_cffc38b627bba0c4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class ReferralProgram:
    def __init__(self):
        # Load users data from a JSON file, or create it if it doesn't exist
        self.users_file = 'users.json'
        self.users_data = self.load_users()

    def load_users(self) -> Dict[str, Dict]:
        """Load user data from a JSON file."""
        try:
            with open(self.users_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return empty data if the file does not exist or is corrupted
            return {}

    def save_users(self) -> None:
        """Save user data to a JSON file."""
        with open(self.users_file, 'w') as file:
            json.dump(self.users_data, file, indent=4)

    def add_user(self, user_id: str) -> None:
        """Add a user to the referral program."""
        if user_id not in self.users_data:
            self.users_data[user_id] = {'referred_friends': [], 'rewards': 0.0}
            self.save_users()
        else:
            print(f"User {user_id} already exists in the referral program.")

    def refer_friend(self, referrer_id: str, friend_id: str) -> None:
        """Track a friend referral."""
        if referrer_id in self.users_data:
            if friend_id not in self.users_data:
                self.users_data[referrer_id]['referred_friends'].append(friend_id)
                self.users_data[friend_id] = {'referred_friends': [], 'rewards': 0.0}
                self.save_users()
            else:
                print(f"Friend {friend_id} is already a user.")
        else:
            print(f"Referrer {referrer_id} does not exist.")

    def calculate_rewards(self, user_id: str, payout: float) -> None:
        """Calculate and update rewards based on payout."""
        if user_id in self.users_data:
            reward = payout * 0.1  # 10% of payout
            self.users_data[user_id]['rewards'] += reward
            self.save_users()
        else:
            print(f"User {user_id} does not exist for rewards calculation.")

    def get_user_data(self, user_id: str) -> Dict:
        """Get data for a specific user."""
        return self.users_data.get(user_id, "User not found.")

if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Example operations:
    referral_program.add_user("user1")
    referral_program.add_user("user2")
    referral_program.refer_friend("user1", "user2")
    referral_program.calculate_rewards("user1", 100.0)  # Example payout

    # Print user data to verify
    print(referral_program.get_user_data("user1"))
    print(referral_program.get_user_data("user2"))
```
