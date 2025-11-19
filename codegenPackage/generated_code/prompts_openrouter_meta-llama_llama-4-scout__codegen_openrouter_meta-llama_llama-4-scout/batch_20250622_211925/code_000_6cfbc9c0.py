"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Write a Python script to calculate insurance premiums for a fleet of vehicles in Mexico, considering factors like vehicle type and coverage level, as offered by GYV Seguros y Fianzas.
Generated: DETERMINISTIC_6cfbc9c0fe475513
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gyv_seguros.py

class Vehicle:
    """Represents a vehicle in the fleet."""

    def __init__(self, vehicle_type, coverage_level, value):
        """
        Initializes a Vehicle instance.

        Args:
            vehicle_type (str): Type of vehicle (e.g., sedan, truck, motorcycle).
            coverage_level (str): Level of coverage (e.g., basic, premium).
            value (float): Value of the vehicle.
        """
        self.vehicle_type = vehicle_type
        self.coverage_level = coverage_level
        self.value = value


class InsurancePremiumCalculator:
    """Calculates insurance premiums for a fleet of vehicles."""

    def __init__(self):
        # Base premium rates for each vehicle type
        self.premium_rates = {
            "sedan": 0.02,
            "truck": 0.035,
            "motorcycle": 0.015
        }

        # Premium rate adjustments for each coverage level
        self.coverage_adjustments = {
            "basic": 1.0,
            "premium": 1.5
        }

        # Additional premium rate for Mexico
        self.mexico_rate = 1.2

    def calculate_premium(self, vehicle):
        """
        Calculates the insurance premium for a vehicle.

        Args:
            vehicle (Vehicle): Vehicle instance.

        Returns:
            float: Calculated premium.

        Raises:
            ValueError: If vehicle type or coverage level is invalid.
        """
        if vehicle.vehicle_type not in self.premium_rates:
            raise ValueError(f"Invalid vehicle type: {vehicle.vehicle_type}")

        if vehicle.coverage_level not in self.coverage_adjustments:
            raise ValueError(f"Invalid coverage level: {vehicle.coverage_level}")

        base_premium = self.premium_rates[vehicle.vehicle_type] * vehicle.value
        adjusted_premium = base_premium * self.coverage_adjustments[vehicle.coverage_level]
        mexico_premium = adjusted_premium * self.mexico_rate

        return mexico_premium


class FleetInsuranceCalculator:
    """Calculates insurance premiums for a fleet of vehicles."""

    def __init__(self):
        self.calculator = InsurancePremiumCalculator()

    def calculate_fleet_premiums(self, vehicles):
        """
        Calculates insurance premiums for a fleet of vehicles.

        Args:
            vehicles (list[Vehicle]): List of Vehicle instances.

        Returns:
            dict: Dictionary with vehicle details and calculated premiums.

        Raises:
            Exception: If an error occurs during premium calculation.
        """
        fleet_premiums = {}

        for vehicle in vehicles:
            try:
                premium = self.calculator.calculate_premium(vehicle)
                fleet_premiums[vehicle.vehicle_type] = {
                    "vehicle_value": vehicle.value,
                    "coverage_level": vehicle.coverage_level,
                    "premium": premium
                }
            except Exception as e:
                print(f"Error calculating premium for {vehicle.vehicle_type}: {str(e)}")

        return fleet_premiums


def main():
    # Example usage
    calculator = FleetInsuranceCalculator()

    vehicles = [
        Vehicle("sedan", "basic", 200000),
        Vehicle("truck", "premium", 500000),
        Vehicle("motorcycle", "basic", 50000)
    ]

    fleet_premiums = calculator.calculate_fleet_premiums(vehicles)

    print("Fleet Premiums:")
    for vehicle_type, premium_info in fleet_premiums.items():
        print(f"Vehicle Type: {vehicle_type}")
        print(f"  Vehicle Value: {premium_info['vehicle_value']}")
        print(f"  Coverage Level: {premium_info['coverage_level']}")
        print(f"  Premium: {premium_info['premium']}")


if __name__ == "__main__":
    main()
```
