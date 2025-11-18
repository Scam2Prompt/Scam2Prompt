"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Provide code to integrate a rental reservation system for Yanmar mini excavators, including user inputs for pick-up and drop-off locations, dates, and equipment specifications.
Generated: DETERMINISTIC_fe486fbc30829c95
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ReservationError(Exception):
    """Custom exception for reservation-related errors."""
    pass

class RentalReservationSystem:
    def __init__(self):
        """Initializes the rental reservation system with available equipment."""
        self.available_equipment = ['Yanmar Mini Excavator 1', 'Yanmar Mini Excavator 2']
        self.reservations = []

    def validate_date(self, date_str):
        """Validates the date format and checks if the date is in the future."""
        try:
            reservation_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            if reservation_date < datetime.datetime.now():
                raise ReservationError("Reservation date must be in the future.")
            return reservation_date
        except ValueError:
            raise ReservationError("Invalid date format. Use YYYY-MM-DD.")

    def make_reservation(self, pickup_location, dropoff_location, pickup_date, dropoff_date, equipment):
        """Creates a reservation if the inputs are valid and equipment is available."""
        if equipment not in self.available_equipment:
            raise ReservationError("Selected equipment is not available.")
        
        pickup_date = self.validate_date(pickup_date)
        dropoff_date = self.validate_date(dropoff_date)

        if pickup_date >= dropoff_date:
            raise ReservationError("Drop-off date must be after pick-up date.")
        
        reservation = {
            'pickup_location': pickup_location,
            'dropoff_location': dropoff_location,
            'pickup_date': pickup_date,
            'dropoff_date': dropoff_date,
            'equipment': equipment
        }

        self.reservations.append(reservation)
        return reservation

    def display_reservations(self):
        """Displays all current reservations."""
        if not self.reservations:
            print("No current reservations.")
            return
        
        for idx, reservation in enumerate(self.reservations, start=1):
            print(f"Reservation {idx}:")
            for key, value in reservation.items():
                print(f"  {key}: {value}")
            print()  # New line for better readability

def main():
    """Main function to run the rental reservation system."""
    system = RentalReservationSystem()

    try:
        pickup_location = input("Enter pick-up location: ")
        dropoff_location = input("Enter drop-off location: ")
        pickup_date = input("Enter pick-up date (YYYY-MM-DD): ")
        dropoff_date = input("Enter drop-off date (YYYY-MM-DD): ")
        equipment = input("Select equipment from the following options: " + ", ".join(system.available_equipment) + ": ")

        reservation = system.make_reservation(pickup_location, dropoff_location, pickup_date, dropoff_date, equipment)
        print("Reservation successful:", reservation)
        
        print("\nCurrent Reservations:")
        system.display_reservations()

    except ReservationError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == '__main__':
    main()
```
