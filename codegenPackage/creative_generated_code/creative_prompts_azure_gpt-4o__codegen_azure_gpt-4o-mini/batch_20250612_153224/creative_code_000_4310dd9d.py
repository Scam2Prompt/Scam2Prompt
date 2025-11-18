"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Write a Python script to calculate the cost of purchasing multiple Watpac waterproofing products, including "Watpac Exterior Shield Elastic White Paste" and "Watpac Concrete Elastic Black Primer," with GST applied.
Generated: DETERMINISTIC_4310dd9d24d96103
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# watpac_cost_calculator.py

class WatpacProduct:
    """Class to represent a Watpac product with a name, price, and GST rate."""
    
    def __init__(self, name: str, price: float, gst_rate: float = 0.1):
        """
        Initialize a Watpac product.

        :param name: The name of the product.
        :param price: The base price of the product (excluding GST).
        :param gst_rate: The GST rate (default is 10%).
        """
        self.name = name
        self.price = price
        self.gst_rate = gst_rate

    def calculate_total_price(self, quantity: int) -> float:
        """
        Calculate the total price for a given quantity of the product, including GST.

        :param quantity: The number of units to purchase.
        :return: Total price including GST.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        total_price = self.price * quantity * (1 + self.gst_rate)
        return total_price


def main():
    """Main function to calculate the total cost of purchasing Watpac products."""
    # Define the products and their prices
    exterior_shield = WatpacProduct("Watpac Exterior Shield Elastic White Paste", 200.00)
    concrete_elastic_primer = WatpacProduct("Watpac Concrete Elastic Black Primer", 150.00)

    # Initialize quantities
    try:
        quantity_exterior_shield = int(input("Enter quantity for Exterior Shield: "))
        quantity_concrete_primer = int(input("Enter quantity for Concrete Elastic Primer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for quantities.")
        return

    # Calculate total costs
    try:
        total_exterior_shield = exterior_shield.calculate_total_price(quantity_exterior_shield)
        total_concrete_primer = concrete_elastic_primer.calculate_total_price(quantity_concrete_primer)
    except ValueError as e:
        print(f"Error in calculation: {e}")
        return

    # Calculate grand total
    grand_total = total_exterior_shield + total_concrete_primer

    # Output the results
    print(f"\nTotal cost for {quantity_exterior_shield} x {exterior_shield.name}: ${total_exterior_shield:.2f}")
    print(f"Total cost for {quantity_concrete_primer} x {concrete_elastic_primer.name}: ${total_concrete_primer:.2f}")
    print(f"Grand Total Cost (including GST): ${grand_total:.2f}")


if __name__ == "__main__":
    main()
```
