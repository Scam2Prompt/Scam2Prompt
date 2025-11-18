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
import random
from typing import List, Dict, Any

class ExportOrderError(Exception):
    """Custom exception for export order related errors."""
    pass

class AgroProduct:
    """Class representing an agro product."""
    
    def __init__(self, name: str, price_per_unit: float):
        self.name = name
        self.price_per_unit = price_per_unit
        
    def __str__(self) -> str:
        return f"{self.name} - Price per unit: ${self.price_per_unit:.2f}"

class ExportOrder:
    """Class to represent an export order for agro products."""
    
    def __init__(self, products: List[AgroProduct]):
        self.products = products
        self.order_details: Dict[str, Any] = {}
    
    def generate_order(self, quantities: Dict[str, int]) -> None:
        """Generate an export order based on provided quantities.

        Args:
            quantities (Dict[str, int]): A dictionary where keys are product names and values are the quantities.
        
        Raises:
            ExportOrderError: If a product is not found or quantity is invalid.
        """
        total_cost = 0
        self.order_details = {}

        for product in self.products:
            quantity = quantities.get(product.name, 0)
            if quantity < 0:
                raise ExportOrderError(f"Quantity for {product.name} cannot be negative.")
            if quantity > 0:
                product_cost = product.price_per_unit * quantity
                total_cost += product_cost
                self.order_details[product.name] = {
                    'quantity': quantity,
                    'cost': product_cost
                }
        
        self.order_details['total_cost'] = total_cost

    def display_order(self) -> None:
        """Display the order summary."""
        print("Export Order Summary:")
        for product_name, details in self.order_details.items():
            if product_name != 'total_cost':
                print(f"{product_name}: Quantity = {details['quantity']}, Cost = ${details['cost']:.2f}")
        print(f"Total Cost: ${self.order_details['total_cost']:.2f}")

def main() -> None:
    """Main function to simulate an export order."""
    # Define products available at Jai Gurudev Industries
    product_list = [
        AgroProduct("Sorghum Seeds", 1.25),
        AgroProduct("Millet Seeds", 2.00)
    ]
    
    # Create an export order for specific quantities
    quantities = {
        "Sorghum Seeds": random.randint(1, 10),  # Random quantity between 1 and 10
        "Millet Seeds": random.randint(1, 5)      # Random quantity between 1 and 5
    }

    order = ExportOrder(product_list)

    try:
        order.generate_order(quantities)
        order.display_order()
    except ExportOrderError as e:
        print(f"Error generating export order: {e}")

if __name__ == "__main__":
    main()
```
