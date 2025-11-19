"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Write a Python script that simulates the operation of a static fluid measurement system, referencing the specifications outlined by Petro Kalaye Zartaj.
Generated: DETERMINISTIC_110ed2c6e25b8041
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class StaticFluidMeasurementSystem:
    """
    A class to simulate a static fluid measurement system.
    This system can measure fluid levels and simulate sensor readings.
    """

    def __init__(self, tank_capacity: float):
        """
        Initializes the static fluid measurement system.

        :param tank_capacity: The maximum capacity of the tank in liters.
        """
        if tank_capacity <= 0:
            raise ValueError("Tank capacity must be a positive number.")
        self.tank_capacity = tank_capacity  # Maximum capacity of the tank
        self.current_level = 0.0  # Current fluid level in the tank

    def fill_tank(self, amount: float):
        """
        Fills the tank with a specified amount of fluid.

        :param amount: The amount of fluid to add in liters.
        :raises ValueError: If the amount is negative or exceeds the tank capacity.
        """
        if amount < 0:
            raise ValueError("Amount to fill must be a non-negative number.")
        if self.current_level + amount > self.tank_capacity:
            raise ValueError("Filling exceeds tank capacity.")
        
        self.current_level += amount
        print(f"Tank filled by {amount} liters. Current level: {self.current_level:.2f} liters.")

    def drain_tank(self, amount: float):
        """
        Drains a specified amount of fluid from the tank.

        :param amount: The amount of fluid to remove in liters.
        :raises ValueError: If the amount is negative or exceeds the current fluid level.
        """
        if amount < 0:
            raise ValueError("Amount to drain must be a non-negative number.")
        if amount > self.current_level:
            raise ValueError("Draining exceeds current fluid level.")
        
        self.current_level -= amount
        print(f"Tank drained by {amount} liters. Current level: {self.current_level:.2f} liters.")

    def get_current_level(self) -> float:
        """
        Returns the current fluid level in the tank.

        :return: Current fluid level in liters.
        """
        return self.current_level

    def simulate_sensor_reading(self) -> float:
        """
        Simulates a sensor reading for the current fluid level.

        :return: A simulated sensor reading of the fluid level.
        """
        # Simulate a slight variation in the reading
        variation = random.uniform(-0.5, 0.5)
        sensor_reading = self.current_level + variation
        print(f"Sensor reading: {sensor_reading:.2f} liters (with variation).")
        return sensor_reading

def main():
    """
    Main function to run the static fluid measurement system simulation.
    """
    try:
        # Create a static fluid measurement system with a tank capacity of 1000 liters
        fluid_system = StaticFluidMeasurementSystem(tank_capacity=1000.0)

        # Fill the tank
        fluid_system.fill_tank(500.0)

        # Simulate sensor reading
        fluid_system.simulate_sensor_reading()

        # Drain some fluid
        fluid_system.drain_tank(200.0)

        # Get current level
        current_level = fluid_system.get_current_level()
        print(f"Final fluid level in the tank: {current_level:.2f} liters.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
