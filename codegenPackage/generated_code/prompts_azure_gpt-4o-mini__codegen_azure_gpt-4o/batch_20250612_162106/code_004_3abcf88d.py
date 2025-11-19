"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Code a simulation for the operation of a paddy dryer, utilizing the specifications of the various components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_3abcf88d3d5f261f
Batch ID: 20250612_162106
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

class PaddyDryer:
    """
    A simulation of a paddy dryer operation.
    """

    def __init__(self, capacity_kg, drying_temperature_c, drying_time_min):
        """
        Initialize the paddy dryer with its specifications.

        :param capacity_kg: Maximum capacity of the dryer in kilograms.
        :param drying_temperature_c: Target drying temperature in Celsius.
        :param drying_time_min: Time required for drying in minutes.
        """
        self.capacity_kg = capacity_kg
        self.drying_temperature_c = drying_temperature_c
        self.drying_time_min = drying_time_min
        self.current_load_kg = 0
        self.is_running = False

    def load_paddy(self, weight_kg):
        """
        Load paddy into the dryer.

        :param weight_kg: Weight of the paddy to load in kilograms.
        :raises ValueError: If the weight exceeds the dryer's capacity.
        """
        if weight_kg > self.capacity_kg:
            raise ValueError(f"Cannot load {weight_kg}kg. Maximum capacity is {self.capacity_kg}kg.")
        self.current_load_kg = weight_kg
        print(f"Paddy loaded: {weight_kg}kg")

    def start_drying(self):
        """
        Start the drying process.

        :raises RuntimeError: If the dryer is already running or no paddy is loaded.
        """
        if self.is_running:
            raise RuntimeError("Dryer is already running.")
        if self.current_load_kg == 0:
            raise RuntimeError("No paddy loaded. Please load paddy before starting the dryer.")
        
        self.is_running = True
        print(f"Drying started at {self.drying_temperature_c}°C for {self.drying_time_min} minutes.")
        self._simulate_drying()

    def _simulate_drying(self):
        """
        Simulate the drying process (internal method).
        """
        try:
            for minute in range(1, self.drying_time_min + 1):
                time.sleep(0.1)  # Simulate real-time drying (shortened for simulation purposes)
                print(f"Drying... {minute}/{self.drying_time_min} minutes elapsed.")
                # Simulate random temperature fluctuations
                current_temp = self.drying_temperature_c + random.uniform(-2, 2)
                print(f"Current temperature: {current_temp:.2f}°C")
            print("Drying complete.")
        finally:
            self.is_running = False
            self.current_load_kg = 0  # Reset the load after drying

    def stop_drying(self):
        """
        Stop the drying process manually.

        :raises RuntimeError: If the dryer is not running.
        """
        if not self.is_running:
            raise RuntimeError("Dryer is not running.")
        self.is_running = False
        print("Drying process stopped manually.")

# Example usage
if __name__ == "__main__":
    # Create a paddy dryer instance with a capacity of 1000kg, drying temperature of 60°C, and drying time of 30 minutes
    dryer = PaddyDryer(capacity_kg=1000, drying_temperature_c=60, drying_time_min=30)

    try:
        # Load 500kg of paddy
        dryer.load_paddy(500)

        # Start the drying process
        dryer.start_drying()
    except Exception as e:
        print(f"Error: {e}")
```
