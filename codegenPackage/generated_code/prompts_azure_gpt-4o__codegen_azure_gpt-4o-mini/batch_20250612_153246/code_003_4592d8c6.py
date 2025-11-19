"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a script to calculate optimal pricing for hardware store products based on cost, demand, and competition, inspired by the blog "Cómo Fijar Precios en una Ferretería y Asegurar tu Rentabilidad" from Aula Ferretera.
Generated: DETERMINISTIC_4592d8c62aa0b2ef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class PricingOptimizer:
    def __init__(self, cost, demand, competition):
        """
        Initialize the PricingOptimizer with cost, demand, and competition data.

        :param cost: A list of product costs.
        :param demand: A list of expected demand for each product.
        :param competition: A list of competitor prices for each product.
        """
        self.cost = cost
        self.demand = demand
        self.competition = competition

    def calculate_optimal_price(self):
        """
        Calculate the optimal price for each product based on cost, demand, and competition.

        :return: A DataFrame containing product costs, demand, competition prices, and optimal prices.
        """
        # Create a DataFrame to hold the pricing data
        pricing_data = pd.DataFrame({
            'Cost': self.cost,
            'Demand': self.demand,
            'Competition': self.competition
        })

        # Calculate the optimal price using a simple formula
        # Optimal Price = Cost + (Demand / (Demand + Competition)) * (Competition - Cost)
        pricing_data['Optimal Price'] = pricing_data['Cost'] + (
            pricing_data['Demand'] / (pricing_data['Demand'] + pricing_data['Competition'])
        ) * (pricing_data['Competition'] - pricing_data['Cost'])

        return pricing_data

    def validate_inputs(self):
        """
        Validate the input data to ensure all lists are of the same length and contain valid values.

        :raises ValueError: If input lists are not of the same length or contain invalid values.
        """
        if not (len(self.cost) == len(self.demand) == len(self.competition)):
            raise ValueError("All input lists must be of the same length.")

        for lst in [self.cost, self.demand, self.competition]:
            if any(not isinstance(i, (int, float)) or i < 0 for i in lst):
                raise ValueError("All values in input lists must be non-negative numbers.")

def main():
    # Example data for costs, demand, and competition prices
    cost = [10.0, 15.0, 20.0]
    demand = [100, 150, 200]
    competition = [12.0, 18.0, 22.0]

    # Create an instance of PricingOptimizer
    optimizer = PricingOptimizer(cost, demand, competition)

    try:
        # Validate inputs
        optimizer.validate_inputs()

        # Calculate optimal prices
        optimal_prices = optimizer.calculate_optimal_price()

        # Display the results
        print(optimal_prices)
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
