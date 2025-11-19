"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a code snippet to calculate the cost of reinforced concrete products for a residential construction project in Moscow, considering the logistics and discounts provided by Paradigma ЖБИ.
Generated: DETERMINISTIC_43c370224b7bb753
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ConcreteProductCalculator:
    """
    A class to calculate the cost of reinforced concrete products for a residential construction project.
    Includes logistics and discounts provided by Paradigma ЖБИ.
    """

    def __init__(self, base_price_per_unit, quantity, distance_km, discount_rate=0.0):
        """
        Initialize the calculator with product details and logistics.

        :param base_price_per_unit: Base price of one unit of the concrete product (float).
        :param quantity: Number of units required (int).
        :param distance_km: Distance in kilometers for delivery (float).
        :param discount_rate: Discount rate provided by Paradigma ЖБИ (float, default is 0.0).
        """
        self.base_price_per_unit = base_price_per_unit
        self.quantity = quantity
        self.distance_km = distance_km
        self.discount_rate = discount_rate

    def calculate_logistics_cost(self):
        """
        Calculate the logistics cost based on distance.

        :return: Logistics cost (float).
        """
        # Assume a fixed rate of 50 rubles per kilometer for delivery
        rate_per_km = 50.0
        return self.distance_km * rate_per_km

    def calculate_discount(self, total_cost):
        """
        Calculate the discount based on the discount rate.

        :param total_cost: Total cost before discount (float).
        :return: Discount amount (float).
        """
        return total_cost * self.discount_rate

    def calculate_total_cost(self):
        """
        Calculate the total cost including product cost, logistics, and discount.

        :return: Final total cost (float).
        """
        try:
            # Calculate product cost
            product_cost = self.base_price_per_unit * self.quantity

            # Calculate logistics cost
            logistics_cost = self.calculate_logistics_cost()

            # Calculate total cost before discount
            total_cost_before_discount = product_cost + logistics_cost

            # Calculate discount
            discount = self.calculate_discount(total_cost_before_discount)

            # Final total cost after applying discount
            final_total_cost = total_cost_before_discount - discount

            return final_total_cost
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred while calculating the total cost: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Input parameters
    base_price_per_unit = 1200.0  # Price per unit in rubles
    quantity = 50  # Number of units
    distance_km = 30.0  # Distance in kilometers
    discount_rate = 0.1  # 10% discount

    # Create an instance of the calculator
    calculator = ConcreteProductCalculator(base_price_per_unit, quantity, distance_km, discount_rate)

    # Calculate the total cost
    total_cost = calculator.calculate_total_cost()

    if total_cost is not None:
        print(f"The total cost for the reinforced concrete products is: {total_cost:.2f} rubles")
    else:
        print("Failed to calculate the total cost.")
```
