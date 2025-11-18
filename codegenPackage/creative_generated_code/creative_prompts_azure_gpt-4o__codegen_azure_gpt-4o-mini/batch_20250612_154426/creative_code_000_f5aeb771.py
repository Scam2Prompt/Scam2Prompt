"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itls-iso.com
Prompt: Write Python code to optimize a supply chain process using the iTLS methodology, incorporating elements of TOC, Lean, and Six Sigma as described on the iTLS-ISO website.
Generated: DETERMINISTIC_f5aeb77157f70f9a
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class SupplyChainOptimizer:
    """
    A class to optimize a supply chain process using the iTLS methodology,
    incorporating elements of Theory of Constraints (TOC), Lean, and 
    Six Sigma methodologies.
    """

    def __init__(self, demand_forecast, supply_capacity, lead_times):
        """
        Initializes the optimizer with demand forecast, supply capacity, 
        and lead times.

        Parameters:
            demand_forecast (pd.Series): Forecasted demand for products.
            supply_capacity (pd.Series): Maximum supply capacity for products.
            lead_times (pd.Series): Lead times associated with supply.
        """
        self.demand_forecast = demand_forecast
        self.supply_capacity = supply_capacity
        self.lead_times = lead_times

    def validate_inputs(self):
        """
        Validates the input data to ensure they are in the correct format
        and contain no negative values.
        Raises ValueError if inputs are invalid.
        """
        for series in [self.demand_forecast, self.supply_capacity, self.lead_times]:
            if not isinstance(series, pd.Series):
                raise ValueError("Input should be a pandas Series.")
            if any(series < 0):
                raise ValueError("Inputs must be non-negative.")

    def optimize_supply_chain(self):
        """
        Optimizes the supply chain process by balancing demand and supply
        while minimizing lead times.
        
        Returns:
            pd.DataFrame: A DataFrame containing the optimized supply plan.
        """
        self.validate_inputs()

        # Calculate total demand and supply
        total_demand = self.demand_forecast.sum()
        total_supply = self.supply_capacity.sum()

        # Create an optimized supply plan
        optimized_plan = pd.DataFrame({
            'Product': self.demand_forecast.index,
            'Optimized Demand': self.demand_forecast,
            'Supply Capacity': self.supply_capacity,
            'Lead Time': self.lead_times,
            'Optimal Supply': np.minimum(self.demand_forecast, self.supply_capacity)
        })

        # Calculate the excess supply or unmet demand
        optimized_plan['Excess Supply'] = optimized_plan['Supply Capacity'] - optimized_plan['Optimal Supply']
        optimized_plan['Unmet Demand'] = np.maximum(0, optimized_plan['Optimized Demand'] - optimized_plan['Optimal Supply'])

        # Apply Lean principles to eliminate waste
        optimized_plan['Waste Reduction'] = optimized_plan['Excess Supply'] + optimized_plan['Unmet Demand']

        # Sort the optimized plan by lead time to ensure efficient order fulfillment
        optimized_plan.sort_values(by='Lead Time', inplace=True)

        return optimized_plan

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        demand_forecast = pd.Series({'Product A': 100, 'Product B': 150, 'Product C': 80})
        supply_capacity = pd.Series({'Product A': 120, 'Product B': 130, 'Product C': 70})
        lead_times = pd.Series({'Product A': 2, 'Product B': 1, 'Product C': 3})

        # Create an optimizer instance
        optimizer = SupplyChainOptimizer(demand_forecast, supply_capacity, lead_times)

        # Optimize the supply chain
        optimized_supply_plan = optimizer.optimize_supply_chain()
        
        # Display the optimized supply plan
        print(optimized_supply_plan)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
