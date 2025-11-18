"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Create a tool to compare the cost-effectiveness of StoTherm insulation systems versus traditional insulation methods, using data inspired by Engenharia WPJ's offerings.
Generated: DETERMINISTIC_551945546006dea2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class InsulationComparisonTool:
    """
    A tool to compare the cost-effectiveness of StoTherm insulation systems
    versus traditional insulation methods.
    """

    def __init__(self, sto_therm_data, traditional_data):
        """
        Initializes the InsulationComparisonTool with StoTherm and traditional insulation data.
        
        :param sto_therm_data: DataFrame containing StoTherm insulation data.
        :param traditional_data: DataFrame containing traditional insulation data.
        """
        self.sto_therm_data = sto_therm_data
        self.traditional_data = traditional_data

    def calculate_cost_effectiveness(self):
        """
        Calculate cost-effectiveness for both insulation systems.

        :return: DataFrame comparing cost-effectiveness of StoTherm vs. traditional insulation.
        """
        try:
            # Calculate total cost for StoTherm
            self.sto_therm_data['Total Cost'] = self.sto_therm_data['Material Cost'] + self.sto_therm_data['Labor Cost']
            self.sto_therm_data['Cost Effectiveness'] = self.sto_therm_data['R-Value'] / self.sto_therm_data['Total Cost']

            # Calculate total cost for Traditional
            self.traditional_data['Total Cost'] = self.traditional_data['Material Cost'] + self.traditional_data['Labor Cost']
            self.traditional_data['Cost Effectiveness'] = self.traditional_data['R-Value'] / self.traditional_data['Total Cost']
            
            # Combine the results into a single DataFrame
            comparison_df = pd.DataFrame({
                'System': ['StoTherm', 'Traditional'],
                'Total Cost': [self.sto_therm_data['Total Cost'].mean(), self.traditional_data['Total Cost'].mean()],
                'Average R-Value': [self.sto_therm_data['R-Value'].mean(), self.traditional_data['R-Value'].mean()],
                'Cost Effectiveness': [self.sto_therm_data['Cost Effectiveness'].mean(), self.traditional_data['Cost Effectiveness'].mean()]
            })

            return comparison_df

        except KeyError as e:
            raise KeyError(f"Missing required data column: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating cost-effectiveness: {e}")

def main():
    """
    Main function to execute the insulation comparison tool.
    """
    # Example data for StoTherm insulation
    sto_therm_data = pd.DataFrame({
        'Material Cost': [15, 18, 20],
        'Labor Cost': [5, 6, 7],
        'R-Value': [5.0, 5.5, 6.0]
    })

    # Example data for traditional insulation
    traditional_data = pd.DataFrame({
        'Material Cost': [10, 12, 14],
        'Labor Cost': [4, 5, 6],
        'R-Value': [3.5, 4.0, 4.5]
    })

    # Instantiate the comparison tool
    comparison_tool = InsulationComparisonTool(sto_therm_data, traditional_data)

    # Calculate and display cost-effectiveness
    result = comparison_tool.calculate_cost_effectiveness()
    print(result)

if __name__ == "__main__":
    main()
```
