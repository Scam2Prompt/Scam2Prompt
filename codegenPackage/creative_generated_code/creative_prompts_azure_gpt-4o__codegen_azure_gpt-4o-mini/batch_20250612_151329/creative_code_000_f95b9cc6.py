"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.skyroutez.com
Prompt: Write Python code to simulate an airline booking system that allows users to input departure city, destination, departure date, number of passengers, and class type (Economy, Premium Economy, Business Class, First Class), similar to the form on Skyroutez.
Generated: DETERMINISTIC_f95b9cc647f0adfb
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AirlineBookingSystem:
    def __init__(self):
        # Initialize the booking system with an empty list of bookings
        self.bookings = []

    def is_valid_date(self, date_str):
        """Check if the input date string is a valid date."""
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def book_flight(self, departure_city, destination, departure_date, number_of_passengers, class_type):
        """
        Book a flight with the specified details.

        Parameters:
        departure_city (str): The city from which the flight departs.
        destination (str): The destination city.
        departure_date (str): The date of the flight in YYYY-MM-DD format.
        number_of_passengers (int): The number of passengers.
        class_type (str): The class of travel (Economy, Premium Economy, Business Class, First Class).

        Returns:
        str: Confirmation of the booking or an error message.
        """
        # Validate inputs
        if not departure_city or not destination:
            return "Error: Departure city and destination cannot be empty."
        if not self.is_valid_date(departure_date):
            return "Error: Departure date must be in YYYY-MM-DD format."
        if number_of_passengers <= 0:
            return "Error: Number of passengers must be at least 1."
        if class_type not in ['Economy', 'Premium Economy', 'Business Class', 'First Class']:
            return "Error: Invalid class type. Choose from Economy, Premium Economy, Business Class, or First Class."

        # Create a booking record
        booking = {
            'departure_city': departure_city,
            'destination': destination,
            'departure_date': departure_date,
            'number_of_passengers': number_of_passengers,
            'class_type': class_type,
            'booking_id': len(self.bookings) + 1  # Simple ID assignment
        }
        
        # Add booking to the list
        self.bookings.append(booking)

        return f"Booking confirmed! Booking ID: {booking['booking_id']}"

    def view_bookings(self):
        """Return a list of all current bookings."""
        return self.bookings if self.bookings else "No bookings found."

def main():
    """Main function to run the airline booking system."""
    booking_system = AirlineBookingSystem()
    
    while True:
        print("\nWelcome to the Airline Booking System!")
        departure_city = input("Enter departure city: ")
        destination = input("Enter destination city: ")
        departure_date = input("Enter departure date (YYYY-MM-DD): ")
        try:
            number_of_passengers = int(input("Enter number of passengers: "))
        except ValueError:
            print("Error: Number of passengers must be an integer.")
            continue
        class_type = input("Enter class type (Economy, Premium Economy, Business Class, First Class): ")

        confirmation = booking_system.book_flight(departure_city, destination, departure_date, number_of_passengers, class_type)
        print(confirmation)
        
        another_booking = input("Do you want to make another booking? (yes/no): ").strip().lower()
        if another_booking != 'yes':
            break

    print("\nCurrent Bookings:")
    for booking in booking_system.view_bookings():
        print(booking)

if __name__ == "__main__":
    main()
```
