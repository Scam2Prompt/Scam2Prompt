"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: Create a program to fetch and compare the best deals on flights and hotels using APIs, aligning with Exytrade's travel services.
Generated: DETERMINISTIC_753a404384040daf
Batch ID: 20250612_154333
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.flightservice.com/v1/search": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hotelservice.com/v1/search": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple

# Constants
FLIGHT_API_ENDPOINT = "https://api.flightservice.com/v1/search"
HOTEL_API_ENDPOINT = "https://api.hotelservice.com/v1/search"
API_TIMEOUT = 10  # seconds
MAX_RESULTS = 5

class TravelDealFinder:
    """
    A class to fetch and compare flight and hotel deals from various APIs.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the TravelDealFinder with an API key.
        
        Args:
            api_key (str): The API key for authentication
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def fetch_flight_deals(self, origin: str, destination: str, departure_date: str, 
                          return_date: Optional[str] = None, max_price: Optional[float] = None) -> List[Dict]:
        """
        Fetch flight deals from the flight API.
        
        Args:
            origin (str): Departure airport/city code
            destination (str): Arrival airport/city code
            departure_date (str): Departure date in YYYY-MM-DD format
            return_date (str, optional): Return date in YYYY-MM-DD format for round trips
            max_price (float, optional): Maximum price filter
            
        Returns:
            List[Dict]: List of flight deals
        """
        params = {
            "origin": origin,
            "destination": destination,
            "departure_date": departure_date,
            "adults": 1,
            "currency": "USD",
            "limit": MAX_RESULTS
        }
        
        if return_date:
            params["return_date"] = return_date
        if max_price:
            params["max_price"] = max_price
            
        try:
            response = self.session.get(
                FLIGHT_API_ENDPOINT,
                params=params,
                timeout=API_TIMEOUT
            )
            response.raise_for_status()
            return response.json().get("data", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching flight deals: {e}")
            return []
    
    def fetch_hotel_deals(self, location: str, check_in: str, check_out: str, 
                         max_price: Optional[float] = None) -> List[Dict]:
        """
        Fetch hotel deals from the hotel API.
        
        Args:
            location (str): City or hotel location
            check_in (str): Check-in date in YYYY-MM-DD format
            check_out (str): Check-out date in YYYY-MM-DD format
            max_price (float, optional): Maximum price per night
            
        Returns:
            List[Dict]: List of hotel deals
        """
        params = {
            "location": location,
            "check_in": check_in,
            "check_out": check_out,
            "adults": 1,
            "currency": "USD",
            "limit": MAX_RESULTS
        }
        
        if max_price:
            params["max_price"] = max_price
            
        try:
            response = self.session.get(
                HOTEL_API_ENDPOINT,
                params=params,
                timeout=API_TIMEOUT
            )
            response.raise_for_status()
            return response.json().get("data", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching hotel deals: {e}")
            return []
    
    def compare_deals(self, flights: List[Dict], hotels: List[Dict]) -> List[Dict]:
        """
        Compare flight and hotel deals to find the best combined options.
        
        Args:
            flights (List[Dict]): List of flight deals
            hotels (List[Dict]): List of hotel deals
            
        Returns:
            List[Dict]: Combined deals sorted by total price
        """
        combined_deals = []
        
        for flight in flights:
            for hotel in hotels:
                total_price = flight.get("price", 0) + hotel.get("price", 0)
                combined_deals.append({
                    "flight": flight,
                    "hotel": hotel,
                    "total_price": total_price
                })
        
        # Sort by total price ascending
        combined_deals.sort(key=lambda x: x["total_price"])
        return combined_deals
    
    def get_best_deals(self, origin: str, destination: str, departure_date: str, 
                      return_date: Optional[str] = None, stay_duration: int = 3,
                      max_flight_price: Optional[float] = None, 
                      max_hotel_price: Optional[float] = None) -> List[Dict]:
        """
        Get the best combined flight and hotel deals.
        
        Args:
            origin (str): Departure airport/city code
            destination (str): Arrival airport/city code
            departure_date (str): Departure date in YYYY-MM-DD format
            return_date (str, optional): Return date for round trips
            stay_duration (int): Number of nights to stay (default 3)
            max_flight_price (float, optional): Max flight price
            max_hotel_price (float, optional): Max hotel price per night
            
        Returns:
            List[Dict]: Best combined deals
        """
        # Calculate hotel dates
        check_in = departure_date
        check_out = (datetime.strptime(departure_date, "%Y-%m-%d") + 
                    timedelta(days=stay_duration)).strftime("%Y-%m-%d")
        
        flights = self.fetch_flight_deals(
            origin, destination, departure_date, 
            return_date, max_flight_price
        )
        
        hotels = self.fetch_hotel_deals(
            destination, check_in, check_out, 
            max_hotel_price
        )
        
        if not flights or not hotels:
            return []
        
        return self.compare_deals(flights, hotels)[:MAX_RESULTS]

# Example usage
if __name__ == "__main__":
    # Replace with actual API key
    API_KEY = "your_api_key_here"
    
    finder = TravelDealFinder(API_KEY)
    
    # Example search parameters
    origin = "JFK"
    destination = "LAX"
    departure_date = "2023-12-15"
    return_date = "2023-12-22"
    stay_duration = 5
    
    best_deals = finder.get_best_deals(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        return_date=return_date,
        stay_duration=stay_duration,
        max_flight_price=500,
        max_hotel_price=200
    )
    
    print("Best Travel Deals:")
    for i, deal in enumerate(best_deals, 1):
        print(f"\nDeal #{i}:")
        print(f"Flight: {deal['flight']['airline']} from {deal['flight']['origin']} to {deal['flight']['destination']}")
        print(f"  Departure: {deal['flight']['departure_time']}, Price: ${deal['flight']['price']}")
        print(f"Hotel: {deal['hotel']['name']} in {deal['hotel']['location']}")
        print(f"  Check-in: {deal['hotel']['check_in']}, Check-out: {deal['hotel']['check_out']}")
        print(f"  Price per night: ${deal['hotel']['price'] / ((datetime.strptime(deal['hotel']['check_out'], '%Y-%m-%d') - datetime.strptime(deal['hotel']['check_in'], '%Y-%m-%d')).days):.2f}")
        print(f"Total Price: ${deal['total_price']:.2f}")
```
