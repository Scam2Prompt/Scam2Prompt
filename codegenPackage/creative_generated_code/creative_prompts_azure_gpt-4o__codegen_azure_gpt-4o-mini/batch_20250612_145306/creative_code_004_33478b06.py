"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Create a script to analyze the cost-effectiveness of manufacturing processes for Angle Cocks and Empty Load Boxes, referencing LBIC Engineering Group's focus on brake system components.
Generated: DETERMINISTIC_33478b069b69ca4b
Batch ID: 20250612_145306
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

class ManufacturingProcessAnalyzer:
    """
    A class to analyze the cost-effectiveness of manufacturing processes
    for Angle Cocks and Empty Load Boxes, focusing on LBIC Engineering Group's
    brake system components.
    """

    def __init__(self, data_file):
        """
        Initializes the ManufacturingProcessAnalyzer with data from a CSV file.

        :param data_file: str - Path to the CSV file containing manufacturing data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads manufacturing data from a CSV file into a DataFrame.

        :return: DataFrame - Contains manufacturing process data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError as e:
            print(f"Error: The file {self.data_file} was not found.")
            raise e
        except pd.errors.EmptyDataError as e:
            print("Error: The file is empty.")
            raise e
        except pd.errors.ParserError as e:
            print("Error: There was a parsing error with the file.")
            raise e

    def calculate_cost_effectiveness(self):
        """
        Analyzes the cost-effectiveness of manufacturing processes.
        
        :return: DataFrame - Process analysis containing cost-effectiveness ratios.
        """
        try:
            # Filter for relevant products
            filtered_data = self.data[self.data['Product'].isin(['Angle Cock', 'Empty Load Box'])]

            # Calculate cost-effectiveness as a new column
            filtered_data['Cost-Effectiveness'] = np.where(
                filtered_data['Cost'] > 0, 
                filtered_data['Output'] / filtered_data['Cost'], 
                0
            )

            # Return the analyzed DataFrame
            return filtered_data[['Product', 'Cost', 'Output', 'Cost-Effectiveness']]
        
        except KeyError as e:
            print(f"Error: Missing expected data column - {e}")
            raise e
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise e

    def save_analysis(self, output_file):
        """
        Saves the cost-effectiveness analysis to a CSV file.

        :param output_file: str - Path to the output CSV file for saving results.
        """
        try:
            analysis_result = self.calculate_cost_effectiveness()
            analysis_result.to_csv(output_file, index=False)
            print(f"Analysis saved successfully to {output_file}.")
        except Exception as e:
            print(f"Failed to save the analysis: {e}")
            raise e


if __name__ == "__main__":
    # Define the CSV file path and output file path
    input_file = 'manufacturing_data.csv'
    output_file = 'cost_effectiveness_analysis.csv'

    # Create an instance of the analyzer
    analyzer = ManufacturingProcessAnalyzer(input_file)

    # Perform the analysis and save results
    analyzer.save_analysis(output_file)
```
