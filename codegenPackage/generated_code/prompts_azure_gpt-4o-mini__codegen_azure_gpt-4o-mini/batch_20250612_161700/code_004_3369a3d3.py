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
class RainwaterHarvestingSystem:
    """
    A class to represent a rainwater harvesting system in a building management software.
    """

    def __init__(self, tank_capacity: float, roof_area: float):
        """
        Initializes the rainwater harvesting system with tank capacity and roof area.

        :param tank_capacity: The capacity of the rainwater tank in liters.
        :param roof_area: The area of the roof in square meters.
        """
        self.tank_capacity = tank_capacity  # in liters
        self.roof_area = roof_area  # in square meters
        self.current_water_level = 0.0  # in liters

    def calculate_rainwater_collection(self, rainfall_mm: float) -> float:
        """
        Calculates the amount of rainwater that can be collected based on rainfall.

        :param rainfall_mm: The amount of rainfall in millimeters.
        :return: The volume of rainwater collected in liters.
        """
        # Convert rainfall from mm to liters collected
        collected_water = (rainfall_mm / 1000) * self.roof_area * 1000  # liters
        return collected_water

    def store_rainwater(self, collected_water: float) -> None:
        """
        Stores the collected rainwater in the tank, ensuring it does not exceed capacity.

        :param collected_water: The amount of collected rainwater in liters.
        """
        if collected_water < 0:
            raise ValueError("Collected water cannot be negative.")

        # Calculate new water level
        new_water_level = self.current_water_level + collected_water

        if new_water_level > self.tank_capacity:
            self.current_water_level = self.tank_capacity
            print("Tank is full. Excess water is not stored.")
        else:
            self.current_water_level = new_water_level

    def use_rainwater(self, amount: float) -> None:
        """
        Uses a specified amount of rainwater from the tank.

        :param amount: The amount of rainwater to use in liters.
        """
        if amount < 0:
            raise ValueError("Amount to use cannot be negative.")

        if amount > self.current_water_level:
            raise ValueError("Not enough rainwater available in the tank.")

        self.current_water_level -= amount

    def get_current_water_level(self) -> float:
        """
        Returns the current water level in the tank.

        :return: The current water level in liters.
        """
        return self.current_water_level

    def reset_system(self) -> None:
        """
        Resets the rainwater harvesting system to its initial state.
        """
        self.current_water_level = 0.0
        print("Rainwater harvesting system has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the rainwater harvesting system
        rwh_system = RainwaterHarvestingSystem(tank_capacity=5000, roof_area=100)

        # Simulate rainfall
        rainfall = 50  # mm
        collected_water = rwh_system.calculate_rainwater_collection(rainfall)
        print(f"Collected water: {collected_water} liters")

        # Store the collected rainwater
        rwh_system.store_rainwater(collected_water)
        print(f"Current water level: {rwh_system.get_current_water_level()} liters")

        # Use some rainwater
        rwh_system.use_rainwater(200)
        print(f"Current water level after use: {rwh_system.get_current_water_level()} liters")

        # Reset the system
        rwh_system.reset_system()
        print(f"Current water level after reset: {rwh_system.get_current_water_level()} liters")

    except ValueError as e:
        print(f"Error: {e}")
```
