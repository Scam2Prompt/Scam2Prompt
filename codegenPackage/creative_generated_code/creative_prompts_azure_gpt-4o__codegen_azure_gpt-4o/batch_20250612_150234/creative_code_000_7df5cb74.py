"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: Write code to simulate a countdown timer similar to "Sophon Time" with a format of HH:MM:SS and a reset feature.
Generated: DETERMINISTIC_7df5cb742c00005c
Batch ID: 20250612_150234
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

class CountdownTimer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initializes the countdown timer with the given hours, minutes, and seconds.

        Args:
        - hours (int): Number of hours to start the countdown.
        - minutes (int): Number of minutes to start the countdown.
        - seconds (int): Number of seconds to start the countdown.
        """
        self.initial_hours = hours
        self.initial_minutes = minutes
        self.initial_seconds = seconds
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.running = False
        self.timer_thread = None

    def start(self):
        """
        Starts the countdown timer.
        """
        if self.running:
            print("Timer is already running.")
            return
        
        self.running = True
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def reset(self):
        """
        Resets the countdown timer to its initial values.
        """
        self.stop()
        self.hours = self.initial_hours
        self.minutes = self.initial_minutes
        self.seconds = self.initial_seconds
        print(f"Timer reset to {self.format_time()}")

    def stop(self):
        """
        Stops the countdown timer.
        """
        self.running = False
        if self.timer_thread:
            self.timer_thread.join()
        self.timer_thread = None

    def format_time(self):
        """
        Formats the current timer values as HH:MM:SS.

        Returns:
        - str: Time formatted as HH:MM:SS.
        """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def _run_timer(self):
        """
        Runs the countdown timer in a separate thread.
        """
        while self.running and (self.hours > 0 or self.minutes > 0 or self.seconds > 0):
            print(self.format_time())  # Display the current time
            time.sleep(1)             # Wait for 1 second
            self._decrement_time()    # Decrement the timer values
        
        if self.running:
            print("Time's up!")
        self.running = False

    def _decrement_time(self):
        """
        Decreases the timer values by one second.
        """
        if self.seconds > 0:
            self.seconds -= 1
        elif self.minutes > 0:
            self.minutes -= 1
            self.seconds = 59
        elif self.hours > 0:
            self.hours -= 1
            self.minutes = 59
            self.seconds = 59

# Example usage:
if __name__ == "__main__":
    timer = CountdownTimer(hours=0, minutes=0, seconds=10)  # 10-second timer
    timer.start()  # Start the timer

    # Simulate user interaction: Reset timer after 5 seconds
    time.sleep(5)
    timer.reset()
    timer.start()  # Restart the timer
```
