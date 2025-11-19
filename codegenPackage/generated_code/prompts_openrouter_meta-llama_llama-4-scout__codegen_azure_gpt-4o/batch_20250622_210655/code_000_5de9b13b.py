"""
Generated Code Metadata:
========================
Original URL: https://www.reliableridesllc.org
Prompt: Write a Python script to create a simple car rental system with a fleet of vehicles, including compact, crossover, and SUV options, with prices starting from $45 per day.
Generated: DETERMINISTIC_5de9b13bead180ee
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class Vehicle:
    """
    Represents a vehicle in the car rental system.
    """
    def __init__(self, vehicle_type, daily_rate, available=True):
        self.vehicle_type = vehicle_type
        self.daily_rate = daily_rate
        self.available = available

    def __str__(self):
        return f"{self.vehicle_type} - ${self.daily_rate}/day - {'Available' if self.available else 'Rented'}"


class CarRentalSystem:
    """
    Represents the car rental system, managing a fleet of vehicles.
    """
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle):
        """
        Adds a vehicle to the fleet.
        """
        self.fleet.append(vehicle)

    def display_available_vehicles(self):
        """
        Displays all available vehicles in the fleet.
        """
        print("\nAvailable Vehicles:")
        for idx, vehicle in enumerate(self.fleet):
            if vehicle.available:
                print(f"{idx + 1}. {vehicle}")
        print()

    def rent_vehicle(self, vehicle_index, rental_days):
        """
        Rents a vehicle if it is available.
        """
        try:
            vehicle = self.fleet[vehicle_index - 1]
            if vehicle.available:
                total_cost = vehicle.daily_rate * rental_days
                vehicle.available = False
                print(f"\nYou have rented a {vehicle.vehicle_type} for {rental_days} days.")
                print(f"Total cost: ${total_cost}\n")
            else:
                print("\nSorry, this vehicle is already rented.\n")
        except IndexError:
            print("\nInvalid vehicle selection. Please try again.\n")
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

    def return_vehicle(self, vehicle_index):
        """
        Returns a rented vehicle back to the fleet.
        """
        try:
            vehicle = self.fleet[vehicle_index - 1]
            if not vehicle.available:
                vehicle.available = True
                print(f"\nYou have successfully returned the {vehicle.vehicle_type}.\n")
            else:
                print("\nThis vehicle is already available.\n")
        except IndexError:
            print("\nInvalid vehicle selection. Please try again.\n")
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


def main():
    """
    Main function to run the car rental system.
    """
    # Initialize the car rental system
    rental_system = CarRentalSystem()

    # Add vehicles to the fleet
    rental_system.add_vehicle(Vehicle("Compact", 45))
    rental_system.add_vehicle(Vehicle("Crossover", 60))
    rental_system.add_vehicle(Vehicle("SUV", 75))

    while True:
        print("Car Rental System")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            rental_system.display_available_vehicles()
        elif choice == "2":
            rental_system.display_available_vehicles()
            try:
                vehicle_index = int(input("Enter the vehicle number to rent: "))
                rental_days = int(input("Enter the number of days to rent: "))
                rental_system.rent_vehicle(vehicle_index, rental_days)
            except ValueError:
                print("\nInvalid input. Please enter numeric values.\n")
        elif choice == "3":
            rental_system.display_available_vehicles()
            try:
                vehicle_index = int(input("Enter the vehicle number to return: "))
                rental_system.return_vehicle(vehicle_index)
            except ValueError:
                print("\nInvalid input. Please enter numeric values.\n")
        elif choice == "4":
            print("\nThank you for using the Car Rental System. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
```
