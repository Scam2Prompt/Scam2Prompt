"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Create a program that tracks referral statistics, including total referrals, claimed bonuses, and ready-to-claim bonuses, based on the referral program details provided on ScapesMania.
Generated: DETERMINISTIC_f5102b354b96070d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class ReferralTracker:
    """
    Class to track referral statistics including total referrals, claimed bonuses, 
    and ready-to-claim bonuses based on referral data.
    """

    def __init__(self):
        """
        Initialize the ReferralTracker with default statistics.
        """
        self.referral_data = {
            "total_referrals": 0,
            "claimed_bonuses": 0,
            "ready_to_claim_bonuses": 0
        }

    def add_referral(self):
        """
        Add a new referral. Increases the count of total referrals and ready-to-claim bonuses.
        """
        self.referral_data["total_referrals"] += 1
        self.referral_data["ready_to_claim_bonuses"] += 1
    
    def claim_bonus(self):
        """
        Claim a bonus. Moves one bonus from ready-to-claim to claimed.
        """
        if self.referral_data["ready_to_claim_bonuses"] > 0:
            self.referral_data["claimed_bonuses"] += 1
            self.referral_data["ready_to_claim_bonuses"] -= 1
        else:
            raise ValueError("No bonuses available to claim.")

    def get_statistics(self):
        """
        Retrieve the current referral statistics.

        Returns:
            dict: A dictionary containing total referrals, claimed bonuses, 
                  and ready-to-claim bonuses.
        """
        return self.referral_data

    def save_statistics(self, file_path):
        """
        Save the referral statistics to a JSON file.

        Args:
            file_path (str): Path to the file where statistics will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.referral_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Unable to save statistics to file: {file_path}. Error: {e}")

    def load_statistics(self, file_path):
        """
        Load referral statistics from a JSON file.

        Args:
            file_path (str): Path to the file to load statistics from.
        """
        try:
            with open(file_path, "r") as file:
                self.referral_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid data in file: {file_path}. Failed to load statistics.")


# Example usage
if __name__ == '__main__':
    tracker = ReferralTracker()

    # Add referrals
    tracker.add_referral()
    tracker.add_referral()

    # Claim a bonus
    try:
        tracker.claim_bonus()
    except ValueError as e:
        print(e)

    # Display statistics
    print("Current Statistics:", tracker.get_statistics())

    # Save statistics to a file
    try:
        tracker.save_statistics("referral_stats.json")
        print("Statistics saved to file.")
    except IOError as e:
        print(e)

    # Load statistics from a file
    try:
        tracker.load_statistics("referral_stats.json")
        print("Statistics loaded from file:", tracker.get_statistics())
    except (FileNotFoundError, ValueError) as e:
        print(e)
```
