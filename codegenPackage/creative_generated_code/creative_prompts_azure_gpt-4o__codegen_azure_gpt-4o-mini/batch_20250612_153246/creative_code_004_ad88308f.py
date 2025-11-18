"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Generate code to automate energy consumption analysis for enterprises, using Python and Excel, based on the solutions provided by Jacek Kaliński.
Generated: DETERMINISTIC_ad88308f168fcafc
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
import os

class EnergyConsumptionAnalyzer:
    """Automates energy consumption analysis for enterprises using Excel data."""

    def __init__(self, excel_file_path):
        """
        Initializes the EnergyConsumptionAnalyzer with the path to the Excel file.

        Args:
            excel_file_path (str): The path to the Excel file containing energy data.
        """
        self.excel_file_path = excel_file_path
        self.data = None

    def load_data(self):
        """Loads energy consumption data from the specified Excel file."""
        try:
            self.data = pd.read_excel(self.excel_file_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file at {self.excel_file_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def analyze_consumption(self):
        """Analyzes energy consumption data and provides summary statistics."""
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        try:
            summary = {
                'Total Consumption': self.data['Consumption'].sum(),
                'Average Consumption': self.data['Consumption'].mean(),
                'Max Consumption': self.data['Consumption'].max(),
                'Min Consumption': self.data['Consumption'].min(),
                'Std Dev Consumption': self.data['Consumption'].std()
            }
            print("Energy consumption analysis complete.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data: {e}")
            raise
        except Exception as e:
            print(f"An error occurred during analysis: {e}")
            raise

    def save_summary_to_excel(self, summary, output_file_path):
        """
        Saves the summary of the energy consumption analysis to an Excel file.

        Args:
            summary (dict): Summary statistics to save.
            output_file_path (str): Path to save the output Excel file.
        """
        try:
            summary_df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
            summary_df.to_excel(output_file_path, index=False)
            print(f"Summary saved to {output_file_path}.")
        except Exception as e:
            print(f"An error occurred while saving to Excel: {e}")
            raise

def main():
    """Main function to run the energy consumption analysis."""
    # Specify the path to the input Excel file and output file
    input_file_path = 'energy_consumption_data.xlsx'
    output_file_path = 'energy_consumption_summary.xlsx'

    # Create the analyzer instance
    analyzer = EnergyConsumptionAnalyzer(input_file_path)

    # Load the data
    analyzer.load_data()

    # Analyze the consumption
    summary = analyzer.analyze_consumption()

    # Save the summary to an Excel file
    analyzer.save_summary_to_excel(summary, output_file_path)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the input Excel file (`energy_consumption_data.xlsx`) contains a column named "Consumption" for the code to work correctly.
