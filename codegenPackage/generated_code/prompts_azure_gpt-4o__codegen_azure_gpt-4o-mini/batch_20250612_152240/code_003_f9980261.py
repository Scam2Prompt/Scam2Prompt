"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: Create a function to monitor tire pressure and detect abnormal losses, incorporating the advice on periodic adjustments and consequences of incorrect pressure from Neumayaa's post-sale service guidelines.
Generated: DETERMINISTIC_f9980261dfb9caf2
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class TirePressureMonitor:
    """
    A class to monitor tire pressure and detect abnormal losses.
    """

    def __init__(self, normal_pressure: float, threshold: float):
        """
        Initializes the TirePressureMonitor with normal pressure and threshold for abnormal loss.

        :param normal_pressure: The normal tire pressure in PSI.
        :param threshold: The threshold for detecting abnormal pressure loss in PSI.
        """
        self.normal_pressure = normal_pressure
        self.threshold = threshold
        self.current_pressure = normal_pressure

    def simulate_pressure_loss(self):
        """
        Simulates random tire pressure loss for testing purposes.
        """
        # Simulate a random pressure loss between 0 to 5 PSI
        loss = random.uniform(0, 5)
        self.current_pressure -= loss
        return loss

    def check_pressure(self):
        """
        Checks the current tire pressure and detects abnormal losses.

        :raises ValueError: If the current pressure is below zero.
        :return: A message indicating the status of the tire pressure.
        """
        if self.current_pressure < 0:
            raise ValueError("Tire pressure cannot be negative.")

        # Calculate the pressure loss
        pressure_loss = self.normal_pressure - self.current_pressure

        if pressure_loss > self.threshold:
            return (f"Warning: Abnormal tire pressure loss detected! "
                    f"Current pressure: {self.current_pressure:.2f} PSI, "
                    f"Loss: {pressure_loss:.2f} PSI. "
                    "Please check the tires and adjust pressure accordingly.")
        else:
            return (f"Tire pressure is normal. Current pressure: {self.current_pressure:.2f} PSI.")

    def adjust_pressure(self, new_pressure: float):
        """
        Adjusts the tire pressure to a new value.

        :param new_pressure: The new tire pressure in PSI.
        :raises ValueError: If the new pressure is negative.
        """
        if new_pressure < 0:
            raise ValueError("New tire pressure cannot be negative.")
        self.current_pressure = new_pressure
        print(f"Tire pressure adjusted to {self.current_pressure:.2f} PSI.")

    def monitor(self, duration: int, interval: int):
        """
        Monitors tire pressure over a specified duration.

        :param duration: Total time to monitor in seconds.
        :param interval: Time interval between checks in seconds.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            loss = self.simulate_pressure_loss()
            print(f"Simulated pressure loss: {loss:.2f} PSI.")
            status = self.check_pressure()
            print(status)
            time.sleep(interval)

# Example usage
if __name__ == "__main__":
    try:
        monitor = TirePressureMonitor(normal_pressure=32.0, threshold=3.0)
        monitor.monitor(duration=30, interval=5)  # Monitor for 30 seconds, checking every 5 seconds
    except ValueError as e:
        print(f"Error: {e}")
```
