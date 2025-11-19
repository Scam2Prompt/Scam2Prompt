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
import sys

class EquipmentRental:
    """Class to represent the rental of heavy equipment."""

    def __init__(self):
        """Initialize the rental equipment with predefined rates."""
        self.equipment_rates = {
            'excavator': 150,  # Rate per day in currency units
            'bulldozer': 200,
            'crane': 300,
            'loader': 180
        }

    def calculate_rental_cost(self, equipment_type, rental_days):
        """
        Calculate the total rental cost for a given equipment type and duration.

        Args:
            equipment_type (str): The type of equipment to rent.
            rental_days (int): The number of days to rent the equipment.

        Returns:
            float: Total rental cost.

        Raises:
            ValueError: If the equipment type is not available or rental days are invalid.
        """
        if equipment_type not in self.equipment_rates:
            raise ValueError(f"Invalid equipment type: {equipment_type}. Available types: {', '.join(self.equipment_rates.keys())}")

        if rental_days <= 0:
            raise ValueError("Rental days must be a positive integer.")

        rate = self.equipment_rates[equipment_type]
        total_cost = rate * rental_days
        return total_cost

def main():
    """Main function to execute the rental cost calculation."""
    rental_service = EquipmentRental()

    # User input for equipment type and rental duration
    try:
        equipment_type = input("Enter the type of equipment (excavator, bulldozer, crane, loader): ").strip().lower()
        rental_days = int(input("Enter the number of days to rent the equipment: "))

        # Calculate the rental cost
        total_cost = rental_service.calculate_rental_cost(equipment_type, rental_days)
        print(f"The total rental cost for {rental_days} days of {equipment_type} is: {total_cost} currency units.")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
