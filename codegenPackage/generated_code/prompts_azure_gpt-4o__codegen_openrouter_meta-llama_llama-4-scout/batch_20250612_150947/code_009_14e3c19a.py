"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write code to simulate the operation of a digital timer in an industrial electrical setup, similar to the products featured on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_14e3c19a6c956ce2
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from threading import Thread

class DigitalTimer:
    """
    Simulates a digital timer in an industrial electrical setup.

    Attributes:
        hours (int): The hours component of the timer.
        minutes (int): The minutes component of the timer.
        seconds (int): The seconds component of the timer.
        running (bool): Whether the timer is currently running.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initializes a new DigitalTimer instance.

        Args:
            hours (int, optional): The hours component of the timer. Defaults to 0.
            minutes (int, optional): The minutes component of the timer. Defaults to 0.
            seconds (int, optional): The seconds component of the timer. Defaults to 0.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.running = False

    def start(self):
        """
        Starts the timer.
        """
        if not self.running:
            self.running = True
            Thread(target=self.decrement_time).start()

    def stop(self):
        """
        Stops the timer.
        """
        self.running = False

    def reset(self, hours=0, minutes=0, seconds=0):
        """
        Resets the timer to the specified time.

        Args:
            hours (int, optional): The new hours component of the timer. Defaults to 0.
            minutes (int, optional): The new minutes component of the timer. Defaults to 0.
            seconds (int, optional): The new seconds component of the timer. Defaults to 0.
        """
        self.stop()
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def decrement_time(self):
        """
        Decrements the timer by one second.
        """
        while self.running:
            if self.seconds > 0:
                self.seconds -= 1
            elif self.minutes > 0:
                self.minutes -= 1
                self.seconds = 59
            elif self.hours > 0:
                self.hours -= 1
                self.minutes = 59
                self.seconds = 59
            else:
                self.running = False
                print("Timer has expired.")
            print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}", end='\r')
            time.sleep(1)

def main():
    try:
        timer = DigitalTimer(0, 1, 0)  # Create a 1-minute timer
        print("Timer started. Press Ctrl+C to exit.")
        timer.start()
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTimer stopped.")

if __name__ == "__main__":
    main()
```
