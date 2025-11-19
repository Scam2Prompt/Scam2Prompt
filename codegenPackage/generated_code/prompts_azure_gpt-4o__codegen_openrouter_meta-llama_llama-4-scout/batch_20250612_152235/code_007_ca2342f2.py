"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Write a program to calculate freight costs dynamically, incorporating Bin Qutab Logistics' ability to match freight with the right vehicle and route while offering flexibility.
Generated: DETERMINISTIC_ca2342f25bfa4bfe
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# freight_calculator.py

from enum import Enum
from typing import Dict

class VehicleType(str, Enum):
    """Enum for vehicle types."""
    TRUCK = "truck"
    VAN = "van"
    CAR = "car"

class FreightCalculator:
    """Calculates freight costs dynamically."""

    def __init__(self, 
                 base_rates: Dict[VehicleType, float], 
                 distance_rates: Dict[VehicleType, float], 
                 fuel_surcharge: float):
        """
        Initializes the freight calculator.

        Args:
        - base_rates (Dict[VehicleType, float]): Base rates for each vehicle type.
        - distance_rates (Dict[VehicleType, float]): Distance-based rates for each vehicle type.
        - fuel_surcharge (float): Fuel surcharge percentage.
        """
        self.base_rates = base_rates
        self.distance_rates = distance_rates
        self.fuel_surcharge = fuel_surcharge

    def calculate_freight_cost(self, 
                              vehicle_type: VehicleType, 
                              weight: float, 
                              distance: float, 
                              fuel_price: float) -> float:
        """
        Calculates the freight cost.

        Args:
        - vehicle_type (VehicleType): Type of vehicle.
        - weight (float): Weight of the freight in kg.
        - distance (float): Distance of the route in km.
        - fuel_price (float): Current fuel price per liter.

        Returns:
        - float: Calculated freight cost.
        """
        # Validate inputs
        if vehicle_type not in self.base_rates:
            raise ValueError("Invalid vehicle type")

        if weight <= 0:
            raise ValueError("Weight must be greater than zero")

        if distance <= 0:
            raise ValueError("Distance must be greater than zero")

        if fuel_price < 0:
            raise ValueError("Fuel price cannot be negative")

        # Calculate base cost
        base_cost = self.base_rates[vehicle_type]

        # Calculate distance-based cost
        distance_cost = self.distance_rates[vehicle_type] * distance

        # Calculate fuel cost
        fuel_cost = self.calculate_fuel_cost(vehicle_type, distance, fuel_price)

        # Calculate total cost with fuel surcharge
        total_cost = (base_cost + distance_cost + fuel_cost) * (1 + self.fuel_surcharge / 100)

        # Apply weight-based surcharge
        total_cost *= self.calculate_weight_surcharge(weight)

        return total_cost

    def calculate_fuel_cost(self, 
                           vehicle_type: VehicleType, 
                           distance: float, 
                           fuel_price: float) -> float:
        """
        Calculates the fuel cost.

        Args:
        - vehicle_type (VehicleType): Type of vehicle.
        - distance (float): Distance of the route in km.
        - fuel_price (float): Current fuel price per liter.

        Returns:
        - float: Calculated fuel cost.
        """
        # Assume fuel consumption rates in liters per km
        fuel_consumption_rates = {
            VehicleType.TRUCK: 0.2,
            VehicleType.VAN: 0.15,
            VehicleType.CAR: 0.1
        }

        fuel_consumption = fuel_consumption_rates[vehicle_type]
        fuel_cost = distance * fuel_consumption * fuel_price
        return fuel_cost

    def calculate_weight_surcharge(self, weight: float) -> float:
        """
        Calculates the weight-based surcharge.

        Args:
        - weight (float): Weight of the freight in kg.

        Returns:
        - float: Weight-based surcharge factor.
        """
        # Assume weight-based surcharge is 1% per 100 kg
        weight_surcharge = 1 + (weight / 100) * 0.01
        return weight_surcharge


def main():
    # Example usage
    base_rates = {
        VehicleType.TRUCK: 100,
        VehicleType.VAN: 50,
        VehicleType.CAR: 20
    }

    distance_rates = {
        VehicleType.TRUCK: 0.5,
        VehicleType.VAN: 0.3,
        VehicleType.CAR: 0.2
    }

    fuel_surcharge = 10  # 10%

    calculator = FreightCalculator(base_rates, distance_rates, fuel_surcharge)

    vehicle_type = VehicleType.TRUCK
    weight = 500  # kg
    distance = 100  # km
    fuel_price = 1.5  # per liter

    try:
        freight_cost = calculator.calculate_freight_cost(vehicle_type, weight, distance, fuel_price)
        print(f"Freight cost: ${freight_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
