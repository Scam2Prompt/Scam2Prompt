"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://localtravelcoupons.com
Prompt: Explain how to implement a booking system for group travel that accommodates multiple airline options, similar to the services provided by Local Travel Coupons.
Generated: DETERMINISTIC_34b5b9bcd114ebfd
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any, Optional

class Flight:
    """Class representing a flight option."""
    
    def __init__(self, airline: str, flight_number: str, price: float, seats_available: int):
        self.airline = airline
        self.flight_number = flight_number
        self.price = price
        self.seats_available = seats_available

    def __repr__(self):
        return f"{self.airline} {self.flight_number} - ${self.price} Seats: {self.seats_available}"

class Booking:
    """Class for handling bookings for group travel."""
    
    def __init__(self):
        self.flights: List[Flight] = []

    def add_flight(self, flight: Flight) -> None:
        """Add a flight option to the booking."""
        self.flights.append(flight)

    def book_flight(self, flight_index: int, quantity: int) -> Optional[str]:
        """Book a specified quantity of seats on a flight.
        
        Args:
            flight_index (int): The index of the flight in the flights list.
            quantity (int): Number of seats to book.

        Returns:
            Optional[str]: Confirmation message or error.
        """
        try:
            flight = self.flights[flight_index]
            if flight.seats_available < quantity:
                return "Not enough seats available."
            flight.seats_available -= quantity
            return f"Successfully booked {quantity} seat(s) on {flight.airline} {flight.flight_number}."
        except IndexError:
            return "Flight selection is out of range."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_available_flights(self) -> List[Dict[str, Any]]:
        """Get a list of available flights for booking.
        
        Returns:
            List[Dict[str, Any]]: Available flights in a dictionary format.
        """
        return [{"airline": flight.airline, "flight_number": flight.flight_number, 
                 "price": flight.price, "seats_available": flight.seats_available} for flight in self.flights]

def load_flights_from_json(file_path: str) -> List[Flight]:
    """Load flight data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing flight data.

    Returns:
        List[Flight]: A list of Flight objects.
    """
    try:
        with open(file_path, 'r') as file:
            flight_data = json.load(file)
            return [Flight(**flight) for flight in flight_data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading flight data: {str(e)}")
        return []

def main():
    """Main function to run the booking system."""
    booking_system = Booking()
    
    # Load flights from a JSON file
    flights = load_flights_from_json("flights.json")
    for flight in flights:
        booking_system.add_flight(flight)

    # Display available flights
    available_flights = booking_system.get_available_flights()
    print("Available Flights:")
    for i, flight in enumerate(available_flights):
        print(f"{i}: {flight}")

    # Example booking (should be replaced with user input in production)
    booking_response = booking_system.book_flight(0, 2)
    print(booking_response)

if __name__ == "__main__":
    main()
```

**Note:** Make sure to create a `flights.json` file with the appropriate flight data structure before running the code. The structure should look like this:

```json
[
    {
        "airline": "Airline A",
        "flight_number": "AA123",
        "price": 199.99,
        "seats_available": 5
    },
    {
        "airline": "Airline B",
        "flight_number": "BB456",
        "price": 299.99,
        "seats_available": 2
    }
]
```
