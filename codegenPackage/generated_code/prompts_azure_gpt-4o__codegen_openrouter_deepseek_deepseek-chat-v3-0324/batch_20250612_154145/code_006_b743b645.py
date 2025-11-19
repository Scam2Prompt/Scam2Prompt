"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Develop a program to manage corporate travel itineraries, including cost optimization and resource mobilization, inspired by KK Travel Solutions' corporate travel management solutions.
Generated: DETERMINISTIC_b743b645a6c4f537
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import requests
from enum import Enum, auto


class TravelClass(Enum):
    ECONOMY = auto()
    PREMIUM_ECONOMY = auto()
    BUSINESS = auto()
    FIRST = auto()


class AccommodationType(Enum):
    HOTEL = auto()
    APARTMENT = auto()
    VILLA = auto()


@dataclass
class Flight:
    flight_number: str
    departure: str
    arrival: str
    departure_time: datetime.datetime
    arrival_time: datetime.datetime
    airline: str
    travel_class: TravelClass
    price: float
    duration: datetime.timedelta


@dataclass
class Accommodation:
    name: str
    location: str
    check_in: datetime.datetime
    check_out: datetime.datetime
    accommodation_type: AccommodationType
    price_per_night: float
    total_price: float


@dataclass
class Transportation:
    type: str
    provider: str
    pickup_location: str
    dropoff_location: str
    pickup_time: datetime.datetime
    price: float


@dataclass
class TravelItinerary:
    employee_id: str
    employee_name: str
    purpose: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    flights: List[Flight]
    accommodations: List[Accommodation]
    transportations: List[Transportation]
    total_cost: float
    status: str = "DRAFT"


