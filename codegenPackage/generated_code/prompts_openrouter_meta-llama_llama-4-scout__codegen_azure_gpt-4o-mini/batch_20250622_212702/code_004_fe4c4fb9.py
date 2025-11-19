"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Write a code snippet in a programming language of your choice to calculate the total cost of a customer's coffee order, considering factors like product price, tax, and shipping cost.
Generated: DETERMINISTIC_fe4c4fb9038d73fb
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CoffeeOrder:
    def __init__(self, product_price, tax_rate, shipping_cost):
        """
        Initializes the CoffeeOrder with product price, tax rate, and shipping cost.

        :param product_price: float, the price of the coffee product
        :param tax_rate: float, the tax rate as a decimal (e.g., 0.07 for 7%)
        :param shipping_cost: float, the cost of shipping
        """
        self.product_price = product_price
        self.tax_rate = tax_rate
        self.shipping_cost = shipping_cost

    def calculate_total_cost(self):
        """
        Calculates the total cost of the coffee order including tax and shipping.

        :return: float, the total cost of the order
        """
        try:
            if self.product_price < 0 or self.tax_rate < 0 or self.shipping_cost < 0:
                raise ValueError("Product price, tax rate, and shipping cost must be non-negative.")

            # Calculate tax
            tax_amount = self.product_price * self.tax_rate
            
            # Calculate total cost
            total_cost = self.product_price + tax_amount + self.shipping_cost
            
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create a CoffeeOrder instance
    order = CoffeeOrder(product_price=5.00, tax_rate=0.07, shipping_cost=2.00)
    
    # Calculate and print the total cost
    total_cost = order.calculate_total_cost()
    if total_cost is not None:
        print(f"The total cost of the coffee order is: ${total_cost:.2f}")
```
