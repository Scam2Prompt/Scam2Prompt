"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimihao.cc
Prompt: Generate a Python script to interact with the "秘密号" service for managing dynamic residential IPs.
Generated: DETERMINISTIC_3c36d30e1397c1a4
Batch ID: 20250612_155955
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.secretnumber.com": {
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

class SecretNumberService:
    """A class to interact with the 秘密号 service for managing dynamic residential IPs."""

    def __init__(self, api_key: str, base_url: str = "https://api.secretnumber.com"):
        """
        Initializes the service with the provided API key and base URL.

        Args:
            api_key (str): The API key for authenticating with the 秘密号 service.
            base_url (str): The base URL of the 秘密号 API. Default is the production URL.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint: str, method: str = 'GET', data: dict = None):
        """
        Makes an HTTP request to the 秘密号 API.

        Args:
            endpoint (str): The API endpoint to interact with.
            method (str): The HTTP method to use (GET, POST, etc.). Default is GET.
            data (dict): The data to send with the request. Default is None.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: Raises an exception for any HTTP error responses.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle general request errors

    def get_dynamic_ip(self):
        """Retrieves a dynamic residential IP from the 秘密号 service."""
        return self._make_request("dynamic_ip", method='GET')

    def release_dynamic_ip(self, ip: str):
        """Releases a previously allocated dynamic residential IP.

        Args:
            ip (str): The IP address to release.
        """
        data = {"ip": ip}
        self._make_request("release_ip", method='POST', data=data)

    def allocate_dynamic_ip(self):
        """Allocates a new dynamic residential IP."""
        return self._make_request("allocate_ip", method='POST')

# Example usage:
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    service = SecretNumberService(api_key=API_KEY)

    try:
        # Allocating a new dynamic IP
        new_ip = service.allocate_dynamic_ip()
        print(f"Allocated new IP: {new_ip}")

        # Getting current dynamic IP
        current_ip = service.get_dynamic_ip()
        print(f"Current dynamic IP: {current_ip}")

        # Releasing the allocated IP
        service.release_dynamic_ip(new_ip['ip'])
        print(f"Released IP: {new_ip['ip']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