class TravelManager:
    def __init__(self):
        self.itineraries: Dict[str, TravelItinerary] = {}

    def create_itinerary(
        self,
        employee_id: str,
        employee_name: str,
        purpose: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> TravelItinerary:
        """Create a new travel itinerary."""
        itinerary = TravelItinerary(
            employee_id=employee_id,
            employee_name=employee_name,
            purpose=purpose,
            start_date=start_date,
            end_date=end_date,
            flights=[],
            accommodations=[],
            transportations=[],
            total_cost=0.0,
        )
        self.itineraries[employee_id] = itinerary
        return itinerary

    def add_flight(
        self,
        employee_id: str,
        flight_number: str,
        departure: str,
        arrival: str,
        departure_time: datetime.datetime,
        arrival_time: datetime.datetime,
        airline: str,
        travel_class: TravelClass,
        price: float,
    ) -> None:
        """Add a flight to an existing itinerary."""
        if employee_id not in self.itineraries:
            raise ValueError("Employee itinerary not found")

        duration = arrival_time - departure_time
        flight = Flight(
            flight_number=flight_number,
            departure=departure,
            arrival=arrival,
            departure_time=departure_time,
            arrival_time=arrival_time,
            airline=airline,
            travel_class=travel_class,
            price=price,
            duration=duration,
        )

        self.itineraries[employee_id].flights.append(flight)
        self._update_total_cost(employee_id, price)

    def add_accommodation(
        self,
        employee_id: str,
        name: str,
        location: str,
        check_in: datetime.datetime,
        check_out: datetime.datetime,
        accommodation_type: AccommodationType,
        price_per_night: float,
    ) -> None:
        """Add accommodation to an existing itinerary."""
        if employee_id not in self.itineraries:
            raise ValueError("Employee itinerary not found")

        nights = (check_out - check_in).days
        total_price = price_per_night * nights

        accommodation = Accommodation(
            name=name,
            location=location,
            check_in=check_in,
            check_out=check_out,
            accommodation_type=accommodation_type,
            price_per_night=price_per_night,
            total_price=total_price,
        )

        self.itineraries[employee_id].accommodations.append(accommodation)
        self._update_total_cost(employee_id, total_price)

    def add_transportation(
        self,
        employee_id: str,
        type: str,
        provider: str,
        pickup_location: str,
        dropoff_location: str,
        pickup_time: datetime.datetime,
        price: float,
    ) -> None:
        """Add transportation to an existing itinerary."""
        if employee_id not in self.itineraries:
            raise ValueError("Employee itinerary not found")

        transportation = Transportation(
            type=type,
            provider=provider,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            pickup_time=pickup_time,
            price=price,
        )

        self.itineraries[employee_id].transportations.append(transportation)
        self._update_total_cost(employee_id, price)

    def _update_total_cost(self, employee_id: str, amount: float) -> None:
        """Update the total cost of an itinerary."""
        self.itineraries[employee_id].total_cost += amount

    def get_itinerary(self, employee_id: str) -> Optional[TravelItinerary]:
        """Retrieve an itinerary by employee ID."""
        return self.itineraries.get(employee_id)

    def optimize_costs(self, employee_id: str) -> None:
        """Optimize costs for an itinerary by finding cheaper alternatives."""
        if employee_id not in self.itineraries:
            raise ValueError("Employee itinerary not found")

        itinerary = self.itineraries[employee_id]

        # Flight optimization - find cheaper flights in same class
        for i, flight in enumerate(itinerary.flights):
            cheaper_flights = self._find_cheaper_flights(
                flight.departure,
                flight.arrival,
                flight.departure_time,
                flight.travel_class,
                flight.price,
            )
            if cheaper_flights:
                itinerary.flights[i] = cheaper_flights[0]
                self._update_total_cost(
                    employee_id, cheaper_flights[0].price - flight.price
                )

        # Accommodation optimization - find cheaper accommodations
        for i, accommodation in enumerate(itinerary.accommodations):
            cheaper_accommodations = self._find_cheaper_accommodations(
                accommodation.location,
                accommodation.check_in,
                accommodation.check_out,
                accommodation.accommodation_type,
                accommodation.price_per_night,
            )
            if cheaper_accommodations:
                itinerary.accommodations[i] = cheaper_accommodations[0]
                self._update_total_cost(
                    employee_id,
                    cheaper_accommodations[0].total_price - accommodation.total_price,
                )

    def _find_cheaper_flights(
        self,
        departure: str,
        arrival: str,
        departure_time: datetime.datetime,
        travel_class: TravelClass,
        max_price: float,
    ) -> List[Flight]:
        """Find cheaper flights matching criteria (mock implementation)."""
        # In a real implementation, this would query a flight API
        return []

    def _find_cheaper_accommodations(
        self,
        location: str,
        check_in: datetime.datetime,
        check_out: datetime.datetime,
        accommodation_type: AccommodationType,
        max_price_per_night: float,
    ) -> List[Accommodation]:
        """Find cheaper accommodations matching criteria (mock implementation)."""
        # In a real implementation, this would query an accommodation API
        return []

    def finalize_itinerary(self, employee_id: str) -> None:
        """Finalize an itinerary and change its status."""
        if employee_id not in self.itineraries:
            raise ValueError("Employee itinerary not found")
        self.itineraries[employee_id].status = "FINALIZED"

    def export_itinerary(self, employee_id: str, format: str = "json") -> str:
        """Export itinerary in specified format."""
        if employee_id not in self.itineraries:
            raise ValueError("Employee itinerary not found")

        itinerary = self.itineraries[employee_id]

        if format == "json":
            return self._export_to_json(itinerary)
        else:
            raise ValueError("Unsupported export format")

    def _export_to_json(self, itinerary: TravelItinerary) -> str:
        """Convert itinerary to JSON string."""
        def datetime_converter(o):
            if isinstance(o, datetime.datetime):
                return o.isoformat()
            elif isinstance(o, datetime.timedelta):
                return str(o)
            elif isinstance(o, Enum):
                return o.name
            raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

        itinerary_dict = asdict(itinerary)
        return json.dumps(itinerary_dict, default=datetime_converter, indent=2)


class TravelAPI:
    def __init__(self, travel_manager: TravelManager):
        self.travel_manager = travel_manager

    def handle_request(self, request_data: dict) -> dict:
        """Handle API requests and return appropriate response."""
        try:
            action = request_data.get("action")
            if action == "create_itinerary":
                return self._handle_create_itinerary(request_data)
            elif action == "add_flight":
                return
