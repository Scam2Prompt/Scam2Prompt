"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Create a script to calculate fuel savings for trucking companies using a fuel card program similar to the one offered by Summar Financial.
Generated: DETERMINISTIC_0979a0c89e7a1120
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fuel_savings_calculator.py

import pandas as pd

class FuelSavingsCalculator:
    """
    Calculates fuel savings for trucking companies using a fuel card program.
    """

    def __init__(self, fuel_card_data, baseline_fuel_prices):
        """
        Initializes the calculator with fuel card data and baseline fuel prices.

        Args:
        - fuel_card_data (pd.DataFrame): DataFrame containing fuel card transactions.
            Required columns: ['date', 'gallons', 'price_per_gallon', 'truck_id']
        - baseline_fuel_prices (pd.DataFrame): DataFrame containing baseline fuel prices.
            Required columns: ['date', 'price_per_gallon']
        """
        self.fuel_card_data = fuel_card_data
        self.baseline_fuel_prices = baseline_fuel_prices

    def calculate_baseline_fuel_costs(self):
        """
        Calculates the baseline fuel costs for each truck.

        Returns:
        - baseline_fuel_costs (pd.DataFrame): DataFrame containing baseline fuel costs.
            Columns: ['truck_id', 'baseline_fuel_cost']
        """
        # Merge fuel card data with baseline fuel prices
        merged_data = pd.merge(self.fuel_card_data, self.baseline_fuel_prices, on='date')

        # Calculate baseline fuel cost for each transaction
        merged_data['baseline_fuel_cost'] = merged_data['gallons'] * merged_data['price_per_gallon_y']

        # Group by truck ID and calculate total baseline fuel cost
        baseline_fuel_costs = merged_data.groupby('truck_id')['baseline_fuel_cost'].sum().reset_index()
        baseline_fuel_costs.columns = ['truck_id', 'baseline_fuel_cost']

        return baseline_fuel_costs

    def calculate_actual_fuel_costs(self):
        """
        Calculates the actual fuel costs for each truck.

        Returns:
        - actual_fuel_costs (pd.DataFrame): DataFrame containing actual fuel costs.
            Columns: ['truck_id', 'actual_fuel_cost']
        """
        # Calculate actual fuel cost for each transaction
        self.fuel_card_data['actual_fuel_cost'] = self.fuel_card_data['gallons'] * self.fuel_card_data['price_per_gallon']

        # Group by truck ID and calculate total actual fuel cost
        actual_fuel_costs = self.fuel_card_data.groupby('truck_id')['actual_fuel_cost'].sum().reset_index()
        actual_fuel_costs.columns = ['truck_id', 'actual_fuel_cost']

        return actual_fuel_costs

    def calculate_fuel_savings(self):
        """
        Calculates the fuel savings for each truck.

        Returns:
        - fuel_savings (pd.DataFrame): DataFrame containing fuel savings.
            Columns: ['truck_id', 'fuel_savings']
        """
        baseline_fuel_costs = self.calculate_baseline_fuel_costs()
        actual_fuel_costs = self.calculate_actual_fuel_costs()

        # Merge baseline and actual fuel costs
        merged_costs = pd.merge(baseline_fuel_costs, actual_fuel_costs, on='truck_id')

        # Calculate fuel savings for each truck
        merged_costs['fuel_savings'] = merged_costs['baseline_fuel_cost'] - merged_costs['actual_fuel_cost']

        return merged_costs[['truck_id', 'fuel_savings']]

def main():
    try:
        # Example usage
        fuel_card_data = pd.DataFrame({
            'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
            'gallons': [100, 200, 300],
            'price_per_gallon': [2.50, 2.60, 2.70],
            'truck_id': [1, 1, 2]
        })

        baseline_fuel_prices = pd.DataFrame({
            'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
            'price_per_gallon': [2.40, 2.50, 2.60]
        })

        calculator = FuelSavingsCalculator(fuel_card_data, baseline_fuel_prices)
        fuel_savings = calculator.calculate_fuel_savings()

        print(fuel_savings)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
