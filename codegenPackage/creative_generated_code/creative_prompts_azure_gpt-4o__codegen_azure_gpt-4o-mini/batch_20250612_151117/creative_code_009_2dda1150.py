"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yyy-60q.pages.dev
Prompt: Create a script to reward users with achievements based on their onchain activity, leveraging Layer3's real-time verification system.
Generated: DETERMINISTIC_2dda1150f13deb05
Batch ID: 20250612_151117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.layer3.com/v1/verify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import time

# Constants
LAYER3_API_URL = "https://api.layer3.com/v1/verify"
ACHIEVEMENTS = {
    "first_transaction": "First Transaction Completed!",
    "loyal_user": "Loyal User - 10 Transactions!",
    "high_value_user": "High Value User - $1,000 in Transactions!"
}

# User class to track user on-chain activities
class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.transaction_count = 0
        self.total_value = 0
        self.achievements = set()

    def add_transaction(self, value):
        """Add a transaction value to the user's total."""
        self.transaction_count += 1
        self.total_value += value
        self.check_achievements(value)

    def check_achievements(self, value):
        """Check and award achievements based on user activity."""
        if self.transaction_count == 1:
            self.award_achievement("first_transaction")
        if self.transaction_count >= 10:
            self.award_achievement("loyal_user")
        if self.total_value >= 1000:
            self.award_achievement("high_value_user")

    def award_achievement(self, achievement_key):
        """Award an achievement to the user."""
        if achievement_key not in self.achievements:
            self.achievements.add(achievement_key)
            print(f"User {self.user_id} awarded: {ACHIEVEMENTS[achievement_key]}")

def verify_user_activity(user_id):
    """Verify on-chain activity for the user via Layer3 API."""
    try:
        response = requests.get(f"{LAYER3_API_URL}/{user_id}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error verifying user {user_id}: {e}")
        return None

def process_user_activity(user_id):
    """Process user's on-chain activity and award achievements."""
    user = User(user_id)
    
    # Simulate fetching user's transaction data
    user_activity = verify_user_activity(user_id)
    if user_activity is None:
        return  # Exit if user activity could not be verified

    for transaction in user_activity.get('transactions', []):
        value = transaction.get('value', 0)
        user.add_transaction(value)
        time.sleep(0.1)  # Simulate time delay for processing

    print(f"User {user_id} has completed {user.transaction_count} transactions with total value ${user.total_value:.2f}")

# Example usage
if __name__ == "__main__":
    # Replace with actual user IDs to process their activities
    user_ids = ["user123", "user456", "user789"]
    
    for user_id in user_ids:
        process_user_activity(user_id)
```
