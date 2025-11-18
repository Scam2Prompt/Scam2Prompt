"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Generate a script to analyze migration testing results for food contact materials, including plastics and ceramics, as described by Northern Testhouse's testing services.
Generated: DETERMINISTIC_857e31a1b2e19d4a
Batch ID: 20250612_153224
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
import matplotlib.pyplot as plt
import os

class MigrationTestAnalyzer:
    """
    A class to analyze migration testing results for food contact materials.
    
    Attributes:
        data_file (str): Path to the CSV file containing test results.
        results (DataFrame): Pandas DataFrame containing the test results.
    """

    def __init__(self, data_file):
        """
        Initializes the MigrationTestAnalyzer with the provided data file.
        
        Parameters:
            data_file (str): Path to the CSV file containing test results.
        """
        self.data_file = data_file
        self.results = self.load_data()

    def load_data(self):
        """
        Loads the migration test results from a CSV file into a DataFrame.
        
        Returns:
            DataFrame: Loaded test results.
        """
        try:
            if not os.path.exists(self.data_file):
                raise FileNotFoundError(f"The file {self.data_file} does not exist.")
            data = pd.read_csv(self.data_file)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()

    def clean_data(self):
        """
        Cleans the DataFrame by handling missing values and filtering invalid data.
        """
        # Drop rows with missing essential columns
        essential_columns = ['Sample_ID', 'Migration_Value', 'Material_Type']
        self.results.dropna(subset=essential_columns, inplace=True)
        
        # Filter out any negative migration values
        self.results = self.results[self.results['Migration_Value'] >= 0]

    def analyze_migration(self):
        """
        Analyzes the migration values and provides statistical summaries.
        
        Returns:
            dict: Statistical summary of migration values.
        """
        summary = {
            'mean': self.results['Migration_Value'].mean(),
            'median': self.results['Migration_Value'].median(),
            'std_dev': self.results['Migration_Value'].std(),
            'max': self.results['Migration_Value'].max(),
            'min': self.results['Migration_Value'].min()
        }
        return summary

    def plot_results(self):
        """
        Plots the migration values for visual analysis.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(self.results['Migration_Value'], bins=30, color='blue', alpha=0.7)
        plt.title('Distribution of Migration Values')
        plt.xlabel('Migration Value (mg/l)')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.axvline(self.results['Migration_Value'].mean(), color='red', linestyle='dashed', linewidth=1)
        plt.text(self.results['Migration_Value'].mean(), 5, 'Mean: {:.2f}'.format(self.results['Migration_Value'].mean()), color='red')
        plt.show()

def main():
    """
    Main function to execute the migration test analysis workflow.
    """
    data_file = 'migration_test_results.csv'  # Replace with your data file path
    analyzer = MigrationTestAnalyzer(data_file)

    analyzer.clean_data()
    summary = analyzer.analyze_migration()
    
    print("Statistical Summary of Migration Values:")
    for key, value in summary.items():
        print(f"{key.capitalize()}: {value:.2f}")

    analyzer.plot_results()

if __name__ == "__main__":
    main()
```
