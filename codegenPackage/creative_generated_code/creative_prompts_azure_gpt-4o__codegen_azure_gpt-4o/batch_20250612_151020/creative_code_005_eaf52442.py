"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mommyanew.com
Prompt: Write code to implement a notification system that alerts parents when their child exceeds a preset screen time limit, based on the recommendations in Mommy Anew's parenting tips.
Generated: DETERMINISTIC_eaf524420dbb9afa
Batch ID: 20250612_151020
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


class ScreenTimeMonitor:
    """
    A class to monitor screen time and notify parents if the child exceeds the limit.
    Based on Mommy Anew's parenting recommendations.
    """
    
    def __init__(self, time_limit_minutes, notify_function):
        """
        Initialize the ScreenTimeMonitor.

        :param time_limit_minutes: Allowed screen time limit in minutes.
        :param notify_function: Function to call for sending notifications.
        """
        self.time_limit = timedelta(minutes=time_limit_minutes)
        self.notify_function = notify_function
        self.start_time = None
        self.end_time = None
        self.screen_time_exceeded = False

    def start_screen_time(self):
        """
        Start tracking screen time.
        """
        self.start_time = datetime.now()
        self.end_time = None
        self.screen_time_exceeded = False
        print("Screen time monitoring started.")

    def end_screen_time(self):
        """
        Stop tracking screen time and check if the limit was exceeded.
        """
        if not self.start_time:
            print("Error: Screen time not started.")
            return
        
        self.end_time = datetime.now()
        total_screen_time = self.end_time - self.start_time

        if total_screen_time > self.time_limit:
            self.screen_time_exceeded = True
            self.notify_parents(total_screen_time)
        else:
            print(f"Screen time within limit. Total: {total_screen_time}.")

        # Reset the start_time for future tracking
        self.start_time = None

    def notify_parents(self, total_screen_time):
        """
        Notify parents if screen time exceeds the limit.

        :param total_screen_time: The total screen time that was recorded.
        """
        if not self.notify_function:
            print("Error: No notification function provided.")
            return
        
        message = (
            f"Alert: Your child's screen time exceeded the limit of {self.time_limit}. "
            f"Total screen time: {total_screen_time}."
        )
        self.notify_function(message)
        print(f"Notification sent: {message}")


def send_notification(message):
    """
    Example notification function. Replace with actual implementation.

    :param message: The message to be sent as a notification.
    """
    # Simulate sending the notification (e.g., via email, SMS, etc.)
    print(f"Sending notification: {message}")


# Example usage:
if __name__ == "__main__":
    # Set screen time limit to 60 minutes
    screen_time_monitor = ScreenTimeMonitor(time_limit_minutes=60, notify_function=send_notification)

    try:
        # Start screen time tracking
        screen_time_monitor.start_screen_time()

        # Simulate screen time usage (e.g., child is using device for 65 minutes)
        time.sleep(5)  # Replace with actual monitoring mechanism
        
        # End screen time tracking
        screen_time_monitor.end_screen_time()

    except Exception as e:
        print(f"An error occurred: {e}")
```
