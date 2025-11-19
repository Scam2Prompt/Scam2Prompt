"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Develop a pricing calculator for taxi services like Innova Crysta or Swift Desire, considering factors like distance, time, and type of vehicle."
Generated: DETERMINISTIC_c7a0394f597e8789
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class VehicleType(str, Enum):
    """ Enum for different types of vehicles """
    INNOVA_CRYSTA = "Innova Crysta"
    SWIFT_DESIRE = "Swift Desire"

class PricingCalculator:
    """ Pricing calculator for taxi services """

    def __init__(self):
        # Base fares for different types of vehicles
        self.base_fares: Dict[VehicleType, float] = {
            VehicleType.INNOVA_CRYSTA: 100,
            VehicleType.SWIFT_DESIRE: 80
        }

        # Per kilometer rates for different types of vehicles
        self.per_km_rates: Dict[VehicleType, float] = {
            VehicleType.INNOVA_CRYSTA: 10,
            VehicleType.SWIFT_DESIRE: 8
        }

        # Per minute rates for different types of vehicles
        self.per_min_rates: Dict[VehicleType, float] = {
            VehicleType.INNOVA_CRYSTA: 0.25,
            VehicleType.SWIFT_DESIRE: 0.20
        }

    def calculate_price(self, vehicle_type: VehicleType, distance: float, time: float) -> float:
        """
        Calculate the price for a taxi ride

        Args:
        - vehicle_type (VehicleType): The type of vehicle
        - distance (float): The distance traveled in kilometers
        - time (float): The time taken in minutes

        Returns:
        - float: The calculated price
        """
        try:
            # Check if vehicle type is valid
            if vehicle_type not in self.base_fares:
                raise ValueError("Invalid vehicle type")

            # Check if distance and time are non-negative
            if distance < 0 or time < 0:
                raise ValueError("Distance and time must be non-negative")

            # Calculate the price
            base_fare = self.base_fares[vehicle_type]
            km_fare = self.per_km_rates[vehicle_type] * distance
            time_fare = self.per_min_rates[vehicle_type] * time
            total_price = base_fare + km_fare + time_fare

            return total_price

        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def get_vehicle_types(self) -> list:
        """ Get a list of available vehicle types """
        return list(self.base_fares.keys())

def main():
    calculator = PricingCalculator()

    print("Available vehicle types:")
    for i, vehicle_type in enumerate(calculator.get_vehicle_types()):
        print(f"{i+1}. {vehicle_type.value}")

    vehicle_type_choice = int(input("Enter the number of your preferred vehicle type: "))
    vehicle_type = calculator.get_vehicle_types()[vehicle_type_choice - 1]

    distance = float(input("Enter the distance traveled in kilometers: "))
    time = float(input("Enter the time taken in minutes: "))

    price = calculator.calculate_price(vehicle_type, distance, time)
    print(f"The calculated price is: ${price:.2f}")

if __name__ == "__main__":
    main()
```
