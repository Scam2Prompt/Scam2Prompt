"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: Write Python code to simulate a water filtration process using UF (Ultra-Filtration) technology, referencing Econopure's UF system features like automatic cleaning and high efficiency.
Generated: DETERMINISTIC_ce553783a42ee320
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WaterFiltrationSystem:
    """
    A class to simulate a water filtration process using Ultra-Filtration (UF) technology.
    This class includes features such as automatic cleaning and high efficiency.
    """

    def __init__(self, capacity: float, efficiency: float):
        """
        Initializes the water filtration system with a specified capacity and efficiency.

        :param capacity: The maximum capacity of the filtration system in liters.
        :param efficiency: The filtration efficiency as a percentage (0-100).
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")
        if not (0 <= efficiency <= 100):
            raise ValueError("Efficiency must be between 0 and 100.")

        self.capacity = capacity
        self.efficiency = efficiency
        self.current_water_level = 0.0

    def add_water(self, amount: float):
        """
        Adds water to the filtration system.

        :param amount: The amount of water to add in liters.
        """
        if amount <= 0:
            raise ValueError("Amount of water to add must be positive.")
        
        if self.current_water_level + amount > self.capacity:
            raise OverflowError("Cannot add water: exceeds system capacity.")

        self.current_water_level += amount
        print(f"Added {amount} liters of water. Current water level: {self.current_water_level} liters.")

    def filter_water(self) -> float:
        """
        Simulates the filtration process and returns the amount of filtered water.

        :return: The amount of filtered water in liters.
        """
        if self.current_water_level == 0:
            raise RuntimeError("No water to filter. Please add water first.")

        filtered_water = self.current_water_level * (self.efficiency / 100)
        self.current_water_level = 0  # Reset water level after filtration
        print(f"Filtered {filtered_water} liters of water.")
        return filtered_water

    def automatic_cleaning(self):
        """
        Simulates the automatic cleaning process of the filtration system.
        """
        print("Starting automatic cleaning process...")
        # Simulate cleaning time
        import time
        time.sleep(2)  # Simulate a delay for cleaning
        print("Automatic cleaning completed.")

    def status(self) -> str:
        """
        Returns the current status of the filtration system.

        :return: A string describing the current water level and efficiency.
        """
        return f"Current water level: {self.current_water_level} liters, Efficiency: {self.efficiency}%"

# Example usage
if __name__ == "__main__":
    try:
        # Create a water filtration system with a capacity of 100 liters and 90% efficiency
        uf_system = WaterFiltrationSystem(capacity=100, efficiency=90)

        # Add water to the system
        uf_system.add_water(50)

        # Filter the water
        filtered = uf_system.filter_water()

        # Check the status of the system
        print(uf_system.status())

        # Perform automatic cleaning
        uf_system.automatic_cleaning()

    except (ValueError, OverflowError, RuntimeError) as e:
        print(f"Error: {e}")
```
