"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate a script to track and display jackpot pools that grow in value and drop multiple times daily, similar to the Epic Drop Jackpots feature on Jackpot Cow Casino.
Generated: DETERMINISTIC_986d558f19d29c72
Batch ID: 20250612_154542
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
import random

class Jackpot:
    """Class representing a single jackpot pool."""

    def __init__(self, name, initial_value, growth_rate, drop_times):
        """
        Initialize the jackpot pool.

        Args:
            name (str): Name of the jackpot pool.
            initial_value (float): Starting value of the jackpot pool.
            growth_rate (float): Rate of growth per second.
            drop_times (list): List of daily drop times (HH:MM format).
        """
        self.name = name
        self.current_value = initial_value
        self.growth_rate = growth_rate
        self.drop_times = [self._convert_to_datetime(time_str) for time_str in drop_times]
        self.last_update_time = datetime.now()

    @staticmethod
    def _convert_to_datetime(time_str):
        """Convert a time string (HH:MM) into a datetime object for today."""
        now = datetime.now()
        hour, minute = map(int, time_str.split(":"))
        return datetime(now.year, now.month, now.day, hour, minute)

    def update_value(self):
        """Update the current jackpot pool value based on elapsed time."""
        now = datetime.now()
        elapsed_seconds = (now - self.last_update_time).total_seconds()
        self.current_value += elapsed_seconds * self.growth_rate
        self.last_update_time = now

    def reset_value(self):
        """Reset the jackpot pool value after a drop."""
        self.current_value = 0

    def check_and_process_drop(self):
        """
        Check if the current time matches any scheduled drop time.
        If yes, reset the jackpot pool value.
        """
        now = datetime.now()
        for drop_time in self.drop_times:
            if drop_time <= now <= drop_time + timedelta(seconds=59):  # Allow a 59-second window for drop
                self.reset_value()
                print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]: Jackpot '{self.name}' dropped!")
                # Update drop time to next day
                self.drop_times = [dt + timedelta(days=1) for dt in self.drop_times]
                break

    def display(self):
        """Display the current status of the jackpot pool."""
        print(
            f"Jackpot '{self.name}': Current Value = ${self.current_value:.2f} | Next Drops = "
            f"{', '.join([dt.strftime('%H:%M') for dt in self.drop_times])}"
        )


class JackpotManager:
    """Class for managing multiple jackpot pools."""

    def __init__(self):
        """Initialize the jackpot manager with an empty list of jackpots."""
        self.jackpots = []

    def add_jackpot(self, name, initial_value, growth_rate, drop_times):
        """
        Add a new jackpot pool to the manager.

        Args:
            name (str): Name of the jackpot pool.
            initial_value (float): Starting value of the jackpot pool.
            growth_rate (float): Rate of growth per second.
            drop_times (list): List of daily drop times (HH:MM format).
        """
        jackpot = Jackpot(name, initial_value, growth_rate, drop_times)
        self.jackpots.append(jackpot)

    def update_jackpots(self):
        """Update the values of all jackpots and check for drops."""
        for jackpot in self.jackpots:
            jackpot.update_value()
            jackpot.check_and_process_drop()

    def display_jackpots(self):
        """Display the status of all jackpots."""
        for jackpot in self.jackpots:
            jackpot.display()

    def run(self, update_interval=1):
        """
        Continuously update and display jackpots.

        Args:
            update_interval (int): Interval in seconds between updates.
        """
        try:
            while True:
                self.update_jackpots()
                self.display_jackpots()
                time.sleep(update_interval)
        except KeyboardInterrupt:
            print("Jackpot Manager stopped.")


if __name__ == "__main__":
    # Initialize the manager and add some jackpots
    manager = JackpotManager()
    manager.add_jackpot(name="Epic Drop", initial_value=1000.0, growth_rate=0.5, drop_times=["12:00", "18:00", "22:00"])
    manager.add_jackpot(name="Mega Drop", initial_value=5000.0, growth_rate=1.0, drop_times=["14:00", "20:00"])

    # Run the manager (updates every second)
    manager.run(update_interval=1)
```
