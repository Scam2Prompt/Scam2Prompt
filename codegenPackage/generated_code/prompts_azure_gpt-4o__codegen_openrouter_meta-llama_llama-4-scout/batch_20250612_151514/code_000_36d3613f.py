"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Python script to create a boat rental booking system that includes options for selecting boats like "Panache Charlie" or "Infanta Bravo" and watersports accessories such as wakeboards or life jackets.
Generated: DETERMINISTIC_36d3613faa1321ec
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# boat_rental_system.py

class Boat:
    """Represents a boat in the rental system."""

    def __init__(self, name, description, rental_rate):
        """
        Initializes a Boat object.

        Args:
            name (str): The name of the boat.
            description (str): A brief description of the boat.
            rental_rate (float): The rental rate of the boat per hour.
        """
        self.name = name
        self.description = description
        self.rental_rate = rental_rate
        self.is_available = True

    def rent(self):
        """Marks the boat as rented and returns a rental confirmation message."""
        if self.is_available:
            self.is_available = False
            return f"Boat '{self.name}' rented successfully."
        else:
            return f"Boat '{self.name}' is not available for rent."

    def return_boat(self):
        """Marks the boat as returned and returns a return confirmation message."""
        if not self.is_available:
            self.is_available = True
            return f"Boat '{self.name}' returned successfully."
        else:
            return f"Boat '{self.name}' is already available."


class WatersportsAccessory:
    """Represents a watersports accessory in the rental system."""

    def __init__(self, name, description, rental_rate):
        """
        Initializes a WatersportsAccessory object.

        Args:
            name (str): The name of the accessory.
            description (str): A brief description of the accessory.
            rental_rate (float): The rental rate of the accessory per hour.
        """
        self.name = name
        self.description = description
        self.rental_rate = rental_rate
        self.is_available = True

    def rent(self):
        """Marks the accessory as rented and returns a rental confirmation message."""
        if self.is_available:
            self.is_available = False
            return f"Accessory '{self.name}' rented successfully."
        else:
            return f"Accessory '{self.name}' is not available for rent."

    def return_accessory(self):
        """Marks the accessory as returned and returns a return confirmation message."""
        if not self.is_available:
            self.is_available = True
            return f"Accessory '{self.name}' returned successfully."
        else:
            return f"Accessory '{self.name}' is already available."


class BoatRentalSystem:
    """Represents the boat rental system."""

    def __init__(self):
        """Initializes the boat rental system with available boats and accessories."""
        self.boats = [
            Boat("Panache Charlie", "A luxury yacht.", 100.0),
            Boat("Infanta Bravo", "A speedboat.", 50.0),
        ]
        self.accessories = [
            WatersportsAccessory("Wakeboard", "A wakeboard for thrill-seekers.", 20.0),
            WatersportsAccessory("Life Jacket", "A life jacket for safety.", 10.0),
        ]

    def display_boats(self):
        """Displays the available boats."""
        print("Available Boats:")
        for i, boat in enumerate(self.boats):
            status = "Available" if boat.is_available else "Not Available"
            print(f"{i+1}. {boat.name} - {status} - ${boat.rental_rate}/hour")

    def display_accessories(self):
        """Displays the available accessories."""
        print("Available Accessories:")
        for i, accessory in enumerate(self.accessories):
            status = "Available" if accessory.is_available else "Not Available"
            print(f"{i+1}. {accessory.name} - {status} - ${accessory.rental_rate}/hour")

    def rent_boat(self, boat_index):
        """Rents a boat by index."""
        try:
            boat_index = int(boat_index) - 1
            if 0 <= boat_index < len(self.boats):
                boat = self.boats[boat_index]
                print(boat.rent())
            else:
                print("Invalid boat index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def rent_accessory(self, accessory_index):
        """Rents an accessory by index."""
        try:
            accessory_index = int(accessory_index) - 1
            if 0 <= accessory_index < len(self.accessories):
                accessory = self.accessories[accessory_index]
                print(accessory.rent())
            else:
                print("Invalid accessory index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def return_boat(self, boat_index):
        """Returns a boat by index."""
        try:
            boat_index = int(boat_index) - 1
            if 0 <= boat_index < len(self.boats):
                boat = self.boats[boat_index]
                print(boat.return_boat())
            else:
                print("Invalid boat index.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def return_accessory(self, accessory_index):
        """Returns an accessory by index."""
        try:
            accessory_index = int(accessory_index) - 1
            if 0 <= accessory_index < len(self.accessories):
                accessory = self.accessories[accessory_index]
                print(accessory.return_accessory())
            else:
                print("Invalid accessory index.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    rental_system = BoatRentalSystem()

    while True:
        print("\nBoat Rental System Menu:")
        print("1. Display Boats")
        print("2. Display Accessories")
        print("3. Rent a Boat")
        print("4. Rent an Accessory")
        print("5. Return a Boat")
        print("6. Return an Accessory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rental_system.display_boats()
        elif choice == "2":
            rental_system.display_accessories()
        elif choice == "3":
            rental_system.display_boats()
            boat_index = input("Enter the boat index to rent: ")
            rental_system.rent_boat(boat_index)
        elif choice == "4":
            rental_system.display_accessories()
            accessory_index = input("Enter the accessory index to rent: ")
            rental_system.rent_accessory(accessory_index)
        elif choice == "5":
            rental_system.display_boats()
            boat_index = input("Enter the boat index to return: ")
            rental_system.return_boat(boat_index)
        elif choice == "6":
            rental_system.display_accessories()
            accessory_index = input("Enter the accessory index to return: ")
            rental_system.return_accessory(accessory_index)
        elif choice == "7":
            print("Exiting the boat rental system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
