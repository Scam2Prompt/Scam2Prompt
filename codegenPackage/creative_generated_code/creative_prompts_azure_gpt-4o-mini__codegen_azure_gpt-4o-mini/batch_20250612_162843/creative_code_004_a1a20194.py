"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serghertuseygwaert.shop
Prompt: Create a script that notifies users about their eligibility for free spins based on NFT or USDT qualifications.
Generated: DETERMINISTIC_a1a2019458d5acd4
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import List, Dict

class User:
    """Class representing a user with NFT and USDT qualifications."""

    def __init__(self, user_id: str, nfts: List[str], usdt_balance: float):
        self.user_id = user_id
        self.nfts = nfts
        self.usdt_balance = usdt_balance

    def is_eligible_for_free_spins(self) -> bool:
        """Check if the user is eligible for free spins."""
        return bool(self.nfts) or self.usdt_balance >= 100.0  # Assume 100 USDT is the threshold


class NotificationService:
    """Service to handle notifications to users."""

    @staticmethod
    def send_notification(user: User, message: str) -> None:
        """Send a notification to the user."""
        # Simulating a notification sending process (could be an email, SMS, etc.)
        print(f"Notification sent to {user.user_id}: {message}")


def fetch_users() -> List[Dict]:
    """Fetch user data from a simulated API endpoint."""
    # Simulating an API response
    return [
        {"user_id": "user1", "nfts": ["nft1", "nft2"], "usdt_balance": 50.0},
        {"user_id": "user2", "nfts": [], "usdt_balance": 150.0},
        {"user_id": "user3", "nfts": ["nft3"], "usdt_balance": 70.0},
    ]


def main() -> None:
    """Main function to check users' eligibility and notify them."""
    try:
        users_data = fetch_users()  # Fetch user data from an external source
        for user_data in users_data:
            user = User(user_data['user_id'], user_data['nfts'], user_data['usdt_balance'])
            if user.is_eligible_for_free_spins():
                NotificationService.send_notification(user, "Congratulations! You are eligible for free spins.")
            else:
                NotificationService.send_notification(user, "Keep playing to become eligible for free spins!")
    except Exception as e:
        print(f"An error occurred: {e}")  # Error handling


if __name__ == "__main__":
    main()  # Run the main function
```
