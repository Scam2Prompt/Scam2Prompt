"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toys-kopitsa.com.ua
Prompt: Develop a small application that allows users to filter soft toys by category, such as "М'які ляльки" or "Тварини", using the "Копиця" product API.
Generated: DETERMINISTIC_061ffa2f064db77a
Batch ID: 20250612_161112
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.kopytsia.com/toys": {
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

class ToyFilterApp:
    """
    A simple application to filter soft toys by category using the 'Копиця' product API.
    """

    BASE_URL = "https://api.kopytsia.com/toys"  # Replace with the actual API endpoint

    def __init__(self):
        """
        Initializes the ToyFilterApp instance.
        """
        self.categories = {
            "М'які ляльки": "soft_dolls",
            "Тварини": "animals"
        }

    def fetch_toys(self):
        """
        Fetches the list of toys from the API.

        Returns:
            list: A list of toys if the request is successful, otherwise raises an error.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()        # Return the JSON response
        except requests.RequestException as e:
            print(f"Error fetching toys: {e}")
            return []

    def filter_toys_by_category(self, category_key):
        """
        Filters toys by the specified category.

        Args:
            category_key (str): The category to filter by.

        Returns:
            list: A list of filtered toys that belong to the specified category.
        """
        toys = self.fetch_toys()
        category_endpoint = self.categories.get(category_key)

        if not category_endpoint:
            print(f"Category '{category_key}' not found.")
            return []

        # Filter toys based on the selected category
        filtered_toys = [toy for toy in toys if toy.get("category") == category_endpoint]
        return filtered_toys

    def display_filtered_toys(self, category_key):
        """
        Displays the filtered toys based on the category selected by the user.

        Args:
            category_key (str): The category to filter and display toys for.
        """
        filtered_toys = self.filter_toys_by_category(category_key)

        if filtered_toys:
            print(f"Toys in category '{category_key}':")
            for toy in filtered_toys:
                print(f"- {toy.get('name')} (ID: {toy.get('id')})")
        else:
            print(f"No toys found in category '{category_key}'.")


if __name__ == "__main__":
    app = ToyFilterApp()

    # Example usage
    category = "М'які ляльки"  # Change to desired category for filtering
    app.display_filtered_toys(category)
```
