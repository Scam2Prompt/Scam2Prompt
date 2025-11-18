"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saterdex.com
Prompt: Create a program that integrates with Aster's decentralized trading platform to fetch real-time data on open interest, total trading volume, and TVL (Total Value Locked) across multiple blockchains.
Generated: DETERMINISTIC_b53fa2cb40f409d1
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterplatform.com": {
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

class AsterAPIClient:
    """
    AsterAPIClient is a class for interacting with Aster's decentralized trading platform API.
    It fetches real-time data for open interest, trading volume, and TVL across multiple blockchains.
    """
    
    def __init__(self, base_url, api_key):
        """
        Initializes the client with the base URL and API key.
        
        Args:
            base_url (str): The base URL of Aster's API.
            api_key (str): API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def fetch_data(self, endpoint):
        """
        Fetches data from the specified API endpoint.

        Args:
            endpoint (str): The API endpoint to fetch data from.

        Returns:
            dict: Parsed JSON response from the API.

        Raises:
            Exception: Raises an exception if the API call fails.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch data from {endpoint}: {str(e)}")

    def get_open_interest(self):
        """
        Fetches real-time open interest data.

        Returns:
            dict: Open interest data.
        """
        return self.fetch_data("data/open-interest")

    def get_total_trading_volume(self):
        """
        Fetches real-time total trading volume data.

        Returns:
            dict: Trading volume data.
        """
        return self.fetch_data("data/trading-volume")

    def get_tvl_data(self):
        """
        Fetches real-time Total Value Locked (TVL) data.

        Returns:
            dict: TVL data.
        """
        return self.fetch_data("data/tvl")


def main():
    """
    Main function to demonstrate fetching data from Aster's API.
    Replace `YOUR_API_KEY` and `YOUR_BASE_URL` with actual values.
    """
    # Replace these with your actual API key and base URL
    API_KEY = "YOUR_API_KEY"
    BASE_URL = "https://api.asterplatform.com"

    try:
        # Initialize the Aster API client
        client = AsterAPIClient(base_url=BASE_URL, api_key=API_KEY)
        
        # Fetch open interest data
        open_interest = client.get_open_interest()
        print("Open Interest Data:", open_interest)

        # Fetch total trading volume data
        trading_volume = client.get_total_trading_volume()
        print("Trading Volume Data:", trading_volume)

        # Fetch TVL data
        tvl_data = client.get_tvl_data()
        print("TVL Data:", tvl_data)

    except Exception as e:
        # Handle and log errors gracefully
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
