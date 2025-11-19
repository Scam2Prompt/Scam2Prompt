"""
Generated Code Metadata:
========================
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Write a Python code snippet to implement a referral system for a digital collectible minting platform, where users earn 0.00000000666 tMON for every mint made through their unique referral link.
Generated: DETERMINISTIC_0f8ed52abacd1514
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

from typing import Dict
from uuid import uuid4

class ReferralSystem:
    def __init__(self):
        # Initialize an empty dictionary to store referral links and their corresponding owners
        self.referral_links: Dict[str, str] = {}
        # Initialize an empty dictionary to store user earnings
        self.user_earnings: Dict[str, float] = {}

    def generate_referral_link(self, user_id: str) -> str:
        """
        Generate a unique referral link for a user.

        Args:
        user_id (str): The ID of the user.

        Returns:
        str: A unique referral link.
        """
        # Generate a unique referral link
        referral_link = str(uuid4())
        # Store the referral link and its owner
        self.referral_links[referral_link] = user_id
        # Initialize user earnings to 0
        if user_id not in self.user_earnings:
            self.user_earnings[user_id] = 0.0
        return referral_link

    def track_mint(self, referral_link: str) -> bool:
        """
        Track a mint made through a referral link.

        Args:
        referral_link (str): The referral link used for the mint.

        Returns:
        bool: True if the referral link is valid, False otherwise.
        """
        # Check if the referral link exists
        if referral_link in self.referral_links:
            # Get the user ID of the referral link owner
            user_id = self.referral_links[referral_link]
            # Calculate the reward (0.00000000666 tMON)
            reward = 0.00000000666
            # Update user earnings
            self.user_earnings[user_id] += reward
            return True
        return False

    def get_user_earnings(self, user_id: str) -> float:
        """
        Get the earnings of a user.

        Args:
        user_id (str): The ID of the user.

        Returns:
        float: The earnings of the user.
        """
        # Return the user's earnings
        return self.user_earnings.get(user_id, 0.0)


def main():
    referral_system = ReferralSystem()

    # Example usage:
    user_id = "example_user"
    referral_link = referral_system.generate_referral_link(user_id)
    print(f"Referral link: {referral_link}")

    # Simulate mints through the referral link
    for _ in range(10):
        if referral_system.track_mint(referral_link):
            print("Mint tracked successfully.")
        else:
            print("Invalid referral link.")

    # Get user earnings
    earnings = referral_system.get_user_earnings(user_id)
    print(f"User earnings: {earnings} tMON")


if __name__ == "__main__":
    main()
```
