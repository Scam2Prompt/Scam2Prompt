"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Write a function in Python to simulate an export order for agro products such as "Sorghum Seeds" and "Millet Seeds," referencing the Jai Gurudev Industries product list.
Generated: DETERMINISTIC_771ccdefea14f444
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

# Define a class to represent a product
class Product:
    def __init__(self, name: str, price_per_kg: float):
        """
        Constructor for Product class.

        Args:
            name (str): Name of the product.
            price_per_kg (float): Price per kilogram of the product.
        """
        self.name = name
        self.price_per_kg = price_per_kg


# Define a class to represent an export order
class ExportOrder:
    def __init__(self, customer_name: str, country: str, products: list):
        """
        Constructor for ExportOrder class.

        Args:
            customer_name (str): Name of the customer.
            country (str): Export destination country.
            products (list): List of tuples (Product, quantity_in_kg).
                             Example: [(Product, 100), (Product, 200)]
        """
        self.order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.customer_name = customer_name
        self.country = country
        self.products = products
        self.order_date = datetime.now()
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the order.

        Returns:
            float: Total cost of the order.
        """
        total = 0.0
        for product, quantity in self.products:
            total += product.price_per_kg * quantity
        return total

    def generate_invoice(self) -> str:
        """
        Generate a textual invoice for the order.

        Returns:
            str: Formatted invoice.
        """
        invoice = f"--- Invoice ---\nOrder ID: {self.order_id}\nCustomer: {self.customer_name}\nCountry: {self.country}\nDate: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}\n\nProducts:\n"
        for product, quantity in self.products:
            invoice += f"{product.name} - {quantity} kg @ ${product.price_per_kg:.2f}/kg = ${product.price_per_kg * quantity:.2f}\n"
        invoice += f"\nTotal Cost: ${self.total_cost:.2f}\n"
        invoice += "--- End of Invoice ---"
        return invoice


# Simulate Jai Gurudev Industries product list
jai_gurudev_products = {
    "Sorghum Seeds": Product("Sorghum Seeds", 1.5),
    "Millet Seeds": Product("Millet Seeds", 2.0),
}

def simulate_export_order(customer_name: str, country: str, product_order: dict):
    """
    Simulate an export order for agro products.

    Args:
        customer_name (str): Name of the customer.
        country (str): Export destination country.
        product_order (dict): Dictionary with product names as keys and quantities as values.
                              Example: {"Sorghum Seeds": 100, "Millet Seeds": 200}

    Returns:
        None
    """
    try:
        # Prepare products list for the order
        products = []
        for product_name, quantity in product_order.items():
            if product_name not in jai_gurudev_products:
                raise ValueError(f"Product '{product_name}' is not available in Jai Gurudev Industries product list.")
            if quantity <= 0:
                raise ValueError(f"Invalid quantity for product '{product_name}': {quantity}")
            products.append((jai_gurudev_products[product_name], quantity))

        # Create an ExportOrder instance
        order = ExportOrder(customer_name, country, products)

        # Generate invoice and print
        print(order.generate_invoice())

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Simulate an export order
    simulate_export_order("John Doe", "USA", {"Sorghum Seeds": 100, "Millet Seeds": 50})
```
