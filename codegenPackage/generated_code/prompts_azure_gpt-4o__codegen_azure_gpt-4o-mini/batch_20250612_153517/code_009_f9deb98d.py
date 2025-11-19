"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a script to analyze and optimize the supply chain for cosmetic product manufacturing, inspired by the logistical capabilities of Fabricare Cosméticos.
Generated: DETERMINISTIC_f9deb98de6885b96
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import List, Dict

class SupplyChainOptimizer:
    """
    A class to analyze and optimize the supply chain for cosmetic product manufacturing.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SupplyChainOptimizer with supply chain data.

        :param data: A pandas DataFrame containing supply chain information.
        """
        self.data = data

    def validate_data(self) -> None:
        """
        Validates the input data for necessary columns and data types.
        Raises ValueError if validation fails.
        """
        required_columns = ['Supplier', 'Product', 'LeadTime', 'Cost', 'Demand']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the supply chain.

        :return: Total cost as a float.
        """
        return (self.data['Cost'] * self.data['Demand']).sum()

    def optimize_supply_chain(self) -> pd.DataFrame:
        """
        Optimizes the supply chain by minimizing costs while meeting demand.

        :return: A DataFrame with optimized supply chain details.
        """
        # Sort suppliers by cost and lead time
        sorted_data = self.data.sort_values(by=['Cost', 'LeadTime'])
        
        optimized_supply = []
        total_demand = sorted_data['Demand'].sum()

        for _, row in sorted_data.iterrows():
            if total_demand <= 0:
                break
            
            supply = min(row['Demand'], total_demand)
            optimized_supply.append({
                'Supplier': row['Supplier'],
                'Product': row['Product'],
                'Supply': supply,
                'Cost': row['Cost'],
                'LeadTime': row['LeadTime']
            })
            total_demand -= supply

        return pd.DataFrame(optimized_supply)

    def analyze_supply_chain(self) -> Dict[str, float]:
        """
        Analyzes the supply chain and returns key metrics.

        :return: A dictionary containing analysis results.
        """
        total_cost = self.calculate_total_cost()
        average_lead_time = self.data['LeadTime'].mean()
        
        return {
            'TotalCost': total_cost,
            'AverageLeadTime': average_lead_time
        }

def main():
    # Sample data for supply chain analysis
    data = {
        'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
        'Product': ['Lipstick', 'Foundation', 'Mascara'],
        'LeadTime': [5, 3, 7],
        'Cost': [2.5, 3.0, 2.0],
        'Demand': [100, 150, 200]
    }

    # Create a DataFrame
    supply_chain_data = pd.DataFrame(data)

    # Initialize the optimizer
    optimizer = SupplyChainOptimizer(supply_chain_data)

    try:
        # Validate the data
        optimizer.validate_data()

        # Analyze the supply chain
        analysis_results = optimizer.analyze_supply_chain()
        print("Supply Chain Analysis Results:", analysis_results)

        # Optimize the supply chain
        optimized_results = optimizer.optimize_supply_chain()
        print("Optimized Supply Chain:", optimized_results)

    except ValueError as e:
        print(f"Data validation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
