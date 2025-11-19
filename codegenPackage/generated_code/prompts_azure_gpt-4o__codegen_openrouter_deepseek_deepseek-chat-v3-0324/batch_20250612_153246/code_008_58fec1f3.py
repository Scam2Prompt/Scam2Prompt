"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: Write code to calculate the total weight of purchased fiberglass products, assuming weight data is available for items like Ceramic Fiber and Carbon Fiber Chopped.
Generated: DETERMINISTIC_58fec1f347c11ea7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FiberglassProduct:
    """
    Represents a fiberglass product with its weight.
    """
    def __init__(self, name: str, weight: float):
        """
        Initialize a fiberglass product.
        
        Args:
            name: Name of the product (e.g., "Ceramic Fiber")
            weight: Weight of the product in kilograms
        """
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"FiberglassProduct(name='{self.name}', weight={self.weight})"


class FiberglassPurchaseCalculator:
    """
    Calculates the total weight of purchased fiberglass products.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product: FiberglassProduct) -> None:
        """
        Add a fiberglass product to the purchase list.
        
        Args:
            product: FiberglassProduct instance to add
        """
        if not isinstance(product, FiberglassProduct):
            raise TypeError("Only FiberglassProduct instances can be added")
        self.products.append(product)

    def calculate_total_weight(self) -> float:
        """
        Calculate the total weight of all added products.
        
        Returns:
            Total weight in kilograms
            
        Raises:
            ValueError: If no products have been added
        """
        if not self.products:
            raise ValueError("No products added to calculate total weight")
        return sum(product.weight for product in self.products)


# Example usage
if __name__ == "__main__":
    try:
        calculator = FiberglassPurchaseCalculator()
        
        # Add products
        calculator.add_product(FiberglassProduct("Ceramic Fiber", 5.2))
        calculator.add_product(FiberglassProduct("Carbon Fiber Chopped", 3.8))
        
        # Calculate total weight
        total_weight = calculator.calculate_total_weight()
        print(f"Total weight of purchased fiberglass products: {total_weight} kg")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
