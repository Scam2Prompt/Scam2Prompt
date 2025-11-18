"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Generate code to calculate the cost reductions achieved by outsourcing credit valuation and collections, inspired by Summar Financial's factoring services.
Generated: DETERMINISTIC_8330ac866bd164bb
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CostReductionCalculator:
    """
    A class to calculate cost reductions achieved by outsourcing credit valuation and collections.
    """

    def __init__(self, internal_costs_df, outsourced_costs_df):
        """
        Initialize the CostReductionCalculator with internal and outsourced costs data.

        :param internal_costs_df: DataFrame containing internal costs with columns ['Department', 'Cost']
        :param outsourced_costs_df: DataFrame containing outsourced costs with columns ['Service', 'Cost']
        """
        self.internal_costs_df = internal_costs_df
        self.outsourced_costs_df = outsourced_costs_df
    
    def validate_dataframes(self):
        """
        Validates the structure of the provided DataFrames.
        
        Raises:
            ValueError: If the DataFrames do not have the expected columns.
        """
        required_columns = ['Department', 'Cost']
        if not all(col in self.internal_costs_df.columns for col in required_columns):
            raise ValueError(f"Internal costs DataFrame must contain columns: {required_columns}")

        if not all(col in self.outsourced_costs_df.columns for col in required_columns):
            raise ValueError(f"Outsourced costs DataFrame must contain columns: {required_columns}")

    def calculate_cost_reduction(self):
        """
        Calculate the cost reduction achieved by outsourcing.

        :return: A dictionary with total internal costs, total outsourced costs, and cost reduction amount.
        """
        self.validate_dataframes()

        # Calculate total internal costs
        total_internal_costs = self.internal_costs_df['Cost'].sum()

        # Calculate total outsourced costs
        total_outsourced_costs = self.outsourced_costs_df['Cost'].sum()

        # Calculate cost reduction
        cost_reduction = total_internal_costs - total_outsourced_costs

        # Prepare the results
        results = {
            'Total Internal Costs': total_internal_costs,
            'Total Outsourced Costs': total_outsourced_costs,
            'Cost Reduction': cost_reduction
        }

        return results


# Sample data for internal and outsourced costs
internal_costs_data = {
    'Department': ['Credit Valuation', 'Collections', 'Risk Management'],
    'Cost': [50000, 30000, 20000]
}

outsourced_costs_data = {
    'Service': ['Factoring Service', 'Outsourced Collection'],
    'Cost': [15000, 10000]
}

# Create DataFrames from sample data
internal_costs_df = pd.DataFrame(internal_costs_data)
outsourced_costs_df = pd.DataFrame(outsourced_costs_data)

# Instantiate the CostReductionCalculator
cost_calculator = CostReductionCalculator(internal_costs_df, outsourced_costs_df)

# Calculate and print the cost reductions
try:
    cost_reduction_results = cost_calculator.calculate_cost_reduction()
    print(cost_reduction_results)
except ValueError as e:
    print(f"Input Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
