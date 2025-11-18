"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Write a program to manage a "For Sale" section for tractor pulling equipment, similar to the listings for puller tires and mini chassis on jobbo.com.au.
Generated: DETERMINISTIC_f58cd4b323daa9ad
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Equipment:
    """Class to represent a piece of equipment for sale."""
    
    def __init__(self, id, name, description, price, seller_contact):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.seller_contact = seller_contact

    def to_dict(self):
        """Convert the Equipment object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'seller_contact': self.seller_contact
        }

class EquipmentManager:
    """Class to manage the listing of equipment."""
    
    def __init__(self, filename='equipment_listings.json'):
        self.filename = filename
        self.equipments = self.load_listings()

    def load_listings(self):
        """Load equipment listings from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                listings = json.load(file)
                return [Equipment(**item) for item in listings]
        except FileNotFoundError:
            return []  # Return an empty list if file does not exist
        except json.JSONDecodeError as e:
            print(f"Error loading listings: {e}")
            return []

    def save_listings(self):
        """Save current equipment listings to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([equipment.to_dict() for equipment in self.equipments], file, indent=4)
        except IOError as e:
            print(f"Error saving listings: {e}")

    def add_equipment(self, name, description, price, seller_contact):
        """Add a new piece of equipment to the listings."""
        new_id = len(self.equipments) + 1  # Simple ID assignment
        new_equipment = Equipment(new_id, name, description, price, seller_contact)
        self.equipments.append(new_equipment)
        self.save_listings()

    def remove_equipment(self, equipment_id):
        """Remove equipment from the listings by ID."""
        self.equipments = [equipment for equipment in self.equipments if equipment.id != equipment_id]
        self.save_listings()

    def list_equipments(self):
        """Return a list of all equipment for sale."""
        return self.equipments

def main():
    """Main function to interact with the EquipmentManager."""
    manager = EquipmentManager()

    while True:
        print("\nFor Sale Section - Tractor Pulling Equipment")
        print("1. List Equipment")
        print("2. Add Equipment")
        print("3. Remove Equipment")
        print("4. Exit")

        choice = input("Please choose an option: ")

        if choice == '1':
            equipments = manager.list_equipments()
            if equipments:
                for equipment in equipments:
                    print(f"{equipment.id}: {equipment.name} - {equipment.price} AUD")
            else:
                print("No equipment listings available.")

        elif choice == '2':
            name = input("Enter equipment name: ")
            description = input("Enter equipment description: ")
            price = float(input("Enter equipment price (in AUD): "))
            seller_contact = input("Enter seller contact information: ")
            manager.add_equipment(name, description, price, seller_contact)
            print("Equipment added successfully.")

        elif choice == '3':
            equipment_id = int(input("Enter the ID of the equipment to remove: "))
            manager.remove_equipment(equipment_id)
            print("Equipment removed successfully.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
```
