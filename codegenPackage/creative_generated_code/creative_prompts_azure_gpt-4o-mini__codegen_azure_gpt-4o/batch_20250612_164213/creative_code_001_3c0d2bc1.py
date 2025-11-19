"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mwxoq1840.ukit.me
Prompt: Write a code snippet to handle expired trial periods in a uKit website.
Generated: DETERMINISTIC_3c0d2bc1104ad877
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TrialExpiryHandler:
    """
    A class to manage trial period expiration for a uKit website.
    """

    def __init__(self, trial_start_date, trial_duration_days):
        """
        Initialize the TrialExpiryHandler.

        :param trial_start_date: The start date of the trial (datetime.date).
        :param trial_duration_days: The duration of the trial in days (int).
        """
        self.trial_start_date = trial_start_date
        self.trial_duration_days = trial_duration_days
        self.expiry_date = self.trial_start_date + datetime.timedelta(days=self.trial_duration_days)

    def is_trial_expired(self):
        """
        Check if the trial period has expired.

        :return: True if the trial period has expired, False otherwise.
        """
        current_date = datetime.date.today()
        return current_date > self.expiry_date

    def handle_expired_trial(self):
        """
        Handle actions when the trial period has expired.
        """
        if self.is_trial_expired():
            # Notify user and restrict access
            self.notify_user()
            self.restrict_access()
        else:
            print("The trial period is still active. Enjoy!")

    def notify_user(self):
        """
        Notify the user that the trial period has expired.
        """
        print("Your trial period has expired. Please upgrade to a premium plan to continue.")

    def restrict_access(self):
        """
        Restrict access to premium features after the trial expires.
        """
        print("Access to premium features has been restricted. Upgrade to regain access.")


# Example usage
if __name__ == "__main__":
    # Replace '2023-09-01' with the actual trial start date
    trial_start_date = datetime.date(2023, 9, 1)
    trial_duration_days = 30  # Configure trial duration

    trial_handler = TrialExpiryHandler(trial_start_date, trial_duration_days)
    
    try:
        trial_handler.handle_expired_trial()
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while processing the trial: {e}")
```
