"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-market.pages.dev
Prompt: Generate a script to interact with the Guildhall API for retrieving liquidity pool data and displaying it in a user-friendly format.
Generated: DETERMINISTIC_dc1d527b648c7d2b
Batch ID: 20250612_152018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.guildhall.io/v1": {
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

class GuildhallAPI:
    BASE_URL = "https://api.guildhall.io/v1"

    def __init__(self):
        """Initialize the GuildhallAPI class."""
        pass

    def get_liquidity_pools(self):
        """Retrieve liquidity pool data from the Guildhall API.

        Returns:
            dict: A dictionary containing liquidity pool data.
            Raises:
                requests.exceptions.RequestException: If an error occurs during the API request.
        """
        endpoint = f"{self.BASE_URL}/liquidity_pools"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse and return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving liquidity pools: {e}")
            return None  # Return None if an error occurs

    def display_liquidity_pools(self, liquidity_pools):
        """Display liquidity pool data in a user-friendly format.

        Args:
            liquidity_pools (dict): The liquidity pool data to display.
        """
        if liquidity_pools is None or len(liquidity_pools) == 0:
            print("No liquidity pool data available.")
            return
        
        print(f"{'Pool Name':<30} {'Liquidity':<20} {'Volume':<20}")
        print("="*70)
        for pool in liquidity_pools.get("data", []):
            name = pool.get("name", "N/A")
            liquidity = pool.get("liquidity", "N/A")
            volume = pool.get("volume", "N/A")
            print(f"{name:<30} {liquidity:<20} {volume:<20}")

def main():
    """Main function to execute the script."""
    api = GuildhallAPI()
    liquidity_pools = api.get_liquidity_pools()  # Fetch liquidity pool data
    api.display_liquidity_pools(liquidity_pools)  # Display the data

if __name__ == "__main__":
    main()  # Run the main function
```
