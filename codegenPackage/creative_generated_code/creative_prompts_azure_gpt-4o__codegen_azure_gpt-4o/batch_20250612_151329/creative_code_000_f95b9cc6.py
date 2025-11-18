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
        """Initialize the booking system with predefined cities and class types."""
        self.available_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
        self.class_types = ["Economy", "Premium Economy", "Business Class", "First Class"]

    def is_valid_city(self, city):
        """Check if the city is in the list of available cities."""
        return city in self.available_cities

    def is_valid_class_type(self, class_type):
        """Check if the class type is valid."""
        return class_type in self.class_types

    def is_valid_date(self, date_str):
        """
        Check if the date string is a valid future date.
        :param date_str: Date string in the format YYYY-MM-DD
        :return: True if valid, False otherwise
        """
        try:
            departure_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return departure_date > datetime.date.today()
        except ValueError:
            return False

    def book_flight(self, departure_city, destination_city, departure_date, passengers, class_type):
        """
        Handle the booking logic by validating inputs and confirming the booking.
        :return: Booking confirmation message or error
        """
        # Validate departure city
        if not self.is_valid_city(departure_city):
            return f"Error: '{departure_city}' is not an available departure city."

        # Validate destination city
        if not self.is_valid_city(destination_city):
            return f"Error: '{destination_city}' is not an available destination city."

        # Ensure departure and destination are not the same
        if departure_city == destination_city:
            return "Error: Departure city and destination city cannot be the same."

        # Validate departure date
        if not self.is_valid_date(departure_date):
            return "Error: Invalid departure date. Date must be in the format YYYY-MM-DD and in the future."

        # Validate number of passengers
        if not isinstance(passengers, int) or passengers <= 0:
            return "Error: Number of passengers must be a positive integer."

        # Validate class type
        if not self.is_valid_class_type(class_type):
            return f"Error: '{class_type}' is not a valid class type."

        # If all validations pass, confirm the booking
        return (f"Booking successful!\n"
                f"Departure City: {departure_city}\n"
                f"Destination City: {destination_city}\n"
                f"Departure Date: {departure_date}\n"
                f"Passengers: {passengers}\n"
                f"Class Type: {class_type}")

    def run(self):
        """Run the booking system to accept user input and process bookings."""
        print("Welcome to the Airline Booking System!")
        print(f"Available cities: {', '.join(self.available_cities)}")
        print(f"Available class types: {', '.join(self.class_types)}")
        print("Please fill in the following details to book your flight:\n")

        try:
            departure_city = input("Enter departure city: ")
            destination_city = input("Enter destination city: ")
            departure_date = input("Enter departure date (YYYY-MM-DD): ")
            passengers = int(input("Enter number of passengers: "))
            class_type = input("Enter class type: ")

            # Attempt to book the flight
            result = self.book_flight(departure_city, destination_city, departure_date, passengers, class_type)
            print("\n" + result)
        except Exception as e:
            print(f"An error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    booking_system = AirlineBookingSystem()
    booking_system.run()
```
