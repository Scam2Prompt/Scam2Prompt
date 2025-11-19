"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Illustrate how to implement a rainwater harvesting system in a building management software, drawing on the techniques discussed by ERA Engineering.
Generated: DETERMINISTIC_3369a3d3947502e1
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RainwaterHarvestingSystem:
    """
    A class to represent a rainwater harvesting system for a building.
    This system collects, stores, and utilizes rainwater for various non-potable uses.
    """

    def __init__(self, tank_capacity: float, roof_area: float):
        """
        Initializes the rainwater harvesting system with a tank capacity and a roof area.

        Parameters:
        tank_capacity (float): The capacity of the storage tank in liters.
        roof_area (float): The area of the roof in square meters.
        """
        self.tank_capacity = tank_capacity  # in liters
        self.roof_area = roof_area  # in square meters
        self.current_storage = 0.0  # Current water storage in liters

    def calculate_rainfall(self, rainfall_mm: float) -> float:
        """
        Calculate the amount of rainwater collected based on the rainfall.

        Parameters:
        rainfall_mm (float): The amount of rainfall in millimeters.

        Returns:
        float: Amount of rainwater collected in liters.
        """
        if rainfall_mm < 0:
            raise ValueError("Rainfall cannot be negative.")
        
        # 1 mm of rainfall on 1 m² produces 1 liter of water
        collected_water = self.roof_area * rainfall_mm
        return collected_water

    def store_rainwater(self, collected_water: float) -> None:
        """
        Store the collected rainwater in the tank.

        Parameters:
        collected_water (float): Amount of collected rainwater in liters.
        """
        if collected_water < 0:
            raise ValueError("Collected water cannot be negative.")
        
        potential_storage = self.current_storage + collected_water
        
        if potential_storage > self.tank_capacity:
            overflow = potential_storage - self.tank_capacity
            self.current_storage = self.tank_capacity  # Fill the tank to its capacity
            print(f"Overflow of {overflow} liters occurs. Excess water will be lost.")
        else:
            self.current_storage = potential_storage

    def utilize_rainwater(self, usage_amount: float) -> None:
        """
        Utilize a specified amount of rainwater from the storage.

        Parameters:
        usage_amount (float): Amount of rainwater to utilize in liters.

        Raises:
        ValueError: If usage amount exceeds available storage.
        """
        if usage_amount < 0:
            raise ValueError("Usage amount cannot be negative.")
        
        if usage_amount > self.current_storage:
            raise ValueError("Not enough rainwater stored for this usage.")

        self.current_storage -= usage_amount
        print(f"Utilized {usage_amount} liters of rainwater. Current storage: {self.current_storage} liters.")

    def get_current_storage(self) -> float:
        """
        Get the current amount of rainwater stored in the tank.

        Returns:
        float: Current storage level in liters.
        """
        return self.current_storage

    def __str__(self) -> str:
        """
        String representation of the rainwater harvesting system.

        Returns:
        str: Descriptive information about the system status.
        """
        return (f"Rainwater Harvesting System:\n"
                f"  Tank Capacity: {self.tank_capacity} liters\n"
                f"  Current Storage: {self.current_storage} liters\n"
                f"  Roof Area: {self.roof_area} m²")


# Example of usage
if __name__ == "__main__":
    try:
        # Initialize the rainwater harvesting system with a tank of 5000 liters and a roof area of 100 m²
        rwh_system = RainwaterHarvestingSystem(tank_capacity=5000, roof_area=100)

        # Simulate a rainfall of 50 mm
        rainfall = 50
        collected_water = rwh_system.calculate_rainfall(rainfall)

        # Store the collected rainfall
        rwh_system.store_rainwater(collected_water)
        print(rwh_system)

        # Utilize some rainwater
        rwh_system.utilize_rainwater(2000)  # Use 2000 liters of rainwater
        print(rwh_system)

    except ValueError as e:
        print(f"Error: {e}")
```
