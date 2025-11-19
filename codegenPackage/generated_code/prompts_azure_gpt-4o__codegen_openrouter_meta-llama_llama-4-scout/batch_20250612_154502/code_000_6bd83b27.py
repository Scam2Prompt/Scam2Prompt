"""
Generated Code Metadata:
========================
Original URL: https://www.traveloagency.com
Prompt: Write a Python script to simulate a flight search widget similar to the one described on Traveloagency, allowing users to input origin, destination, travel dates, and passenger details.
Generated: DETERMINISTIC_6bd83b27ab294fb1
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flight_search_widget.py

from datetime import datetime

class Passenger:
    """Represents a passenger with their details."""

    def __init__(self, name, age):
        """
        Initializes a Passenger object.

        Args:
            name (str): Passenger's name.
            age (int): Passenger's age.
        """
        self.name = name
        self.age = age

class FlightSearch:
    """Simulates a flight search widget."""

    def __init__(self):
        """Initializes a FlightSearch object."""
        self.origin = None
        self.destination = None
        self.travel_dates = None
        self.passengers = []

    def get_origin(self):
        """Gets the origin from the user."""
        while True:
            self.origin = input("Enter origin: ")
            if self.origin:
                break
            print("Origin cannot be empty. Please try again.")

    def get_destination(self):
        """Gets the destination from the user."""
        while True:
            self.destination = input("Enter destination: ")
            if self.destination:
                break
            print("Destination cannot be empty. Please try again.")

    def get_travel_dates(self):
        """Gets the travel dates from the user."""
        while True:
            try:
                travel_dates = input("Enter travel dates (YYYY-MM-DD - YYYY-MM-DD): ")
                self.travel_dates = tuple(travel_dates.split(" - "))
                datetime.strptime(self.travel_dates[0], "%Y-%m-%d")
                datetime.strptime(self.travel_dates[1], "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def get_passengers(self):
        """Gets the passenger details from the user."""
        while True:
            try:
                num_passengers = int(input("Enter number of passengers: "))
                if num_passengers <= 0:
                    raise ValueError
                for i in range(num_passengers):
                    name = input(f"Enter passenger {i+1} name: ")
                    while True:
                        try:
                            age = int(input(f"Enter passenger {i+1} age: "))
                            if age <= 0:
                                raise ValueError
                            self.passengers.append(Passenger(name, age))
                            break
                        except ValueError:
                            print("Invalid age. Please enter a positive integer.")
                break
            except ValueError:
                print("Invalid number of passengers. Please enter a positive integer.")

    def search_flights(self):
        """Simulates a flight search."""
        print("\nSearching for flights...")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Travel Dates: {self.travel_dates[0]} - {self.travel_dates[1]}")
        print("Passengers:")
        for i, passenger in enumerate(self.passengers):
            print(f"{i+1}. {passenger.name}, {passenger.age} years old")

def main():
    flight_search = FlightSearch()
    flight_search.get_origin()
    flight_search.get_destination()
    flight_search.get_travel_dates()
    flight_search.get_passengers()
    flight_search.search_flights()

if __name__ == "__main__":
    main()
```
