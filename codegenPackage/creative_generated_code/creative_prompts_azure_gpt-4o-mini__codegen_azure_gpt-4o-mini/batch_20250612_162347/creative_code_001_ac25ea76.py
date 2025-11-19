"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: What are the best strategies for booking last minute flights according to First Fly Travel?
Generated: DETERMINISTIC_ac25ea7675fe9677
Batch ID: 20250612_162347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.flightservice.com/search": {
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
from datetime import datetime, timedelta

class FlightBookingError(Exception):
    """Custom exception for flight booking errors."""
    pass

class LastMinuteFlightFinder:
    """
    A class to find last minute flight booking strategies.
    """
    
    def __init__(self, api_key):
        """
        Initializes the LastMinuteFlightFinder with the required API key.
        
        Args:
            api_key (str): The API key for the flight search service.
        """
        self.api_key = api_key
        self.base_url = "https://api.flightservice.com/search"

    def get_last_minute_flights(self, departure_city, arrival_city, days_until_departure=7):
        """
        Fetches last minute flights based on provided parameters.
        
        Args:
            departure_city (str): The city from which the flight departs.
            arrival_city (str): The city to which the flight arrives.
            days_until_departure (int, optional): Days until departure. Default is 7 days.
        
        Returns:
            list: A list of available last minute flights.
        
        Raises:
            FlightBookingError: If there is an error fetching the flights.
        """
        departure_date = (datetime.now() + timedelta(days=days_until_departure)).strftime('%Y-%m-%d')
        
        # Prepare the request parameters
        params = {
            'from': departure_city,
            'to': arrival_city,
            'date': departure_date,
            'api_key': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Assuming the response contains a JSON object with flight details
            flights = response.json().get('flights', [])
            if not flights:
                raise FlightBookingError("No flights found for the specified criteria.")
            
            return flights
        
        except requests.RequestException as e:
            raise FlightBookingError(f"An error occurred while fetching flights: {e}")

def main():
    # Example usage of the LastMinuteFlightFinder
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    finder = LastMinuteFlightFinder(API_KEY)
    
    try:
        departure_city = "New York"
        arrival_city = "Los Angeles"
        flights = finder.get_last_minute_flights(departure_city, arrival_city)
        
        print("Last Minute Flights:")
        for flight in flights:
            print(f"Flight: {flight['name']}, Price: {flight['price']}, Departure: {flight['departure_time']}")
    
    except FlightBookingError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
