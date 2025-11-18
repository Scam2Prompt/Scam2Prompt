"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Write a Python script to simulate an online car rental booking system that includes features like selecting a car, choosing a pickup location, and confirming a booking without requiring a credit card or deposit.
Generated: DETERMINISTIC_b85befe0b2417de2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Car:
    def __init__(self, model, available=True):
        self.model = model
        self.available = available

class Location:
    def __init__(self, name):
        self.name = name

class Booking:
    def __init__(self, car, location, pickup_date, return_date):
        self.car = car
        self.location = location
        self.pickup_date = pickup_date
        self.return_date = return_date

class CarRentalSystem:
    def __init__(self):
        self.cars = [
            Car("Toyota Corolla"),
            Car("Ford Mustang"),
            Car("Chevrolet Camaro")
        ]
        self.locations = [
            Location("Airport"),
            Location("Downtown"),
            Location("Suburb")
        ]
        self.bookings = []

    def display_cars(self):
        print("Available Cars:")
        for idx, car in enumerate(self.cars):
            if car.available:
                print(f"{idx + 1}. {car.model}")

    def display_locations(self):
        print("Pickup Locations:")
        for idx, location in enumerate(self.locations):
            print(f"{idx + 1}. {location.name}")

    def select_car(self, car_index):
        """Selects a car based on the index provided."""
        try:
            car = self.cars[car_index - 1]
            if not car.available:
                raise ValueError("Selected car is not available.")
            return car
        except IndexError:
            raise ValueError("Invalid car selection.")
    
    def select_location(self, location_index):
        """Selects a pickup location based on the index provided."""
        try:
            return self.locations[location_index - 1]
        except IndexError:
            raise ValueError("Invalid location selection.")

    def confirm_booking(self, car, location, pickup_date, return_date):
        """Confirms the booking and updates the car availability."""
        if pickup_date >= return_date:
            raise ValueError("Pickup date must be before return date.")
        
        # Create a new booking
        booking = Booking(car, location, pickup_date, return_date)
        self.bookings.append(booking)
        car.available = False  # Mark the car as not available
        print(f"Booking confirmed for {car.model} at {location.name} from {pickup_date} to {return_date}.")

def main():
    """Main function to run the car rental system."""
    system = CarRentalSystem()
    
    try:
        # Display available cars
        system.display_cars()
        car_choice = int(input("Select the car by number: "))
        selected_car = system.select_car(car_choice)

        # Display pickup locations
        system.display_locations()
        location_choice = int(input("Select the pickup location by number: "))
        selected_location = system.select_location(location_choice)

        # Input pickup and return dates
        pickup_date_str = input("Enter pickup date (YYYY-MM-DD): ")
        return_date_str = input("Enter return date (YYYY-MM-DD): ")
        
        pickup_date = datetime.datetime.strptime(pickup_date_str, "%Y-%m-%d").date()
        return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()
        
        # Confirm booking
        system.confirm_booking(selected_car, selected_location, pickup_date, return_date)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
