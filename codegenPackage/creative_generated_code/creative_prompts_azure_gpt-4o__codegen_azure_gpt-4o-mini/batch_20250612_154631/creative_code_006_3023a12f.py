"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaredrop.in
Prompt: Provide an example of how to securely retrieve internet-based data using Flare's Engage feature in a blockchain application.
Generated: DETERMINISTIC_3023a12f6df6532e
Batch ID: 20250612_154631
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.flare.xyz/engage": {
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
from requests.exceptions import RequestException

class FlareEngage:
    """
    A class to interact with Flare's Engage feature to securely retrieve data.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the FlareEngage class with the given API URL and API key.

        :param api_url: The base URL for the Flare API
        :param api_key: The API key for authenticating requests
        """
        self.api_url = api_url
        self.api_key = api_key

    def retrieve_data(self, endpoint, params=None):
        """
        Retrieves data from the specified endpoint using GET request.

        :param endpoint: The API endpoint to retrieve data from
        :param params: Optional parameters to include in the request
        :return: Response data in JSON format
        :raises RequestException: If there is an error during the request
        :raises ValueError: If the response is not valid JSON
        """
        url = f"{self.api_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
        except RequestException as e:
            # Log the error or raise a custom error
            raise RequestException(f"Error retrieving data from {url}: {str(e)}")

        try:
            return response.json()  # Attempt to return JSON response
        except ValueError:
            # Raise an error if JSON decoding fails
            raise ValueError(f"Response from {url} is not valid JSON")

# Example usage:
if __name__ == "__main__":
    API_URL = "https://api.flare.xyz/engage"  # Replace with the actual API URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    flare_engage = FlareEngage(API_URL, API_KEY)
    
    try:
        data = flare_engage.retrieve_data("some_endpoint", params={"key": "value"})
        print(data)  # Handle data as needed
    except RequestException as req_err:
        print(f"Request error: {req_err}")
    except ValueError as json_err:
        print(f"JSON error: {json_err}")
```
