"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hypr.pages.dev
Prompt: Develop a script to track referral code usage and user connections on a platform like Hyperliquid.
Generated: DETERMINISTIC_a516286d52d04c54
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from collections import defaultdict

class ReferralTracker:
    """
    Class to track referral code usage and user connections on a platform.
    """

    def __init__(self):
        # Dictionary to store user connections: {referral_code: [list_of_users]}
        self.referral_connections = defaultdict(list)
        # Dictionary to store which referral code belongs to which user: {user_id: referral_code}
        self.user_referral_code_map = {}
        # Dictionary to store usage count for each referral code: {referral_code: usage_count}
        self.referral_code_usage = defaultdict(int)

    def generate_referral_code(self, user_id):
        """
        Generate a unique referral code for a user.
        """
        if user_id in self.user_referral_code_map:
            raise ValueError(f"User '{user_id}' already has a referral code.")
        
        # Generate a unique referral code (UUID-based)
        referral_code = str(uuid.uuid4())
        self.user_referral_code_map[user_id] = referral_code
        self.referral_connections[referral_code] = []  # Initialize empty connections list
        self.referral_code_usage[referral_code] = 0   # Initialize usage count

        return referral_code

    def use_referral_code(self, referral_code, new_user_id):
        """
        Register a new user using a referral code.
        """
        if referral_code not in self.referral_connections:
            raise ValueError(f"Referral code '{referral_code}' is invalid.")

        if new_user_id in self.user_referral_code_map:
            raise ValueError(f"User '{new_user_id}' already exists in the system.")

        # Add the new user to the connections list
        self.referral_connections[referral_code].append(new_user_id)
        # Map the new user to the referral code
        self.user_referral_code_map[new_user_id] = referral_code
        # Increment the usage count for the referral code
        self.referral_code_usage[referral_code] += 1

    def get_user_connections(self, user_id):
        """
        Get all users connected via the referral code of the given user.
        """
        if user_id not in self.user_referral_code_map:
            raise ValueError(f"User '{user_id}' does not have a referral code.")

        referral_code = self.user_referral_code_map[user_id]
        return self.referral_connections[referral_code]

    def get_referral_code_usage(self, referral_code):
        """
        Get the usage count for a specific referral code.
        """
        if referral_code not in self.referral_code_usage:
            raise ValueError(f"Referral code '{referral_code}' is invalid.")

        return self.referral_code_usage[referral_code]

    def get_all_referral_data(self):
        """
        Get all referral data including connections and usage counts.
        """
        return {
            "referral_connections": dict(self.referral_connections),
            "referral_code_usage": dict(self.referral_code_usage)
        }


# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()

    try:
        user1_id = "user1"
        user2_id = "user2"
        user3_id = "user3"

        # Generate referral code for user1
        user1_referral_code = tracker.generate_referral_code(user1_id)
        print(f"User1 Referral Code: {user1_referral_code}")

        # User2 uses User1's referral code
        tracker.use_referral_code(user1_referral_code, user2_id)
        print(f"User2 connected to User1's referral code.")

        # User3 uses User1's referral code
        tracker.use_referral_code(user1_referral_code, user3_id)
        print(f"User3 connected to User1's referral code.")

        # Fetch connections for User1
        user1_connections = tracker.get_user_connections(user1_id)
        print(f"User1 Connections: {user1_connections}")

        # Fetch referral code usage for User1's code
        usage_count = tracker.get_referral_code_usage(user1_referral_code)
        print(f"User1 Referral Code Usage: {usage_count}")

        # Get all referral data
        all_referral_data = tracker.get_all_referral_data()
        print("All Referral Data:", all_referral_data)

    except Exception as e:
        print(f"Error: {e}")
```
