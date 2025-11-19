"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Generate a Python script that simulates a free trial feature for a gaming website, allowing users to play without registration, similar to the trial feature of Pixxie928.
Generated: DETERMINISTIC_25021969925f157a
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class FreeTrialManager:
    """
    Class to manage free trial sessions for users
    """

    def __init__(self, trial_duration_minutes=30):
        """
        Initialize the FreeTrialManager with a default trial duration.

        Args:
            trial_duration_minutes (int): Duration of the free trial in minutes.
        """
        self.trial_duration = timedelta(minutes=trial_duration_minutes)
        self.active_trials = {}  # Stores active trials in the format {user_id: expiration_time}

    def start_trial(self, user_id):
        """
        Start a free trial for a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Confirmation message indicating trial start.
        """
        if user_id in self.active_trials:
            return "Trial already active for this user."

        expiration_time = datetime.now() + self.trial_duration
        self.active_trials[user_id] = expiration_time
        return f"Free trial started for user {user_id}. Expires at {expiration_time}."

    def check_trial_status(self, user_id):
        """
        Check the status of a user's free trial.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Status message indicating trial validity or expiration.
        """
        if user_id not in self.active_trials:
            return "No active trial found for this user."

        expiration_time = self.active_trials[user_id]
        if datetime.now() > expiration_time:
            self.active_trials.pop(user_id)  # Remove expired trial
            return f"Free trial for user {user_id} has expired."
        else:
            remaining_time = expiration_time - datetime.now()
            return f"Free trial for user {user_id} is active. Time remaining: {remaining_time}."

    def end_trial(self, user_id):
        """
        End a user's free trial manually.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Confirmation message indicating trial end.
        """
        if user_id in self.active_trials:
            self.active_trials.pop(user_id)
            return f"Free trial for user {user_id} has been ended."
        return "No active trial found for this user."


def main():
    """
    Main function to demonstrate the FreeTrialManager functionality.
    """
    trial_manager = FreeTrialManager(trial_duration_minutes=30)

    print("Welcome to the gaming website free trial system!")

    while True:
        print("\nOptions:")
        print("1. Start a free trial")
        print("2. Check trial status")
        print("3. End trial")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            user_id = input("Enter user ID to start trial: ").strip()
            print(trial_manager.start_trial(user_id))
        elif choice == 2:
            user_id = input("Enter user ID to check trial status: ").strip()
            print(trial_manager.check_trial_status(user_id))
        elif choice == 3:
            user_id = input("Enter user ID to end trial: ").strip()
            print(trial_manager.end_trial(user_id))
        elif choice == 4:
            print("Exiting the free trial system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        time.sleep(1)  # Add a brief pause for better user experience


if __name__ == "__main__":
    main()
```
