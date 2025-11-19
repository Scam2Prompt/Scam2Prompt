"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://intudesa.com
Prompt: Generate a Python script that interacts with a real estate API to search for properties in Tudela, Navarra, filtering by type such as "Casa" or "Piso" and price range.
Generated: DETERMINISTIC_81a72b506b0d6efd
Batch ID: 20250612_162325
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/properties/search": {
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

class RealEstateAPI:
    """
    A class to interact with a real estate API to search for properties.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the RealEstateAPI with necessary credentials.

        :param api_key: API key for authenticating requests
        :param base_url: Base URL of the real estate API
        """
        self.api_key = api_key
        self.base_url = base_url

    def search_properties(self, location, property_type, min_price=None, max_price=None):
        """
        Searches for properties based on given criteria.

        :param location: The location to filter properties (e.g., "Tudela, Navarra")
        :param property_type: The type of property (e.g., "Casa" or "Piso")
        :param min_price: Minimum price filter (optional)
        :param max_price: Maximum price filter (optional)
        :return: JSON response containing properties or None in case of error
        """
        try:
            # Prepare the parameters for the API request
            params = {
                'location': location,
                'type': property_type,
                'min_price': min_price,
                'max_price': max_price,
                'api_key': self.api_key
            }

            # Filter out None values from params
            params = {k: v for k, v in params.items() if v is not None}

            # Make the GET request to the real estate API
            response = requests.get(self.base_url, params=params)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Return the JSON response
            return response.json()
        except requests.RequestException as e:
            # Log the exception and return None
            print(f"Error while fetching properties: {e}")
            return None


if __name__ == "__main__":
    # Initialize the API client with your credentials
    API_KEY = 'your_api_key_here'
    BASE_URL = 'https://api.example.com/properties/search'  # Replace with the actual API endpoint

    # Create an instance of RealEstateAPI
    real_estate_api = RealEstateAPI(api_key=API_KEY, base_url=BASE_URL)

    # Set search criteria
    location = "Tudela, Navarra"
    property_type = "Casa"  # or "Piso"
    min_price = 100000      # Example minimum price
    max_price = 300000      # Example maximum price

    # Search for properties
    properties = real_estate_api.search_properties(location, property_type, min_price, max_price)

    # Check if properties were found
    if properties:
        print("Properties found:")
        for property in properties:
            print(property)
    else:
        print("No properties found or an error occurred.")
```
