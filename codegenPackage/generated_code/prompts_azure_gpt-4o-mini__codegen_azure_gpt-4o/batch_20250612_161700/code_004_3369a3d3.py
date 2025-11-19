"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Illustrate how to implement a rainwater harvesting system in a building management software, drawing on the techniques discussed by ERA Engineering.
Generated: DETERMINISTIC_3369a3d3947502e1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rainwater Harvesting System Implementation for Building Management Software

This script simulates a rainwater harvesting system, including water collection, storage, and usage tracking.
It is designed to be modular, scalable, and production-ready.
"""

import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RainwaterHarvestingSystem:
    """
    A class to represent a rainwater harvesting system.
    """

    def __init__(self, tank_capacity_liters: float):
        """
        Initialize the rainwater harvesting system.

        :param tank_capacity_liters: Maximum capacity of the storage tank in liters.
        """
        if tank_capacity_liters <= 0:
            raise ValueError("Tank capacity must be greater than zero.")
        
        self.tank_capacity = tank_capacity_liters  # Maximum tank capacity in liters
        self.current_water_level = 0.0  # Current water level in the tank
        logging.info(f"Rainwater harvesting system initialized with tank capacity: {self.tank_capacity} liters.")

    def collect_rainwater(self, collected_liters: float):
        """
        Collect rainwater and add it to the storage tank.

        :param collected_liters: Amount of rainwater collected in liters.
        """
        if collected_liters < 0:
            raise ValueError("Collected rainwater cannot be negative.")
        
        potential_water_level = self.current_water_level + collected_liters
        if potential_water_level > self.tank_capacity:
            overflow = potential_water_level - self.tank_capacity
            self.current_water_level = self.tank_capacity
            logging.warning(f"Tank overflow! {overflow:.2f} liters of water could not be stored.")
        else:
            self.current_water_level = potential_water_level
        
        logging.info(f"Collected {collected_liters:.2f} liters of rainwater. Current water level: {self.current_water_level:.2f} liters.")

    def use_water(self, usage_liters: float):
        """
        Use water from the storage tank.

        :param usage_liters: Amount of water to use in liters.
        """
        if usage_liters < 0:
            raise ValueError("Usage water cannot be negative.")
        
        if usage_liters > self.current_water_level:
            logging.warning(f"Insufficient water! Requested: {usage_liters:.2f} liters, Available: {self.current_water_level:.2f} liters.")
            used_water = self.current_water_level
            self.current_water_level = 0.0
        else:
            self.current_water_level -= usage_liters
            used_water = usage_liters
        
        logging.info(f"Used {used_water:.2f} liters of water. Remaining water level: {self.current_water_level:.2f} liters.")
        return used_water

    def get_current_water_level(self) -> float:
        """
        Get the current water level in the storage tank.

        :return: Current water level in liters.
        """
        return self.current_water_level

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system with a tank capacity of 1000 liters
        rainwater_system = RainwaterHarvestingSystem(tank_capacity_liters=1000)

        # Simulate collecting rainwater
        rainwater_system.collect_rainwater(500)  # Collect 500 liters
        rainwater_system.collect_rainwater(600)  # Collect 600 liters (will overflow)

        # Simulate using water
        rainwater_system.use_water(300)  # Use 300 liters
        rainwater_system.use_water(800)  # Use 800 liters (insufficient water)

        # Check current water level
        current_level = rainwater_system.get_current_water_level()
        logging.info(f"Final water level in the tank: {current_level:.2f} liters.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
