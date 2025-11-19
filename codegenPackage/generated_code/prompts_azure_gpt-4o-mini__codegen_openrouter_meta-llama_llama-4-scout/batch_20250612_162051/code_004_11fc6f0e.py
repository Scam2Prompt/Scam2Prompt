"""
Generated Code Metadata:
========================
Original URL: https://www.hostalcasadelmar.es
Prompt: Design a code snippet that fetches and displays breakfast menu items from a restaurant API, inspired by the offerings at the Restobar of Hostal Casa del Mar.
Generated: DETERMINISTIC_11fc6f0e0beebd59
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/restaurant-api": {
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
import json

class RestaurantAPI:
    def __init__(self, api_url, api_key=None):
        """
        Initialize the RestaurantAPI class.

        Args:
            api_url (str): The URL of the restaurant API.
            api_key (str, optional): The API key for authentication. Defaults to None.
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_breakfast_menu(self):
        """
        Fetch breakfast menu items from the restaurant API.

        Returns:
            list: A list of breakfast menu items.

        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        try:
            headers = {}
            if self.api_key:
                headers['Authorization'] = f"Bearer {self.api_key}"

            response = requests.get(f"{self.api_url}/breakfast-menu", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

def display_breakfast_menu(menu_items):
    """
    Display breakfast menu items.

    Args:
        menu_items (list): A list of breakfast menu items.
    """
    if not menu_items:
        print("No breakfast menu items available.")
        return

    print("Breakfast Menu:")
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item['name']}: ${item['price']}")
        print(f"  - {item['description']}")

def main():
    api_url = "https://example.com/restaurant-api"  # Replace with the actual API URL
    api_key = "your_api_key"  # Replace with the actual API key

    restaurant_api = RestaurantAPI(api_url, api_key)
    menu_items = restaurant_api.get_breakfast_menu()
    display_breakfast_menu(menu_items)

if __name__ == "__main__":
    main()
```
