"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.host
Prompt: Create a Python script using the Shopify API to retrieve and display inventory levels for spa gift baskets and aromatherapy products in real-time on a self-care e-commerce site.
Generated: DETERMINISTIC_ae0650c989b33cb8
Batch ID: 20250612_154621
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{SHOP_NAME}.myshopify.com/admin/api/2023-10/products.json": {
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
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Shopify API configuration
SHOP_NAME = 'your-shop-name'  # Replace with your Shopify shop name
ACCESS_TOKEN = 'your-access-token'  # Replace with your Shopify access token

# Define the product types to retrieve
PRODUCT_TYPES = ['Spa Gift Baskets', 'Aromatherapy Products']

# Function to get inventory levels
def get_inventory_levels(product_types):
    """
    Retrieves inventory levels for specified product types from Shopify.

    Args:
        product_types (list): List of product types to retrieve inventory for.

    Returns:
        dict: A dictionary containing product types and their inventory levels.
    """
    inventory_levels = {}
    
    for product_type in product_types:
        try:
            # Shopify API endpoint for products
            url = f'https://{SHOP_NAME}.myshopify.com/admin/api/2023-10/products.json'
            headers = {
                'X-Shopify-Access-Token': ACCESS_TOKEN,
                'Content-Type': 'application/json'
            }

            # Send GET request to retrieve products
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            products = response.json().get('products', [])
            # Filter products by type and get their inventory levels
            for product in products:
                if product.get('product_type') == product_type:
                    variants = product.get('variants', [])
                    for variant in variants:
                        inventory_levels[variant['id']] = {
                            'title': product['title'],
                            'inventory_quantity': variant['inventory_quantity']
                        }
                    
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve products for type '{product_type}': {e}")
    
    return inventory_levels

# Main function to execute the script
def main():
    """
    Main entry point of the script.
    """
    logging.info("Retrieving inventory levels...")
    inventory = get_inventory_levels(PRODUCT_TYPES)
    
    if inventory:
        logging.info("Inventory levels retrieved successfully.")
        for variant_id, details in inventory.items():
            logging.info(f"Product: {details['title']}, Inventory: {details['inventory_quantity']}")
    else:
        logging.info("No inventory levels found for specified product types.")

if __name__ == "__main__":
    main()
```

Make sure to replace `your-shop-name` and `your-access-token` with your actual Shopify shop name and access token before running the script.
