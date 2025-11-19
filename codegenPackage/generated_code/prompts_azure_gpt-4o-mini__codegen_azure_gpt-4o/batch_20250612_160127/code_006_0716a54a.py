"""
Generated Code Metadata:
========================
Original URL: https://orangepepe.pages.dev
Prompt: How does the Orange Pepe project plan to utilize e-commerce for its holders, and what types of products will be available?
Generated: DETERMINISTIC_0716a54a307c1fdb
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Orange Pepe E-Commerce Platform Simulation

This script demonstrates how the Orange Pepe project plans to utilize e-commerce for its holders.
It includes a mock implementation of an e-commerce platform where holders can purchase exclusive products.
"""

import json

# Define a custom exception for invalid holder access
class HolderAccessError(Exception):
    pass

# Mock database of holders and their access levels
HOLDERS_DB = {
    "holder1": {"name": "Alice", "access_level": "premium"},
    "holder2": {"name": "Bob", "access_level": "standard"},
    "holder3": {"name": "Charlie", "access_level": "premium"},
}

# Mock product catalog
PRODUCT_CATALOG = [
    {"id": 1, "name": "Orange Pepe T-Shirt", "price": 25.99, "exclusive": False},
    {"id": 2, "name": "Orange Pepe Mug", "price": 15.99, "exclusive": False},
    {"id": 3, "name": "Limited Edition Orange Pepe NFT", "price": 199.99, "exclusive": True},
    {"id": 4, "name": "Orange Pepe Hoodie", "price": 45.99, "exclusive": False},
    {"id": 5, "name": "Orange Pepe Premium Art Print", "price": 99.99, "exclusive": True},
]

def authenticate_holder(holder_id):
    """
    Authenticate a holder based on their ID.
    
    Args:
        holder_id (str): The ID of the holder.
    
    Returns:
        dict: Holder information if authentication is successful.
    
    Raises:
        HolderAccessError: If the holder ID is invalid.
    """
    holder = HOLDERS_DB.get(holder_id)
    if not holder:
        raise HolderAccessError(f"Holder ID '{holder_id}' not found.")
    return holder

def get_available_products(holder):
    """
    Retrieve the list of products available to a holder based on their access level.
    
    Args:
        holder (dict): The authenticated holder's information.
    
    Returns:
        list: A list of products available to the holder.
    """
    access_level = holder["access_level"]
    if access_level == "premium":
        # Premium holders can access all products
        return PRODUCT_CATALOG
    elif access_level == "standard":
        # Standard holders can access only non-exclusive products
        return [product for product in PRODUCT_CATALOG if not product["exclusive"]]
    else:
        # If access level is unknown, return an empty list
        return []

def display_products(products):
    """
    Display the list of products in a user-friendly format.
    
    Args:
        products (list): The list of products to display.
    """
    print("\nAvailable Products:")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")

def main():
    """
    Main function to simulate the Orange Pepe e-commerce platform.
    """
    print("Welcome to the Orange Pepe E-Commerce Platform!")
    holder_id = input("Please enter your holder ID: ").strip()
    
    try:
        # Authenticate the holder
        holder = authenticate_holder(holder_id)
        print(f"Hello, {holder['name']}! You have {holder['access_level']} access.")
        
        # Get available products for the holder
        products = get_available_products(holder)
        
        # Display the products
        display_products(products)
        
    except HolderAccessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
