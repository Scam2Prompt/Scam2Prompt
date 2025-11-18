"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Suggest Python libraries for simulating the functionality of differential switches and timers, such as those listed on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_854a2bd74d3d091f
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import threading

class DifferentialSwitch:
    """
    A class to simulate the behavior of a differential switch.
    It activates a load when the input voltage is within a certain range.
    """

    def __init__(self, lower_limit, upper_limit):
        """
        Initialize the differential switch with specified limits.
        
        :param lower_limit: The lower voltage limit for activation.
        :param upper_limit: The upper voltage limit for activation.
        """
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.load_active = False

    def check_voltage(self, voltage):
        """
        Check if the provided voltage is within the activation range.
        
        :param voltage: The input voltage to check.
        :return: True if within limits, otherwise False.
        """
        if self.lower_limit <= voltage <= self.upper_limit:
            self.activate_load()
            return True
        else:
            self.deactivate_load()
            return False

    def activate_load(self):
        """Activate the load and set load_active to True."""
        if not self.load_active:
            self.load_active = True
            print("Load activated.")

    def deactivate_load(self):
        """Deactivate the load and set load_active to False."""
        if self.load_active:
            self.load_active = False
            print("Load deactivated.")


class Timer:
    """
    A class to simulate a timer functionality.
    It allows setting a timer for a specific duration.
    """

    def __init__(self, duration):
        """
        Initialize the timer with a specified duration.
        
        :param duration: The duration for the timer in seconds.
        """
        self.duration = duration
        self.timer_thread = None

    def start_timer(self):
        """Start the timer and execute the countdown in a separate thread."""
        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self._countdown)
            self.timer_thread.start()
        else:
            print("Timer is already running.")

    def _countdown(self):
        """Internal method to handle countdown logic."""
        print(f"Timer started for {self.duration} seconds.")
        for remaining in range(self.duration, 0, -1):
            print(f"Time left: {remaining} seconds")
            time.sleep(1)
        print("Timer finished.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a differential switch with specific voltage limits
        diff_switch = DifferentialSwitch(lower_limit=5.0, upper_limit=15.0)
        
        # Simulate checking different voltage levels
        voltages_to_check = [3.0, 6.0, 12.0, 16.0]
        for voltage in voltages_to_check:
            print(f"Checking voltage: {voltage}V")
            diff_switch.check_voltage(voltage)
            time.sleep(1)  # Simulate delay between checks

        # Create and start a timer for 5 seconds
        timer = Timer(duration=5)
        timer.start_timer()

    except Exception as e:
        print(f"An error occurred: {e}")
```
