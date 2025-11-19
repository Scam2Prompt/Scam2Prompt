"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Write a Python function that retrieves and displays product information from an API for a company specializing in organic and medicinal plants, similar to Oromáticas.
Generated: DETERMINISTIC_901d7c2235b18204
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/products": {
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

class ProductAPIError(Exception):
    """Custom exception for API errors."""
    pass

def fetch_product_info(api_url):
    """
    Fetches product information from the specified API.

    Args:
        api_url (str): The URL of the API endpoint.

    Returns:
        list: A list of product information dictionaries.

    Raises:
        ProductAPIError: If an error occurs while fetching data from the API.
        ValueError: If the API response is not valid.
    """
    
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        
        # Raise an error for bad responses
        response.raise_for_status()
        
        # Parse the JSON response
        product_data = response.json()

        # Validate the response structure
        if not isinstance(product_data, list):
            raise ValueError("API response is not a valid list.")

        return product_data

    except requests.exceptions.HTTPError as http_err:
        raise ProductAPIError(f"HTTP error occurred: {http_err}") from http_err
    except ValueError as val_err:
        raise ProductAPIError(f"Value error occurred: {val_err}") from val_err
    except Exception as err:
        raise ProductAPIError(f"An unexpected error occurred: {err}") from err


def display_product_info(product_info):
    """
    Displays the product information in a readable format.

    Args:
        product_info (list): A list of product information dictionaries.
    """
    
    if not product_info:
        print("No product information available.")
        return

    for product in product_info:
        try:
            # Extract and display relevant product information
            name = product.get('name', 'N/A')
            description = product.get('description', 'N/A')
            price = product.get('price', 'N/A')
            availability = product.get('availability', 'N/A')

            print(f"Product Name: {name}")
            print(f"Description: {description}")
            print(f"Price: {price}")
            print(f"Availability: {availability}")
            print("-" * 40)  # Separator line
        except Exception as e:
            print(f"Error displaying product data: {e}")


if __name__ == "__main__":
    # Example API URL (replace with the actual API endpoint)
    api_url = "https://api.example.com/products"

    try:
        products = fetch_product_info(api_url)
        display_product_info(products)
    except ProductAPIError as api_err:
        print(f"Failed to retrieve product information: {api_err}")
```
