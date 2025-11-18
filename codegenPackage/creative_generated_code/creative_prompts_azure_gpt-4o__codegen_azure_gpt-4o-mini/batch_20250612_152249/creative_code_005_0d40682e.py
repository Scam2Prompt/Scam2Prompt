"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibqsvjqfvqtsrjjykxkbbgwkxnz32gxfxyrhaa4y5d3xr67l6gnzq.ipfs.dweb.link
Prompt: Suggest tools or libraries to compute and display pricing for digital assets, as hinted at in the FantasyTop Pack content.
Generated: DETERMINISTIC_0d40682e8194c711
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/digital-assets/prices": {
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

class DigitalAssetPricing:
    """
    A class to compute and display pricing for digital assets using public APIs.
    """

    def __init__(self, api_url):
        """
        Initializes the DigitalAssetPricing instance with the API URL.

        Parameters:
        api_url (str): The URL of the API to fetch digital asset prices.
        """
        self.api_url = api_url

    def fetch_asset_prices(self):
        """
        Fetches the current prices of digital assets from the API.

        Returns:
        dict: A dictionary containing asset prices if the request is successful.
        None: If the request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response as a dictionary
        except requests.exceptions.RequestException as e:
            print(f"Error fetching asset prices: {e}")
            return None

    def display_prices(self, asset_data):
        """
        Displays the asset prices in a user-friendly format.

        Parameters:
        asset_data (dict): A dictionary containing asset prices to display.
        """
        if asset_data is None:
            print("No asset data available to display.")
            return
        
        print("Current Digital Asset Prices:")
        for asset, price in asset_data.items():
            print(f"{asset}: ${price:.2f}")  # Format price to 2 decimal places

    def run(self):
        """
        Executes the pricing computation and display process.
        """
        asset_data = self.fetch_asset_prices()
        self.display_prices(asset_data)


if __name__ == "__main__":
    # Example API URL for fetching digital asset prices
    API_URL = "https://api.example.com/digital-assets/prices"
    
    # Create an instance of the DigitalAssetPricing class
    pricing_tool = DigitalAssetPricing(API_URL)
    
    # Run the pricing computation and display
    pricing_tool.run()
```
