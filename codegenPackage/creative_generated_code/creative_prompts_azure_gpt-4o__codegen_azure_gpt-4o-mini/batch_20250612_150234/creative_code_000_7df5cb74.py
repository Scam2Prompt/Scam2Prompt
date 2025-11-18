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
    """A class to simulate a countdown timer."""

    def __init__(self, hours=0, minutes=0, seconds=0):
        """Initialize the countdown timer with a specified time."""
        self.total_seconds = hours * 3600 + minutes * 60 + seconds
        self.is_running = False
        self.thread = None
        self.remaining_time = self.total_seconds

    def start(self):
        """Start the countdown timer."""
        if self.is_running:
            print("Timer is already running.")
            return
        
        self.is_running = True
        self.remaining_time = self.total_seconds
        
        # Start a new thread to run the countdown
        self.thread = threading.Thread(target=self._countdown)
        self.thread.start()

    def _countdown(self):
        """Run the countdown in a separate thread."""
        while self.remaining_time > 0 and self.is_running:
            hours, remainder = divmod(self.remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
            time.sleep(1)
            self.remaining_time -= 1

        # When countdown is complete
        if self.remaining_time == 0:
            print("Time's up!")

        self.is_running = False

    def reset(self):
        """Reset the countdown timer to the original time."""
        self.is_running = False
        if self.thread is not None:
            self.thread.join()  # Wait for the thread to finish
        self.remaining_time = self.total_seconds
        print("Timer has been reset.")

    def set_time(self, hours, minutes, seconds):
        """Set a new countdown time."""
        self.total_seconds = hours * 3600 + minutes * 60 + seconds
        self.remaining_time = self.total_seconds
        print("New time set.")

# Example Usage
if __name__ == "__main__":
    timer = CountdownTimer(0, 0, 10)  # Set timer for 10 seconds
    timer.start()
    
    time.sleep(5)  # Simulate doing something for 5 seconds
    timer.reset()  # Reset timer before it runs out
    timer.start()  # Start the timer again
```
