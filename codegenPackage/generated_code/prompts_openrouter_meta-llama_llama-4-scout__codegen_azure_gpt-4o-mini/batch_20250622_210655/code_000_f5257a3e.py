"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Write a Python code snippet to calculate the amount of DEF required for a BS-VI diesel engine vehicle equipped with SCR technology.
Generated: DETERMINISTIC_f5257a3ebdf7ac0c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DEFCalculator:
    """
    A class to calculate the amount of Diesel Exhaust Fluid (DEF) required for a BS-VI diesel engine vehicle
    equipped with SCR (Selective Catalytic Reduction) technology.
    """

    def __init__(self, fuel_consumption: float, distance: float):
        """
        Initializes the DEFCalculator with fuel consumption and distance.

        :param fuel_consumption: The fuel consumption of the vehicle in liters per 100 km.
        :param distance: The distance to be traveled in kilometers.
        """
        if fuel_consumption <= 0:
            raise ValueError("Fuel consumption must be greater than zero.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        self.fuel_consumption = fuel_consumption
        self.distance = distance

    def calculate_def(self) -> float:
        """
        Calculates the amount of DEF required based on the fuel consumption and distance.

        The typical DEF consumption rate for BS-VI vehicles is approximately 5% of diesel consumption.

        :return: The amount of DEF required in liters.
        """
        # Calculate total fuel consumed for the given distance
        total_fuel_consumed = (self.fuel_consumption / 100) * self.distance
        
        # Calculate DEF required (5% of total fuel consumed)
        def_required = total_fuel_consumed * 0.05
        
        return def_required

def main():
    """
    Main function to execute the DEF calculation.
    """
    try:
        # Example values for fuel consumption and distance
        fuel_consumption = 8.0  # liters per 100 km
        distance = 500.0  # kilometers

        # Create an instance of DEFCalculator
        def_calculator = DEFCalculator(fuel_consumption, distance)

        # Calculate the DEF required
        def_amount = def_calculator.calculate_def()

        # Output the result
        print(f"Amount of DEF required for {distance} km: {def_amount:.2f} liters")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
