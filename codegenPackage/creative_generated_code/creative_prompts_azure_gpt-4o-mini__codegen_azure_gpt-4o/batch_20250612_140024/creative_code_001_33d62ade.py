"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgmarkazi.com
Prompt: Write a Python script that interacts with an API to fetch product details for smartphones and accessories, specifically for brands like Samsung and Huawei.
Generated: DETERMINISTIC_33d62ade90032c6b
Batch ID: 20250612_140024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/products": {
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Constants
API_URL = "https://example.com/api/products"  # Replace with the actual API endpoint
BRANDS = ["Samsung", "Huawei"]
CATEGORIES = ["Smartphones", "Accessories"]

def fetch_product_details(api_url, brands, categories):
    """
    Fetch product details from the API for specific brands and categories.

    Args:
        api_url (str): The base URL of the API.
        brands (list): List of brand names to filter.
        categories (list): List of categories to filter.

    Returns:
        list: A list of product details matching the specified filters.
    """
    try:
        # Prepare API request payload
        payload = {
            "brands": brands,
            "categories": categories
        }
        
        logging.info("Sending request to API...")
        response = requests.get(api_url, params=payload)

        # Check if the response status is OK
        if response.status_code != 200:
            logging.error(f"Failed to fetch products. Status code: {response.status_code}")
            return []

        # Parse response JSON
        data = response.json()
        logging.info(f"Received {len(data)} products from API.")
        return data

    except requests.RequestException as e:
        logging.error(f"An error occurred while making the API request: {e}")
        return []
    except ValueError as e:
        logging.error(f"Failed to parse JSON response: {e}")
        return []

def main():
    """
    Main function to retrieve product details and display them.
    """
    logging.info("Starting product details fetch script...")

    # Fetch product details
    products = fetch_product_details(API_URL, BRANDS, CATEGORIES)

    # Display product details
    if products:
        logging.info("Displaying product details:")
        for product in products:
            print(f"Name: {product.get('name', 'N/A')}")
            print(f"Brand: {product.get('brand', 'N/A')}")
            print(f"Category: {product.get('category', 'N/A')}")
            print(f"Price: ${product.get('price', 'N/A')}")
            print("-" * 40)
    else:
        logging.info("No products found.")

if __name__ == "__main__":
    main()
```
