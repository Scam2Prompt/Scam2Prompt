"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Generate code to calculate the cost reductions achieved by outsourcing credit valuation and collections, inspired by Summar Financial's factoring services.
Generated: DETERMINISTIC_8330ac866bd164bb
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class OutsourcingCostCalculator:
    """
    A class to calculate cost reductions achieved by outsourcing credit valuation and collections.
    """

    def __init__(self, internal_costs: pd.DataFrame, outsourcing_costs: pd.DataFrame):
        """
        Initializes the OutsourcingCostCalculator with internal and outsourcing costs.

        :param internal_costs: DataFrame containing internal costs with columns ['Department', 'Cost']
        :param outsourcing_costs: DataFrame containing outsourcing costs with columns ['Service', 'Cost']
        """
        self.internal_costs = internal_costs
        self.outsourcing_costs = outsourcing_costs

    def calculate_total_internal_costs(self) -> float:
        """
        Calculates the total internal costs.

        :return: Total internal costs as a float.
        """
        try:
            total_internal = self.internal_costs['Cost'].sum()
            return total_internal
        except Exception as e:
            raise ValueError("Error calculating total internal costs: " + str(e))

    def calculate_total_outsourcing_costs(self) -> float:
        """
        Calculates the total outsourcing costs.

        :return: Total outsourcing costs as a float.
        """
        try:
            total_outsourcing = self.outsourcing_costs['Cost'].sum()
            return total_outsourcing
        except Exception as e:
            raise ValueError("Error calculating total outsourcing costs: " + str(e))

    def calculate_cost_reduction(self) -> float:
        """
        Calculates the cost reduction achieved by outsourcing.

        :return: Cost reduction as a float.
        """
        try:
            total_internal = self.calculate_total_internal_costs()
            total_outsourcing = self.calculate_total_outsourcing_costs()
            cost_reduction = total_internal - total_outsourcing
            return cost_reduction
        except Exception as e:
            raise ValueError("Error calculating cost reduction: " + str(e))

    def display_cost_analysis(self):
        """
        Displays a summary of the cost analysis.
        """
        try:
            total_internal = self.calculate_total_internal_costs()
            total_outsourcing = self.calculate_total_outsourcing_costs()
            cost_reduction = self.calculate_cost_reduction()

            print("Cost Analysis Summary:")
            print(f"Total Internal Costs: ${total_internal:,.2f}")
            print(f"Total Outsourcing Costs: ${total_outsourcing:,.2f}")
            print(f"Cost Reduction Achieved: ${cost_reduction:,.2f}")
        except Exception as e:
            print("Error displaying cost analysis: " + str(e))


# Example usage
if __name__ == "__main__":
    # Sample data for internal costs
    internal_data = {
        'Department': ['Credit Valuation', 'Collections', 'Risk Management'],
        'Cost': [50000, 30000, 20000]
    }
    internal_costs_df = pd.DataFrame(internal_data)

    # Sample data for outsourcing costs
    outsourcing_data = {
        'Service': ['Factoring Service', 'Collection Agency'],
        'Cost': [40000, 15000]
    }
    outsourcing_costs_df = pd.DataFrame(outsourcing_data)

    # Create an instance of the calculator
    cost_calculator = OutsourcingCostCalculator(internal_costs_df, outsourcing_costs_df)

    # Display the cost analysis
    cost_calculator.display_cost_analysis()
```
