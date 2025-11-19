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
class Vehicle:
    """Base class for all vehicles in the rental system."""
    
    def __init__(self, vehicle_type, daily_rate):
        self.vehicle_type = vehicle_type
        self.daily_rate = daily_rate

    def get_daily_rate(self):
        """Return the daily rental rate of the vehicle."""
        return self.daily_rate


class Compact(Vehicle):
    """Class representing a compact vehicle."""
    
    def __init__(self):
        super().__init__('Compact', 45)


class Crossover(Vehicle):
    """Class representing a crossover vehicle."""
    
    def __init__(self):
        super().__init__('Crossover', 60)


class SUV(Vehicle):
    """Class representing an SUV vehicle."""
    
    def __init__(self):
        super().__init__('SUV', 75)


class CarRentalSystem:
    """Class to manage the car rental system."""
    
    def __init__(self):
        self.fleet = {
            'compact': Compact(),
            'crossover': Crossover(),
            'suv': SUV()
        }
        self.rented_vehicles = {}

    def display_fleet(self):
        """Display available vehicles and their rates."""
        print("Available Vehicles:")
        for vehicle in self.fleet.values():
            print(f"{vehicle.vehicle_type}: ${vehicle.get_daily_rate()} per day")

    def rent_vehicle(self, vehicle_type, days):
        """Rent a vehicle for a specified number of days."""
        if vehicle_type not in self.fleet:
            raise ValueError("Vehicle type not available.")
        
        if days <= 0:
            raise ValueError("Number of rental days must be greater than zero.")
        
        vehicle = self.fleet[vehicle_type]
        total_cost = vehicle.get_daily_rate() * days
        self.rented_vehicles[vehicle_type] = days
        print(f"Rented {vehicle_type} for {days} days. Total cost: ${total_cost}")

    def return_vehicle(self, vehicle_type):
        """Return a rented vehicle."""
        if vehicle_type not in self.rented_vehicles:
            raise ValueError("This vehicle was not rented.")
        
        del self.rented_vehicles[vehicle_type]
        print(f"{vehicle_type} has been returned.")


def main():
    """Main function to run the car rental system."""
    rental_system = CarRentalSystem()
    
    while True:
        print("\n--- Car Rental System ---")
        rental_system.display_fleet()
        
        action = input("Would you like to rent or return a vehicle? (rent/return/exit): ").strip().lower()
        
        if action == 'rent':
            vehicle_type = input("Enter vehicle type (compact/crossover/suv): ").strip().lower()
            try:
                days = int(input("Enter number of rental days: "))
                rental_system.rent_vehicle(vehicle_type, days)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif action == 'return':
            vehicle_type = input("Enter vehicle type to return: ").strip().lower()
            try:
                rental_system.return_vehicle(vehicle_type)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif action == 'exit':
            print("Exiting the car rental system. Thank you!")
            break
        
        else:
            print("Invalid action. Please choose rent, return, or exit.")


if __name__ == "__main__":
    main()
```
