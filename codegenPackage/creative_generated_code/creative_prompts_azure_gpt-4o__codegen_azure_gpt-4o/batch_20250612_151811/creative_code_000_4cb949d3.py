"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswap-suhii.weebly.com
Prompt: Write code to create a travel booking system that includes features for flight plans, hotel bookings, and travel activities, similar to the services described on the Sushiswap-Suhii website.
Generated: DETERMINISTIC_4cb949d3e030ba41
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TravelBookingSystem:
    """
    A system to manage travel bookings including flight plans,
    hotel bookings, and travel activities.
    """

    def __init__(self):
        self.flights = []
        self.hotels = []
        self.activities = []
    
    # Flight Booking Management
    def create_flight(self, flight_number, origin, destination, departure_time, arrival_time):
        """
        Adds a flight plan to the system.

        :param flight_number: Unique identifier for the flight
        :param origin: Starting location
        :param destination: Target location
        :param departure_time: Departure time (datetime object)
        :param arrival_time: Arrival time (datetime object)
        """
        if arrival_time <= departure_time:
            raise ValueError("Arrival time must be after departure time.")
        
        flight = {
            "flight_number": flight_number,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time
        }
        self.flights.append(flight)
        return flight

    def list_flights(self):
        """Returns all flight plans stored in the system."""
        return self.flights
    
    # Hotel Booking Management
    def create_hotel_booking(self, hotel_name, location, check_in, check_out, guests):
        """
        Adds a hotel booking to the system.

        :param hotel_name: Name of the hotel
        :param location: Location of the hotel
        :param check_in: Check-in date (datetime object)
        :param check_out: Check-out date (datetime object)
        :param guests: Number of guests
        """
        if check_out <= check_in:
            raise ValueError("Check-out date must be after check-in date.")
        
        hotel_booking = {
            "hotel_name": hotel_name,
            "location": location,
            "check_in": check_in,
            "check_out": check_out,
            "guests": guests
        }
        self.hotels.append(hotel_booking)
        return hotel_booking

    def list_hotel_bookings(self):
        """Returns all hotel bookings stored in the system."""
        return self.hotels
    
    # Activity Booking Management
    def create_activity(self, activity_name, location, date, participants):
        """
        Adds a travel activity to the system.

        :param activity_name: Name of the activity
        :param location: Location of the activity
        :param date: Date of the activity (datetime object)
        :param participants: Number of participants
        """
        if participants <= 0:
            raise ValueError("Number of participants must be greater than zero.")
        
        activity = {
            "activity_name": activity_name,
            "location": location,
            "date": date,
            "participants": participants
        }
        self.activities.append(activity)
        return activity

    def list_activities(self):
        """Returns all travel activities stored in the system."""
        return self.activities

# Example of usage
if __name__ == "__main__":
    try:
        system = TravelBookingSystem()

        # Create a flight booking
        flight = system.create_flight(
            flight_number="AA123",
            origin="New York",
            destination="Los Angeles",
            departure_time=datetime.datetime(2023, 10, 10, 8, 0),
            arrival_time=datetime.datetime(2023, 10, 10, 11, 0)
        )
        print("Flight Added:", flight)

        # Create a hotel booking
        hotel = system.create_hotel_booking(
            hotel_name="Hilton",
            location="Los Angeles",
            check_in=datetime.datetime(2023, 10, 10),
            check_out=datetime.datetime(2023, 10, 15),
            guests=2
        )
        print("Hotel Added:", hotel)

        # Create a travel activity
        activity = system.create_activity(
            activity_name="City Tour",
            location="Los Angeles",
            date=datetime.datetime(2023, 10, 11),
            participants=4
        )
        print("Activity Added:", activity)

        # List all bookings
        print("All Flights:", system.list_flights())
        print("All Hotels:", system.list_hotel_bookings())
        print("All Activities:", system.list_activities())
    
    except Exception as e:
        print("An error occurred:", e)
```
