"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxeratravel.com
Prompt: Develop an API request to fetch luxury cruise options from a travel agency, ensuring it includes details about partnerships with brands like Seabourn and Viking Cruises.
Generated: DETERMINISTIC_4d547d4b7ab9c7da
Batch ID: 20250612_161112
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.travelagency.com/v1": {
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

class CruiseAPIClient:
    """
    A client for fetching luxury cruise options from a travel agency API.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the CruiseAPIClient with the base URL and API key.

        :param base_url: The base URL for the API
        :param api_key: The API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_luxury_cruises(self, brand=None):
        """
        Fetches luxury cruise options, optionally filtered by brand.

        :param brand: The brand to filter results (e.g., 'Seabourn', 'Viking Cruises')
        :return: A list of luxury cruise options
        :raises Exception: If the API request fails
        """
        # Construct the endpoint URL
        endpoint = f"{self.base_url}/cruises/luxury"
        
        # Prepare the query parameters
        params = {
            'api_key': self.api_key,
            'brand': brand
        }

        try:
            # Make the API request
            response = requests.get(endpoint, params=params)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (e.g., 404, 500)
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            # Handle other requests-related errors
            print(f"Request error occurred: {req_err}")
            raise
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            print("Failed to decode JSON response")
            raise

# Example usage
if __name__ == "__main__":
    # Configuration for the API client
    API_BASE_URL = "https://api.travelagency.com/v1"
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Create an instance of the API client
    cruise_client = CruiseAPIClient(API_BASE_URL, API_KEY)

    # Fetch luxury cruises with brand filtering
    try:
        luxury_cruises = cruise_client.get_luxury_cruises(brand="Seabourn")
        print(json.dumps(luxury_cruises, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
