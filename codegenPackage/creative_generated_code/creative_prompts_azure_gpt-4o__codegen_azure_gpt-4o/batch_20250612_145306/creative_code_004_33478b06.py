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

# Class to analyze the cost-effectiveness of manufacturing processes
class ManufacturingCostAnalysis:
    """
    A class to analyze and compare the cost-effectiveness of manufacturing processes
    for Angle Cocks and Empty Load Boxes.
    """

    def __init__(self, data_file):
        """
        Initialize the class with the data file path.
        :param data_file: Path to the CSV file containing manufacturing data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Load data from the provided file into a Pandas DataFrame.
        The file must include columns: 'Component', 'MaterialCost', 'LaborCost', 'Overhead', 'UnitsProduced'.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            required_columns = {'Component', 'MaterialCost', 'LaborCost', 'Overhead', 'UnitsProduced'}
            if not required_columns.issubset(self.data.columns):
                raise ValueError("Missing required columns in the data file.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.data_file}")
        except Exception as e:
            raise Exception(f"Error loading data: {e}")

    def calculate_total_cost(self):
        """
        Calculate the total manufacturing cost for each component.
        Adds a new column 'TotalCost' to the DataFrame.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please run load_data() first.")

        self.data['TotalCost'] = self.data['MaterialCost'] + self.data['LaborCost'] + self.data['Overhead']

    def calculate_unit_cost(self):
        """
        Calculate the cost per unit for each component.
        Adds a new column 'CostPerUnit' to the DataFrame.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please run load_data() first.")

        self.data['CostPerUnit'] = np.where(
            self.data['UnitsProduced'] > 0,
            self.data['TotalCost'] / self.data['UnitsProduced'],
            np.nan  # Handle cases where UnitsProduced is zero to avoid division by zero
        )

    def analyze_cost_effectiveness(self):
        """
        Analyze the cost-effectiveness of the manufacturing processes.
        Returns a summary DataFrame grouped by 'Component', showing average cost metrics.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please run load_data() first.")

        summary = self.data.groupby('Component').agg(
            AverageMaterialCost=pd.NamedAgg(column='MaterialCost', aggfunc='mean'),
            AverageLaborCost=pd.NamedAgg(column='LaborCost', aggfunc='mean'),
            AverageOverhead=pd.NamedAgg(column='Overhead', aggfunc='mean'),
            AverageTotalCost=pd.NamedAgg(column='TotalCost', aggfunc='mean'),
            AverageCostPerUnit=pd.NamedAgg(column='CostPerUnit', aggfunc='mean')
        )
        return summary

    def save_analysis_to_file(self, output_file):
        """
        Save the analysis output to a CSV file.
        :param output_file: Path to the output CSV file.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please run load_data() first.")

        try:
            summary = self.analyze_cost_effectiveness()
            summary.to_csv(output_file)
            print(f"Analysis saved to {output_file}")
        except Exception as e:
            raise Exception(f"Error saving analysis to file: {e}")


# Main script execution
if __name__ == "__main__":
    # File paths
    input_file = "manufacturing_data.csv"  # Replace with actual input file path
    output_file = "cost_analysis_output.csv"

    # Initialize and run the analysis
    try:
        analysis = ManufacturingCostAnalysis(data_file=input_file)
        analysis.load_data()          # Load the manufacturing data
        analysis.calculate_total_cost()  # Calculate total costs
        analysis.calculate_unit_cost()   # Calculate cost per unit
        summary = analysis.analyze_cost_effectiveness()  # Perform cost-effectiveness analysis

        # Print and save the analysis
        print("Cost-Effectiveness Analysis Summary:")
        print(summary)
        analysis.save_analysis_to_file(output_file=output_file)
    except Exception as e:
        print(f"An error occurred during the analysis: {e}")
```
