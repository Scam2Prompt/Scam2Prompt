"""
Generated Code Metadata:
========================
Original URL: https://kgtrading.co.jp
Prompt: The webpage does not contain relevant technical content for generating prompts related to code, APIs, or libraries.
Generated: DETERMINISTIC_b98e58080c5b66c2
Batch ID: 20250612_150653
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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

class APIClient:
    """
    A simple API client to interact with a RESTful API.
    """

    def __init__(self, base_url):
        """
        Initializes the API client with a base URL.

        :param base_url: The base URL of the API.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.

        :param endpoint: The API endpoint to send the request to.
        :param params: Optional dictionary of query parameters.
        :return: The response data in JSON format.
        :raises: Exception if the request fails or returns an error.
        """
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"GET request failed: {e}")

    def post(self, endpoint, data=None):
        """
        Sends a POST request to the specified endpoint.

        :param endpoint: The API endpoint to send the request to.
        :param data: Optional dictionary of data to send in the body.
        :return: The response data in JSON format.
        :raises: Exception if the request fails or returns an error.
        """
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"POST request failed: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the API client with the base URL
    api_client = APIClient("https://api.example.com")

    # Example GET request
    try:
        data = api_client.get("data")
        print("GET response:", data)
    except Exception as e:
        print(e)

    # Example POST request
    try:
        payload = {"key": "value"}
        response = api_client.post("data", data=payload)
        print("POST response:", response)
    except Exception as e:
        print(e)
```
