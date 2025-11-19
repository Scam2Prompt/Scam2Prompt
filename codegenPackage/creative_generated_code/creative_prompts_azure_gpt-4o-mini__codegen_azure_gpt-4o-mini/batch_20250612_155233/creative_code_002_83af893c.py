"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medium.byethost10.com
Prompt: Write a Python script that utilizes the free SSL feature on iFastNet Web Hosting.
Generated: DETERMINISTIC_83af893cb9f018ac
Batch ID: 20250612_155233
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/v1/ssl": {
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

class SSLManager:
    """Class to manage SSL certificates using iFastNet Web Hosting's API."""

    def __init__(self, api_key: str):
        """
        Initializes the SSLManager with the provided API key.

        Args:
            api_key (str): The API key for authenticating requests to iFastNet.
        """
        self.api_key = api_key
        self.base_url = "https://api.ifastnet.com/v1/ssl"  # Base URL for the SSL API

    def enable_ssl(self, domain: str) -> dict:
        """
        Enables SSL for the specified domain.

        Args:
            domain (str): The domain for which to enable SSL.

        Returns:
            dict: The response from the API, containing status and message.
        """
        endpoint = f"{self.base_url}/enable"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        payload = {'domain': domain}

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
            return response.json()  # Return the JSON response from the API
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
        return {"status": "error", "message": "Failed to enable SSL"}

    def check_ssl_status(self, domain: str) -> dict:
        """
        Checks the SSL status for the specified domain.

        Args:
            domain (str): The domain for which to check SSL status.

        Returns:
            dict: The response from the API, containing status and message.
        """
        endpoint = f"{self.base_url}/status"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        payload = {'domain': domain}

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()  # Return the JSON response from the API
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
        return {"status": "error", "message": "Failed to check SSL status"}

if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual iFastNet API key
    DOMAIN = "your_domain_here"      # Replace with your domain

    ssl_manager = SSLManager(API_KEY)

    # Enable SSL for the specified domain
    enable_response = ssl_manager.enable_ssl(DOMAIN)
    print("Enable SSL Response:", enable_response)

    # Check the SSL status for the specified domain
    status_response = ssl_manager.check_ssl_status(DOMAIN)
    print("SSL Status Response:", status_response)
```
