"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Write Python code to simulate a flight search API that replicates Tripocost's functionality, including filtering by origin, destination, departure date, return date, and class type (economy, business, etc.).
Generated: DETERMINISTIC_2e2449764c0363ce
Batch ID: 20250612_154529
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
    """Class to represent a flight."""
    
    def __init__(self, origin: str, destination: str, departure_date: str, return_date: Optional[str], class_type: str):
        self.origin = origin
        self.destination = destination
        self.departure_date = self._validate_date(departure_date)
        self.return_date = self._validate_date(return_date) if return_date else None
        self.class_type = class_type

    @staticmethod
    def _validate_date(date_str: str) -> datetime.date:
        """Validates the date string and converts it to a date object."""
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.")

class FlightSearchAPI:
    """Class to simulate a flight search API."""
    
    def __init__(self):
        self.flights = []  # List to store available flights

    def add_flight(self, flight: Flight):
        """Adds a flight to the flight list."""
        self.flights.append(flight)

    def search_flights(self, origin: str, destination: str, departure_date: str, return_date: Optional[str], class_type: str) -> List[Dict]:
        """
        Searches for flights based on provided criteria.
        
        Parameters:
            origin (str): The origin airport code.
            destination (str): The destination airport code.
            departure_date (str): The departure date in YYYY-MM-DD format.
            return_date (Optional[str]): The return date in YYYY-MM-DD format.
            class_type (str): The class type (economy, business, etc.).
        
        Returns:
            List[Dict]: A list of available flights matching the criteria.
        """
        matching_flights = []
        
        # Validate departure and return dates
        dep_date = Flight._validate_date(departure_date)
        if return_date:
            ret_date = Flight._validate_date(return_date)
            if ret_date < dep_date:
                raise ValueError("Return date cannot be earlier than departure date.")
        
        for flight in self.flights:
            if (flight.origin == origin and
                flight.destination == destination and
                flight.departure_date == dep_date and
                (not return_date or flight.return_date == ret_date) and
                flight.class_type == class_type):
                matching_flights.append({
                    "origin": flight.origin,
                    "destination": flight.destination,
                    "departure_date": flight.departure_date.isoformat(),
                    "return_date": flight.return_date.isoformat() if flight.return_date else None,
                    "class_type": flight.class_type
                })
        
        if not matching_flights:
            print("No flights found matching your criteria.")
        
        return matching_flights

# Example Usage
if __name__ == "__main__":
    flight_api = FlightSearchAPI()
    
    # Adding some sample flights
    flight_api.add_flight(Flight("NYC", "LAX", "2023-12-01", "2023-12-15", "economy"))
    flight_api.add_flight(Flight("NYC", "LAX", "2023-12-01", None, "business"))
    flight_api.add_flight(Flight("LAX", "NYC", "2023-12-15", None, "economy"))

    # Searching for flights
    try:
        results = flight_api.search_flights("NYC", "LAX", "2023-12-01", "2023-12-15", "economy")
        print("Search Results:", results)
    except ValueError as e:
        print("Error:", e)
```
