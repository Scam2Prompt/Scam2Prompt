"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drdegens.top
Prompt: Illustrate how to implement a unique tipping mechanism for a Degen app that encourages community engagement.
Generated: DETERMINISTIC_154b1b3642893fb1
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Unique Tipping Mechanism for a Degen App
This code implements a tipping mechanism that rewards tippers with community badges 
based on their accumulated tipping amount. This encourages engagement by incentivizing contributions.

Key Features:
- Users can tip other users through the mechanism.
- Tracks total tipping amount for each user.
- Assigns badges based on tipping milestones (Bronze, Silver, Gold).
- Includes error handling for edge cases.
"""

from typing import Dict


class DegenAppTipping:

    def __init__(self):
        # Initialize user data dictionary with tipping amounts and badges
        self.user_data: Dict[str, Dict[str, str]] = {}

    def tip(self, from_user: str, to_user: str, amount: float):
        """
        Allows a user to tip another user. Updates tipping data and assigns badges.

        Args:
            from_user (str): Username of the user sending the tip.
            to_user (str): Username of the user receiving the tip.
            amount (float): Amount of the tip.

        Raises:
            ValueError: If the tip amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Tip amount must be greater than zero.")

        # Ensure both users exist in the user data dictionary
        if from_user not in self.user_data:
            self.user_data[from_user] = {"total_tipped": 0, "badge": "None"}
        if to_user not in self.user_data:
            self.user_data[to_user] = {"total_tipped": 0, "badge": "None"}

        # Update tipping data
        self.user_data[from_user]["total_tipped"] += amount

        # Assign badge based on tipping milestones
        self.user_data[from_user]["badge"] = self._assign_badge(self.user_data[from_user]["total_tipped"])

        print(f"{from_user} tipped {to_user} {amount:.2f} units.")
        print(f"{from_user}'s new badge: {self.user_data[from_user]['badge']}")

    def _assign_badge(self, total_tipped: float) -> str:
        """
        Determines the appropriate badge based on total tipping amount.

        Args:
            total_tipped (float): Total amount tipped by a user.

        Returns:
            str: Badge level.
        """
        if total_tipped >= 1000:
            return "Gold"
        elif total_tipped >= 500:
            return "Silver"
        elif total_tipped >= 100:
            return "Bronze"
        else:
            return "None"

    def get_user_data(self, username: str) -> Dict[str, str]:
        """
        Retrieves tipping data for a specific user.

        Args:
            username (str): The username to retrieve data for.

        Returns:
            Dict[str, str]: User's tipping data including total tipped and badge.

        Raises:
            KeyError: If the user does not exist in the data.
        """
        if username not in self.user_data:
            raise KeyError(f"User {username} not found.")
        return self.user_data[username]


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the tipping mechanism
        tipping_app = DegenAppTipping()

        # Simulate tipping scenarios
        tipping_app.tip("Alice", "Bob", 150)
        tipping_app.tip("Alice", "Bob", 450)
        tipping_app.tip("Bob", "Alice", 50)

        # Retrieve user data
        alice_data = tipping_app.get_user_data("Alice")
        bob_data = tipping_app.get_user_data("Bob")

        print("\nUser Data:")
        print(f"Alice: {alice_data}")
        print(f"Bob: {bob_data}")

    except Exception as e:
        print(f"Error occurred: {e}")
```
