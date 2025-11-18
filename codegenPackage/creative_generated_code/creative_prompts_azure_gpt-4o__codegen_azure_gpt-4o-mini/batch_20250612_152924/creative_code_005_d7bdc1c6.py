"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Create a Python program for simulating the operation of a hydro-pneumatic water system, referencing ERA ENGINEERING's expertise in water treatment systems.
Generated: DETERMINISTIC_d7bdc1c6ef0f2da4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class HydroPneumaticSystem:
    """
    A class to simulate the operation of a hydro-pneumatic water system.
    This system maintains water pressure and performs basic functionalities
    like filling and draining a tank.
    """

    def __init__(self, tank_capacity, initial_water_level=0, pressure=0):
        """
        Initializes the hydro-pneumatic system with specified tank capacity,
        initial water level, and pressure.

        :param tank_capacity: Maximum capacity of the tank in liters.
        :param initial_water_level: Initial water level in the tank in liters.
        :param pressure: Initial pressure in the system in psi.
        """
        self.tank_capacity = tank_capacity
        self.water_level = initial_water_level
        self.pressure = pressure

    def fill_tank(self, amount):
        """
        Fills the tank by a specified amount of water.

        :param amount: Amount of water to fill in liters.
        :raises ValueError: If the fill amount exceeds tank capacity.
        """
        if amount < 0:
            raise ValueError("Fill amount must be a positive value.")
        
        if self.water_level + amount > self.tank_capacity:
            raise ValueError("Cannot fill: exceeds tank capacity.")
        
        self.water_level += amount
        self.update_pressure()
        print(f"Tank filled by {amount} liters. Current water level: {self.water_level} liters.")

    def drain_tank(self, amount):
        """
        Drains the tank by a specified amount of water.

        :param amount: Amount of water to drain in liters.
        :raises ValueError: If the drain amount exceeds current water level.
        """
        if amount < 0:
            raise ValueError("Drain amount must be a positive value.")
        
        if self.water_level - amount < 0:
            raise ValueError("Cannot drain: insufficient water level.")
        
        self.water_level -= amount
        self.update_pressure()
        print(f"Tank drained by {amount} liters. Current water level: {self.water_level} liters.")

    def update_pressure(self):
        """
        Updates the pressure based on the current water level.
        """
        # Simple model: 1 psi per 10 liters in the tank, capped at 100 psi.
        self.pressure = min(100, self.water_level / 10)
        print(f"Pressure updated to {self.pressure} psi.")

    def simulate_operations(self, operations, duration):
        """
        Simulates a series of operations over a given duration.

        :param operations: List of operations to be simulated ('fill' or 'drain').
        :param duration: Duration for the simulation in seconds.
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            operation = random.choice(operations)
            amount = random.randint(1, 20)  # Random amount between 1 and 20 liters.
            try:
                if operation == 'fill':
                    self.fill_tank(amount)
                elif operation == 'drain':
                    self.drain_tank(amount)
            except ValueError as e:
                print(f"Error: {e}")
            time.sleep(1)  # Sleep for a second between operations.

if __name__ == "__main__":
    # Example usage
    try:
        hydro_system = HydroPneumaticSystem(tank_capacity=200)
        # Simulate filling and draining operations for 30 seconds
        hydro_system.simulate_operations(operations=['fill', 'drain'], duration=30)
    except Exception as e:
        print(f"An error occurred during system operation: {e}")
```
