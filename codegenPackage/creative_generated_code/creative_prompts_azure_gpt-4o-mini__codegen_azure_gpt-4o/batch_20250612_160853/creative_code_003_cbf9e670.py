"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foiegras-badaud-sarlat.fr
Prompt: Develop a code sample that displays a list of products with their prices, specifically focusing on the foie gras d'oie and canard from the Périgord region.
Generated: DETERMINISTIC_cbf9e670f21e73e2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Define a class for Product
class Product:
    def __init__(self, name, region, price):
        """
        Initializes a Product instance.

        :param name: Name of the product
        :param region: Region where the product is sourced from
        :param price: Price of the product
        """
        self.name = name
        self.region = region
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the Product.
        """
        return f"{self.name} (Region: {self.region}, Price: ${self.price:.2f})"

# Define a function to filter and display products from the Périgord region
def display_products(products_list):
    """
    Filters and displays products from the Périgord region.

    :param products_list: List of Product objects
    """
    try:
        print("Products from the Périgord region:")

        # Filter products specific to Périgord region
        perigord_products = [product for product in products_list if product.region.lower() == "périgord"]

        if not perigord_products:
            print("No products found from the Périgord region.")
            return

        # Display each product
        for product in perigord_products:
            print(product)

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred while displaying products: {str(e)}")


# Main function to execute the program
def main():
    """
    Main function to execute the product display logic.
    """
    try:
        # Define a list of products
        products = [
            Product("Foie gras d'oie", "Périgord", 45.99),
            Product("Foie gras de canard", "Périgord", 37.50),
            Product("Duck confit", "Gascony", 25.00),
            Product("Truffle oil", "Périgord", 18.75),
            Product("Cheese platter", "Normandy", 22.30)
        ]

        # Display Périgord region products
        display_products(products)

    except Exception as e:
        # Handle unexpected exceptions in the main function
        print(f"An error occurred: {str(e)}")


# Execute the program
if __name__ == "__main__":
    main()
```
