"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Generate code to calculate the fuel consumption of an MG car model (e.g., NSE 1.5L engine with 5.3L/100km) over a given distance in kilometers.
Generated: DETERMINISTIC_b6c9e18abfd8dcaf
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FuelConsumptionCalculator:
    """
    A class to calculate fuel consumption for an MG car model.

    Attributes:
        fuel_consumption_per_100km (float): Fuel consumption in liters per 100 km.
    """

    def __init__(self, fuel_consumption_per_100km):
        """
        Initializes the FuelConsumptionCalculator with the specified fuel consumption.

        Args:
            fuel_consumption_per_100km (float): Fuel consumption in liters per 100 km.
        
        Raises:
            ValueError: If fuel_consumption_per_100km is negative.
        """
        if fuel_consumption_per_100km < 0:
            raise ValueError("Fuel consumption must be a non-negative value.")
        self.fuel_consumption_per_100km = fuel_consumption_per_100km

    def calculate_fuel_consumed(self, distance_km):
        """
        Calculates the fuel consumed over a given distance.

        Args:
            distance_km (float): The distance traveled in kilometers.
        
        Returns:
            float: The amount of fuel consumed in liters.

        Raises:
            ValueError: If distance_km is negative.
        """
        if distance_km < 0:
            raise ValueError("Distance must be a non-negative value.")
        
        # Calculate fuel consumed based on distance and fuel consumption rate
        fuel_consumed = (distance_km / 100) * self.fuel_consumption_per_100km
        return fuel_consumed


def main():
    """
    Main function to execute the fuel consumption calculation.
    """
    # Create a FuelConsumptionCalculator instance for an MG car with a specified fuel consumption rate
    mg_fuel_calculator = FuelConsumptionCalculator(fuel_consumption_per_100km=5.3)

    # Example distance input
    distance_km = 150  # Distance in kilometers

    try:
        # Calculate fuel consumed for the given distance
        fuel_used = mg_fuel_calculator.calculate_fuel_consumed(distance_km)
        print(f"Fuel consumed for {distance_km} km: {fuel_used:.2f} liters")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
