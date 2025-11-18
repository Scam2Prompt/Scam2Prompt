"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Create a Python script to fetch and display cashback offers from over 900 online stores using an API similar to Shoppiday's.
Generated: DETERMINISTIC_2df16ecabc74a073
Batch ID: 20250612_145114
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.shoppiday.com/v1/cashback-offers": {
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

class CashbackFetcher:
    """
    A class to fetch cashback offers from an API for various online stores.
    """

    API_URL = "https://api.shoppiday.com/v1/cashback-offers"  # Example API endpoint

    def __init__(self, api_key):
        """
        Initializes the CashbackFetcher with the necessary API key.

        :param api_key: str - The API key for authenticating requests to the cashback API.
        """
        self.api_key = api_key

    def fetch_cashback_offers(self):
        """
        Fetches cashback offers from the online stores.

        :return: list - A list of cashback offers or an error message.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',  # Set the authorization header
            'Content-Type': 'application/json'  # Set content type to JSON
        }
        
        try:
            response = requests.get(self.API_URL, headers=headers)  # Make a GET request

            # Raise an exception for HTTP error responses
            response.raise_for_status()

            # Parse the JSON response
            cashback_offers = response.json()

            return cashback_offers.get('offers', [])  # Return the offers if they exist

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log request errors
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error occurred: {json_err}")  # Log JSON parsing errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

        return []  # Return an empty list in case of errors

    def display_offers(self, offers):
        """
        Displays the cashback offers in a readable format.

        :param offers: list - A list of cashback offers to display.
        """
        if not offers:
            print("No cashback offers available.")
            return
        
        print("Cashback Offers:")
        for offer in offers:
            title = offer.get('title', 'No title')
            cashback = offer.get('cashback', 'No cashback')
            store = offer.get('store', 'Unknown store')
            print(f"- {title} from {store}: {cashback}")

if __name__ == "__main__":
    # Example usage
    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    cashback_fetcher = CashbackFetcher(api_key)

    offers = cashback_fetcher.fetch_cashback_offers()  # Fetch cashback offers
    cashback_fetcher.display_offers(offers)  # Display the fetched offers
```
