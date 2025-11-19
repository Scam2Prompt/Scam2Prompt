"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Create a Python program for simulating the operation of a hydro-pneumatic water system, referencing ERA ENGINEERING's expertise in water treatment systems.
Generated: DETERMINISTIC_d7bdc1c6ef0f2da4
Batch ID: 20250612_152924
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

class HydroPneumaticSystem:
    """
    A class to simulate the operation of a hydro-pneumatic water system.
    This system manages water pressure and flow using pneumatic principles.
    """

    def __init__(self, tank_capacity, initial_water_level, pump_capacity):
        """
        Initializes the hydro-pneumatic system with given parameters.

        :param tank_capacity: Maximum capacity of the water tank in liters.
        :param initial_water_level: Initial water level in the tank in liters.
        :param pump_capacity: Pump capacity in liters per minute.
        """
        self.tank_capacity = tank_capacity
        self.water_level = initial_water_level
        self.pump_capacity = pump_capacity
        self.is_pump_on = False

        if not (0 <= self.water_level <= self.tank_capacity):
            raise ValueError("Initial water level must be between 0 and tank capacity.")

    def start_pump(self):
        """Starts the water pump to fill the tank."""
        self.is_pump_on = True
        print("Pump started.")

    def stop_pump(self):
        """Stops the water pump."""
        self.is_pump_on = False
        print("Pump stopped.")

    def fill_tank(self, duration):
        """
        Fills the tank for a specified duration.

        :param duration: Duration in minutes to fill the tank.
        """
        if not self.is_pump_on:
            raise RuntimeError("Pump must be started before filling the tank.")

        for minute in range(duration):
            if self.water_level < self.tank_capacity:
                self.water_level += self.pump_capacity
                if self.water_level > self.tank_capacity:
                    self.water_level = self.tank_capacity
                print(f"Minute {minute + 1}: Water level is {self.water_level} liters.")
            else:
                print("Tank is full.")
                break
            time.sleep(1)  # Simulate time passing

    def use_water(self, amount):
        """
        Simulates using water from the tank.

        :param amount: Amount of water to use in liters.
        """
        if amount < 0:
            raise ValueError("Amount of water to use must be non-negative.")

        if self.water_level >= amount:
            self.water_level -= amount
            print(f"Used {amount} liters of water. Remaining water level: {self.water_level} liters.")
        else:
            print("Not enough water in the tank to fulfill the request.")

    def get_water_level(self):
        """Returns the current water level in the tank."""
        return self.water_level

    def simulate(self):
        """Simulates the operation of the hydro-pneumatic system."""
        try:
            self.start_pump()
            self.fill_tank(duration=5)  # Fill for 5 minutes
            self.stop_pump()

            # Simulate water usage
            for _ in range(3):
                water_to_use = random.randint(1, 50)  # Randomly use between 1 and 50 liters
                self.use_water(water_to_use)
                time.sleep(1)  # Simulate time passing

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create a hydro-pneumatic system with a tank capacity of 500 liters,
    # an initial water level of 100 liters, and a pump capacity of 20 liters per minute.
    system = HydroPneumaticSystem(tank_capacity=500, initial_water_level=100, pump_capacity=20)
    system.simulate()
```
