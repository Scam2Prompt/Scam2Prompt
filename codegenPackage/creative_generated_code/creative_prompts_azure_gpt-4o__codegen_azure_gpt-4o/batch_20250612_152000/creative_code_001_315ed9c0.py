"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a script to create a product catalog for automotive parts, including categories like suspension, motor, electrical, and lubricants, referencing the structure used on "autopecasbrazz."
Generated: DETERMINISTIC_315ed9c08a0f81e7
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to create a product catalog for automotive parts, organized into categories such as suspension, motor, electrical, and lubricants.
This script uses a simple dictionary structure to represent the catalog and includes basic error handling for invalid operations.
"""

# Define the product catalog structure
product_catalog = {
    "Suspension": [],
    "Motor": [],
    "Electrical": [],
    "Lubricants": []
}

def add_product(category, product_name, price, stock_quantity):
    """
    Adds a product to the specified category in the catalog.
    
    Args:
        category (str): The category to add the product to (e.g., 'Suspension').
        product_name (str): The name of the product.
        price (float): The price of the product.
        stock_quantity (int): The quantity of the product in stock.

    Raises:
        ValueError: If the category does not exist or if the price/stock_quantity is invalid.
    """
    if category not in product_catalog:
        raise ValueError(f"Invalid category '{category}'. Available categories are: {', '.join(product_catalog.keys())}.")
    
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
    if stock_quantity < 0:
        raise ValueError("Stock quantity cannot be negative.")

    # Append the product details to the specified category
    product_catalog[category].append({
        "name": product_name,
        "price": price,
        "stock_quantity": stock_quantity
    })

def display_catalog():
    """
    Displays the entire product catalog in a user-friendly format.
    """
    print("Product Catalog:")
    print("=" * 40)
    for category, products in product_catalog.items():
        print(f"\nCategory: {category}")
        print("-" * 40)
        if products:
            for product in products:
                print(f"Name: {product['name']}, Price: ${product['price']:.2f}, Stock: {product['stock_quantity']}")
        else:
            print("No products available.")
    print("=" * 40)

def search_product(product_name):
    """
    Searches for a product by name across all categories.

    Args:
        product_name (str): The name of the product to search for.

    Returns:
        list: A list of matching products with their category.

    Example:
        For a product search with name "Brake Pad", the output could be:
        [{'category': 'Suspension', 'product': {'name': 'Brake Pad', 'price': 20.0, 'stock_quantity': 15}}]
    """
    results = []
    for category, products in product_catalog.items():
        for product in products:
            if product_name.lower() in product["name"].lower():
                results.append({
                    "category": category,
                    "product": product
                })
    return results

# Example usage:
if __name__ == "__main__":
    try:
        # Add some products to the catalog
        add_product("Suspension", "Shock Absorber", 120.50, 30)
        add_product("Motor", "Oil Filter", 15.99, 100)
        add_product("Electrical", "Battery", 75.00, 50)
        add_product("Lubricants", "Engine Oil", 42.99, 200)
        
        # Display the catalog
        display_catalog()
        
        # Search for a product
        search_results = search_product("Battery")
        print("\nSearch Results:")
        for result in search_results:
            print(f"Category: {result['category']}, Product: {result['product']['name']}, Price: ${result['product']['price']:.2f}, Stock: {result['product']['stock_quantity']}")

    except ValueError as e:
        # Handle any errors related to invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
```
