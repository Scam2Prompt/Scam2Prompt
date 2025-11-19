"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinburstfire.blogspot.com
Prompt: Create a code snippet that interacts with a shoe inventory API to filter and display options for running shoes and sandals, inspired by the categories listed on the Poocoin Burst Fire website.
Generated: DETERMINISTIC_279df84cbe7014c8
Batch ID: 20250612_162945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.shoeinventory.com/v1": {
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

class ShoeInventoryAPI:
    """
    A class to interact with the shoe inventory API.
    """

    BASE_URL = "https://api.shoeinventory.com/v1"

    def __init__(self):
        """
        Initializes the ShoeInventoryAPI class.
        """
        self.session = requests.Session()

    def fetch_shoes(self, category):
        """
        Fetches shoes from the inventory based on the specified category.

        Parameters:
        category (str): The category of shoes to filter (e.g., 'running', 'sandals').

        Returns:
        list: A list of shoes in the specified category.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/shoes", params={"category": category})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('shoes', [])
        except requests.RequestException as e:
            print(f"Error fetching shoes: {e}")
            return []

    def display_shoes(self, shoes):
        """
        Displays the shoes in a readable format.

        Parameters:
        shoes (list): A list of shoe dictionaries to display.
        """
        if not shoes:
            print("No shoes found.")
            return

        print(f"{'Brand':<15} {'Model':<20} {'Price':<10}")
        print("-" * 45)
        for shoe in shoes:
            print(f"{shoe['brand']:<15} {shoe['model']:<20} ${shoe['price']:<10.2f}")

def main():
    """
    Main function to run the shoe inventory filter and display.
    """
    api = ShoeInventoryAPI()

    # Fetch and display running shoes
    print("Running Shoes:")
    running_shoes = api.fetch_shoes('running')
    api.display_shoes(running_shoes)

    print("\nSandals:")
    # Fetch and display sandals
    sandals = api.fetch_shoes('sandals')
    api.display_shoes(sandals)

if __name__ == "__main__":
    main()
```
