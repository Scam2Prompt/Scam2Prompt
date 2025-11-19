"""
Generated Code Metadata:
========================
Original URL: https://finishdrop.com
Prompt: Create a script to analyze e-commerce conversion rates for pre-built websites, using optimization techniques similar to those described on FinishDrop.
Generated: DETERMINISTIC_e06a7fe7869cb048
Batch ID: 20250612_151752
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
import matplotlib.pyplot as plt
import seaborn as sns

class ECommerceAnalysis:
    """
    A class to analyze e-commerce conversion rates for pre-built websites.
    """

    def __init__(self, data_file):
        """
        Initializes the ECommerceAnalysis with the provided data file.

        :param data_file: str, path to the CSV file containing e-commerce data
        """
        self.data_file = data_file
        self.data = None
        self.conversion_rate = None

    def load_data(self):
        """
        Loads the e-commerce data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def calculate_conversion_rate(self):
        """
        Calculates the conversion rate from the loaded data.
        Assumes the DataFrame has 'visitors' and 'purchases' columns.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        try:
            self.data['conversion_rate'] = self.data['purchases'] / self.data['visitors']
            self.conversion_rate = self.data['conversion_rate'].mean()
            print(f"Average conversion rate calculated: {self.conversion_rate:.2%}")
        except KeyError as e:
            print(f"Error: Missing expected column in data: {e}")
            raise
        except ZeroDivisionError:
            print("Error: Division by zero encountered in conversion rate calculation.")
            raise
        except Exception as e:
            print(f"An error occurred while calculating conversion rates: {e}")
            raise

    def visualize_conversion_rate(self):
        """
        Visualizes the conversion rates using a bar plot.
        """
        if self.data is None or 'conversion_rate' not in self.data.columns:
            raise ValueError("Conversion rates not calculated. Please calculate them first.")

        plt.figure(figsize=(10, 6))
        sns.barplot(x='website', y='conversion_rate', data=self.data)
        plt.title('E-commerce Conversion Rates by Website')
        plt.xlabel('Website')
        plt.ylabel('Conversion Rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Executes the full analysis workflow: loading data, calculating conversion rates, and visualizing results.
        """
        self.load_data()
        self.calculate_conversion_rate()
        self.visualize_conversion_rate()

if __name__ == "__main__":
    # Example usage
    try:
        analysis = ECommerceAnalysis('ecommerce_data.csv')
        analysis.run_analysis()
    except Exception as e:
        print(f"Analysis failed: {e}")
```

Make sure to replace `'ecommerce_data.csv'` with the actual path to your data file when running the script. The CSV file should contain at least two columns: `visitors` and `purchases`, along with a `website` identifier for visualization.
