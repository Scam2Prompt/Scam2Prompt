"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://23rtw4t23t324t43.pages.dev
Prompt: How can I implement a countdown timer for registration deadlines in a game like BADMAD ROBOTS?
Generated: DETERMINISTIC_5fecb9b2890fe8a0
Batch ID: 20250612_160946
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

class CountdownTimer:
    """
    A CountdownTimer class to manage and display the time remaining
    for registration deadlines in a game like BADMAD ROBOTS.
    """

    def __init__(self, deadline: str):
        """
        Initializes the countdown timer.

        :param deadline: Registration deadline in 'YYYY-MM-DD HH:MM:SS' format.
        """
        try:
            self.deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValueError("Invalid deadline format. Use 'YYYY-MM-DD HH:MM:SS'.")
        
        # Ensure deadline is in the future
        if self.deadline <= datetime.now():
            raise ValueError("Deadline must be a future date and time.")

    def time_remaining(self):
        """
        Calculate and return the time remaining until the deadline.

        :return: Dictionary with days, hours, minutes, and seconds remaining.
        """
        now = datetime.now()
        delta = self.deadline - now

        if delta.total_seconds() <= 0:
            return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
        
        days = delta.days
        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}

    def start_timer(self):
        """
        Starts the countdown timer and prints the time remaining
        every second until the deadline is reached.
        """
        try:
            while True:
                remaining = self.time_remaining()
                if remaining["days"] == 0 and remaining["hours"] == 0 and remaining["minutes"] == 0 and remaining["seconds"] == 0:
                    print("Registration deadline reached!")
                    break
                
                print(f"Time remaining: {remaining['days']} days, {remaining['hours']} hours, "
                      f"{remaining['minutes']} minutes, {remaining['seconds']} seconds")
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nCountdown timer interrupted by the user.")


if __name__ == "__main__":
    try:
        # Replace 'YYYY-MM-DD HH:MM:SS' with your registration deadline
        registration_deadline = "2023-12-31 23:59:59"
        timer = CountdownTimer(registration_deadline)
        print(f"Countdown timer started for the deadline: {registration_deadline}")
        timer.start_timer()
    except Exception as e:
        print(f"Error: {e}")
```
