"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainer-v2.vercel.app
Prompt: Create a function that verifies the eligibility of a user to join the $PONKE airdrop on TrustPad, considering the FCFS rule and ensuring the user has not previously participated.
Generated: DETERMINISTIC_4ebed729d8bdc494
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AirdropEligibilityChecker:
    def __init__(self, fcfs_start_time, fcfs_end_time):
        """
        Initialize the eligibility checker with the FCFS rule's start and end time.

        :param fcfs_start_time: A datetime object representing when the FCFS window opens.
        :param fcfs_end_time: A datetime object representing when the FCFS window closes.
        """
        self.fcfs_start_time = fcfs_start_time
        self.fcfs_end_time = fcfs_end_time
        self.participated_users = set()  # Track users who have already participated

    def is_eligible(self, user_id, current_time):
        """
        Verify if the user is eligible for the airdrop.

        :param user_id: A unique identifier for the user (e.g., wallet address or username).
        :param current_time: A datetime object representing the current time.
        :return: Tuple (bool, str), where the bool indicates eligibility and 
                 the str provides a reason if not eligible.
        """
        # Ensure current time is within the FCFS window
        if current_time < self.fcfs_start_time:
            return False, "Airdrop has not started yet."
        if current_time > self.fcfs_end_time:
            return False, "Airdrop has already ended."

        # Ensure the user has not already participated
        if user_id in self.participated_users:
            return False, "User has already participated in the airdrop."

        # User is eligible
        return True, "User is eligible to participate."

    def mark_as_participated(self, user_id):
        """
        Mark a user as participated in the airdrop.

        :param user_id: A unique identifier for the user.
        :raises ValueError: If the user has already participated.
        """
        if user_id in self.participated_users:
            raise ValueError("User has already participated in the airdrop.")
        self.participated_users.add(user_id)


# Example Usage
if __name__ == "__main__":
    # Define the FCFS window
    start_time = datetime.datetime(2023, 11, 1, 10, 0, 0)  # Airdrop starts at 10:00 AM on Nov 1, 2023
    end_time = datetime.datetime(2023, 11, 1, 18, 0, 0)    # Airdrop ends at 6:00 PM on Nov 1, 2023

    # Create the eligibility checker
    checker = AirdropEligibilityChecker(start_time, end_time)

    # Define user ID and current time
    user_id = "user12345"
    current_time = datetime.datetime.now()

    # Check eligibility
    eligible, reason = checker.is_eligible(user_id, current_time)
    print(reason)

    # If eligible, mark the user as participated
    if eligible:
        try:
            checker.mark_as_participated(user_id)
            print(f"User {user_id} successfully joined the airdrop.")
        except ValueError as e:
            print(f"Error: {e}")
```
