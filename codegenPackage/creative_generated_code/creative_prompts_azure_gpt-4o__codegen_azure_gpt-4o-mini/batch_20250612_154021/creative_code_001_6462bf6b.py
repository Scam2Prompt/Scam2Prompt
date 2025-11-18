"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectvox.pages.dev
Prompt: Create a script to check the rarity of items or roles within a blockchain-based guild system, referencing features like "Check Rarity" from the Guildhall website.
Generated: DETERMINISTIC_6462bf6b3125f621
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.guildhall.io/v1/items": {
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

class GuildItemRarityChecker:
    """A class to check the rarity of items in a blockchain-based guild system."""

    BASE_API_URL = "https://api.guildhall.io/v1/items"

    def __init__(self, api_key):
        """Initialize the checker with a given API key."""
        self.api_key = api_key

    def fetch_item_data(self, item_id):
        """Fetch item data from the Guildhall API.

        Args:
            item_id (str): The ID of the item to fetch.

        Returns:
            dict: A dictionary containing item data.

        Raises:
            ValueError: If the item ID is invalid or not found.
            Exception: For other unexpected errors.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = requests.get(f"{self.BASE_API_URL}/{item_id}", headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()

            if 'error' in data:
                raise ValueError(data['error'])

            return data
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except ValueError as value_err:
            print(f"Value error occurred: {value_err}")
            raise
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
            raise

    def check_rarity(self, item_id):
        """Check the rarity of the specified item.

        Args:
            item_id (str): The ID of the item to check.

        Returns:
            str: A string representing the rarity of the item.
        """
        item_data = self.fetch_item_data(item_id)
        rarity = item_data.get('rarity', 'Unknown rarity')
        return rarity

def main():
    # Example usage of the GuildItemRarityChecker class
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    item_id = "example_item_id"  # Replace with the actual item ID to check

    rarity_checker = GuildItemRarityChecker(api_key=API_KEY)

    try:
        rarity = rarity_checker.check_rarity(item_id)
        print(f"The rarity of the item with ID {item_id} is: {rarity}")
    except Exception as e:
        print(f"Failed to check rarity: {e}")

if __name__ == "__main__":
    main()
```
