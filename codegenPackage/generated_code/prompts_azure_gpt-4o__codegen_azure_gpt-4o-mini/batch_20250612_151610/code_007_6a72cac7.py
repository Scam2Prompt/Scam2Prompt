"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Write a program to calculate shipping costs for air, sea, and land freight options, based on the services provided by Portline Shipping & Logistic.
Generated: DETERMINISTIC_6a72cac770c5307b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs for air, sea, and land freight options.
    """

    def __init__(self):
        # Define base rates for different shipping methods
        self.base_rates = {
            'air': 5.00,  # per kg
            'sea': 2.00,  # per kg
            'land': 3.00  # per kg
        }

    def calculate_cost(self, method, weight):
        """
        Calculate the shipping cost based on the method and weight.

        :param method: str - The shipping method ('air', 'sea', 'land')
        :param weight: float - The weight of the shipment in kilograms
        :return: float - The calculated shipping cost
        :raises ValueError: If the shipping method is invalid or weight is negative
        """
        if method not in self.base_rates:
            raise ValueError(f"Invalid shipping method: {method}. Choose from {list(self.base_rates.keys())}.")
        
        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        # Calculate the total cost
        cost = self.base_rates[method] * weight
        return cost

    def display_cost(self, method, weight):
        """
        Display the shipping cost for the given method and weight.

        :param method: str - The shipping method ('air', 'sea', 'land')
        :param weight: float - The weight of the shipment in kilograms
        """
        try:
            cost = self.calculate_cost(method, weight)
            print(f"The shipping cost for {weight} kg via {method} is: ${cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage of the ShippingCostCalculator
    calculator = ShippingCostCalculator()

    # Sample inputs for demonstration
    shipping_methods = ['air', 'sea', 'land']
    weights = [10, 20, -5]  # The last weight is intentionally negative to demonstrate error handling

    for method in shipping_methods:
        for weight in weights:
            calculator.display_cost(method, weight)
```
