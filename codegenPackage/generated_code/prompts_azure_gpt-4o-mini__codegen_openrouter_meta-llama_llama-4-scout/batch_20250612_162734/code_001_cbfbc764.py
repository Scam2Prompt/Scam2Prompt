"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Write a Python function that simulates the operation of a "turbina ferramental" in a manufacturing process, incorporating safety checks.
Generated: DETERMINISTIC_cbfbc76418e08618
Batch ID: 20250612_162734
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

class TurbinaFerramental:
    """
    Simulates the operation of a turbina ferramental in a manufacturing process.
    """

    def __init__(self, max_speed=100, min_speed=0, optimal_speed=50):
        """
        Initializes the TurbinaFerramental with speed limits.

        Args:
            max_speed (int): Maximum allowed speed. Defaults to 100.
            min_speed (int): Minimum allowed speed. Defaults to 0.
            optimal_speed (int): Optimal operating speed. Defaults to 50.
        """
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.optimal_speed = optimal_speed
        self.current_speed = 0
        self.is_running = False

    def start(self):
        """
        Starts the turbina ferramental.
        """
        if not self.is_running:
            self.is_running = True
            print("Turbina ferramental started.")
        else:
            print("Turbina ferramental is already running.")

    def stop(self):
        """
        Stops the turbina ferramental.
        """
        if self.is_running:
            self.is_running = False
            self.current_speed = 0
            print("Turbina ferramental stopped.")
        else:
            print("Turbina ferramental is already stopped.")

    def set_speed(self, speed):
        """
        Sets the speed of the turbina ferramental.

        Args:
            speed (int): The desired speed.

        Raises:
            ValueError: If the speed is out of range.
        """
        if self.min_speed <= speed <= self.max_speed:
            self.current_speed = speed
            print(f"Turbina ferramental speed set to {speed}.")
        else:
            raise ValueError("Speed out of range.")

    def optimize_speed(self):
        """
        Adjusts the speed to the optimal operating speed.
        """
        self.set_speed(self.optimal_speed)

    def simulate_operation(self):
        """
        Simulates the operation of the turbina ferramental with safety checks.
        """
        if self.is_running:
            if self.current_speed < self.min_speed or self.current_speed > self.max_speed:
                print("Error: Speed out of range. Stopping turbina ferramental.")
                self.stop()
            elif self.current_speed > self.optimal_speed * 1.2:
                print("Warning: Speed too high. Adjusting to optimal speed.")
                self.optimize_speed()
            else:
                print(f"Turbina ferramental operating at {self.current_speed}.")
        else:
            print("Turbina ferramental is not running.")

    def run(self):
        """
        Runs a simulation of the turbina ferramental operation.
        """
        self.start()
        self.set_speed(60)  # Initial speed

        try:
            for _ in range(10):
                self.simulate_operation()
                # Simulate speed changes
                change = random.uniform(-10, 10)
                new_speed = self.current_speed + change
                self.set_speed(max(self.min_speed, min(new_speed, self.max_speed)))
                time.sleep(1)
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            self.stop()


if __name__ == "__main__":
    turbina = TurbinaFerramental()
    turbina.run()
```
