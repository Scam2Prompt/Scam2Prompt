"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idgfiber.com
Prompt: Write code to calculate the total weight of purchased fiberglass products, assuming weight data is available for items like Ceramic Fiber and Carbon Fiber Chopped.
Generated: DETERMINISTIC_58fec1f347c11ea7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FiberglassProduct:
    """Class to represent a fiberglass product with its weight."""
    
    def __init__(self, name: str, weight_per_unit: float):
        """
        Initializes a new fiberglass product.
        
        :param name: Name of the fiberglass product
        :param weight_per_unit: Weight of a single unit of the product in kilograms
        """
        self.name = name
        self.weight_per_unit = weight_per_unit


class Purchase:
    """Class to handle the purchase of fiberglass products."""
    
    def __init__(self):
        """Initializes an empty list of purchased products."""
        self.products = []
    
    def add_product(self, product: FiberglassProduct, quantity: int):
        """
        Adds a product to the purchase list.
        
        :param product: An instance of FiberglassProduct to add
        :param quantity: Number of units of the product being purchased
        :raises ValueError: If quantity is not a positive integer
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        self.products.append((product, quantity))

    def calculate_total_weight(self) -> float:
        """
        Calculates the total weight of all purchased fiberglass products.
        
        :return: Total weight in kilograms
        """
        total_weight = 0.0
        for product, quantity in self.products:
            total_weight += product.weight_per_unit * quantity
        
        return total_weight


def main():
    """Main function to demonstrate the purchase and weight calculation."""
    try:
        # Create instances of fiberglass products with their weights
        ceramic_fiber = FiberglassProduct("Ceramic Fiber", 5.0)  # Weight per unit in kg
        carbon_fiber_chopped = FiberglassProduct("Carbon Fiber Chopped", 3.5)  # Weight per unit in kg

        # Initialize purchase
        purchase = Purchase()
        
        # Add products to the purchase
        purchase.add_product(ceramic_fiber, 10)  # 10 units of Ceramic Fiber
        purchase.add_product(carbon_fiber_chopped, 5)  # 5 units of Carbon Fiber Chopped

        # Calculate and print the total weight of purchased products
        total_weight = purchase.calculate_total_weight()
        print(f"Total weight of purchased fiberglass products: {total_weight:.2f} kg")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
