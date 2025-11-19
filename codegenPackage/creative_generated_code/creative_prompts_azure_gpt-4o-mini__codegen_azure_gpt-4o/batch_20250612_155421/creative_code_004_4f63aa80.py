"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Outline an API request to retrieve product details for Bicknell Racing Products available at Metal Fab Pro Race Shop, including performance parts and their features.
Generated: DETERMINISTIC_4f63aa80b1cb7283
Batch ID: 20250612_155421
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.metalfabproraceshop.com": {
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

def fetch_product_details(base_url, api_key, product_category):
    """
    Fetch product details from the Metal Fab Pro Race Shop API.

    Args:
        base_url (str): The base URL of the API.
        api_key (str): The API key for authentication.
        product_category (str): The category of products to retrieve.

    Returns:
        dict: A dictionary containing product details, or None if an error occurs.
    """
    # Set the endpoint for the API request
    endpoint = f"{base_url}/products"

    # Define the headers with the authentication details
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define the query parameters
    params = {
        "category": product_category  # Filter products by category
    }

    try:
        # Make the API request
        response = requests.get(endpoint, headers=headers, params=params)
        
        # Raise an HTTPError if the response status code is unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        product_data = response.json()
        return product_data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    # Return None if an error occurs
    return None


if __name__ == "__main__":
    # Base URL for the Metal Fab Pro Race Shop API
    BASE_URL = "https://api.metalfabproraceshop.com"

    # Your API key for authentication
    API_KEY = "your_api_key_here"

    # Category of products to fetch (e.g., "Bicknell Racing Products")
    PRODUCT_CATEGORY = "Bicknell Racing Products"

    # Fetch product details
    products = fetch_product_details(BASE_URL, API_KEY, PRODUCT_CATEGORY)

    if products:
        print("Product Details:")
        for product in products.get("data", []):
            print(f"Name: {product.get('name')}")
            print(f"Features: {product.get('features')}")
            print(f"Price: ${product.get('price')}")
            print("-" * 40)
    else:
        print("Failed to retrieve product details.")
```
