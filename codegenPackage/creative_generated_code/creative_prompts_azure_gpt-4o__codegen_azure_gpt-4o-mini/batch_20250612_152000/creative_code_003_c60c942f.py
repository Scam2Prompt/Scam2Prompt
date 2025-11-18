"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Create a function to display product details, including pricing, application, and specifications, for items like "Filtro Do Ar Condicionado Sem Carvão - Wega - AKX-1540" from "autopecasbrazz."
Generated: DETERMINISTIC_c60c942fccb92ec5
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    A class to represent a product with its details.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        application (str): The application of the product.
        specifications (dict): The specifications of the product.
    """

    def __init__(self, name, price, application, specifications):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            application (str): The application of the product.
            specifications (dict): The specifications of the product.
        """
        self.name = name
        self.price = price
        self.application = application
        self.specifications = specifications

    def display_details(self):
        """
        Displays the details of the product in a formatted manner.
        """
        # Handle situations where the product might not have some details
        try:
            print(f"Product Name: {self.name}")
            print(f"Price: R${self.price:.2f}")
            print(f"Application: {self.application}")
            print("Specifications:")
            for spec_key, spec_value in self.specifications.items():
                print(f"  - {spec_key}: {spec_value}")
        except Exception as e:
            print("An error occurred while displaying product details:", str(e))


def create_and_display_product():
    """
    Creates a sample product and displays its details.
    """
    # Sample data for the product
    product_name = "Filtro Do Ar Condicionado Sem Carvão - Wega - AKX-1540"
    product_price = 59.90  # Example price
    product_application = "Compatible with various car models for air conditioning."
    product_specifications = {
        "Dimensions": "25 x 15 x 5 cm",
        "Weight": "200 g",
        "Material": "Plastic",
        "Filter Type": "Non-activated Carbon"
    }

    # Create an instance of Product
    product = Product(product_name, product_price, product_application, product_specifications)
    
    # Display the product details
    product.display_details()


if __name__ == "__main__":
    create_and_display_product()
```
