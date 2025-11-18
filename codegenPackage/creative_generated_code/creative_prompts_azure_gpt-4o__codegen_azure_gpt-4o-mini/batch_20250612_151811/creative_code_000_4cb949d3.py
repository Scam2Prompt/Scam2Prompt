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
from typing import List, Dict, Optional

class Flight:
    """Class to represent a flight plan."""
    def __init__(self, flight_number: str, departure: str, arrival: str, departure_time: datetime.datetime, arrival_time: datetime.datetime):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __str__(self):
        return f"Flight {self.flight_number} from {self.departure} to {self.arrival}"


class Hotel:
    """Class to represent a hotel booking."""
    def __init__(self, name: str, check_in: datetime.date, check_out: datetime.date, price_per_night: float):
        self.name = name
        self.check_in = check_in
        self.check_out = check_out
        self.price_per_night = price_per_night

    def total_cost(self) -> float:
        """Calculates total cost of the hotel stay."""
        num_nights = (self.check_out - self.check_in).days
        return num_nights * self.price_per_night

    def __str__(self):
        return f"Hotel {self.name} from {self.check_in} to {self.check_out}"


class Activity:
    """Class to represent a travel activity."""
    def __init__(self, activity_name: str, date: datetime.date, cost: float):
        self.activity_name = activity_name
        self.date = date
        self.cost = cost

    def __str__(self):
        return f"Activity: {self.activity_name} on {self.date}, Cost: {self.cost}"


class TravelBookingSystem:
    """Class to manage the travel booking system."""

    def __init__(self):
        self.flights: List[Flight] = []
        self.hotels: List[Hotel] = []
        self.activities: List[Activity] = []

    def add_flight(self, flight: Flight):
        """Adds a flight to the system."""
        self.flights.append(flight)

    def book_hotel(self, hotel: Hotel) -> Optional[str]:
        """Books a hotel and returns the booking confirmation."""
        if hotel.check_out <= hotel.check_in:
            return "Error: Check-out date must be after check-in date."
        self.hotels.append(hotel)
        return f"Hotel {hotel.name} booked successfully."

    def add_activity(self, activity: Activity):
        """Adds an activity to the travel itinerary."""
        self.activities.append(activity)

    def total_cost(self) -> float:
        """Calculates the total cost of flights, hotels, and activities."""
        flight_cost = len(self.flights) * 200  # Placeholder for flight cost calculation
        hotel_cost = sum(hotel.total_cost() for hotel in self.hotels)
        activity_cost = sum(activity.cost for activity in self.activities)
        return flight_cost + hotel_cost + activity_cost

    def summary(self) -> Dict[str, List[str]]:
        """Returns a summary of the travel bookings."""
        return {
            "flights": [str(flight) for flight in self.flights],
            "hotels": [str(hotel) for hotel in self.hotels],
            "activities": [str(activity) for activity in self.activities],
        }

# Example usage
if __name__ == "__main__":
    try:
        travel_system = TravelBookingSystem()

        # Adding flights
        flight_1 = Flight("AA123", "NYC", "LAX", datetime.datetime(2023, 12, 1, 10, 0), datetime.datetime(2023, 12, 1, 13, 0))
        travel_system.add_flight(flight_1)
        
        # Booking a hotel
        hotel_1 = Hotel("Grand Hotel", datetime.date(2023, 12, 1), datetime.date(2023, 12, 5), 150.0)
        print(travel_system.book_hotel(hotel_1))

        # Adding activities
        activity_1 = Activity("City Tour", datetime.date(2023, 12, 2), 75.0)
        travel_system.add_activity(activity_1)

        # Print summary and total cost
        print(travel_system.summary())
        print(f"Total Cost: ${travel_system.total_cost():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
