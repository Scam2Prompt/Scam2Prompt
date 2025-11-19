"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalflightguide.com
Prompt: Write a code snippet that integrates with a flight booking API to streamline the process of scheduling and changing flights, similar to the services offered by Global Flight Guide.
Generated: DETERMINISTIC_bbf13fc0146c3eeb
Batch ID: 20250612_163928
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.flightbooking.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class FlightBookingAPI:
    """
    A class to interact with the Flight Booking API.
    """

    BASE_URL = "https://api.flightbooking.com/v1"  # Base URL for the Flight Booking API
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

    def __init__(self):
        """
        Initializes the FlightBookingAPI instance.
        """
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }

    def search_flights(self, departure, arrival, date):
        """
        Searches for available flights.

        :param departure: The departure airport code.
        :param arrival: The arrival airport code.
        :param date: The date of the flight (YYYY-MM-DD).
        :return: A list of available flights or an error message.
        """
        try:
            url = f"{self.BASE_URL}/flights/search"
            params = {
                "departure": departure,
                "arrival": arrival,
                "date": date
            }
            response = requests.get(url, headers=self.headers, params=params)

            # Check for successful response
            response.raise_for_status()
            return response.json()  # Return the JSON response

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def book_flight(self, flight_id, passenger_info):
        """
        Books a flight based on flight ID and passenger information.

        :param flight_id: The ID of the flight to book.
        :param passenger_info: A dictionary containing passenger details.
        :return: Booking confirmation or an error message.
        """
        try:
            url = f"{self.BASE_URL}/flights/{flight_id}/book"
            payload = json.dumps(passenger_info)
            response = requests.post(url, headers=self.headers, data=payload)

            # Check for successful response
            response.raise_for_status()
            return response.json()  # Return the booking confirmation

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def change_flight(self, booking_id, new_flight_id):
        """
        Changes an existing flight booking.

        :param booking_id: The ID of the existing booking.
        :param new_flight_id: The ID of the new flight to change to.
        :return: Confirmation of the change or an error message.
        """
        try:
            url = f"{self.BASE_URL}/bookings/{booking_id}/change"
            payload = json.dumps({"new_flight_id": new_flight_id})
            response = requests.put(url, headers=self.headers, data=payload)

            # Check for successful response
            response.raise_for_status()
            return response.json()  # Return the change confirmation

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

# Example usage:
if __name__ == "__main__":
    api = FlightBookingAPI()
    
    # Search for flights
    flights = api.search_flights("LAX", "JFK", "2023-12-15")
    print(flights)

    # Book a flight (example payload)
    booking_confirmation = api.book_flight("FLIGHT_ID", {"name": "John Doe", "email": "john@example.com"})
    print(booking_confirmation)

    # Change a flight booking
    change_confirmation = api.change_flight("BOOKING_ID", "NEW_FLIGHT_ID")
    print(change_confirmation)
```
