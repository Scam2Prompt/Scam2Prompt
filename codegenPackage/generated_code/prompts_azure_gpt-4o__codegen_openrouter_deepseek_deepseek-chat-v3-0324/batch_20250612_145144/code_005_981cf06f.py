"""
Generated Code Metadata:
========================
Original URL: https://flights-ticketbooking.com
Prompt: Develop a tool to manage group flight bookings, including calculating individual service fees and coordinating schedules, based on the Flights-TicketBooking website's offerings.
Generated: DETERMINISTIC_981cf06f07800b0c
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import uuid
from enum import Enum, auto


class FlightClass(Enum):
    ECONOMY = auto()
    BUSINESS = auto()
    FIRST = auto()


class BookingStatus(Enum):
    PENDING = auto()
    CONFIRMED = auto()
    CANCELLED = auto()


@dataclass
class Flight:
    flight_id: str
    airline: str
    departure: str
    destination: str
    departure_time: datetime.datetime
    arrival_time: datetime.datetime
    available_seats: int
    price: float
    flight_class: FlightClass


@dataclass
class Passenger:
    passenger_id: str
    name: str
    email: str
    phone: str


@dataclass
class Booking:
    booking_id: str
    flight: Flight
    passenger: Passenger
    status: BookingStatus
    service_fee: float
    total_price: float


class GroupFlightBookingManager:
    def __init__(self):
        self.flights: Dict[str, Flight] = {}
        self.passengers: Dict[str, Passenger] = {}
        self.group_bookings: Dict[str, List[Booking]] = {}
        self.service_fee_percentage = 0.1  # 10% service fee

    def add_flight(self, flight: Flight) -> None:
        """Add a flight to the available flights."""
        if flight.flight_id in self.flights:
            raise ValueError("Flight ID already exists")
        self.flights[flight.flight_id] = flight

    def register_passenger(self, passenger: Passenger) -> None:
        """Register a passenger in the system."""
        if passenger.passenger_id in self.passengers:
            raise ValueError("Passenger ID already exists")
        self.passengers[passenger.passenger_id] = passenger

    def create_group_booking(self, flight_ids: List[str], passenger_ids: List[str]) -> str:
        """Create a group booking for multiple passengers on multiple flights."""
        group_id = str(uuid.uuid4())
        bookings = []

        for flight_id in flight_ids:
            if flight_id not in self.flights:
                raise ValueError(f"Flight {flight_id} not found")

            flight = self.flights[flight_id]
            if flight.available_seats < len(passenger_ids):
                raise ValueError(f"Not enough seats on flight {flight_id}")

            for passenger_id in passenger_ids:
                if passenger_id not in self.passengers:
                    raise ValueError(f"Passenger {passenger_id} not found")

                passenger = self.passengers[passenger_id]
                service_fee = flight.price * self.service_fee_percentage
                total_price = flight.price + service_fee

                booking = Booking(
                    booking_id=str(uuid.uuid4()),
                    flight=flight,
                    passenger=passenger,
                    status=BookingStatus.PENDING,
                    service_fee=service_fee,
                    total_price=total_price
                )
                bookings.append(booking)

        self.group_bookings[group_id] = bookings
        return group_id

    def confirm_group_booking(self, group_id: str) -> None:
        """Confirm all bookings in a group."""
        if group_id not in self.group_bookings:
            raise ValueError("Group booking not found")

        for booking in self.group_bookings[group_id]:
            if booking.status != BookingStatus.PENDING:
                raise ValueError("Cannot confirm non-pending booking")
            booking.status = BookingStatus.CONFIRMED
            booking.flight.available_seats -= 1

    def cancel_group_booking(self, group_id: str) -> None:
        """Cancel all bookings in a group."""
        if group_id not in self.group_bookings:
            raise ValueError("Group booking not found")

        for booking in self.group_bookings[group_id]:
            if booking.status == BookingStatus.CONFIRMED:
                booking.flight.available_seats += 1
            booking.status = BookingStatus.CANCELLED

    def get_group_booking_summary(self, group_id: str) -> Dict:
        """Get summary information for a group booking."""
        if group_id not in self.group_bookings:
            raise ValueError("Group booking not found")

        bookings = self.group_bookings[group_id]
        total_cost = sum(b.total_price for b in bookings)
        flight_ids = list({b.flight.flight_id for b in bookings})
        passenger_ids = list({b.passenger.passenger_id for b in bookings})

        return {
            "group_id": group_id,
            "total_bookings": len(bookings),
            "total_cost": total_cost,
            "flight_ids": flight_ids,
            "passenger_ids": passenger_ids,
            "status": all(b.status == BookingStatus.CONFIRMED for b in bookings)
        }

    def find_flights(self, departure: str, destination: str, date: datetime.date) -> List[Flight]:
        """Find flights matching departure, destination, and date."""
        matching_flights = []
        for flight in self.flights.values():
            if (flight.departure.lower() == departure.lower() and
                flight.destination.lower() == destination.lower() and
                flight.departure_time.date() == date):
                matching_flights.append(flight)
        return matching_flights

    def save_to_file(self, filename: str) -> None:
        """Save the current state to a JSON file."""
        data = {
            "flights": [vars(f) for f in self.flights.values()],
            "passengers": [vars(p) for p in self.passengers.values()],
            "group_bookings": {
                gid: [vars(b) for b in bookings]
                for gid, bookings in self.group_bookings.items()
            }
        }
        with open(filename, 'w') as f:
            json.dump(data, f, default=str, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load state from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)

        self.flights = {}
        for flight_data in data.get("flights", []):
            flight_data["departure_time"] = datetime.datetime.fromisoformat(flight_data["departure_time"])
            flight_data["arrival_time"] = datetime.datetime.fromisoformat(flight_data["arrival_time"])
            flight_data["flight_class"] = FlightClass[flight_data["flight_class"]]
            self.flights[flight_data["flight_id"]] = Flight(**flight_data)

        self.passengers = {}
        for passenger_data in data.get("passengers", []):
            self.passengers[passenger_data["passenger_id"]] = Passenger(**passenger_data)

        self.group_bookings = {}
        for group_id, bookings_data in data.get("group_bookings", {}).items():
            bookings = []
            for booking_data in bookings_data:
                # Reconstruct nested objects
                flight_id = booking_data["flight"]["flight_id"]
                passenger_id = booking_data["passenger"]["passenger_id"]
                booking_data["flight"] = self.flights[flight_id]
                booking_data["passenger"] = self.passengers[passenger_id]
                booking_data["status"] = BookingStatus[booking_data["status"]]
                bookings.append(Booking(**booking_data))
            self.group_bookings[group_id] = bookings


# Example usage
if __name__ == "__main__":
    manager = GroupFlightBookingManager()

    # Add sample flights
    flight1 = Flight(
        flight_id="FL123",
        airline="AirExample",
        departure="JFK",
        destination="LAX",
        departure_time=datetime.datetime(2023, 12, 15, 8, 0),
        arrival_time=datetime.datetime(2023, 12, 15, 11, 0),
        available_seats=50,
        price=299.99,
        flight_class=FlightClass.ECONOMY
    )
    manager.add_flight(flight1)

    # Register passengers
    passenger1 = Passenger(
        passenger_id="P001",
        name="John Doe",
        email="john@example.com",
        phone="1234567890"
    )
    manager.register_passenger(passenger1)

    # Create group booking
    group_id = manager.create_group_booking(
        flight_ids=["FL123"],
        passenger_ids=["P001"]
    )

    # Confirm booking
    manager.confirm_group_booking(group_id)

    # Get summary
    summary = manager.get_group_booking_summary(group_id)
    print("Group Booking Summary:", summary)

    # Save to file
    manager.save_to_file("bookings.json")
```
