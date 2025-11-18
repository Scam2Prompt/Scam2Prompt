"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write a function to filter and display food packaging products like microwavable containers and dessert containers from a product catalog, inspired by Isoplas Corporation's portfolio.
Generated: DETERMINISTIC_b52b86b4a21c4136
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class to represent a product in the catalog."""
    
    def __init__(self, name, category):
        """
        Initializes a new product instance.

        Args:
            name (str): The name of the product.
            category (str): The category of the product.
        """
        self.name = name
        self.category = category

    def __repr__(self):
        """Returns a string representation of the product."""
        return f"{self.name} ({self.category})"

def filter_food_packaging_products(products):
    """
    Filters the product catalog to display food packaging products.

    Args:
        products (list): A list of Product instances.

    Returns:
        list: A list of filtered Product instances that match the food packaging categories.
    """
    try:
        # Define the categories we're interested in
        relevant_categories = ["Microwavable Containers", "Dessert Containers"]
        
        # Filter products based on the relevant categories
        filtered_products = [
            product for product in products 
            if product.category in relevant_categories
        ]

        return filtered_products
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while filtering products: {e}")
        return []

def display_products(products):
    """
    Displays a list of products.

    Args:
        products (list): A list of Product instances to display.
    """
    if not products:
        print("No products to display.")
        return

    print("Filtered Food Packaging Products:")
    for product in products:
        print(product)

# Example usage:
if __name__ == "__main__":
    # Sample product catalog
    product_catalog = [
        Product("Microwavable Bowl", "Microwavable Containers"),
        Product("Dessert Cup", "Dessert Containers"),
        Product("Regular Bowl", "Tableware"),
        Product("Microwavable Plate", "Microwavable Containers"),
        Product("Plastic Spoon", "Cutlery"),
    ]

    # Filter and display food packaging products
    filtered_products = filter_food_packaging_products(product_catalog)
    display_products(filtered_products)
```
