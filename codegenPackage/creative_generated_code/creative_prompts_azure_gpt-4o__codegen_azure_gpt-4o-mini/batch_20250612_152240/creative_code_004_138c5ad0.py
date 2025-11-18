"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Create Python code to simulate multi-stock and multi-fleet Operating Models using openMSE. Include an example of configuring fleet selectivity.
Generated: DETERMINISTIC_138c5ad06a95dfc7
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openMSE as mse
import numpy as np

# Define the parameters for the operating model
class OperatingModel:
    def __init__(self, stocks, fleets, selectivity):
        """
        Initialize the Operating Model with stocks, fleets, and selectivity.

        :param stocks: List of stock names
        :param fleets: List of fleet names
        :param selectivity: Dictionary mapping fleet names to selectivity functions
        """
        self.stocks = stocks
        self.fleets = fleets
        self.selectivity = selectivity
        
        # Check if provided selectivity functions are valid
        self.validate_selectivity()

    def validate_selectivity(self):
        """Validate the selectivity functions for each fleet."""
        for fleet in self.fleets:
            if fleet not in self.selectivity:
                raise ValueError(f"Selectivity function for fleet '{fleet}' is not defined.")

    def simulate(self, years=10):
        """
        Simulate the operating model over a specified number of years.

        :param years: Number of years to simulate
        :return: A dictionary with the simulation results for each stock
        """
        results = {stock: [] for stock in self.stocks}

        for year in range(years):
            for stock in self.stocks:
                # Apply selectivity function for each fleet
                total_catch = sum(self.selectivity[fleet](stock) for fleet in self.fleets)
                results[stock].append(total_catch)

        return results

# Example selectivity functions
def fleet_a_selectivity(stock):
    """Selectivity function for Fleet A."""
    return np.random.uniform(0.5, 1.0) * 100  # Random catch between 50 and 100

def fleet_b_selectivity(stock):
    """Selectivity function for Fleet B."""
    return np.random.uniform(0.3, 0.7) * 150  # Random catch between 45 and 105

# Main execution
if __name__ == "__main__":
    # Define stocks and fleets
    stocks = ['Stock1', 'Stock2']
    fleets = ['FleetA', 'FleetB']

    # Define the selectivity dictionary
    selectivity = {
        'FleetA': fleet_a_selectivity,
        'FleetB': fleet_b_selectivity
    }

    try:
        # Initialize the operating model
        operating_model = OperatingModel(stocks, fleets, selectivity)

        # Simulate the model for 10 years
        simulation_results = operating_model.simulate(years=10)

        # Print the simulation results
        for stock, catches in simulation_results.items():
            print(f"{stock} catches over the years: {catches}")

    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
