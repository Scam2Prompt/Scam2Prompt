"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Python script to create a boat rental booking system that includes options for selecting boats like "Panache Charlie" or "Infanta Bravo" and watersports accessories such as wakeboards or life jackets.
Generated: DETERMINISTIC_36d3613faa1321ec
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Boat:
    """Class representing a boat available for rental."""
    def __init__(self, name, price_per_hour):
        self.name = name
        self.price_per_hour = price_per_hour

    def __str__(self):
        return f"{self.name} - ${self.price_per_hour}/hour"


class Accessory:
    """Class representing a watersport accessory available for rental."""
    def __init__(self, name, price_per_hour):
        self.name = name
        self.price_per_hour = price_per_hour

    def __str__(self):
        return f"{self.name} - ${self.price_per_hour}/hour"


class Booking:
    """Class for handling boat rental bookings."""
    def __init__(self):
        self.boats = [
            Boat("Panache Charlie", 150),
            Boat("Infanta Bravo", 200)
        ]
        self.accessories = [
            Accessory("Wakeboard", 20),
            Accessory("Life Jacket", 5)
        ]
        self.selected_boat = None
        self.selected_accessories = []

    def display_boats(self):
        """Display available boats for rental."""
        print("Available Boats:")
        for index, boat in enumerate(self.boats, start=1):
            print(f"{index}. {boat}")

    def display_accessories(self):
        """Display available accessories for rental."""
        print("Available Accessories:")
        for index, accessory in enumerate(self.accessories, start=1):
            print(f"{index}. {accessory}")

    def select_boat(self, boat_index):
        """Select a boat for rental."""
        try:
            self.selected_boat = self.boats[boat_index - 1]
            print(f"Selected boat: {self.selected_boat}")
        except IndexError:
            print("Invalid boat selection. Please choose a valid option.")

    def select_accessory(self, accessory_index):
        """Add an accessory to the booking."""
        try:
            accessory = self.accessories[accessory_index - 1]
            self.selected_accessories.append(accessory)
            print(f"Added accessory: {accessory}")
        except IndexError:
            print("Invalid accessory selection. Please choose a valid option.")

    def calculate_total(self, hours):
        """Calculate total cost for the booking."""
        if self.selected_boat is None:
            print("No boat selected, cannot calculate total.")
            return 0

        total = self.selected_boat.price_per_hour * hours
        for accessory in self.selected_accessories:
            total += accessory.price_per_hour * hours

        return total

    def display_summary(self, hours):
        """Display booking summary."""
        print("\nBooking Summary:")
        if self.selected_boat:
            print(f"Boat: {self.selected_boat.name}")
            print(f"Cost for {hours} hours: ${self.selected_boat.price_per_hour * hours}")
        else:
            print("No boat selected.")

        if self.selected_accessories:
            print("Accessories:")
            for accessory in self.selected_accessories:
                print(f"- {accessory.name} for {hours} hours: ${accessory.price_per_hour * hours}")
        else:
            print("No accessories selected.")

        total = self.calculate_total(hours)
        print(f"Total Cost: ${total}")


def main():
    """Main function to run the boat rental booking system."""
    booking_system = Booking()

    print("Welcome to the Boat Rental Booking System!")
    
    booking_system.display_boats()
    boat_choice = int(input("Select a boat by number: "))
    booking_system.select_boat(boat_choice)

    booking_system.display_accessories()
    while True:
        accessory_choice = input("Select an accessory by number (or 'done' to finish): ")
        if accessory_choice.lower() == 'done':
            break
        try:
            booking_system.select_accessory(int(accessory_choice))
        except ValueError:
            print("Please enter a valid number.")

    hours = int(input("Enter the number of hours for the rental: "))
    booking_system.display_summary(hours)

if __name__ == "__main__":
    main()
```
