"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Create a Python script to calculate the total cooking capacity (in kg) for a combination of Caja China, Cilindro, and Parrilla products purchased from Meat Master.
Generated: DETERMINISTIC_643aed0a83a08320
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CookingCapacityCalculator:
    """
    A class to calculate the total cooking capacity for a combination of 
    Caja China, Cilindro, and Parrilla products.
    """

    def __init__(self):
        self.products = {
            'Caja China': 50,  # kg capacity for Caja China
            'Cilindro': 30,    # kg capacity for Cilindro
            'Parrilla': 25      # kg capacity for Parrilla
        }
        self.total_capacity = 0

    def add_product(self, product_name, quantity):
        """
        Adds the capacity of a specified product to the total capacity.

        :param product_name: Name of the product (str)
        :param quantity: Number of products (int)
        :raises ValueError: If the product name is invalid or quantity is non-positive
        """
        if product_name not in self.products:
            raise ValueError(f"Invalid product name: {product_name}. Available options are: {list(self.products.keys())}.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate and add the capacity for the given product
        capacity = self.products[product_name] * quantity
        self.total_capacity += capacity
        print(f"Added {quantity} x {product_name} (Total Capacity: {self.total_capacity} kg)")

    def get_total_capacity(self):
        """
        Returns the total cooking capacity calculated.

        :return: Total cooking capacity (int)
        """
        return self.total_capacity


def main():
    """
    Main function to execute the cooking capacity calculation.
    """
    calculator = CookingCapacityCalculator()

    # Sample input; in production, inputs could be taken from user or a data source
    purchases = {
        'Caja China': 2,
        'Cilindro': 3,
        'Parrilla': 1
    }

    try:
        for product, quantity in purchases.items():
            calculator.add_product(product, quantity)

        total_capacity = calculator.get_total_capacity()
        print(f"Total Cooking Capacity: {total_capacity} kg")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
