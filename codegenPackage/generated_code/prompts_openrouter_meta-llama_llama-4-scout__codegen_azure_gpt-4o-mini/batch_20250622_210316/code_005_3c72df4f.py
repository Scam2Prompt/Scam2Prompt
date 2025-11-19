"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Write a code snippet in Python to calculate the total cost of refractory products for a specific industrial application, considering factors like product quantity, unit price, and taxes."
Generated: DETERMINISTIC_3c72df4fb2c18bd6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RefractoryProduct:
    """
    A class to represent a refractory product and calculate its total cost.
    """

    def __init__(self, name: str, unit_price: float, quantity: int, tax_rate: float):
        """
        Initializes a new instance of RefractoryProduct.

        :param name: Name of the refractory product
        :param unit_price: Price per unit of the product
        :param quantity: Quantity of the product
        :param tax_rate: Tax rate applicable to the product (as a decimal)
        """
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.tax_rate = tax_rate

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the refractory products including tax.

        :return: Total cost including tax
        """
        if self.unit_price < 0 or self.quantity < 0 or self.tax_rate < 0:
            raise ValueError("Unit price, quantity, and tax rate must be non-negative.")

        subtotal = self.unit_price * self.quantity
        total_tax = subtotal * self.tax_rate
        total_cost = subtotal + total_tax
        return total_cost


def main():
    """
    Main function to demonstrate the calculation of total cost for refractory products.
    """
    try:
        # Example data for the refractory product
        product_name = "High-Temperature Brick"
        unit_price = 50.0  # Price per unit
        quantity = 100      # Number of units
        tax_rate = 0.08    # 8% tax rate

        # Create an instance of RefractoryProduct
        refractory_product = RefractoryProduct(product_name, unit_price, quantity, tax_rate)

        # Calculate the total cost
        total_cost = refractory_product.calculate_total_cost()

        # Output the result
        print(f"Total cost for {quantity} units of {product_name}: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
