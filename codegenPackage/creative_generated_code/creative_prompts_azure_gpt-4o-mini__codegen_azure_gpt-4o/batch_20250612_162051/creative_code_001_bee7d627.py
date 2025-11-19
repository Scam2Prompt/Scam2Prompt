"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Write an API call example for retrieving product details from an online airsoft store, focusing on items like MultiCam® hats and tactical patches available on Simplymente Airsoft.
Generated: DETERMINISTIC_bee7d6275bd4b9a3
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.simplymenteairsoft.com/products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.simplymenteairsoft.com/products`": {
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

def fetch_product_details(category, keywords):
    """
    Fetch product details from Simplymente Airsoft store API.

    Args:
        category (str): The category of the product (e.g., 'hats', 'patches').
        keywords (str): A keyword filter for the search (e.g., 'MultiCam').

    Returns:
        list: A list of product details matching the criteria.

    Raises:
        Exception: If the API request fails.
    """
    # Base URL of the Simplymente Airsoft API (replace with the actual endpoint)
    BASE_URL = "https://api.simplymenteairsoft.com/products"

    # Query parameters for the API request
    params = {
        "category": category,
        "search": keywords,
        "limit": 10  # Limit the results to the first 10 items
    }

    try:
        # Send GET request to the API
        response = requests.get(BASE_URL, params=params)

        # Raise an HTTPError if the status code isn't 200
        response.raise_for_status()

        # Parse the JSON response
        products = response.json()

        # Return the list of products
        return products

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        raise Exception(f"An error occurred while fetching product details: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Fetch MultiCam hats
        products = fetch_product_details(category="hats", keywords="MultiCam")
        
        # Output the fetched product details
        print("Retrieved Product Details:")
        for product in products:
            print(f"- {product['name']} (Price: {product['price']}, Stock: {product['stock']})")

    except Exception as e:
        # Handle and print any errors
        print(e)
```

> **Note:** Replace `https://api.simplymenteairsoft.com/products` with the actual API endpoint of Simplymente Airsoft, as this is a placeholder URL. Also, ensure that the response structure (e.g., `product['name']`, `product['price']`, `product['stock']`) matches the real API output.
