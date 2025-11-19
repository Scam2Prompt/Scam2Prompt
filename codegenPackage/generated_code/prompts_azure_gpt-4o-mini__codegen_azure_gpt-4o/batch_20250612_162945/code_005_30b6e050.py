"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Create a sample code snippet that demonstrates how to gamify healthcare data sharing in a way similar to BitDoctor's DeSci initiative.
Generated: DETERMINISTIC_30b6e050950d71a5
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime

# Constants
POINTS_PER_SHARE = 10  # Points awarded for sharing data
BADGE_THRESHOLDS = [50, 100, 200]  # Points required for badges
BADGES = ["Bronze", "Silver", "Gold"]  # Badge names

# User class to manage user data and gamification
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.points = 0
        self.badges = []
        self.shared_data = []

    def share_data(self, data):
        """
        Simulates sharing healthcare data and awards points.
        :param data: Dictionary containing healthcare data.
        """
        try:
            # Validate data format
            if not isinstance(data, dict):
                raise ValueError("Data must be a dictionary.")

            # Simulate data sharing (e.g., sending to a server)
            self.shared_data.append({
                "data": data,
                "timestamp": datetime.now().isoformat()
            })

            # Award points
            self.points += POINTS_PER_SHARE
            self._check_badges()

            print(f"Data shared successfully! You earned {POINTS_PER_SHARE} points.")
        except Exception as e:
            print(f"Error sharing data: {e}")

    def _check_badges(self):
        """
        Checks if the user qualifies for a new badge based on points.
        """
        for threshold, badge in zip(BADGE_THRESHOLDS, BADGES):
            if self.points >= threshold and badge not in self.badges:
                self.badges.append(badge)
                print(f"Congratulations! You earned the '{badge}' badge.")

    def get_status(self):
        """
        Returns the user's current status including points and badges.
        """
        return {
            "user_id": self.user_id,
            "name": self.name,
            "points": self.points,
            "badges": self.badges,
            "shared_data_count": len(self.shared_data)
        }

# Example usage
if __name__ == "__main__":
    # Create a user
    user = User(user_id=random.randint(1000, 9999), name="Alice")

    # Simulate sharing healthcare data
    sample_data = {
        "heart_rate": 72,
        "steps": 10000,
        "sleep_hours": 8
    }
    user.share_data(sample_data)

    # Share more data
    user.share_data({"blood_pressure": "120/80", "calories_burned": 500})

    # Get user status
    status = user.get_status()
    print(json.dumps(status, indent=4))
```
