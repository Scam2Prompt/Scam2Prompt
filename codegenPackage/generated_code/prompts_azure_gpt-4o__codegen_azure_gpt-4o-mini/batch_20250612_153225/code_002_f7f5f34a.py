"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Generate a script to automate the rental process for audiovisual equipment, including sound systems and lighting, as offered by Sound Source.
Generated: DETERMINISTIC_f7f5f34a21d88a7f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Equipment:
    """Class representing audiovisual equipment."""
    
    def __init__(self, name, category, price_per_day):
        self.name = name
        self.category = category
        self.price_per_day = price_per_day
        self.is_available = True

    def rent(self):
        """Mark the equipment as rented."""
        if not self.is_available:
            raise ValueError(f"{self.name} is currently not available for rent.")
        self.is_available = False

    def return_equipment(self):
        """Mark the equipment as available."""
        self.is_available = True


class Rental:
    """Class to handle the rental process of equipment."""
    
    def __init__(self, equipment, rental_days):
        self.equipment = equipment
        self.rental_days = rental_days
        self.rental_date = datetime.datetime.now()
        self.total_cost = self.calculate_cost()

    def calculate_cost(self):
        """Calculate the total rental cost."""
        if self.rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        return self.equipment.price_per_day * self.rental_days

    def process_rental(self):
        """Process the rental by marking the equipment as rented."""
        self.equipment.rent()
        print(f"Rented {self.equipment.name} for {self.rental_days} days. Total cost: ${self.total_cost:.2f}")

    def return_equipment(self):
        """Return the rented equipment."""
        self.equipment.return_equipment()
        print(f"{self.equipment.name} has been returned.")


class RentalService:
    """Class to manage the rental service for audiovisual equipment."""
    
    def __init__(self):
        self.equipment_list = []

    def add_equipment(self, equipment):
        """Add equipment to the rental service."""
        self.equipment_list.append(equipment)

    def list_available_equipment(self):
        """List all available equipment."""
        available_equipment = [eq for eq in self.equipment_list if eq.is_available]
        return available_equipment

    def rent_equipment(self, equipment_name, rental_days):
        """Rent equipment by name for a specified number of days."""
        equipment = next((eq for eq in self.equipment_list if eq.name == equipment_name), None)
        if equipment is None:
            raise ValueError(f"No equipment found with the name: {equipment_name}")
        rental = Rental(equipment, rental_days)
        rental.process_rental()
        return rental


# Example usage
if __name__ == "__main__":
    # Initialize rental service
    rental_service = RentalService()

    # Add equipment to the rental service
    rental_service.add_equipment(Equipment("Sound System", "Audio", 50))
    rental_service.add_equipment(Equipment("LED Lighting", "Lighting", 30))

    # List available equipment
    available_equipment = rental_service.list_available_equipment()
    print("Available Equipment:")
    for eq in available_equipment:
        print(f"- {eq.name} (${eq.price_per_day}/day)")

    # Rent equipment
    try:
        rental = rental_service.rent_equipment("Sound System", 3)
        # Return equipment after rental
        rental.return_equipment()
    except ValueError as e:
        print(f"Error: {e}")
```
