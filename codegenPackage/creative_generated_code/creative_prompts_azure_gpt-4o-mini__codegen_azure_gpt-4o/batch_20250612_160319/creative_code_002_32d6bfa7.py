"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suplementosdeaz.blogspot.com
Prompt: How can I implement an API call to fetch the latest prices for "Max Titanium Top Whey 3w" protein supplements listed on suplementosdeaz?
Generated: DETERMINISTIC_32d6bfa7e98b32d7
Batch ID: 20250612_160319
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://suplementosdeaz.com/api/products`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://suplementosdeaz.com/api/products": {
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

def fetch_latest_prices(product_name, base_url="https://suplementosdeaz.com/api/products"):
    """
    Fetches the latest prices for a given product from Suplementos de Az API.

    Args:
        product_name (str): Name of the product to search for.
        base_url (str): Base URL for the API endpoint. Defaults to Suplementos de Az API.
    
    Returns:
        list: A list of dictionaries containing product information including prices.
    
    Raises:
        ValueError: If the product name is empty or missing.
        requests.exceptions.RequestException: If there is a network-related error.
    """
    if not product_name:
        raise ValueError("Product name must not be empty.")

    try:
        # Define the query parameters for the API call
        params = {"search": product_name}

        # Make the GET request to the API
        response = requests.get(base_url, params=params)

        # Raise an exception for HTTP error responses
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract relevant product information
        products = [
            {
                "name": item.get("name"),
                "price": item.get("price"),
                "currency": item.get("currency"),
                "url": item.get("url")
            }
            for item in data.get("products", [])
            if product_name.lower() in item.get("name", "").lower()
        ]

        return products

    except requests.exceptions.RequestException as e:
        # Log the detailed error message and raise
        raise RuntimeError(f"Failed to fetch product prices: {e}")

# Example usage
if __name__ == "__main__":
    try:
        product_name = "Max Titanium Top Whey 3w"
        prices = fetch_latest_prices(product_name)
        
        # Print the fetched product information
        if prices:
            print(f"Prices for '{product_name}':")
            for product in prices:
                print(f"- {product['name']} | {product['price']} {product['currency']} | URL: {product['url']}")
        else:
            print(f"No products found for '{product_name}'.")
    except Exception as error:
        print(f"Error: {error}")
```

- Make sure to replace `https://suplementosdeaz.com/api/products` with the actual API endpoint URL provided by Suplementos de Az if it differs.
- Ensure proper API access permissions (e.g., API keys or authentication) are set up if required.
