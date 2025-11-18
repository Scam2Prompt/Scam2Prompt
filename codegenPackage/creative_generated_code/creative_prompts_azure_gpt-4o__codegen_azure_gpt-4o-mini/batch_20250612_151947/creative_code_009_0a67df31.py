"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Provide instructions for adding a product category to a website catalog, referencing the "Добавить категорию товаров (Сайт-каталог 2.0)" documentation on https://ra-don.com.
Generated: DETERMINISTIC_0a67df318445cecb
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/catalog": {
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

class ProductCategoryManager:
    """
    A class to manage product categories in a website catalog.

    Attributes:
        api_url (str): The base URL for the catalog API.
        headers (dict): The headers for API requests.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the ProductCategoryManager with the API URL and key.

        Args:
            api_url (str): The base URL for the catalog API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def add_category(self, category_name, category_description):
        """
        Adds a new product category to the catalog.

        Args:
            category_name (str): The name of the category to be added.
            category_description (str): A description of the category.

        Returns:
            dict: The response from the API containing the new category data.

        Raises:
            ValueError: If the category name or description is empty.
            Exception: If there's an error during the API request.
        """
        if not category_name or not category_description:
            raise ValueError("Category name and description must not be empty.")

        category_data = {
            'name': category_name,
            'description': category_description
        }

        try:
            response = requests.post(f'{self.api_url}/categories', headers=self.headers, json=category_data)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Return the JSON response containing the category data
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Log HTTP errors
            raise
        except Exception as err:
            print(f'An error occurred: {err}')  # Log other errors
            raise

if __name__ == '__main__':
    # Example usage
    api_url = 'https://api.example.com/catalog'  # Update with actual API URL
    api_key = 'your_api_key_here'  # Update with actual API key

    category_manager = ProductCategoryManager(api_url, api_key)

    try:
        new_category = category_manager.add_category('Electronics', 'Devices and gadgets related to technology.')
        print('Category added successfully:', new_category)
    except Exception as e:
        print('Failed to add category:', e)
```
