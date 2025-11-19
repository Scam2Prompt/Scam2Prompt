"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write code to control the operation of JECO's fire crash truck, simulating its water bowser and hydraulic systems.
Generated: DETERMINISTIC_94559fdf6bad9849
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FireCrashTruck:
    def __init__(self):
        """Initialize the fire crash truck with default states."""
        self.water_bowser_capacity = 1000  # in liters
        self.current_water_level = 1000  # in liters
        self.hydraulic_system_active = False

    def fill_water_bowser(self, amount):
        """
        Fill the water bowser with a specified amount of water.
        
        :param amount: Amount of water to fill in liters.
        :raises ValueError: If the amount is negative or exceeds capacity.
        """
        if amount < 0:
            raise ValueError("Amount to fill cannot be negative.")
        if self.current_water_level + amount > self.water_bowser_capacity:
            raise ValueError("Cannot exceed water bowser capacity.")
        
        self.current_water_level += amount
        print(f"Water bowser filled. Current water level: {self.current_water_level} liters.")

    def use_water(self, amount):
        """
        Use a specified amount of water from the water bowser.
        
        :param amount: Amount of water to use in liters.
        :raises ValueError: If the amount is negative or exceeds current water level.
        """
        if amount < 0:
            raise ValueError("Amount to use cannot be negative.")
        if amount > self.current_water_level:
            raise ValueError("Not enough water in the bowser.")
        
        self.current_water_level -= amount
        print(f"Used {amount} liters of water. Current water level: {self.current_water_level} liters.")

    def activate_hydraulic_system(self):
        """Activate the hydraulic system."""
        if not self.hydraulic_system_active:
            self.hydraulic_system_active = True
            print("Hydraulic system activated.")
        else:
            print("Hydraulic system is already active.")

    def deactivate_hydraulic_system(self):
        """Deactivate the hydraulic system."""
        if self.hydraulic_system_active:
            self.hydraulic_system_active = False
            print("Hydraulic system deactivated.")
        else:
            print("Hydraulic system is already inactive.")

    def status_report(self):
        """Generate a status report of the fire crash truck."""
        report = (
            f"Current water level: {self.current_water_level} liters\n"
            f"Hydraulic system active: {self.hydraulic_system_active}\n"
        )
        print(report)

# Example usage
if __name__ == "__main__":
    try:
        truck = FireCrashTruck()
        truck.status_report()
        truck.fill_water_bowser(200)
        truck.use_water(150)
        truck.activate_hydraulic_system()
        truck.deactivate_hydraulic_system()
        truck.status_report()
    except ValueError as e:
        print(f"Error: {e}")
```
