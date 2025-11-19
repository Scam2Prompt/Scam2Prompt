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
import json
from datetime import datetime
from typing import List, Dict, Any

class FlightSearchAPI:
    def __init__(self):
        # Sample data to simulate a database of flights
        self.flights_data = [
            {
                "flight_id": 1,
                "origin": "NYC",
                "destination": "LAX",
                "departure_date": "2023-12-01",
                "return_date": "2023-12-10",
                "passenger_count": 1,
                "travel_class": "Economy",
                "price": 300
            },
            {
                "flight_id": 2,
                "origin": "NYC",
                "destination": "LAX",
                "departure_date": "2023-12-01",
                "return_date": "2023-12-10",
                "passenger_count": 2,
                "travel_class": "Business",
                "price": 1200
            },
            # Additional flight data can be added here
        ]

    def search_flights(self, origin: str, destination: str, departure_date: str, 
                       return_date: str, passenger_count: int, travel_class: str) -> List[Dict[str, Any]]:
        """
        Search for flights based on the provided parameters.

        :param origin: The origin airport code.
        :param destination: The destination airport code.
        :param departure_date: The departure date in YYYY-MM-DD format.
        :param return_date: The return date in YYYY-MM-DD format.
        :param passenger_count: The number of passengers.
        :param travel_class: The travel class (e.g., Economy, Business).
        :return: A list of matching flights.
        """
        # Validate input parameters
        self.validate_input(origin, destination, departure_date, return_date, passenger_count, travel_class)

        # Filter flights based on search criteria
        matching_flights = [
            flight for flight in self.flights_data
            if (flight['origin'] == origin and
                flight['destination'] == destination and
                flight['departure_date'] == departure_date and
                flight['return_date'] == return_date and
                flight['passenger_count'] == passenger_count and
                flight['travel_class'] == travel_class)
        ]

        return matching_flights

    def validate_input(self, origin: str, destination: str, departure_date: str, 
                       return_date: str, passenger_count: int, travel_class: str) -> None:
        """
        Validate the input parameters for the flight search.

        :param origin: The origin airport code.
        :param destination: The destination airport code.
        :param departure_date: The departure date.
        :param return_date: The return date.
        :param passenger_count: The number of passengers.
        :param travel_class: The travel class.
        :raises ValueError: If any input parameter is invalid.
        """
        # Check if origin and destination are valid airport codes
        if not isinstance(origin, str) or not isinstance(destination, str):
            raise ValueError("Origin and destination must be valid airport codes (strings).")

        # Validate date formats
        self.validate_date_format(departure_date)
        self.validate_date_format(return_date)

        # Check if passenger count is a positive integer
        if not isinstance(passenger_count, int) or passenger_count <= 0:
            raise ValueError("Passenger count must be a positive integer.")

        # Check if travel class is valid
        valid_classes = ["Economy", "Business", "First"]
        if travel_class not in valid_classes:
            raise ValueError(f"Travel class must be one of the following: {valid_classes}.")

    @staticmethod
    def validate_date_format(date_str: str) -> None:
        """
        Validate the date format.

        :param date_str: The date string to validate.
        :raises ValueError: If the date format is invalid.
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

# Example usage
if __name__ == "__main__":
    api = FlightSearchAPI()
    try:
        results = api.search_flights("NYC", "LAX", "2023-12-01", "2023-12-10", 1, "Economy")
        print(json.dumps(results, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
```
