"""
Generated Code Metadata:
========================
Original URL: https://poocoinburstfire.blogspot.com
Prompt: Create a code snippet that interacts with a shoe inventory API to filter and display options for running shoes and sandals, inspired by the categories listed on the Poocoin Burst Fire website.
Generated: DETERMINISTIC_279df84cbe7014c8
Batch ID: 20250612_162945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-shoe-api.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional

class ShoeInventoryAPI:
    """
    A class to interact with a shoe inventory API to filter and display running shoes and sandals.
    """

    def __init__(self, api_base_url: str):
        """
        Initialize the ShoeInventoryAPI with the base URL of the API.
        
        Args:
            api_base_url (str): Base URL of the shoe inventory API.
        """
        self.api_base_url = api_base_url

    def fetch_shoes_by_category(self, category: str) -> Optional[List[Dict]]:
        """
        Fetch shoes from the API filtered by category.
        
        Args:
            category (str): Category of shoes to fetch (e.g., 'running', 'sandals').
        
        Returns:
            Optional[List[Dict]]: List of shoe data in dictionary format, or None if the request fails.
        """
        try:
            response = requests.get(
                f"{self.api_base_url}/shoes",
                params={"category": category},
                timeout=10
            )
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching shoes for category {category}: {e}")
            return None

    def display_shoe_options(self, category: str) -> None:
        """
        Display shoe options for a specific category.
        
        Args:
            category (str): Category of shoes to display (e.g., 'running', 'sandals').
        """
        shoes = self.fetch_shoes_by_category(category)
        if not shoes:
            print(f"No shoes found for category: {category}")
            return

        print(f"\n===== {category.capitalize()} Shoes =====")
        for shoe in shoes:
            print(f"Name: {shoe.get('name', 'N/A')}")
            print(f"Price: ${shoe.get('price', 0):.2f}")
            print(f"Available Sizes: {', '.join(shoe.get('sizes', []))}")
            print(f"Color: {shoe.get('color', 'N/A')}")
            print("-" * 30)

# Example usage
if __name__ == "__main__":
    # Initialize the API client with the base URL
    api = ShoeInventoryAPI("https://example-shoe-api.com")

    # Display running shoes
    api.display_shoe_options("running")

    # Display sandals
    api.display_shoe_options("sandals")
```
