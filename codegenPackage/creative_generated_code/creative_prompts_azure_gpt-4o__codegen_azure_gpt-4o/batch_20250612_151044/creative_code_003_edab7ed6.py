"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Write a script to simulate a search functionality for Jiomart Digital's 20,000+ products, allowing users to filter by category, price range, and brand.
Generated: DETERMINISTIC_edab7ed6c0e6bd42
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample dataset representing Jiomart Digital's products (normally fetched from a database)
PRODUCTS = [
    {"id": 1, "name": "Smartphone A", "category": "Electronics", "brand": "BrandX", "price": 14999},
    {"id": 2, "name": "Laptop B", "category": "Electronics", "brand": "BrandY", "price": 59999},
    {"id": 3, "name": "Vacuum Cleaner C", "category": "Home Appliances", "brand": "BrandZ", "price": 7999},
    {"id": 4, "name": "Mixer Grinder D", "category": "Home Appliances", "brand": "BrandX", "price": 3499},
    # More products should be added here to simulate a larger dataset.
]

def search_products(category=None, price_range=None, brand=None):
    """
    Filters products based on category, price range, and brand.
    
    Args:
        category (str): Filter by category (e.g., 'Electronics', 'Home Appliances').
        price_range (tuple): A tuple of (min_price, max_price) to filter products within a price range.
        brand (str): Filter by brand (e.g., 'BrandX', 'BrandY').
    
    Returns:
        list: A list of filtered products matching the search criteria.
    """
    try:
        # Start with all products
        filtered_products = PRODUCTS

        # Filter by category (if specified)
        if category:
            filtered_products = [product for product in filtered_products if product["category"] == category]

        # Filter by price range (if specified)
        if price_range:
            min_price, max_price = price_range
            filtered_products = [
                product for product in filtered_products if min_price <= product["price"] <= max_price
            ]

        # Filter by brand (if specified)
        if brand:
            filtered_products = [product for product in filtered_products if product["brand"] == brand]

        return filtered_products

    except Exception as e:
        # Log error and return an empty list
        print(f"Error occurred during search: {e}")
        return []

def main():
    """
    Main function to demonstrate the product search functionality.
    """
    print("Welcome to Jiomart Digital Product Search!")

    # Example filters (input can be taken from users in production)
    category = input("Enter product category (or leave blank): ").strip() or None
    price_range_input = input("Enter price range (e.g., 1000-5000 or leave blank): ").strip()
    price_range = (
        tuple(map(int, price_range_input.split('-'))) if price_range_input else None
    )
    brand = input("Enter product brand (or leave blank): ").strip() or None

    # Perform the search
    results = search_products(category, price_range, brand)

    # Display results
    if results:
        print(f"\nFound {len(results)} products:")
        print(json.dumps(results, indent=4))
    else:
        print("\nNo products match your search criteria.")

if __name__ == "__main__":
    main()
```
