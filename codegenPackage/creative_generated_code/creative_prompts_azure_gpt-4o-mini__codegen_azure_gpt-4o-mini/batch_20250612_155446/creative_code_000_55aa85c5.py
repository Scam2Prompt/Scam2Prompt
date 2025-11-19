"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiakert.com
Prompt: Generate a Python script that utilizes an API to fetch health and wellness product data similar to those offered by EnergiaKert.
Generated: DETERMINISTIC_55aa85c5e00d0b46
Batch ID: 20250612_155446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/products": {
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

class HealthWellnessAPI:
    """
    A class to interact with the Health and Wellness API.
    This class provides methods to fetch product data similar to EnergiaKert.
    """

    BASE_URL = "https://api.example.com/products"  # Replace with actual API endpoint

    def __init__(self, api_key):
        """
        Initialize the HealthWellnessAPI class with an API key.

        :param api_key: str: The API key for authenticating requests.
        """
        self.api_key = api_key

    def fetch_product_data(self):
        """
        Fetches health and wellness product data from the API.

        :return: dict: The product data retrieved from the API.

        :raises Exception: If the API request fails or returns an error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(self.BASE_URL, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return the response data as JSON

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise Exception("Failed to fetch product data from the API.") from http_err
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log the error
            raise Exception("Error occurred while making the request.") from req_err

def main():
    """
    Main function to execute the script and fetch product data.
    """
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    wellness_api = HealthWellnessAPI(api_key=API_KEY)

    try:
        product_data = wellness_api.fetch_product_data()
        print(json.dumps(product_data, indent=4))  # Pretty print the product data

    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any exceptions raised during execution

if __name__ == "__main__":
    main()
```
