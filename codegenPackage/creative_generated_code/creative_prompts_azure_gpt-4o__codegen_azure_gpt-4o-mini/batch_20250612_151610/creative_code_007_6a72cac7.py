"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Write a program to calculate shipping costs for air, sea, and land freight options, based on the services provided by Portline Shipping & Logistic.
Generated: DETERMINISTIC_6a72cac770c5307b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs based on the mode of transportation.
    """

    def __init__(self):
        # Define base costs for each shipping method
        self.base_costs = {
            'air': 5.0,  # cost per kg for air freight
            'sea': 2.0,  # cost per kg for sea freight
            'land': 1.5   # cost per kg for land freight
        }

    def calculate_cost(self, method: str, weight: float) -> float:
        """
        Calculate the shipping cost based on the method and weight.

        Params:
        method (str): The shipping method ('air', 'sea', or 'land').
        weight (float): The weight of the shipment in kilograms.

        Returns:
        float: The calculated shipping cost.

        Raises:
        ValueError: If the shipping method is invalid or weight is non-positive.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        method = method.lower()
        if method not in self.base_costs:
            raise ValueError(f"Invalid shipping method: {method}. "
                             "Valid options are 'air', 'sea', or 'land'.")

        cost = self.base_costs[method] * weight
        return cost

def main():
    """
    Main function to execute the shipping cost calculator.
    Prompts the user for shipping method and weight, and prints the cost.
    """
    calculator = ShippingCostCalculator()

    try:
        # User input for shipping method
        method = input("Enter shipping method (air, sea, land): ")
        
        # User input for weight
        weight = float(input("Enter weight of the shipment in kg: "))

        # Calculate and print the shipping cost
        cost = calculator.calculate_cost(method, weight)
        print(f"The shipping cost for {weight} kg via {method} is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
