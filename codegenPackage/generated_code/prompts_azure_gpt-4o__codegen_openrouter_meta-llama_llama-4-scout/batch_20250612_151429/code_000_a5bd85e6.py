"""
Generated Code Metadata:
========================
Original URL: https://www.fareobuddy.com
Prompt: Write Python code to simulate a flight search API that includes parameters for origin, destination, departure date, return date, passenger count, and travel class, inspired by FareObuddy's advanced search options.
Generated: DETERMINISTIC_a5bd85e655644767
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class TravelClass(str, Enum):
    ECONOMY = "economy"
    PREMIUM_ECONOMY = "premium_economy"
    BUSINESS = "business"
    FIRST_CLASS = "first_class"

class Flight:
    def __init__(self, flight_id: int, origin: str, destination: str, departure_date: datetime, return_date: datetime, travel_class: TravelClass, price: float):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date
        self.travel_class = travel_class
        self.price = price

class FlightSearchAPI:
    def __init__(self):
        self.flights = [
            Flight(1, "New York", "Los Angeles", datetime(2024, 9, 20), datetime(2024, 9, 25), TravelClass.ECONOMY, 400.0),
            Flight(2, "New York", "Los Angeles", datetime(2024, 9, 20), datetime(2024, 9, 25), TravelClass.BUSINESS, 1000.0),
            Flight(3, "Los Angeles", "New York", datetime(2024, 9, 22), datetime(2024, 9, 27), TravelClass.ECONOMY, 420.0),
            Flight(4, "Los Angeles", "New York", datetime(2024, 9, 22), datetime(2024, 9, 27), TravelClass.PREMIUM_ECONOMY, 600.0),
        ]

    def search_flights(self, origin: str, destination: str, departure_date: str, return_date: str, passenger_count: int, travel_class: TravelClass) -> List[Dict]:
        try:
            departure_date_obj = datetime.strptime(departure_date, "%Y-%m-%d")
            return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")

            if return_date_obj < departure_date_obj:
                raise ValueError("Return date must be after departure date")

            if passenger_count <= 0:
                raise ValueError("Passenger count must be greater than 0")

            matching_flights = [flight for flight in self.flights 
                                if flight.origin == origin 
                                and flight.destination == destination 
                                and flight.departure_date == departure_date_obj 
                                and flight.return_date == return_date_obj 
                                and flight.travel_class == travel_class]

            result = []
            for flight in matching_flights:
                result.append({
                    "flight_id": flight.flight_id,
                    "origin": flight.origin,
                    "destination": flight.destination,
                    "departure_date": flight.departure_date.strftime("%Y-%m-%d"),
                    "return_date": flight.return_date.strftime("%Y-%m-%d"),
                    "travel_class": flight.travel_class.value,
                    "price": flight.price * passenger_count,  # Calculate total price based on passenger count
                })

            return result

        except ValueError as e:
            print(f"Error: {e}")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

def main():
    api = FlightSearchAPI()
    origin = "New York"
    destination = "Los Angeles"
    departure_date = "2024-09-20"
    return_date = "2024-09-25"
    passenger_count = 2
    travel_class = TravelClass.ECONOMY

    result = api.search_flights(origin, destination, departure_date, return_date, passenger_count, travel_class)
    print(result)

if __name__ == "__main__":
    main()
```
