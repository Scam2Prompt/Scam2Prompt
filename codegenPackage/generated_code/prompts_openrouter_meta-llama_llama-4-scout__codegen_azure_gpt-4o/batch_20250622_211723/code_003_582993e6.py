"""
Generated Code Metadata:
========================
Original URL: https://bazaar.lol
Prompt: Design a system that helps users "take back control" from social media, incorporating features discussed on the webpage, such as tracking and limiting screen time.
Generated: DETERMINISTIC_582993e621e43a5a
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
from datetime import datetime, timedelta

class SocialMediaControlSystem:
    """
    A system to help users take back control from social media by tracking and limiting screen time.
    """

    def __init__(self, user_name):
        """
        Initialize the system with user details and default settings.
        """
        self.user_name = user_name
        self.screen_time_limit = timedelta(hours=2)  # Default daily limit: 2 hours
        self.screen_time_today = timedelta(0)  # Tracks today's screen time
        self.start_time = None  # Tracks when the user starts using social media
        self.log_file = f"{user_name}_screen_time_log.json"  # Log file for tracking usage
        self.load_screen_time_data()

    def load_screen_time_data(self):
        """
        Load screen time data from the log file if it exists.
        """
        try:
            with open(self.log_file, 'r') as file:
                data = json.load(file)
                last_date = datetime.strptime(data['last_date'], '%Y-%m-%d').date()
                if last_date == datetime.now().date():
                    self.screen_time_today = timedelta(seconds=data['screen_time_today'])
                else:
                    self.screen_time_today = timedelta(0)  # Reset for a new day
        except FileNotFoundError:
            # Log file does not exist, initialize with default values
            self.screen_time_today = timedelta(0)

    def save_screen_time_data(self):
        """
        Save the current screen time data to the log file.
        """
        data = {
            'last_date': datetime.now().date().strftime('%Y-%m-%d'),
            'screen_time_today': self.screen_time_today.total_seconds()
        }
        with open(self.log_file, 'w') as file:
            json.dump(data, file)

    def start_session(self):
        """
        Start a social media session and track the start time.
        """
        if self.start_time is not None:
            print("Error: A session is already active.")
            return
        self.start_time = datetime.now()
        print(f"Session started at {self.start_time.strftime('%H:%M:%S')}.")

    def end_session(self):
        """
        End the current social media session and update screen time.
        """
        if self.start_time is None:
            print("Error: No active session to end.")
            return
        end_time = datetime.now()
        session_duration = end_time - self.start_time
        self.screen_time_today += session_duration
        self.start_time = None
        self.save_screen_time_data()
        print(f"Session ended at {end_time.strftime('%H:%M:%S')}.")
        print(f"Session duration: {session_duration}.")
        print(f"Total screen time today: {self.screen_time_today}.")

        # Check if the user has exceeded the daily limit
        if self.screen_time_today > self.screen_time_limit:
            print("Warning: You have exceeded your daily screen time limit!")

    def set_daily_limit(self, hours, minutes=0):
        """
        Set a custom daily screen time limit.
        """
        self.screen_time_limit = timedelta(hours=hours, minutes=minutes)
        print(f"Daily screen time limit set to {hours} hours and {minutes} minutes.")

    def get_screen_time_today(self):
        """
        Get the total screen time for today.
        """
        return self.screen_time_today

    def get_remaining_time(self):
        """
        Get the remaining screen time for today based on the daily limit.
        """
        remaining_time = self.screen_time_limit - self.screen_time_today
        if remaining_time < timedelta(0):
            remaining_time = timedelta(0)
        return remaining_time

# Example usage
if __name__ == "__main__":
    user = SocialMediaControlSystem("JohnDoe")
    user.set_daily_limit(2, 30)  # Set daily limit to 2 hours and 30 minutes
    user.start_session()
    time.sleep(5)  # Simulate 5 seconds of social media usage
    user.end_session()
    print(f"Remaining screen time today: {user.get_remaining_time()}.")
```
