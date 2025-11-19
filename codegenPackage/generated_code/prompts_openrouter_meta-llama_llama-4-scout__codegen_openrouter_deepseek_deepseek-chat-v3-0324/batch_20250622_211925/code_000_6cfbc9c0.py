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
from enum import Enum
from typing import Dict, List, Optional

class VehicleType(Enum):
    """Enum representing different vehicle types."""
    SEDAN = "sedan"
    SUV = "suv"
    PICKUP = "pickup"
    TRUCK = "truck"
    MOTORCYCLE = "motorcycle"

class CoverageLevel(Enum):
    """Enum representing different coverage levels."""
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"

class InsuranceCalculator:
    """Class to calculate insurance premiums for a fleet of vehicles."""

    # Base premium rates per vehicle type (in MXN)
    BASE_RATES = {
        VehicleType.SEDAN: 5000,
        VehicleType.SUV: 7000,
        VehicleType.PICKUP: 6500,
        VehicleType.TRUCK: 10000,
        VehicleType.MOTORCYCLE: 3000
    }

    # Coverage multipliers
    COVERAGE_MULTIPLIERS = {
        CoverageLevel.BASIC: 1.0,
        CoverageLevel.STANDARD: 1.5,
        CoverageLevel.PREMIUM: 2.0
    }

    def __init__(self):
        """Initialize the calculator with default rates."""
        self.vehicle_data = []

    def add_vehicle(self, vehicle_type: VehicleType, coverage_level: CoverageLevel) -> None:
        """Add a vehicle to the fleet for premium calculation.
        
        Args:
            vehicle_type: Type of the vehicle (from VehicleType enum)
            coverage_level: Desired coverage level (from CoverageLevel enum)
        """
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type")
        if not isinstance(coverage_level, CoverageLevel):
            raise ValueError("Invalid coverage level")

        self.vehicle_data.append({
            "vehicle_type": vehicle_type,
            "coverage_level": coverage_level
        })

    def calculate_premium(self, vehicle_type: VehicleType, coverage_level: CoverageLevel) -> float:
        """Calculate premium for a single vehicle.
        
        Args:
            vehicle_type: Type of the vehicle
            coverage_level: Desired coverage level
            
        Returns:
            Calculated premium amount in MXN
        """
        base_rate = self.BASE_RATES.get(vehicle_type)
        if base_rate is None:
            raise ValueError("Unsupported vehicle type")

        multiplier = self.COVERAGE_MULTIPLIERS.get(coverage_level)
        if multiplier is None:
            raise ValueError("Unsupported coverage level")

        return base_rate * multiplier

    def calculate_fleet_premium(self) -> Dict[str, float]:
        """Calculate total premium for all vehicles in the fleet.
        
        Returns:
            Dictionary with total premium and individual premiums
        """
        if not self.vehicle_data:
            raise ValueError("No vehicles in the fleet")

        total_premium = 0.0
        individual_premiums = []

        for vehicle in self.vehicle_data:
            premium = self.calculate_premium(
                vehicle["vehicle_type"],
                vehicle["coverage_level"]
            )
            total_premium += premium
            individual_premiums.append({
                "vehicle_type": vehicle["vehicle_type"].value,
                "coverage_level": vehicle["coverage_level"].value,
                "premium": premium
            })

        return {
            "total_premium": total_premium,
            "individual_premiums": individual_premiums
        }

    def save_to_json(self, filename: str) -> None:
        """Save fleet data and premiums to a JSON file.
        
        Args:
            filename: Path to the output JSON file
        """
        try:
            fleet_data = self.calculate_fleet_premium()
            with open(filename, 'w') as f:
                json.dump(fleet_data, f, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save to JSON: {str(e)}")

    def load_from_json(self, filename: str) -> None:
        """Load fleet data from a JSON file.
        
        Args:
            filename: Path to the input JSON file
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.vehicle_data = []
                for vehicle in data.get("individual_premiums", []):
                    self.add_vehicle(
                        VehicleType(vehicle["vehicle_type"]),
                        CoverageLevel(vehicle["coverage_level"])
                    )
        except Exception as e:
            raise IOError(f"Failed to load from JSON: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        calculator = InsuranceCalculator()
        
        # Add vehicles to the fleet
        calculator.add_vehicle(VehicleType.SEDAN, CoverageLevel.STANDARD)
        calculator.add_vehicle(VehicleType.SUV, CoverageLevel.PREMIUM)
        calculator.add_vehicle(VehicleType.PICKUP, CoverageLevel.BASIC)
        
        # Calculate and print fleet premium
        fleet_premium = calculator.calculate_fleet_premium()
        print("Fleet Premium Calculation:")
        print(json.dumps(fleet_premium, indent=4))
        
        # Save to JSON
        calculator.save_to_json("fleet_premiums.json")
        print("Data saved to fleet_premiums.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
