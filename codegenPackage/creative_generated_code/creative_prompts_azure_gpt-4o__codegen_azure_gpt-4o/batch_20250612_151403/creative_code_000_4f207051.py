"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Write Python code to generate a list of eco-friendly promotional products, including customizable reusable bags, using a mock API for Grupo ProBolsa's inventory system.
Generated: DETERMINISTIC_4f207051b5f636e9
Batch ID: 20250612_151403
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mockapi.grupo-probolsa.com/inventory": {
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

# Define the base URL of the mock API
API_BASE_URL = "https://mockapi.grupo-probolsa.com/inventory"

def fetch_promotional_products():
    """
    Fetch eco-friendly promotional products from Grupo ProBolsa's inventory system.

    Returns:
        list: A list of dictionaries containing product details.
    """
    try:
        # Make a GET request to fetch the inventory data
        response = requests.get(f"{API_BASE_URL}/products")

        # Raise an exception if the request fails
        response.raise_for_status()

        # Parse the JSON response
        products = response.json()

        # Filter products to include only eco-friendly promotional items
        eco_friendly_products = [
            product for product in products
            if product.get("is_eco_friendly") and product.get("category") == "promotional"
        ]

        return eco_friendly_products

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching data from API: {e}")
        return []
    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error parsing response data: {e}")
        return []
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """
    Main execution function to display eco-friendly promotional products.
    """
    print("Fetching eco-friendly promotional products...")
    products = fetch_promotional_products()

    if not products:
        print("No eco-friendly promotional products found.")
        return

    print("Eco-friendly promotional products:")
    for product in products:
        # Display product details
        print(f"Product Name: {product.get('name')}")
        print(f"Description: {product.get('description')}")
        print(f"Price: ${product.get('price'):.2f}")
        print(f"Customizable: {'Yes' if product.get('is_customizable') else 'No'}")
        print("-" * 40)

if __name__ == "__main__":
    main()
```
