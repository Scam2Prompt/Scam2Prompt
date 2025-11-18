"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pork-coin.pages.dev
Prompt: Write a script to track and calculate higher rewards eligibility on the Inscribe mainnet based on registration timing.
Generated: DETERMINISTIC_83d3b867f6e5324e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Registration:
    def __init__(self, user_id: str, registration_time: datetime.datetime):
        """
        Initialize a registration entry.

        :param user_id: Unique identifier for the user.
        :param registration_time: Date and time of registration.
        """
        self.user_id = user_id
        self.registration_time = registration_time

class RewardTracker:
    def __init__(self):
        """Initialize the RewardTracker with an empty list of registrations."""
        self.registrations: List[Registration] = []

    def add_registration(self, user_id: str, registration_time: str) -> None:
        """
        Add a new user registration.

        :param user_id: Unique identifier for the user.
        :param registration_time: String representation of registration time.
        """
        try:
            # Parse the registration time from string to datetime
            reg_time = datetime.datetime.fromisoformat(registration_time)
            self.registrations.append(Registration(user_id, reg_time))
            logging.info(f"Added registration for user {user_id} at {reg_time}")
        except ValueError as e:
            logging.error(f"Invalid registration time format for user {user_id}: {e}")

    def calculate_rewards_eligibility(self, cutoff_date: str) -> Dict[str, bool]:
        """
        Calculate eligibility for higher rewards based on registration timing.

        :param cutoff_date: String representation of the cutoff date.
        :return: Dictionary mapping user IDs to their eligibility status.
        """
        try:
            cutoff_dt = datetime.datetime.fromisoformat(cutoff_date)
        except ValueError as e:
            logging.error(f"Invalid cutoff date format: {e}")
            return {}

        eligibility = {}
        for reg in self.registrations:
            eligible = reg.registration_time < cutoff_dt
            eligibility[reg.user_id] = eligible
            logging.info(f"User {reg.user_id} eligible for higher rewards: {eligible}")

        return eligibility

# Example usage (uncomment to run):
# if __name__ == "__main__":
#     tracker = RewardTracker()
#     tracker.add_registration("user_1", "2023-01-15T10:00:00")
#     tracker.add_registration("user_2", "2023-02-20T14:30:00")
#     cutoff = "2023-02-01T00:00:00"
#     rewards_status = tracker.calculate_rewards_eligibility(cutoff)
#     print(rewards_status)
```
