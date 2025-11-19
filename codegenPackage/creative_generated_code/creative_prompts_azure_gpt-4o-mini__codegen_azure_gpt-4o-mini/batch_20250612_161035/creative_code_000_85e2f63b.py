"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkarabia.net
Prompt: Write a Python script to calculate the cost of renting heavy equipment from Spark Arabia, considering different types of equipment and rental durations.
Generated: DETERMINISTIC_85e2f63b616ef169
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EquipmentRentalService:
    """A class to manage the rental of heavy equipment."""

    def __init__(self):
        """Initialize the rental service with equipment data."""
        self.equipment_data = {
            "excavator": {"daily_rate": 300, "weekly_rate": 1500, "monthly_rate": 6000},
            "bulldozer": {"daily_rate": 350, "weekly_rate": 1750, "monthly_rate": 7000},
            "crane": {"daily_rate": 500, "weekly_rate": 2500, "monthly_rate": 10000}
        }

    def calculate_rental_cost(self, equipment_type, rental_duration, duration_unit):
        """
        Calculate the total rental cost based on equipment type and duration.

        :param equipment_type: Type of equipment to rent (str)
        :param rental_duration: Duration for which the equipment is rented (int)
        :param duration_unit: Unit of duration ('daily', 'weekly', or 'monthly') (str)
        :return: Total cost for the rental (float)
        :raises ValueError: If the equipment type or duration unit is invalid
        """
        if equipment_type not in self.equipment_data:
            raise ValueError(f"Invalid equipment type: {equipment_type}")
        if duration_unit not in ['daily', 'weekly', 'monthly']:
            raise ValueError(f"Invalid duration unit: {duration_unit}")

        rates = self.equipment_data[equipment_type]
        if duration_unit == 'daily':
            cost = rates['daily_rate'] * rental_duration
        elif duration_unit == 'weekly':
            cost = rates['weekly_rate'] * rental_duration
        elif duration_unit == 'monthly':
            cost = rates['monthly_rate'] * rental_duration

        return cost

    def display_equipment_list(self):
        """Display the available equipment and their rental rates."""
        print("Available Equipment for Rent:")
        for equipment, rates in self.equipment_data.items():
            print(f"{equipment.capitalize()}: Daily Rate: ${rates['daily_rate']}, "
                  f"Weekly Rate: ${rates['weekly_rate']}, Monthly Rate: ${rates['monthly_rate']}")

def main():
    """Main function to execute the rental cost calculation."""
    rental_service = EquipmentRentalService()
    
    # Display available equipment
    rental_service.display_equipment_list()

    # User input for rental calculation
    try:
        equipment_type = input("Enter the type of equipment you want to rent: ").strip().lower()
        rental_duration = int(input("Enter the rental duration: "))
        duration_unit = input("Enter the duration unit (daily, weekly, monthly): ").strip().lower()
        
        total_cost = rental_service.calculate_rental_cost(equipment_type, rental_duration, duration_unit)
        print(f"The total cost for renting a {equipment_type} for {rental_duration} {duration_unit}(s) is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
