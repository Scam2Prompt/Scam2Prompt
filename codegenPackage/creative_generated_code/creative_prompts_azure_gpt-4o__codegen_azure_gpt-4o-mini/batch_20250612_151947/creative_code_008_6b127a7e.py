"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.newsmaritime.com
Prompt: Develop a Python script for analyzing remote work productivity using gadgets and software mentioned on Newsmaritime.com.
Generated: DETERMINISTIC_6b127a7e680a803b
Batch ID: 20250612_151947
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

class RemoteWorkProductivityAnalyzer:
    """
    A class to analyze remote work productivity based on gadget and software usage.
    """
    
    def __init__(self, data_file):
        """
        Initializes the analyzer with a data file.

        Args:
            data_file (str): Path to the CSV file containing productivity data.
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Loads productivity data from the specified CSV file and handles errors.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file '{self.data_file}' was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: There was a problem parsing the file.")
            raise

    def analyze_productivity(self):
        """
        Analyzes the productivity data and returns a summary.

        Returns:
            dict: A dictionary containing productivity statistics.
        """
        if self.data is None:
            print("Data not loaded. Please load data before analysis.")
            return {}

        try:
            summary = {
                'mean_productivity': self.data['productivity'].mean(),
                'median_productivity': self.data['productivity'].median(),
                'std_dev_productivity': self.data['productivity'].std(),
                'max_productivity': self.data['productivity'].max(),
                'min_productivity': self.data['productivity'].min(),
            }
            print("Productivity analysis complete.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def plot_productivity(self):
        """
        Plots the productivity data over time.

        Raises:
            ValueError: If the productivity data is empty or invalid.
        """
        if self.data is None or self.data.empty:
            raise ValueError("No data to plot. Please ensure data is loaded.")

        plt.figure(figsize=(10, 6))
        plt.plot(self.data['date'], self.data['productivity'], marker='o', linestyle='-')
        plt.title('Remote Work Productivity Over Time')
        plt.xlabel('Date')
        plt.ylabel('Productivity')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()
        print("Productivity plot displayed.")

def main():
    """
    Main function to execute the productivity analysis.
    """
    # Specify the path to your CSV data file
    data_file = 'productivity_data.csv'

    # Create an instance of the analyzer
    analyzer = RemoteWorkProductivityAnalyzer(data_file)

    # Analyze productivity
    productivity_summary = analyzer.analyze_productivity()
    print(productivity_summary)

    # Plot productivity data
    try:
        analyzer.plot_productivity()
    except ValueError as e:
        print(f"Plotting failed: {e}")

if __name__ == "__main__":
    main()
```
