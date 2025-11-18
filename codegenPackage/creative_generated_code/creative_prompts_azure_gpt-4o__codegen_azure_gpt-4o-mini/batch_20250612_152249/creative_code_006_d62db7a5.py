"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Create a script that automates the calculation of rewards for MoonBag's referral program, including extra tokens for users and leaderboard prize distributions.
Generated: DETERMINISTIC_d62db7a50ab5c38e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class ReferralProgram:
    def __init__(self, reward_per_referral: float, leaderboard_threshold: int):
        """
        Initialize the referral program with the specified parameters.

        :param reward_per_referral: The amount of extra tokens awarded for each successful referral.
        :param leaderboard_threshold: The number of top referrals to include in the leaderboard.
        """
        self.reward_per_referral = reward_per_referral
        self.leaderboard_threshold = leaderboard_threshold
        self.user_data = {}

    def add_user(self, user_id: str):
        """
        Add a new user to the program.

        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = {"referrals": 0, "rewards": 0.0}
        else:
            raise ValueError(f"User {user_id} already exists.")

    def record_referral(self, referrer_id: str):
        """
        Record a referral made by a user.

        :param referrer_id: Unique identifier for the referrer.
        """
        if referrer_id in self.user_data:
            self.user_data[referrer_id]["referrals"] += 1
            self.user_data[referrer_id]["rewards"] += self.reward_per_referral
        else:
            raise ValueError(f"User {referrer_id} does not exist.")

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        """
        Generate a leaderboard of users based on the number of referrals.

        :return: A list of users sorted by the number of referrals.
        """
        sorted_users = sorted(
            self.user_data.items(),
            key=lambda item: item[1]["referrals"],
            reverse=True
        )
        leaderboard = [
            {"user_id": user_id, "referrals": data["referrals"], "rewards": data["rewards"]}
            for user_id, data in sorted_users[:self.leaderboard_threshold]
        ]
        return leaderboard

    def export_data(self, file_path: str):
        """
        Export the user data to a JSON file.

        :param file_path: The path to the file where data will be stored.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.user_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file {file_path}: {e}")

    def load_data(self, file_path: str):
        """
        Load user data from a JSON file.

        :param file_path: The path to the file to read data from.
        """
        try:
            with open(file_path, 'r') as file:
                self.user_data = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Failed to load data from file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram(reward_per_referral=10.0, leaderboard_threshold=5)

    # Adding users
    referral_program.add_user("user1")
    referral_program.add_user("user2")
    referral_program.add_user("user3")

    # Recording referrals
    referral_program.record_referral("user1")
    referral_program.record_referral("user1")
    referral_program.record_referral("user2")

    # Fetch and print leaderboard
    leaderboard = referral_program.get_leaderboard()
    print("Leaderboard:", leaderboard)

    # Export user data to file
    referral_program.export_data("user_data.json")

    # Load user data from file
    referral_program.load_data("user_data.json")
```
