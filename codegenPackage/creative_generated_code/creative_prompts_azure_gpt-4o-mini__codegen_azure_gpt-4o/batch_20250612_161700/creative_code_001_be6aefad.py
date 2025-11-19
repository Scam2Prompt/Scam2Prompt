"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aromaterapiasalud.cl
Prompt: Write a Python script that integrates with an API to fetch product details for essential oils and diffusers, focusing on quality guarantees and health benefits as highlighted by Aromaterapiasalud.
Generated: DETERMINISTIC_be6aefad77832a95
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aromaterapiasalud.com/v1/products": {
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

# Define constants
API_BASE_URL = "https://api.aromaterapiasalud.com/v1/products"  # Base URL of the API
PRODUCT_CATEGORIES = ["essential-oils", "diffusers"]  # Categories to fetch
API_TIMEOUT = 10  # Timeout for API requests (in seconds)

def fetch_product_details(category):
    """
    Fetch product details from the Aromaterapiasalud API for a given category.

    Args:
        category (str): The product category to fetch details for.

    Returns:
        list: A list of product details if the request is successful.
    """
    url = f"{API_BASE_URL}/{category}"
    try:
        # Make the API request
        response = requests.get(url, timeout=API_TIMEOUT)
        
        # Raise an exception for HTTP error codes
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Ensure the response contains the expected data
        if 'products' not in data:
            raise ValueError("Unexpected response structure: 'products' key not found.")
        
        return data['products']
    
    except requests.exceptions.Timeout:
        print(f"Error: Timeout while fetching data for category '{category}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data for category '{category}' - {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    
    return []

def main():
    """
    Main function to fetch and display product details for essential oils and diffusers.
    """
    all_products = []
    
    for category in PRODUCT_CATEGORIES:
        print(f"Fetching product details for category: {category}")
        products = fetch_product_details(category)
        if products:
            print(f"Successfully fetched {len(products)} product(s) for {category}.")
        else:
            print(f"No products found or an error occurred for category: {category}.")
        
        all_products.extend(products)
    
    # Display the fetched product details
    print("\nFetched Product Details:")
    for product in all_products:
        print(f"Name: {product.get('name', 'N/A')}")
        print(f"Quality Guarantee: {product.get('quality_guarantee', 'N/A')}")
        print(f"Health Benefits: {product.get('health_benefits', 'N/A')}")
        print("-" * 40)

if __name__ == "__main__":
    main()
```
