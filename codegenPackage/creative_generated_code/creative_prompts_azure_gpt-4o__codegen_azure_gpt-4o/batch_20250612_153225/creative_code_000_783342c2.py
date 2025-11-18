"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Write Python code using the Shopify API to create a product listing for a "Travis Scott Cactus Jack Hoodie" with attributes like price, description, and images.
Generated: DETERMINISTIC_783342c2007d8209
Batch ID: 20250612_153225
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/cactus_jack_hoodie_front.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/cactus_jack_hoodie_back.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/2023-01": {
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
import shopify
import os

# Function to create a new Shopify product
def create_shopify_product(product_title, product_description, product_price, product_images):
    try:
        # Initialize Shopify API session
        # Replace these variables with your Shopify store credentials
        API_KEY = os.getenv("SHOPIFY_API_KEY")  # Set your Shopify API key in an environment variable
        PASSWORD = os.getenv("SHOPIFY_API_PASSWORD")  # Set your API password in an environment variable
        SHOP_NAME = os.getenv("SHOPIFY_SHOP_NAME")  # Your Shopify shop name

        shopify.ShopifyResource.set_site(f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/2023-01")  # Adjust API version as needed

        # Create a new product object
        new_product = shopify.Product()
        new_product.title = product_title  # Set product title
        new_product.body_html = product_description  # Set product description

        # Add price as a variant
        variant = shopify.Variant()
        variant.price = product_price
        new_product.variants = [variant]

        # Attach images to the product
        new_product.images = []
        for image_url in product_images:
            product_image = shopify.Image()
            product_image.src = image_url  # URL of the product image
            new_product.images.append(product_image)

        # Save the product to Shopify
        if new_product.save():
            print(f"Product '{product_title}' created successfully!")
            return new_product.id  # Return the product ID
        else:
            print("Failed to create product. Errors:", new_product.errors.full_messages)
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Product details
    product_title = "Travis Scott Cactus Jack Hoodie"
    product_description = """This premium hoodie features the iconic Cactus Jack logo, designed by Travis Scott.
Perfect for fans and streetwear enthusiasts."""
    product_price = "120.00"  # Price in USD
    product_images = [
        "https://example.com/images/cactus_jack_hoodie_front.jpg",
        "https://example.com/images/cactus_jack_hoodie_back.jpg"
    ]

    # Create product using the Shopify API
    product_id = create_shopify_product(product_title, product_description, product_price, product_images)

    if product_id:
        print(f"Created product with ID: {product_id}")
    else:
        print("Product creation failed.")
```

**Note**: Before running this code, you need to install the `shopifyapi` Python package (`pip install shopifyapi`) and set up your Shopify store credentials. Ensure your environment variables (`SHOPIFY_API_KEY`, `SHOPIFY_API_PASSWORD`, `SHOPIFY_SHOP_NAME`) are correctly configured.
