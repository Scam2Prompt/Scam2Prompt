"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Generate a code snippet to integrate an API for booking outdoor advertising spaces, referencing the unique features of WOW MEDIA's digital and outdoor advertising products.
Generated: DETERMINISTIC_9716b31ec337b120
Batch ID: 20250612_163848
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wowmedia.com/v1/advertising": {
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

class WowMediaAPI:
    """
    A class to interact with the WOW MEDIA API for booking outdoor advertising spaces.
    """

    BASE_URL = "https://api.wowmedia.com/v1/advertising"
    
    def __init__(self, api_key):
        """
        Initializes the WowMediaAPI with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating requests to the WOW MEDIA API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the WOW MEDIA API.
        
        Args:
            endpoint (str): The API endpoint to call.
            method (str): The HTTP method to use (GET, POST, etc.).
            data (dict, optional): The data to send in the body of the request (for POST).

        Returns:
            Response: The response object from the requests library.

        Raises:
            Exception: Raises an exception for HTTP errors or failed requests.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method")

            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Parse and return the JSON response

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise

    def book_ad_space(self, location_id, campaign_details):
        """
        Books an advertising space at a specified location.
        
        Args:
            location_id (str): The unique identifier for the advertising location.
            campaign_details (dict): Details of the campaign to be booked.

        Returns:
            dict: The booking confirmation details from the API.
        
        Raises:
            Exception: Raises an exception for HTTP errors or failed requests.
        """
        endpoint = f"locations/{location_id}/book"
        return self._make_request(endpoint, method='POST', data=campaign_details)

    def list_available_locations(self):
        """
        Retrieves a list of available outdoor advertising locations.
        
        Returns:
            list: A list of available advertising locations.
        
        Raises:
            Exception: Raises an exception for HTTP errors or failed requests.
        """
        endpoint = "locations"
        return self._make_request(endpoint, method='GET')


# Example usage (commented out for production readiness)
# api_key = "your_api_key_here"
# wow_media_api = WowMediaAPI(api_key)
# try:
#     locations = wow_media_api.list_available_locations()
#     print("Available Locations:", locations)
#     booking_details = {
#         "campaign_name": "Summer Sale",
#         "duration": "30 days",
#         "start_date": "2023-06-01",
#     }
#     booking_confirmation = wow_media_api.book_ad_space(locations[0]['id'], booking_details)
#     print("Booking Confirmation:", booking_confirmation)
# except Exception as e:
#     print("An error occurred during the WOW MEDIA API interaction:", e)
```
