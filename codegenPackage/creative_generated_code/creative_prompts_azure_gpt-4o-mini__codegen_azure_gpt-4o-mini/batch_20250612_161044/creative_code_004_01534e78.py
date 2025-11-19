"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acessx-bitkub.blogspot.com
Prompt: Explain how to authenticate requests to the Bitkub API and provide sample code for a successful connection.
Generated: DETERMINISTIC_01534e7816a8a588
Batch ID: 20250612_161044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bitkub.com": {
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
import time
import hmac
import hashlib

class BitkubAPI:
    """A simple client to interact with the Bitkub API."""

    BASE_URL = 'https://api.bitkub.com'

    def __init__(self, api_key: str, api_secret: str):
        """
        Initializes the BitkubAPI client with provided API key and secret.
        
        :param api_key: API key for authentication
        :param api_secret: API secret for authentication
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def generate_signature(self, payload: dict) -> str:
        """
        Generates a HMAC SHA256 signature for the request payload.

        :param payload: The request payload
        :return: Hex-encoded signature
        """
        # Convert payload to a string and encode it
        payload_string = json.dumps(payload)
        # Create a HMAC SHA256 signature
        signature = hmac.new(self.api_secret.encode(), payload_string.encode(), hashlib.sha256).hexdigest()
        return signature

    def send_request(self, endpoint: str, method: str = 'GET', params: dict = None) -> dict:
        """
        Sends a request to the Bitkub API.

        :param endpoint: The API endpoint to call
        :param method: The HTTP method (GET/POST)
        :param params: The request parameters
        :return: The response from the API
        :raises Exception: If the request fails
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            'Content-Type': 'application/json',
            'X-BTKAPI-KEY': self.api_key,
            'X-BTKAPI-SIGN': self.generate_signature(params or {})
        }

        try:
            if method.upper() == 'POST':
                response = requests.post(url, json=params, headers=headers)
            else:
                response = requests.get(url, params=params, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Log and raise HTTP error
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Log and raise general error

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' and 'your_api_secret' with your actual Bitkub API credentials
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'

    bitkub_client = BitkubAPI(api_key, api_secret)

    # Example request to get server time
    try:
        response = bitkub_client.send_request('/api/market/ticker', 'GET', {'sym': 'BTC_THB'})
        print(response)  # Print the response from Bitkub API
    except Exception as e:
        print(f"Error: {e}")  # Handle any errors that occur during the request
```
