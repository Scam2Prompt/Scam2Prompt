"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soundsource.tn
Prompt: Generate a script to automate the rental process for audiovisual equipment, including sound systems and lighting, as offered by Sound Source.
Generated: DETERMINISTIC_f7f5f34a21d88a7f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class EquipmentRental:
    """Class to manage the rental process for audiovisual equipment."""
    
    def __init__(self):
        self.equipments = self.load_equipment_data()
        self.rentals = []

    def load_equipment_data(self) -> List[Dict[str, Any]]:
        """Load equipment data from a JSON file."""
        try:
            with open('equipment_data.json', 'r') as file:
                equipment_data = json.load(file)
                return equipment_data
        except FileNotFoundError:
            print("Error: Equipment data file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data.")
            return []

    def display_available_equipments(self) -> None:
        """Display available equipment for rental."""
        print("Available Equipment for Rental:")
        for equipment in self.equipments:
            print(f"{equipment['id']}: {equipment['name']} - ${equipment['daily_rate']} per day")
    
    def rent_equipment(self, equipment_id: int, rental_days: int) -> None:
        """Process equipment rental."""
        equipment = self.find_equipment_by_id(equipment_id)
        if equipment and rental_days > 0:
            total_cost = rental_days * equipment['daily_rate']
            self.rentals.append({
                'equipment': equipment,
                'rental_days': rental_days,
                'total_cost': total_cost
            })
            print(f"Successfully rented {equipment['name']} for {rental_days} days. Total cost: ${total_cost}")
        else:
            print("Error: Invalid equipment ID or rental days.")

    def find_equipment_by_id(self, equipment_id: int) -> Dict[str, Any]:
        """Find equipment by ID."""
        for equipment in self.equipments:
            if equipment['id'] == equipment_id:
                return equipment
        print("Error: Equipment not found.")
        return None

    def return_equipment(self, equipment_id: int) -> None:
        """Process the return of rented equipment."""
        for rental in self.rentals:
            if rental['equipment']['id'] == equipment_id:
                self.rentals.remove(rental)
                print(f"Successfully returned {rental['equipment']['name']}.")
                return
        print("Error: Equipment not found in rentals.")

    def display_rentals(self) -> None:
        """Display current rentals."""
        if not self.rentals:
            print("No current rentals.")
            return
        print("Current Rentals:")
        for rental in self.rentals:
            equipment = rental['equipment']
            print(f"{equipment['name']} - {rental['rental_days']} days, Total cost: ${rental['total_cost']}")

def main():
    rental_service = EquipmentRental()
    rental_service.display_available_equipments()

    # Example process flow
    rental_service.rent_equipment(1, 3)  # Replace with actual equipment_id and days
    rental_service.display_rentals()
    rental_service.return_equipment(1)  # Replace with actual equipment_id
    rental_service.display_rentals()

if __name__ == "__main__":
    main()
```

**Note:** For the code to work as intended, an `equipment_data.json` file with the structure should be provided. An example structure can be:

```json
[
    {"id": 1, "name": "Basic Sound System", "daily_rate": 50},
    {"id": 2, "name": "Advanced Lighting Kit", "daily_rate": 80}
]
```
