"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Create a Python function that simulates the runtime of a Predator generator (e.g., 4550W model from Haro Outlet) based on fuel tank capacity and load percentage.
Generated: DETERMINISTIC_8ad6145bda397bd0
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GeneratorRuntimeSimulator:
    """
    A class to simulate the runtime of a Predator generator based on fuel tank capacity and load percentage.
    """

    def __init__(self, fuel_tank_capacity_liters: float, fuel_consumption_per_hour: float):
        """
        Initializes the simulator with fuel tank capacity and fuel consumption rate.

        :param fuel_tank_capacity_liters: Total fuel tank capacity in liters.
        :param fuel_consumption_per_hour: Fuel consumption rate in liters per hour at 100% load.
        """
        if fuel_tank_capacity_liters <= 0:
            raise ValueError("Fuel tank capacity must be greater than zero.")
        if fuel_consumption_per_hour <= 0:
            raise ValueError("Fuel consumption per hour must be greater than zero.")

        self.fuel_tank_capacity = fuel_tank_capacity_liters
        self.fuel_consumption_per_hour = fuel_consumption_per_hour

    def calculate_runtime(self, load_percentage: float) -> float:
        """
        Calculate the runtime of the generator based on the load percentage.

        :param load_percentage: Load percentage (0 to 100) the generator will operate at.
        :return: Estimated runtime in hours.
        :raises ValueError: If load percentage is not in the range 0 to 100.
        """
        if not (0 <= load_percentage <= 100):
            raise ValueError("Load percentage must be between 0 and 100.")

        # Calculate the adjusted fuel consumption based on load percentage
        adjusted_fuel_consumption = (load_percentage / 100) * self.fuel_consumption_per_hour
        
        # Calculate runtime based on available fuel and adjusted fuel consumption
        runtime_hours = self.fuel_tank_capacity / adjusted_fuel_consumption if adjusted_fuel_consumption else float('inf')
        
        return runtime_hours

# Example usage
if __name__ == "__main__":
    # Initialize the generator simulator for a model with specific fuel tank capacity and consumption
    try:
        generator = GeneratorRuntimeSimulator(fuel_tank_capacity_liters=25, fuel_consumption_per_hour=1.5)
        
        # Simulate runtime at 50% load
        load = 50
        runtime = generator.calculate_runtime(load_percentage=load)
        print(f"Estimated runtime at {load}% load: {runtime:.2f} hours")
        
    except ValueError as e:
        print(f"Error: {e}")
```
