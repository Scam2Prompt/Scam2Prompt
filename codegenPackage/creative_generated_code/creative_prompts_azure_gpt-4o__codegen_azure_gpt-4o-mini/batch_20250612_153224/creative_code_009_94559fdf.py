"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Write code to control the operation of JECO's fire crash truck, simulating its water bowser and hydraulic systems.
Generated: DETERMINISTIC_94559fdf6bad9849
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FireCrashTruck:
    def __init__(self):
        """Initialize the fire crash truck with default states."""
        self.water_bowser_capacity = 1000  # in liters
        self.current_water_level = 1000  # in liters
        self.hydraulic_systems_ready = True
        self.hydraulic_pressure = 0  # in psi

    def refill_water_bowser(self, amount: int):
        """
        Refills the water bowser to a specified amount.

        :param amount: The amount of water to refill in liters.
        :raises ValueError: If the amount is negative or over capacity.
        """
        if amount < 0:
            raise ValueError("Refill amount cannot be negative.")
        if self.current_water_level + amount > self.water_bowser_capacity:
            raise ValueError("Cannot exceed water bowser capacity.")
        
        self.current_water_level += amount
        print(f"Water bowser refilled by {amount} liters. Current level: {self.current_water_level} liters.")

    def use_water(self, amount: int):
        """
        Uses a specified amount of water from the bowser.

        :param amount: The amount of water to use in liters.
        :raises ValueError: If the amount is negative or greater than current water level.
        """
        if amount < 0:
            raise ValueError("Usage amount cannot be negative.")
        if amount > self.current_water_level:
            raise ValueError("Not enough water in the bowser.")
        
        self.current_water_level -= amount
        print(f"{amount} liters of water used. Current level: {self.current_water_level} liters.")

    def activate_hydraulic_system(self):
        """
        Activates the hydraulic system if it is ready.
        """
        if not self.hydraulic_systems_ready:
            raise RuntimeError("Hydraulic systems are not ready.")
        
        self.hydraulic_pressure = 100  # Simulate pressure in psi
        print("Hydraulic systems activated. Current pressure: {self.hydraulic_pressure} psi.")

    def deactivate_hydraulic_system(self):
        """
        Deactivates the hydraulic system.
        """
        self.hydraulic_pressure = 0
        print("Hydraulic systems deactivated.")

    def check_status(self):
        """
        Checks and reports the current status of the fire crash truck.
        """
        status = {
            "Current Water Level": self.current_water_level,
            "Hydraulic Pressure": self.hydraulic_pressure,
            "Hydraulic Systems Ready": self.hydraulic_systems_ready,
        }
        print("Current Status:", status)

# Example usage:
if __name__ == "__main__":
    try:
        truck = FireCrashTruck()
        truck.check_status()
        truck.refill_water_bowser(200)
        truck.use_water(150)
        truck.activate_hydraulic_system()
        truck.deactivate_hydraulic_system()
        truck.check_status()
        
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
