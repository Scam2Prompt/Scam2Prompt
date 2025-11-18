"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Create a program to compare freight forwarding costs across air and sea modes, using Alexa Shipping's logistics solutions as a model.
Generated: DETERMINISTIC_204fb5d10826cd36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class FreightForwardingCostComparer:
    """
    A class to compare freight forwarding costs between air and sea modes.
    """

    def __init__(self, air_cost_per_kg, sea_cost_per_kg):
        """
        Initializes the FreightForwardingCostComparer with costs per kg for air and sea shipping.
        
        :param air_cost_per_kg: Cost of shipping via air per kilogram
        :param sea_cost_per_kg: Cost of shipping via sea per kilogram
        """
        self.air_cost_per_kg = air_cost_per_kg
        self.sea_cost_per_kg = sea_cost_per_kg

    def calculate_air_cost(self, weight):
        """
        Calculate the total air shipping cost for a given weight.
        
        :param weight: Weight of the shipment in kilograms
        :return: Total cost for air shipping
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return self.air_cost_per_kg * weight

    def calculate_sea_cost(self, weight):
        """
        Calculate the total sea shipping cost for a given weight.
        
        :param weight: Weight of the shipment in kilograms
        :return: Total cost for sea shipping
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return self.sea_cost_per_kg * weight

    def compare_costs(self, weight):
        """
        Compare the air and sea shipping costs for a given weight.
        
        :param weight: Weight of the shipment in kilograms
        :return: A tuple containing the air cost and sea cost
        """
        air_cost = self.calculate_air_cost(weight)
        sea_cost = self.calculate_sea_cost(weight)
        return air_cost, sea_cost

def main():
    """
    Main function to run the cost comparison program.
    """
    try:
        # Example costs per kg for air and sea
        air_cost_per_kg = 5.0  # Example cost for air
        sea_cost_per_kg = 2.0   # Example cost for sea

        # Initialize cost comparer
        comparer = FreightForwardingCostComparer(air_cost_per_kg, sea_cost_per_kg)

        # Input weight from user
        weight = float(input("Enter the weight of the shipment (in kg): "))
        
        # Get the comparison
        air_cost, sea_cost = comparer.compare_costs(weight)

        # Display results
        print(f"Air shipping cost: ${air_cost:.2f}")
        print(f"Sea shipping cost: ${sea_cost:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
