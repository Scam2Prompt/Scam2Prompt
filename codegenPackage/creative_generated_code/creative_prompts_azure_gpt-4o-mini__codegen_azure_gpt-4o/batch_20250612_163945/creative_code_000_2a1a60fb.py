"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofiberconnection.blogspot.com
Prompt: How can I implement a free trial feature for a Jio Fiber connection in my application?
Generated: DETERMINISTIC_2a1a60fbb3aeeee9
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FreeTrialManager:
    """
    A class to manage free trial features for Jio Fiber connections.
    """

    def __init__(self, trial_duration_days=30):
        """
        Initialize the FreeTrialManager with a default trial duration.

        :param trial_duration_days: Number of days for the free trial (default is 30 days).
        """
        self.trial_duration_days = trial_duration_days
        self.users = {}  # Dictionary to store user information

    def start_free_trial(self, user_id):
        """
        Start a free trial for a new user.

        :param user_id: Unique identifier for the user.
        :return: None
        """
        if user_id in self.users:
            raise ValueError("User is already registered for the free trial.")
        
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=self.trial_duration_days)
        
        # Store trial details in the users dictionary
        self.users[user_id] = {
            "start_date": start_date,
            "end_date": end_date,
            "is_trial_active": True
        }
        print(f"Free trial started for user {user_id} (ends on {end_date}).")

    def check_trial_status(self, user_id):
        """
        Check the status of a user's free trial.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing trial status information.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        user_data = self.users[user_id]
        current_date = datetime.date.today()
        
        if current_date > user_data["end_date"]:
            user_data["is_trial_active"] = False
        
        return user_data

    def end_free_trial(self, user_id):
        """
        Manually end a user's free trial before the scheduled end date.

        :param user_id: Unique identifier for the user.
        :return: None
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        self.users[user_id]["is_trial_active"] = False
        print(f"Free trial ended for user {user_id}.")

# Example usage of the FreeTrialManager class
if __name__ == "__main__":
    try:
        # Initialize the free trial manager
        free_trial_manager = FreeTrialManager(trial_duration_days=30)
        
        # Start a free trial for a user
        free_trial_manager.start_free_trial("user123")
        
        # Check the user's trial status
        status = free_trial_manager.check_trial_status("user123")
        print(f"Trial Status: {status}")
        
        # End the user's free trial manually
        free_trial_manager.end_free_trial("user123")
        
        # Check the trial status again
        status = free_trial_manager.check_trial_status("user123")
        print(f"Trial Status After End: {status}")

    except Exception as e:
        print(f"Error: {e}")
```
