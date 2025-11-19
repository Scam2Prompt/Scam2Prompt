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
import json

class Vehicle:
    """Class representing a vehicle in the fleet."""
    
    def __init__(self, vehicle_type, base_value, coverage_level):
        """
        Initialize a Vehicle instance.

        :param vehicle_type: Type of the vehicle (e.g., 'car', 'truck', 'motorcycle').
        :param base_value: Base value of the vehicle for premium calculation.
        :param coverage_level: Level of coverage (e.g., 'basic', 'standard', 'premium').
        """
        self.vehicle_type = vehicle_type
        self.base_value = base_value
        self.coverage_level = coverage_level

    def calculate_premium(self):
        """
        Calculate the insurance premium based on vehicle type and coverage level.

        :return: Calculated premium amount.
        """
        # Define base rates for different vehicle types
        base_rates = {
            'car': 0.05,
            'truck': 0.07,
            'motorcycle': 0.04
        }

        # Define coverage multipliers
        coverage_multipliers = {
            'basic': 1.0,
            'standard': 1.5,
            'premium': 2.0
        }

        # Get the base rate for the vehicle type
        base_rate = base_rates.get(self.vehicle_type.lower())
        if base_rate is None:
            raise ValueError(f"Invalid vehicle type: {self.vehicle_type}")

        # Get the coverage multiplier
        coverage_multiplier = coverage_multipliers.get(self.coverage_level.lower())
        if coverage_multiplier is None:
            raise ValueError(f"Invalid coverage level: {self.coverage_level}")

        # Calculate the premium
        premium = self.base_value * base_rate * coverage_multiplier
        return premium


class FleetInsurance:
    """Class to manage a fleet of vehicles and calculate total insurance premiums."""
    
    def __init__(self):
        """Initialize an empty list to hold vehicles."""
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Add a vehicle to the fleet.

        :param vehicle: Vehicle instance to be added.
        """
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Expected a Vehicle instance.")
        self.vehicles.append(vehicle)

    def calculate_total_premium(self):
        """
        Calculate the total insurance premium for the fleet.

        :return: Total premium amount for all vehicles in the fleet.
        """
        total_premium = 0.0
        for vehicle in self.vehicles:
            total_premium += vehicle.calculate_premium()
        return total_premium


def main():
    """Main function to execute the insurance premium calculation."""
    fleet_insurance = FleetInsurance()

    # Example vehicle data (could be loaded from a database or API)
    vehicle_data = [
        {"vehicle_type": "car", "base_value": 20000, "coverage_level": "standard"},
        {"vehicle_type": "truck", "base_value": 30000, "coverage_level": "premium"},
        {"vehicle_type": "motorcycle", "base_value": 15000, "coverage_level": "basic"},
    ]

    # Add vehicles to the fleet
    for data in vehicle_data:
        try:
            vehicle = Vehicle(data['vehicle_type'], data['base_value'], data['coverage_level'])
            fleet_insurance.add_vehicle(vehicle)
        except (ValueError, TypeError) as e:
            print(f"Error adding vehicle: {e}")

    # Calculate and display the total premium
    total_premium = fleet_insurance.calculate_total_premium()
    print(f"Total Insurance Premium for the Fleet: ${total_premium:.2f}")


if __name__ == "__main__":
    main()
```
