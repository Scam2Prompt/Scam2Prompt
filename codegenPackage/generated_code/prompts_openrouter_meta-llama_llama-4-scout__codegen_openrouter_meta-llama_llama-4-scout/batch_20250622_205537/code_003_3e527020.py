"""
Generated Code Metadata:
========================
Original URL: https://musicequipment.site
Prompt: Write a Python script to create a simple music equipment inventory management system.
Generated: DETERMINISTIC_3e527020e40463ae
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# music_equipment_inventory.py

class MusicEquipment:
    def __init__(self, id, name, type, quantity, price):
        """
        Initialize a MusicEquipment object.

        Args:
            id (int): Unique identifier for the equipment.
            name (str): Name of the equipment.
            type (str): Type of the equipment (e.g., guitar, amplifier, etc.).
            quantity (int): Quantity of the equipment in stock.
            price (float): Price of the equipment.
        """
        self.id = id
        self.name = name
        self.type = type
        self.quantity = quantity
        self.price = price

class MusicEquipmentInventory:
    def __init__(self):
        """
        Initialize an empty music equipment inventory.
        """
        self.equipment = {}

    def add_equipment(self, equipment):
        """
        Add a music equipment to the inventory.

        Args:
            equipment (MusicEquipment): The equipment to add.

        Raises:
            ValueError: If the equipment ID already exists in the inventory.
        """
        if equipment.id in self.equipment:
            raise ValueError("Equipment ID already exists in the inventory")
        self.equipment[equipment.id] = equipment

    def remove_equipment(self, id):
        """
        Remove a music equipment from the inventory.

        Args:
            id (int): The ID of the equipment to remove.

        Raises:
            KeyError: If the equipment ID does not exist in the inventory.
        """
        if id not in self.equipment:
            raise KeyError("Equipment ID does not exist in the inventory")
        del self.equipment[id]

    def update_equipment(self, id, **kwargs):
        """
        Update a music equipment in the inventory.

        Args:
            id (int): The ID of the equipment to update.
            **kwargs: The updated attributes.

        Raises:
            KeyError: If the equipment ID does not exist in the inventory.
        """
        if id not in self.equipment:
            raise KeyError("Equipment ID does not exist in the inventory")
        for key, value in kwargs.items():
            setattr(self.equipment[id], key, value)

    def get_equipment(self, id):
        """
        Get a music equipment from the inventory.

        Args:
            id (int): The ID of the equipment to get.

        Returns:
            MusicEquipment: The equipment with the specified ID.

        Raises:
            KeyError: If the equipment ID does not exist in the inventory.
        """
        if id not in self.equipment:
            raise KeyError("Equipment ID does not exist in the inventory")
        return self.equipment[id]

    def list_equipment(self):
        """
        List all music equipment in the inventory.

        Returns:
            list: A list of MusicEquipment objects.
        """
        return list(self.equipment.values())

def main():
    # Create an inventory
    inventory = MusicEquipmentInventory()

    while True:
        print("\nMusic Equipment Inventory Management System")
        print("1. Add equipment")
        print("2. Remove equipment")
        print("3. Update equipment")
        print("4. Get equipment")
        print("5. List equipment")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                id = int(input("Enter equipment ID: "))
                name = input("Enter equipment name: ")
                type = input("Enter equipment type: ")
                quantity = int(input("Enter equipment quantity: "))
                price = float(input("Enter equipment price: "))
                equipment = MusicEquipment(id, name, type, quantity, price)
                inventory.add_equipment(equipment)
                print("Equipment added successfully")
            elif choice == "2":
                id = int(input("Enter equipment ID: "))
                inventory.remove_equipment(id)
                print("Equipment removed successfully")
            elif choice == "3":
                id = int(input("Enter equipment ID: "))
                name = input("Enter new equipment name (press Enter to skip): ")
                type = input("Enter new equipment type (press Enter to skip): ")
                quantity = input("Enter new equipment quantity (press Enter to skip): ")
                price = input("Enter new equipment price (press Enter to skip): ")
                kwargs = {}
                if name:
                    kwargs["name"] = name
                if type:
                    kwargs["type"] = type
                if quantity:
                    kwargs["quantity"] = int(quantity)
                if price:
                    kwargs["price"] = float(price)
                inventory.update_equipment(id, **kwargs)
                print("Equipment updated successfully")
            elif choice == "4":
                id = int(input("Enter equipment ID: "))
                equipment = inventory.get_equipment(id)
                print(f"ID: {equipment.id}")
                print(f"Name: {equipment.name}")
                print(f"Type: {equipment.type}")
                print(f"Quantity: {equipment.quantity}")
                print(f"Price: {equipment.price}")
            elif choice == "5":
                equipment_list = inventory.list_equipment()
                for equipment in equipment_list:
                    print(f"ID: {equipment.id}")
                    print(f"Name: {equipment.name}")
                    print(f"Type: {equipment.type}")
                    print(f"Quantity: {equipment.quantity}")
                    print(f"Price: {equipment.price}")
                    print("------------------------")
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
