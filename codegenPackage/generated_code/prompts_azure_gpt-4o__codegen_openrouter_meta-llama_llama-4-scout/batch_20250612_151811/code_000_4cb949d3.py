"""
Generated Code Metadata:
========================
Original URL: https://sushiswap-suhii.weebly.com
Prompt: Write code to create a travel booking system that includes features for flight plans, hotel bookings, and travel activities, similar to the services described on the Sushiswap-Suhii website.
Generated: DETERMINISTIC_4cb949d3e030ba41
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_booking_system.py

from datetime import datetime
from typing import List, Dict

class FlightPlan:
    """Represents a flight plan with departure and arrival cities and dates."""

    def __init__(self, departure_city: str, arrival_city: str, departure_date: str, arrival_date: str):
        """
        Initializes a FlightPlan object.

        Args:
        - departure_city (str): The city of departure.
        - arrival_city (str): The city of arrival.
        - departure_date (str): The date of departure in YYYY-MM-DD format.
        - arrival_date (str): The date of arrival in YYYY-MM-DD format.
        """
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_date = datetime.strptime(departure_date, "%Y-%m-%d")
        self.arrival_date = datetime.strptime(arrival_date, "%Y-%m-%d")

    def __str__(self):
        return f"Flight from {self.departure_city} to {self.arrival_city} on {self.departure_date.date()} to {self.arrival_date.date()}"


class HotelBooking:
    """Represents a hotel booking with hotel name, location, and dates."""

    def __init__(self, hotel_name: str, location: str, check_in_date: str, check_out_date: str):
        """
        Initializes a HotelBooking object.

        Args:
        - hotel_name (str): The name of the hotel.
        - location (str): The location of the hotel.
        - check_in_date (str): The check-in date in YYYY-MM-DD format.
        - check_out_date (str): The check-out date in YYYY-MM-DD format.
        """
        self.hotel_name = hotel_name
        self.location = location
        self.check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
        self.check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")

    def __str__(self):
        return f"Hotel booking at {self.hotel_name} in {self.location} from {self.check_in_date.date()} to {self.check_out_date.date()}"


class TravelActivity:
    """Represents a travel activity with activity name, location, and date."""

    def __init__(self, activity_name: str, location: str, activity_date: str):
        """
        Initializes a TravelActivity object.

        Args:
        - activity_name (str): The name of the activity.
        - location (str): The location of the activity.
        - activity_date (str): The date of the activity in YYYY-MM-DD format.
        """
        self.activity_name = activity_name
        self.location = location
        self.activity_date = datetime.strptime(activity_date, "%Y-%m-%d")

    def __str__(self):
        return f"Activity: {self.activity_name} in {self.location} on {self.activity_date.date()}"


class TravelBookingSystem:
    """Manages flight plans, hotel bookings, and travel activities."""

    def __init__(self):
        self.flight_plans: List[FlightPlan] = []
        self.hotel_bookings: List[HotelBooking] = []
        self.travel_activities: List[TravelActivity] = []

    def add_flight_plan(self, flight_plan: FlightPlan):
        """Adds a flight plan to the system."""
        self.flight_plans.append(flight_plan)

    def add_hotel_booking(self, hotel_booking: HotelBooking):
        """Adds a hotel booking to the system."""
        self.hotel_bookings.append(hotel_booking)

    def add_travel_activity(self, travel_activity: TravelActivity):
        """Adds a travel activity to the system."""
        self.travel_activities.append(travel_activity)

    def view_bookings(self):
        """Displays all bookings in the system."""
        print("Flight Plans:")
        for i, flight_plan in enumerate(self.flight_plans, start=1):
            print(f"{i}. {flight_plan}")
        print("\nHotel Bookings:")
        for i, hotel_booking in enumerate(self.hotel_bookings, start=1):
            print(f"{i}. {hotel_booking}")
        print("\nTravel Activities:")
        for i, travel_activity in enumerate(self.travel_activities, start=1):
            print(f"{i}. {travel_activity}")


def main():
    try:
        booking_system = TravelBookingSystem()

        while True:
            print("\nTravel Booking System")
            print("1. Add Flight Plan")
            print("2. Add Hotel Booking")
            print("3. Add Travel Activity")
            print("4. View Bookings")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                departure_city = input("Enter departure city: ")
                arrival_city = input("Enter arrival city: ")
                departure_date = input("Enter departure date (YYYY-MM-DD): ")
                arrival_date = input("Enter arrival date (YYYY-MM-DD): ")
                flight_plan = FlightPlan(departure_city, arrival_city, departure_date, arrival_date)
                booking_system.add_flight_plan(flight_plan)
            elif choice == "2":
                hotel_name = input("Enter hotel name: ")
                location = input("Enter hotel location: ")
                check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
                check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
                hotel_booking = HotelBooking(hotel_name, location, check_in_date, check_out_date)
                booking_system.add_hotel_booking(hotel_booking)
            elif choice == "3":
                activity_name = input("Enter activity name: ")
                location = input("Enter activity location: ")
                activity_date = input("Enter activity date (YYYY-MM-DD): ")
                travel_activity = TravelActivity(activity_name, location, activity_date)
                booking_system.add_travel_activity(travel_activity)
            elif choice == "4":
                booking_system.view_bookings()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
