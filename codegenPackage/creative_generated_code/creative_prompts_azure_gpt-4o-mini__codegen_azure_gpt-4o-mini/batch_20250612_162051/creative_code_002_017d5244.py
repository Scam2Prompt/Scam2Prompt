"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Write a Python function that calculates the total cost of purchasing various Watpac waterproofing chemicals, including GST for products like cement additives and water sealers.
Generated: DETERMINISTIC_017d524420d123d5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ChemicalProduct:
    """Represents a chemical product with a name, base price, and GST rate."""

    def __init__(self, name: str, base_price: float, gst_rate: float = 0.10):
        """
        Initializes a ChemicalProduct instance.

        Args:
            name (str): The name of the chemical product.
            base_price (float): The base price of the product.
            gst_rate (float): The GST rate applicable to the product (default is 10%).
        """
        self.name = name
        self.base_price = base_price
        self.gst_rate = gst_rate

    def total_cost(self) -> float:
        """Calculates the total cost including GST."""
        return self.base_price * (1 + self.gst_rate)


def calculate_total_cost(products: list) -> float:
    """
    Calculates the total cost of all chemical products including GST.

    Args:
        products (list): A list of ChemicalProduct instances.

    Returns:
        float: The total cost of the products including GST.
    """
    if not isinstance(products, list):
        raise ValueError("Products must be a list of ChemicalProduct instances.")
    
    total = 0.0
    for product in products:
        if not isinstance(product, ChemicalProduct):
            raise ValueError("All items in the products list must be instances of ChemicalProduct.")
        total += product.total_cost()
    
    return total


# Example usage
if __name__ == "__main__":
    # Define a list of chemical products
    product_list = [
        ChemicalProduct(name="Cement Additive", base_price=50.00),
        ChemicalProduct(name="Water Sealer", base_price=75.00)
    ]

    try:
        # Calculate the total cost
        total_cost = calculate_total_cost(product_list)
        print(f"The total cost of the products including GST is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"An error occurred: {e}")
```
