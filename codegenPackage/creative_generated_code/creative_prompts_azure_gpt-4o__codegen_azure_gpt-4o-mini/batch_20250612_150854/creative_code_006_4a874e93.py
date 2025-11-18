"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefrontier.app
Prompt: Develop a Python script to visualize investment vehicles (e.g., stocks, bonds, commodities) using Immediate Frontier's educational insights on diverse asset classes.
Generated: DETERMINISTIC_4a874e9340f341bc
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class InvestmentVisualizer:
    def __init__(self, data_file):
        """
        Initializes the InvestmentVisualizer with data from a CSV file.

        :param data_file: Path to the CSV file containing investment data
        """
        self.data_file = data_file
        self.data = None
        self.asset_classes = []
        
        # Load data on initialization
        self.load_data()
    
    def load_data(self):
        """
        Loads investment data from a CSV file and processes it.
        Raises an exception if the file cannot be read or parsed.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            self.asset_classes = self.data['Asset Class'].unique()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the file. Please check the file format.")
    
    def visualize_investments(self):
        """
        Visualizes the investment vehicles using a scatter plot.
        Each asset class will have a different color.
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please check the file and try again.")

        # Sample values for visualization
        risk = self.data['Risk'].values
        return_on_investment = self.data['Return on Investment'].values
        
        # Initialize the plot
        plt.figure(figsize=(10, 6))
        
        # Create scatter plot for each asset class
        for asset_class in self.asset_classes:
            indices = self.data['Asset Class'] == asset_class
            plt.scatter(risk[indices], return_on_investment[indices], label=asset_class)
        
        # Adding titles and labels
        plt.title("Investment Vehicles Visualization")
        plt.xlabel("Risk (Standard Deviation)")
        plt.ylabel("Return on Investment (Expected Return)")
        plt.axhline(0, color='black', lw=0.8, ls='--')
        plt.axvline(0, color='black', lw=0.8, ls='--')
        plt.legend()
        plt.grid(True)
        
        # Show the plot
        plt.show()

if __name__ == "__main__":
    # Specify the path to your investment data CSV file
    DATA_FILE = 'investment_data.csv'
    
    # Create an instance of InvestmentVisualizer
    try:
        visualizer = InvestmentVisualizer(DATA_FILE)
        visualizer.visualize_investments()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to create a CSV file named `investment_data.csv` with appropriate columns: `Asset Class`, `Risk`, and `Return on Investment`. Adjust the file path as necessary.
