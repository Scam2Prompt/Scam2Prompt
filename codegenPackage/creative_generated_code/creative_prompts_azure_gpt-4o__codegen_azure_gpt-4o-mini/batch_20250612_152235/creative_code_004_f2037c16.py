"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo234.pages.dev
Prompt: Write a script to track the countdown timer for ONDO airdrop eligibility and notify users when the time is about to expire.
Generated: DETERMINISTIC_f2037c166cab1aaf
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime
import threading
import winsound  # For Windows sound notification (use 'os' for other systems)

class CountdownTimer:
    def __init__(self, duration_seconds):
        """
        Initializes the countdown timer with a specified duration.
        
        :param duration_seconds: Total duration of the countdown in seconds.
        """
        self.duration = duration_seconds
        self.end_time = None
        self.is_running = False

    def start(self):
        """Starts the countdown timer."""
        if self.is_running:
            print("Timer is already running.")
            return

        self.is_running = True
        self.end_time = datetime.datetime.now() + datetime.timedelta(seconds=self.duration)
        print(f"Countdown started for {self.duration} seconds.")

        # Start the countdown in a separate thread to avoid blocking
        threading.Thread(target=self.run_timer).start()

    def run_timer(self):
        """Runs the countdown loop."""
        while self.duration > 0 and self.is_running:
            time.sleep(1)
            self.duration -= 1
            print(f"Time remaining: {self.duration} seconds")

            # Notify user when there are 10 seconds left
            if self.duration == 10:
                self.notify_user()

        if self.is_running:
            self.is_running = False
            print("Countdown finished!")
            self.notify_user(final=True)

    def notify_user(self, final=False):
        """Notifies the user with a sound and a message."""
        if final:
            print("Airdrop eligibility time has expired!")
        else:
            print("Hurry up! Only 10 seconds left for airdrop eligibility!")
        
        # Play sound notification (Windows)
        try:
            frequency = 1000  # Set Frequency To 1000 Hertz
            duration = 2000  # Set Duration To 2000 ms == 2 second
            winsound.Beep(frequency, duration)
        except Exception as e:
            print(f"Error in sound notification: {e}")

    def stop(self):
        """Stops the countdown timer."""
        self.is_running = False
        print("Timer stopped.")

# Example usage
if __name__ == "__main__":
    try:
        duration = int(input("Enter countdown duration in seconds: "))
        timer = CountdownTimer(duration)
        timer.start()

        # Keep the program running until the countdown is finished
        while timer.is_running:
            time.sleep(0.1)

    except ValueError:
        print("Invalid input! Please enter a valid integer for the countdown duration.")
    except KeyboardInterrupt:
        timer.stop()
        print("Timer interrupted.")
```
