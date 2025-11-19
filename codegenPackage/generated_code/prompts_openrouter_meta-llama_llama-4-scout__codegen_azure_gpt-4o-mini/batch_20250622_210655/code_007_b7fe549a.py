"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Write a code example for implementing a tractor-mounted water bowzer using JECO's hydraulic systems.
Generated: DETERMINISTIC_b7fe549a6ce3bf19
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicSystem:
    """
    A class to represent a hydraulic system for controlling the water bowser.
    """

    def __init__(self):
        self.pressure = 0  # Pressure in psi
        self.flow_rate = 0  # Flow rate in gallons per minute

    def set_pressure(self, pressure):
        """
        Set the hydraulic pressure.

        :param pressure: Pressure in psi
        :raises ValueError: If pressure is negative
        """
        if pressure < 0:
            raise ValueError("Pressure cannot be negative.")
        self.pressure = pressure

    def set_flow_rate(self, flow_rate):
        """
        Set the flow rate of the hydraulic system.

        :param flow_rate: Flow rate in gallons per minute
        :raises ValueError: If flow rate is negative
        """
        if flow_rate < 0:
            raise ValueError("Flow rate cannot be negative.")
        self.flow_rate = flow_rate

    def activate(self):
        """
        Activate the hydraulic system.
        """
        if self.pressure == 0 or self.flow_rate == 0:
            raise RuntimeError("Cannot activate hydraulic system: pressure or flow rate is zero.")
        print(f"Hydraulic system activated with pressure: {self.pressure} psi and flow rate: {self.flow_rate} GPM.")


class WaterBowser:
    """
    A class to represent a tractor-mounted water bowser.
    """

    def __init__(self, hydraulic_system):
        """
        Initialize the water bowser with a hydraulic system.

        :param hydraulic_system: An instance of HydraulicSystem
        """
        self.hydraulic_system = hydraulic_system
        self.water_capacity = 1000  # Capacity in gallons
        self.current_water_level = 0  # Current water level in gallons

    def fill_water(self, amount):
        """
        Fill the water bowser with a specified amount of water.

        :param amount: Amount of water to fill in gallons
        :raises ValueError: If amount is negative or exceeds capacity
        """
        if amount < 0:
            raise ValueError("Amount to fill cannot be negative.")
        if self.current_water_level + amount > self.water_capacity:
            raise ValueError("Cannot fill beyond water capacity.")
        self.current_water_level += amount
        print(f"Water bowser filled. Current water level: {self.current_water_level} gallons.")

    def empty_water(self):
        """
        Empty the water bowser.
        """
        self.current_water_level = 0
        print("Water bowser emptied.")

    def spray_water(self):
        """
        Spray water using the hydraulic system.
        """
        if self.current_water_level == 0:
            raise RuntimeError("Cannot spray water: water bowser is empty.")
        self.hydraulic_system.activate()
        print(f"Spraying water. Current water level: {self.current_water_level} gallons.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a hydraulic system
        hydraulic_system = HydraulicSystem()
        hydraulic_system.set_pressure(1500)  # Set pressure to 1500 psi
        hydraulic_system.set_flow_rate(50)    # Set flow rate to 50 GPM

        # Create a water bowser
        water_bowser = WaterBowser(hydraulic_system)
        water_bowser.fill_water(500)  # Fill with 500 gallons
        water_bowser.spray_water()     # Spray water
        water_bowser.empty_water()     # Empty the water bowser

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
