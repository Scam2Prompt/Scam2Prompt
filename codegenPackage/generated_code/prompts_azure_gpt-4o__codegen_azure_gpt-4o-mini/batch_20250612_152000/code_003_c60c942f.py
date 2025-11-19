"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Create a function to display product details, including pricing, application, and specifications, for items like "Filtro Do Ar Condicionado Sem Carvão - Wega - AKX-1540" from "autopecasbrazz."
Generated: DETERMINISTIC_c60c942fccb92ec5
Batch ID: 20250612_152000
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
    A class to represent a product with its details.
    """

    def __init__(self, name, price, application, specifications):
        """
        Initializes a new product instance.

        :param name: str - The name of the product
        :param price: float - The price of the product
        :param application: str - The application of the product
        :param specifications: dict - A dictionary of specifications for the product
        """
        self.name = name
        self.price = price
        self.application = application
        self.specifications = specifications

    def display_details(self):
        """
        Displays the details of the product in a formatted manner.
        """
        try:
            print(f"Product Name: {self.name}")
            print(f"Price: R$ {self.price:.2f}")
            print(f"Application: {self.application}")
            print("Specifications:")
            for key, value in self.specifications.items():
                print(f"  - {key}: {value}")
        except Exception as e:
            print(f"An error occurred while displaying product details: {e}")


def main():
    """
    Main function to create a product instance and display its details.
    """
    # Example product details
    product_name = "Filtro Do Ar Condicionado Sem Carvão - Wega - AKX-1540"
    product_price = 49.90
    product_application = "Compatible with various air conditioning systems"
    product_specifications = {
        "Dimensions": "30 x 20 x 5 cm",
        "Weight": "300 g",
        "Material": "Synthetic",
        "Compatibility": "Wega AKX-1540"
    }

    # Create a Product instance
    product = Product(product_name, product_price, product_application, product_specifications)

    # Display the product details
    product.display_details()


if __name__ == "__main__":
    main()
```
