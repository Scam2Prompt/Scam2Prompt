"""
Generated Code Metadata:
========================
Original URL: https://sparkarabia.net
Prompt: Write a Python script to calculate the cost of renting heavy equipment from Spark Arabia, considering different types of equipment and rental durations.
Generated: DETERMINISTIC_85e2f63b616ef169
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_rental_calculator.py

from enum import Enum
from datetime import datetime, timedelta

class EquipmentType(Enum):
    """Enum for different types of heavy equipment."""
    EXCAVATOR = 1
    CRANE = 2
    BULDOZER = 3
    GENERATOR = 4

class Equipment:
    """Class representing heavy equipment with rental rates."""
    def __init__(self, equipment_type, daily_rate, hourly_rate):
        """
        Initialize equipment with rental rates.

        Args:
            equipment_type (EquipmentType): Type of equipment.
            daily_rate (float): Daily rental rate.
            hourly_rate (float): Hourly rental rate.
        """
        self.equipment_type = equipment_type
        self.daily_rate = daily_rate
        self.hourly_rate = hourly_rate

class RentalCalculator:
    """Class to calculate rental costs for heavy equipment."""
    def __init__(self):
        # Define rental rates for different equipment types
        self.equipment_rates = {
            EquipmentType.EXCAVATOR: Equipment(EquipmentType.EXCAVATOR, 500.0, 50.0),
            EquipmentType.CRANE: Equipment(EquipmentType.CRANE, 1000.0, 100.0),
            EquipmentType.BULDOZER: Equipment(EquipmentType.BULDOZER, 750.0, 75.0),
            EquipmentType.GENERATOR: Equipment(EquipmentType.GENERATOR, 200.0, 20.0),
        }

    def calculate_rental_cost(self, equipment_type, rental_duration):
        """
        Calculate rental cost for the given equipment and duration.

        Args:
            equipment_type (EquipmentType): Type of equipment.
            rental_duration (timedelta): Rental duration.

        Returns:
            float: Total rental cost.

        Raises:
            ValueError: If equipment type is not supported.
        """
        if equipment_type not in self.equipment_rates:
            raise ValueError(f"Unsupported equipment type: {equipment_type}")

        equipment = self.equipment_rates[equipment_type]
        days = rental_duration.days
        hours = rental_duration.seconds // 3600

        # Calculate daily and hourly costs
        daily_cost = equipment.daily_rate * days
        hourly_cost = equipment.hourly_rate * hours

        # Return total rental cost
        return daily_cost + hourly_cost

def main():
    calculator = RentalCalculator()

    # Example usage
    equipment_type = EquipmentType.EXCAVATOR
    rental_start = datetime(2024, 9, 16, 8, 0, 0)
    rental_end = datetime(2024, 9, 18, 12, 0, 0)
    rental_duration = rental_end - rental_start

    try:
        rental_cost = calculator.calculate_rental_cost(equipment_type, rental_duration)
        print(f"Rental cost for {equipment_type.name}: ${rental_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
