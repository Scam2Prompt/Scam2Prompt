"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pc.bigwhales.com
Prompt: Generate a script to fetch real-time data for gold and oil prices using an API that aligns with Bigwhales' investment platform capabilities.
Generated: DETERMINISTIC_72185856560c5e44
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/commodities": {
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
from datetime import datetime


class InvestmentDataFetcher:
    """
    A class to fetch real-time data for gold and oil prices using an external API.
    Designed to align with Bigwhales' investment platform capabilities.
    """

    def __init__(self, api_url: str, api_key: str):
        """
        Initialize the InvestmentDataFetcher with API credentials.

        :param api_url: The base URL of the API to fetch data.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def fetch_data(self, commodity: str) -> dict:
        """
        Fetch real-time data for the specified commodity.

        :param commodity: The commodity to fetch data for (e.g., 'gold', 'oil').
        :return: A dictionary containing the fetched data.
        """
        try:
            # Construct the API endpoint URL
            endpoint = f"{self.api_url}/{commodity}/price"

            # Set up headers for the API request
            headers = {"Authorization": f"Bearer {self.api_key}"}

            # Send GET request to the API
            response = requests.get(endpoint, headers=headers)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()
            return data

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")
        except json.JSONDecodeError as json_err:
            print(f"Error decoding JSON response: {json_err}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
        return {}

    def format_data(self, data: dict) -> str:
        """
        Format the fetched data for display or logging.

        :param data: The raw data dictionary.
        :return: A formatted string representation of the data.
        """
        try:
            # Extract key details from the data
            price = data.get("price", "N/A")
            currency = data.get("currency", "N/A")
            timestamp = data.get("timestamp", None)

            # Convert timestamp to a readable format if available
            if timestamp:
                timestamp = datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M:%S")

            formatted_data = f"Price: {price} {currency}\nLast Updated: {timestamp}"
            return formatted_data

        except Exception as err:
            print(f"Error formatting data: {err}")
            return "Error formatting data."

    def fetch_and_display(self, commodity: str):
        """
        Fetch and display real-time data for the specified commodity.

        :param commodity: The commodity to fetch data for (e.g., 'gold', 'oil').
        """
        print(f"Fetching data for {commodity.capitalize()}...")
        data = self.fetch_data(commodity)

        if data:
            formatted_data = self.format_data(data)
            print(f"\nReal-Time {commodity.capitalize()} Data:\n{formatted_data}")
        else:
            print("Failed to fetch data.")


# Example usage
if __name__ == "__main__":
    # Replace with your actual API URL and API key
    API_URL = "https://api.example.com/commodities"
    API_KEY = "your_api_key_here"

    # Initialize the data fetcher
    fetcher = InvestmentDataFetcher(API_URL, API_KEY)

    # Fetch and display real-time gold and oil data
    fetcher.fetch_and_display("gold")
    fetcher.fetch_and_display("oil")
```
