"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Write a code snippet for a travel booking application that integrates with a tour package API for Ayodhya tours from major Indian cities.
Generated: DETERMINISTIC_0134cb895cd7e9c0
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tourpackages.com/v1": {
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

class TourPackageAPI:
    """
    A class to interact with the Tour Package API
    for booking Ayodhya tours from major Indian cities.
    """
    
    BASE_URL = "https://api.tourpackages.com/v1"  # Replace with the actual API URL

    def __init__(self, api_key):
        """
        Initializes the API client with an API key.
        
        :param api_key: API key for authenticating requests.
        """
        self.api_key = api_key

    def get_tour_packages(self, city):
        """
        Fetches available tour packages for Ayodhya from the specified city.
        
        :param city: The city from which the tour starts.
        :return: List of tour packages or error message.
        """
        url = f"{self.BASE_URL}/packages/ayodhya?city={city}"
        headers = {'Authorization': f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors

            packages = response.json()  # Parse the JSON response
            return packages

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as err:
            return f"Error occurred: {err}"
        except ValueError as json_err:
            return f"JSON decoding failed: {json_err}"

class TravelBooking:
    """
    A class to handle the travel booking process.
    """
    
    def __init__(self, api_key):
        """
        Initializes the TravelBooking class with an API key.
        
        :param api_key: API key for the Tour Package API.
        """
        self.api_client = TourPackageAPI(api_key)

    def find_tours(self, city):
        """
        Finds and displays tour packages for Ayodhya based on the given city.
        
        :param city: The city from which the tour starts.
        """
        print(f"Searching for Ayodhya tour packages from {city}...")
        tour_packages = self.api_client.get_tour_packages(city)

        if isinstance(tour_packages, list):
            print("Available tour packages:")
            for idx, package in enumerate(tour_packages, start=1):
                print(f"{idx}. {package['name']} - Price: {package['price']}")
        else:
            print(tour_packages)  # Print the error message

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    travel_booking = TravelBooking(API_KEY)
    
    # Find tours from a specific city
    city_input = input("Enter your city: ")
    travel_booking.find_tours(city_input)
```
