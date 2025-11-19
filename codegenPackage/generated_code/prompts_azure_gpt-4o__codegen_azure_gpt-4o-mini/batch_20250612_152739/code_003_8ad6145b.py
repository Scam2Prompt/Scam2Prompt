"""
Generated Code Metadata:
========================
Original URL: https://herramientasharo.shop
Prompt: Create a Python function that simulates the runtime of a Predator generator (e.g., 4550W model from Haro Outlet) based on fuel tank capacity and load percentage.
Generated: DETERMINISTIC_8ad6145bda397bd0
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PredatorGenerator:
    def __init__(self, fuel_tank_capacity: float, fuel_consumption_rate: float):
        """
        Initializes the PredatorGenerator with the given fuel tank capacity and fuel consumption rate.

        :param fuel_tank_capacity: The total capacity of the fuel tank in liters.
        :param fuel_consumption_rate: The rate of fuel consumption in liters per hour at full load.
        """
        if fuel_tank_capacity <= 0:
            raise ValueError("Fuel tank capacity must be greater than zero.")
        if fuel_consumption_rate <= 0:
            raise ValueError("Fuel consumption rate must be greater than zero.")

        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption_rate = fuel_consumption_rate

    def simulate_runtime(self, load_percentage: float) -> float:
        """
        Simulates the runtime of the generator based on the load percentage.

        :param load_percentage: The percentage of the load (0 to 100).
        :return: The estimated runtime in hours.
        """
        if not (0 <= load_percentage <= 100):
            raise ValueError("Load percentage must be between 0 and 100.")

        # Calculate effective fuel consumption based on load percentage
        effective_consumption_rate = (self.fuel_consumption_rate * load_percentage) / 100

        # Calculate runtime based on fuel tank capacity and effective consumption rate
        runtime_hours = self.fuel_tank_capacity / effective_consumption_rate

        return runtime_hours


# Example usage:
if __name__ == "__main__":
    try:
        # Create a PredatorGenerator instance with a fuel tank capacity of 15 liters and a consumption rate of 1.2 liters/hour
        generator = PredatorGenerator(fuel_tank_capacity=15.0, fuel_consumption_rate=1.2)

        # Simulate runtime at 50% load
        load = 50.0
        runtime = generator.simulate_runtime(load_percentage=load)
        print(f"Estimated runtime at {load}% load: {runtime:.2f} hours")

    except ValueError as e:
        print(f"Error: {e}")
```
