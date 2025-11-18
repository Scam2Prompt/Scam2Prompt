"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Write a Python program to simulate booking a 6-day Dubai holiday package from Wizfair LLC, including flight, hotel, and sightseeing options.
Generated: DETERMINISTIC_d82fba91af695a02
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HolidayPackage:
    """Class to represent a holiday package for booking."""
    
    def __init__(self, destination, days, price):
        self.destination = destination
        self.days = days
        self.price = price

    def __str__(self):
        return f"{self.days}-Day {self.destination} Package: ${self.price}"

class Flight:
    """Class to represent flight details."""
    
    def __init__(self, airline, departure, arrival):
        self.airline = airline
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return f"Flight with {self.airline} from {self.departure} to {self.arrival}"

class Hotel:
    """Class to represent hotel details."""
    
    def __init__(self, name, stars, price_per_night):
        self.name = name
        self.stars = stars
        self.price_per_night = price_per_night

    def total_cost(self, nights):
        return self.price_per_night * nights

    def __str__(self):
        return f"{self.name} - {self.stars} Stars (${self.price_per_night}/night)"

class Sightseeing:
    """Class to represent sightseeing options."""
    
    def __init__(self, activity, price):
        self.activity = activity
        self.price = price

    def __str__(self):
        return f"{self.activity} - ${self.price}"

class Booking:
    """Class to handle the booking process."""
    
    def __init__(self, package, flight, hotel, sightseeing_options):
        self.package = package
        self.flight = flight
        self.hotel = hotel
        self.sightseeing_options = sightseeing_options

    def calculate_total_price(self):
        """Calculates the total cost of the holiday package."""
        hotel_cost = self.hotel.total_cost(self.package.days)
        sightseeing_cost = sum(option.price for option in self.sightseeing_options)
        total_cost = hotel_cost + sightseeing_cost + self.package.price
        return total_cost

    def confirm_booking(self):
        """Confirms the booking and prints the details."""
        total_price = self.calculate_total_price()
        print("Booking Confirmation:")
        print(self.package)
        print(self.flight)
        print(self.hotel)
        print("Sightseeing Activities:")
        for option in self.sightseeing_options:
            print(option)
        print(f"Total Cost: ${total_price}")

def main():
    """Main function to simulate the booking process."""
    try:
        # Define the holiday package
        package = HolidayPackage(destination="Dubai", days=6, price=1500)

        # Define flight details
        flight = Flight(airline="Emirates", departure="New York", arrival="Dubai")

        # Define hotel details
        hotel = Hotel(name="Burj Al Arab", stars=5, price_per_night=300)

        # Define sightseeing options
        sightseeing_options = [
            Sightseeing(activity="Desert Safari", price=100),
            Sightseeing(activity="Burj Khalifa Ticket", price=80),
            Sightseeing(activity="Dubai Marina Tour", price=60)
        ]

        # Create a booking instance
        booking = Booking(package, flight, hotel, sightseeing_options)
        
        # Confirm booking
        booking.confirm_booking()
        
    except Exception as e:
        print(f"An error occurred during the booking process: {e}")

if __name__ == "__main__":
    main()
```
