"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Write a Python script using the WooCommerce API to fetch product details, including categories like "Tusser silk saree" and "Madhubani Painting Suit with Dupatta," from an eCommerce WordPress site like Weavely.
Generated: DETERMINISTIC_5829b7d9eb4b3cf0
Batch ID: 20250612_150327
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://weavely.com/wp-json/wc/v3/products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://weavely.com/wp-json/wc/v3/products`.": {
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
from requests.auth import HTTPBasicAuth

# Define WooCommerce API credentials and endpoint
API_URL = "https://weavely.com/wp-json/wc/v3/products"
CONSUMER_KEY = "your_consumer_key"  # Replace with your WooCommerce consumer key
CONSUMER_SECRET = "your_consumer_secret"  # Replace with your WooCommerce consumer secret

# Define the categories to filter products
TARGET_CATEGORIES = ["Tusser silk saree", "Madhubani Painting Suit with Dupatta"]

def fetch_products():
    """
    Fetch product details from WooCommerce API for specific categories.
    Returns:
        list: A list of product details from the target categories.
    """
    try:
        # Make GET request to WooCommerce API with basic authentication
        response = requests.get(API_URL, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
        
        # Handle HTTP errors
        response.raise_for_status()
        
        # Parse JSON response
        products = response.json()
        
        # Filter products based on target categories
        filtered_products = []
        for product in products:
            for category in product.get('categories', []):
                if category.get('name') in TARGET_CATEGORIES:
                    filtered_products.append(product)
                    break
        
        return filtered_products
    
    except requests.exceptions.RequestException as e:
        # Log and re-raise exceptions for proper error handling
        print(f"Error fetching products: {e}")
        raise

def main():
    """
    Main function to fetch and display product details.
    """
    try:
        # Fetch products from WooCommerce API
        products = fetch_products()
        
        # Display product details
        if products:
            print("Products in target categories:")
            for product in products:
                print(f"Name: {product['name']}")
                print(f"Price: {product.get('price', 'N/A')}")
                print(f"Category: {[cat['name'] for cat in product.get('categories', [])]}")
                print(f"Stock Status: {product.get('stock_status', 'N/A')}")
                print("="*40)
        else:
            print("No products found in the target categories.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `your_consumer_key` and `your_consumer_secret` with your actual WooCommerce API credentials.
2. The script assumes the WooCommerce API is accessible at `https://weavely.com/wp-json/wc/v3/products`. Update the `API_URL` if your WooCommerce site uses a different structure.
3. Install the `requests` library if not already available: `pip install requests`.
4. Ensure your WooCommerce API credentials have the necessary permissions to access product data.
