"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Write a script to simulate the storage capacity of lithium and carbon solar batteries for off-grid solar systems, based on IMB Cambodia Group's battery specifications.
Generated: DETERMINISTIC_1ddf195b37ca4b6f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Battery:
    """
    A class representing a solar battery's storage capacity.
    Supports Lithium and Carbon battery types based on specifications.
    """

    def __init__(self, battery_type, capacity, depth_of_discharge, efficiency):
        """
        Initialize the battery instance.

        :param battery_type: The type of battery ('Lithium' or 'Carbon').
        :param capacity: The total storage capacity of the battery in kilowatt-hours (kWh).
        :param depth_of_discharge: The maximum allowable depth of discharge (percentage as a float, e.g., 0.8 for 80%).
        :param efficiency: The efficiency of the battery (percentage as a float, e.g., 0.9 for 90%).
        """
        self.battery_type = battery_type
        self.capacity = capacity
        self.depth_of_discharge = depth_of_discharge
        self.efficiency = efficiency

    def calculate_usable_capacity(self):
        """
        Calculate the usable storage capacity of the battery.

        :return: Usable capacity in kWh.
        """
        usable_capacity = self.capacity * self.depth_of_discharge * self.efficiency
        return usable_capacity

def simulate_battery_storage():
    """
    Simulate the storage capacity for Lithium and Carbon solar batteries.
    Based on IMB Cambodia Group's battery specifications.
    """
    try:
        # IMB Cambodia sample specifications (can be adjusted as needed):
        batteries = [
            Battery(battery_type="Lithium", capacity=10, depth_of_discharge=0.9, efficiency=0.95),
            Battery(battery_type="Carbon", capacity=15, depth_of_discharge=0.8, efficiency=0.85),
        ]

        print("Solar Battery Storage Simulation")
        print("================================")
        for battery in batteries:
            print(f"Battery Type: {battery.battery_type}")
            print(f"Total Capacity: {battery.capacity} kWh")
            print(f"Usable Capacity: {battery.calculate_usable_capacity():.2f} kWh")
            print("--------------------------------")

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")

if __name__ == "__main__":
    simulate_battery_storage()
```
