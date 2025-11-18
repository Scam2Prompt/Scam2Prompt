"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fiberproximus.be
Prompt: Develop a script to integrate Fiberdeals' promotional offers into a mobile app, focusing on Flex packs with internet, mobile, and TV.
Generated: DETERMINISTIC_8ae3d3dc834bec68
Batch ID: 20250612_151509
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fiberdeals.com/v1/offers": {
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

class FiberDealsAPI:
    """
    A class to interact with the Fiberdeals API to fetch promotional offers.
    """

    BASE_URL = "https://api.fiberdeals.com/v1/offers"

    def __init__(self, api_key):
        """
        Initializes the FiberDealsAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Fiberdeals API.
        """
        self.api_key = api_key

    def get_flex_packs(self):
        """
        Fetches Flex packs that include internet, mobile, and TV offers.

        Returns:
            list: A list of Flex pack offers if successful, otherwise an empty list.
        """
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(self.BASE_URL, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            offers = response.json().get('offers', [])
            flex_packs = self._filter_flex_packs(offers)
            return flex_packs
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return []
        except Exception as err:
            print(f"An error occurred: {err}")
            return []

    def _filter_flex_packs(self, offers):
        """
        Filters the offers to only include Flex packs with internet, mobile, and TV.

        Args:
            offers (list): The list of offers to filter.

        Returns:
            list: A list of filtered Flex pack offers.
        """
        flex_packs = []
        for offer in offers:
            if (offer.get('type') == 'Flex' and
                    'internet' in offer.get('features', []) and
                    'mobile' in offer.get('features', []) and
                    'TV' in offer.get('features', [])):
                flex_packs.append(offer)
        return flex_packs


def main():
    """
    Main function to run the FiberDeals API integration.
    """
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    fiber_deals = FiberDealsAPI(api_key)
    
    flex_packs = fiber_deals.get_flex_packs()
    
    if flex_packs:
        print("Flex Packs with Internet, Mobile, and TV offers:")
        for index, pack in enumerate(flex_packs, start=1):
            print(f"{index}. {pack['name']}: {pack['description']}")
    else:
        print("No Flex packs found or an error occurred.")


if __name__ == "__main__":
    main()
```
