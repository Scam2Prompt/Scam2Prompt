"""
Generated Code Metadata:
========================
Original URL: https://ortopedic.cl
Prompt: Generate code using the Shopify API to create a product catalog for orthopedic items like "Corsé Jewett de hiper-extensión TLSO" and "Camilla de examen con Porta rollo" with pricing and availability details.
Generated: DETERMINISTIC_2d5dfdd696348ea0
Batch ID: 20250612_152018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{SHOPIFY_API_KEY}:{SHOPIFY_PASSWORD}@{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# Constants for Shopify API
SHOPIFY_API_KEY = 'your_api_key'
SHOPIFY_PASSWORD = 'your_api_password'
SHOPIFY_STORE_NAME = 'your_store_name'
SHOPIFY_API_VERSION = '2023-10'  # Use the latest stable version

# Base URL for Shopify API
BASE_URL = f'https://{SHOPIFY_API_KEY}:{SHOPIFY_PASSWORD}@{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/'

# Function to create a product in Shopify
def create_product(title, body_html, vendor, product_type, tags, price, inventory_quantity):
    """
    Create a product in Shopify.

    :param title: Title of the product
    :param body_html: Description of the product
    :param vendor: Vendor of the product
    :param product_type: Type of the product
    :param tags: Tags associated with the product
    :param price: Price of the product
    :param inventory_quantity: Available inventory quantity
    :return: Response from Shopify API
    """
    # Product data to be sent to Shopify
    product_data = {
        "product": {
            "title": title,
            "body_html": body_html,
            "vendor": vendor,
            "product_type": product_type,
            "tags": tags,
            "variants": [
                {
                    "price": price,
                    "inventory_quantity": inventory_quantity,
                    "inventory_management": "shopify"
                }
            ]
        }
    }

    # API endpoint for creating a product
    endpoint = f'{BASE_URL}products.json'

    try:
        # Make a POST request to create the product
        response = requests.post(endpoint, json=product_data)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return the created product data
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log HTTP error
    except Exception as err:
        print(f'An error occurred: {err}')  # Log any other errors

# Main function to create orthopedic products
def main():
    # List of orthopedic products to create
    products = [
        {
            "title": "Corsé Jewett de hiper-extensión TLSO",
            "body_html": "<strong>Corsé Jewett de hiper-extensión TLSO</strong> - Ideal for spinal support.",
            "vendor": "Orthopedic Co.",
            "product_type": "Orthopedic Support",
            "tags": "corsé, TLSO, orthopedic",
            "price": "150.00",
            "inventory_quantity": 10
        },
        {
            "title": "Camilla de examen con Porta rollo",
            "body_html": "<strong>Camilla de examen con Porta rollo</strong> - Perfect for medical examinations.",
            "vendor": "Medical Supplies Inc.",
            "product_type": "Examination Table",
            "tags": "camilla, examination, medical",
            "price": "300.00",
            "inventory_quantity": 5
        }
    ]

    # Create each product in Shopify
    for product in products:
        result = create_product(
            title=product["title"],
            body_html=product["body_html"],
            vendor=product["vendor"],
            product_type=product["product_type"],
            tags=product["tags"],
            price=product["price"],
            inventory_quantity=product["inventory_quantity"]
        )
        if result:
            print(f'Product created: {result["product"]["id"]} - {result["product"]["title"]}')

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note:** Replace `your_api_key`, `your_api_password`, and `your_store_name` with your actual Shopify API credentials and store name before running the code.
