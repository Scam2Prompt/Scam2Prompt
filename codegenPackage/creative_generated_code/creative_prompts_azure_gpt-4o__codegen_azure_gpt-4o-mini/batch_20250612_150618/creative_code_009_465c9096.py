"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Suggest tools or frameworks for developing a location-based product availability feature, similar to the "Seleccione Lugar de Búsqueda" functionality on "Mass Compras."
Generated: DETERMINISTIC_465c90963ced1670
Batch ID: 20250612_150618
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.location-service.com/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://ipinfo.io/json": {
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
# location_based_availability.py

import requests

class LocationBasedAvailability:
    def __init__(self, api_key):
        """
        Initialize the LocationBasedAvailability class with API key.
        
        :param api_key: str: API key for the external location service
        """
        self.api_key = api_key
        self.base_url = "https://api.location-service.com/v1/"

    def get_user_location(self):
        """
        Retrieve user's current geographic location.

        :return: dict: A dictionary containing latitude and longitude
        :raises Exception: If the geolocation retrieval fails
        """
        try:
            # Sample geolocation API call
            response = requests.get("https://ipinfo.io/json")
            response.raise_for_status()  # Raise an error for bad responses
            location_data = response.json()
            return {
                "latitude": location_data["loc"].split(",")[0],
                "longitude": location_data["loc"].split(",")[1]
            }
        except requests.RequestException as e:
            raise Exception("Failed to retrieve user location: {}".format(e))

    def check_product_availability(self, product_id, user_location):
        """
        Check product availability based on user location.

        :param product_id: str: The ID of the product to check
        :param user_location: dict: User's location with latitude and longitude
        :return: dict: Availability information for the product
        :raises Exception: If the availability check fails
        """
        try:
            availability_url = f"{self.base_url}availability?product_id={product_id}&lat={user_location['latitude']}&lon={user_location['longitude']}&api_key={self.api_key}"
            response = requests.get(availability_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception("Failed to check product availability: {}".format(e))

    def suggest_availability(self, product_id):
        """
        Suggest the availability of a product based on user location.

        :param product_id: str: The ID of the product to check availability
        :return: dict: Suggested product availability details
        """
        try:
            user_location = self.get_user_location()
            availability_info = self.check_product_availability(product_id, user_location)
            return availability_info
        except Exception as e:
            print("Error: {}".format(e))
            return {"error": str(e)}

# Example usage:
if __name__ == '__main__':
    # Replace 'YOUR_API_KEY' with a valid API key for the location service
    location_service = LocationBasedAvailability(api_key='YOUR_API_KEY')
    
    product_id = '12345'  # Example product ID to check
    availability = location_service.suggest_availability(product_id)
    print(availability)
```
