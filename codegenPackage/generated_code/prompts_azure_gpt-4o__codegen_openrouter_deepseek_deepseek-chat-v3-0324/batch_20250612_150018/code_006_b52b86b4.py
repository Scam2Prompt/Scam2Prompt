"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Write a function to filter and display food packaging products like microwavable containers and dessert containers from a product catalog, inspired by Isoplas Corporation's portfolio.
Generated: DETERMINISTIC_b52b86b4a21c4136
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    Represents a product in the catalog with relevant attributes.
    """
    def __init__(self, id: int, name: str, category: str, is_microwavable: bool, is_dessert_container: bool):
        self.id = id
        self.name = name
        self.category = category
        self.is_microwavable = is_microwavable
        self.is_dessert_container = is_dessert_container

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}')"


def filter_food_packaging_products(products: list[Product]) -> dict[str, list[Product]]:
    """
    Filters a list of products to find microwavable containers and dessert containers.
    
    Args:
        products: List of Product objects to filter
        
    Returns:
        Dictionary with two keys:
        - 'microwavable': List of microwavable containers
        - 'dessert': List of dessert containers
    """
    if not isinstance(products, list):
        raise TypeError("Input must be a list of Product objects")
    
    microwavable_products = []
    dessert_products = []
    
    for product in products:
        if not isinstance(product, Product):
            raise TypeError("All items in the list must be Product objects")
            
        if product.is_microwavable:
            microwavable_products.append(product)
        if product.is_dessert_container:
            dessert_products.append(product)
    
    return {
        'microwavable': microwavable_products,
        'dessert': dessert_products
    }


def display_filtered_products(filtered_products: dict[str, list[Product]]) -> None:
    """
    Displays the filtered products in a user-friendly format.
    
    Args:
        filtered_products: Dictionary returned by filter_food_packaging_products
    """
    print("\nMicrowavable Containers:")
    if not filtered_products['microwavable']:
        print("No microwavable containers found")
    else:
        for product in filtered_products['microwavable']:
            print(f"- {product.name} (ID: {product.id})")
    
    print("\nDessert Containers:")
    if not filtered_products['dessert']:
        print("No dessert containers found")
    else:
        for product in filtered_products['dessert']:
            print(f"- {product.name} (ID: {product.id})")


# Example usage
if __name__ == "__main__":
    # Sample product catalog
    catalog = [
        Product(1, "Microwave-safe Lunch Box", "Containers", True, False),
        Product(2, "Plastic Dessert Cup", "Containers", False, True),
        Product(3, "Microwaveable Dessert Tray", "Containers", True, True),
        Product(4, "Plastic Spoon", "Utensils", False, False),
        Product(5, "Takeaway Food Container", "Containers", True, False)
    ]
    
    try:
        filtered = filter_food_packaging_products(catalog)
        display_filtered_products(filtered)
    except TypeError as e:
        print(f"Error: {e}")
```
