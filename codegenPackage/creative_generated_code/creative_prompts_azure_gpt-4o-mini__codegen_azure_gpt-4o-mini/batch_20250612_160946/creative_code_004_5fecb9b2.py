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
import threading
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, end_time):
        """
        Initialize the countdown timer with the given end time.
        
        :param end_time: datetime object representing the deadline for registration
        """
        self.end_time = end_time
        self.running = False
        self.timer_thread = None

    def start(self):
        """
        Start the countdown timer.
        """
        if self.running:
            print("Timer is already running.")
            return

        self.running = True
        self.timer_thread = threading.Thread(target=self._countdown)
        self.timer_thread.start()

    def stop(self):
        """
        Stop the countdown timer.
        """
        self.running = False
        if self.timer_thread is not None:
            self.timer_thread.join()
            self.timer_thread = None

    def _countdown(self):
        """
        Run the countdown in a separate thread.
        This method calculates the time left until the deadline and prints it.
        """
        while self.running:
            now = datetime.now()
            time_left = self.end_time - now

            # If the deadline has passed, stop the timer and notify
            if time_left <= timedelta(0):
                print("Registration deadline has passed!")
                self.running = False
                break

            # Format the remaining time
            days, seconds = time_left.days, time_left.seconds
            hours = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            # Print the countdown
            print(f"Time left for registration: {days}d {hours}h {minutes}m {seconds}s", end='\r')

            # Sleep for 1 second before updating the countdown
            time.sleep(1)

        print("\nCountdown timer stopped.")

# Example usage
if __name__ == "__main__":
    # Define the registration deadline (e.g., 10 minutes from now)
    registration_deadline = datetime.now() + timedelta(minutes=10)

    # Create a countdown timer
    countdown_timer = CountdownTimer(end_time=registration_deadline)

    # Start the countdown timer
    try:
        countdown_timer.start()
        # Keep the main thread alive while the timer runs
        while countdown_timer.running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping the timer...")
        countdown_timer.stop()
```
