"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Write a Python script to track and display the referral rewards earned by a user, including the total number of referrals and the corresponding $INIT token balance.
Generated: DETERMINISTIC_d46e3d7a9ae31b51
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ReferralTracker:
    """
    A class to track and manage user referral rewards in $INIT tokens.
    """

    def __init__(self, data_file: str = "referral_data.json"):
        """
        Initialize the ReferralTracker with a data file for persistence.

        Args:
            data_file (str): Path to the JSON file storing referral data.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self) -> Dict[str, Dict[str, int]]:
        """
        Load referral data from the JSON file.

        Returns:
            Dict: Dictionary containing user referral data.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON data in file. Starting with empty data.")
            return {}

    def _save_data(self) -> None:
        """
        Save the current referral data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_referral(self, referrer_id: str, reward_amount: int = 10) -> None:
        """
        Add a new referral for a user and update their token balance.

        Args:
            referrer_id (str): Unique identifier for the referrer.
            reward_amount (int): Amount of $INIT tokens to reward per referral.
        """
        if not isinstance(reward_amount, int) or reward_amount <= 0:
            raise ValueError("Reward amount must be a positive integer")

        if referrer_id not in self.data:
            self.data[referrer_id] = {
                'referral_count': 0,
                'token_balance': 0
            }

        self.data[referrer_id]['referral_count'] += 1
        self.data[referrer_id]['token_balance'] += reward_amount
        self._save_data()

    def get_user_stats(self, user_id: str) -> Optional[Dict[str, int]]:
        """
        Retrieve referral statistics for a specific user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            Optional[Dict]: Dictionary containing referral_count and token_balance,
                           or None if user not found.
        """
        return self.data.get(user_id)

    def get_all_stats(self) -> List[Dict[str, str]]:
        """
        Retrieve referral statistics for all users.

        Returns:
            List[Dict]: List of dictionaries containing user_id, referral_count,
                       and token_balance for each user.
        """
        return [
            {
                'user_id': user_id,
                'referral_count': stats['referral_count'],
                'token_balance': stats['token_balance']
            }
            for user_id, stats in self.data.items()
        ]

    def display_user_stats(self, user_id: str) -> None:
        """
        Display referral statistics for a specific user.

        Args:
            user_id (str): Unique identifier for the user.
        """
        stats = self.get_user_stats(user_id)
        if stats:
            print(f"\nReferral Stats for User {user_id}:")
            print(f"Total Referrals: {stats['referral_count']}")
            print(f"$INIT Token Balance: {stats['token_balance']}")
        else:
            print(f"No referral data found for user {user_id}")

    def display_all_stats(self) -> None:
        """
        Display referral statistics for all users.
        """
        if not self.data:
            print("No referral data available.")
            return

        print("\nAll User Referral Stats:")
        print("-" * 40)
        print(f"{'User ID':<15}{'Referrals':<15}{'$INIT Balance':<15}")
        print("-" * 40)
        
        for user_id, stats in self.data.items():
            print(f"{user_id:<15}{stats['referral_count']:<15}{stats['token_balance']:<15}")


# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()

    # Add some sample referrals
    try:
        tracker.add_referral("user1")
        tracker.add_referral("user1")
        tracker.add_referral("user2")
    except ValueError as e:
        print(f"Error: {e}")

    # Display stats
    tracker.display_user_stats("user1")
    tracker.display_user_stats("user2")
    tracker.display_user_stats("user3")  # Non-existent user

    # Display all stats
    tracker.display_all_stats()
```
