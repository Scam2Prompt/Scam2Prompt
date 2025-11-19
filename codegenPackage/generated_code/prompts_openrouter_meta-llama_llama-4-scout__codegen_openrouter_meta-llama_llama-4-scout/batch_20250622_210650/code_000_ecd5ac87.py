"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Write a Python script to manage an inventory of medicinal plants, including tracking plant species, quantities, and uses, inspired by Oromaticas' agroecological approach."
Generated: DETERMINISTIC_ecd5ac87d04f56bc
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# medicinal_plant_inventory.py

class MedicinalPlant:
    """Represents a medicinal plant with its species, quantity, and uses."""

    def __init__(self, species, quantity, uses=None):
        """
        Initializes a MedicinalPlant instance.

        Args:
            species (str): The plant species.
            quantity (int): The quantity of the plant.
            uses (list[str], optional): The uses of the plant. Defaults to None.
        """
        self.species = species
        self.quantity = quantity
        self.uses = uses if uses else []

    def add_use(self, use):
        """Adds a use to the plant."""
        self.uses.append(use)

    def remove_use(self, use):
        """Removes a use from the plant."""
        if use in self.uses:
            self.uses.remove(use)

    def update_quantity(self, quantity):
        """Updates the quantity of the plant."""
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Quantity must be non-negative")

    def __str__(self):
        return f"{self.species} - Quantity: {self.quantity}, Uses: {', '.join(self.uses)}"


class MedicinalPlantInventory:
    """Manages an inventory of medicinal plants."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.plants = {}

    def add_plant(self, plant):
        """
        Adds a plant to the inventory.

        Args:
            plant (MedicinalPlant): The plant to add.
        """
        self.plants[plant.species] = plant

    def remove_plant(self, species):
        """
        Removes a plant from the inventory.

        Args:
            species (str): The species of the plant to remove.
        """
        if species in self.plants:
            del self.plants[species]

    def get_plant(self, species):
        """
        Retrieves a plant from the inventory.

        Args:
            species (str): The species of the plant to retrieve.

        Returns:
            MedicinalPlant: The plant instance or None if not found.
        """
        return self.plants.get(species)

    def update_plant_quantity(self, species, quantity):
        """
        Updates the quantity of a plant in the inventory.

        Args:
            species (str): The species of the plant to update.
            quantity (int): The new quantity.
        """
        plant = self.get_plant(species)
        if plant:
            plant.update_quantity(quantity)

    def __str__(self):
        inventory_str = "Medicinal Plant Inventory:\n"
        for plant in self.plants.values():
            inventory_str += f"- {plant}\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = MedicinalPlantInventory()

    while True:
        print("\n1. Add plant")
        print("2. Remove plant")
        print("3. Update plant quantity")
        print("4. Get plant info")
        print("5. List all plants")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                species = input("Enter plant species: ")
                quantity = int(input("Enter plant quantity: "))
                uses = input("Enter plant uses (comma-separated): ").split(',')
                uses = [use.strip() for use in uses]
                plant = MedicinalPlant(species, quantity, uses)
                inventory.add_plant(plant)
            elif choice == "2":
                species = input("Enter plant species to remove: ")
                inventory.remove_plant(species)
            elif choice == "3":
                species = input("Enter plant species to update: ")
                quantity = int(input("Enter new quantity: "))
                inventory.update_plant_quantity(species, quantity)
            elif choice == "4":
                species = input("Enter plant species to retrieve: ")
                plant = inventory.get_plant(species)
                if plant:
                    print(plant)
                else:
                    print("Plant not found")
            elif choice == "5":
                print(inventory)
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose again.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
