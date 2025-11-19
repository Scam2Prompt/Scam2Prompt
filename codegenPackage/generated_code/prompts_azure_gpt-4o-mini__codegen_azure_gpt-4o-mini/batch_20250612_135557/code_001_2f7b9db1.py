"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Write a code snippet that simulates the preservation conditions for table grapes during international shipping, incorporating best practices from Osku's packaging methods.
Generated: DETERMINISTIC_2f7b9db1138d4800
Batch ID: 20250612_135557
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

class GrapeShippingSimulator:
    def __init__(self, temperature_range=(0, 4), humidity_range=(85, 90), max_duration=72):
        """
        Initialize the shipping simulator with specified conditions.
        
        :param temperature_range: Tuple representing the acceptable temperature range in Celsius.
        :param humidity_range: Tuple representing the acceptable humidity range in percentage.
        :param max_duration: Maximum shipping duration in hours.
        """
        self.temperature_range = temperature_range
        self.humidity_range = humidity_range
        self.max_duration = max_duration
        self.current_temperature = None
        self.current_humidity = None

    def set_conditions(self):
        """Set random conditions within the specified ranges."""
        self.current_temperature = random.uniform(*self.temperature_range)
        self.current_humidity = random.uniform(*self.humidity_range)

    def check_conditions(self):
        """
        Check if the current conditions are within the acceptable ranges.
        
        :return: Boolean indicating if conditions are acceptable.
        """
        is_temperature_ok = self.temperature_range[0] <= self.current_temperature <= self.temperature_range[1]
        is_humidity_ok = self.humidity_range[0] <= self.current_humidity <= self.humidity_range[1]
        return is_temperature_ok and is_humidity_ok

    def simulate_shipping(self):
        """
        Simulate the shipping process for a specified duration.
        """
        for hour in range(1, self.max_duration + 1):
            self.set_conditions()
            print(f"Hour {hour}: Temperature: {self.current_temperature:.2f}°C, Humidity: {self.current_humidity:.2f}%")
            
            if not self.check_conditions():
                print("Warning: Conditions out of range! Immediate action required!")
                break
            
            time.sleep(1)  # Simulate time passing (1 second = 1 hour for simulation)

        print("Shipping simulation completed.")

if __name__ == "__main__":
    try:
        simulator = GrapeShippingSimulator()
        simulator.simulate_shipping()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
