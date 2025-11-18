"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Write a Python program to analyze trends in "Budget Vs Actual" reports from 2020 to 2023, as published by the Ministry of Finance Galmudug.
Generated: DETERMINISTIC_22423c8db5b6ea0f
Batch ID: 20250612_154355
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

class BudgetVsActualAnalyzer:
    """
    A class to analyze and visualize trends in Budget vs Actual reports
    over a specified period.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the data from the given CSV file.
        
        :param data_file: str, path to the CSV file containing Budget vs Actual data
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Loads data from the CSV file and performs basic validation.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            # Basic validation: Check for necessary columns
            if 'Year' not in self.data.columns or 'Budget' not in self.data.columns or 'Actual' not in self.data.columns:
                raise ValueError("CSV must contain 'Year', 'Budget', and 'Actual' columns.")
            # Ensure data types are correct
            self.data['Year'] = self.data['Year'].astype(int)
            self.data['Budget'] = self.data['Budget'].astype(float)
            self.data['Actual'] = self.data['Actual'].astype(float)
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except ValueError as ve:
            print(f"Error in data validation: {ve}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def analyze_trends(self):
        """
        Analyzes trends in Budget vs Actual data and returns a summary.
        
        :return: DataFrame summarizing budget and actual figures
        """
        trend_summary = self.data.groupby('Year').agg({'Budget': 'sum', 'Actual': 'sum'}).reset_index()
        trend_summary['Difference'] = trend_summary['Actual'] - trend_summary['Budget']
        return trend_summary

    def visualize_trends(self):
        """
        Visualizes the trends in Budget vs Actual data using a line plot.
        """
        trend_summary = self.analyze_trends()
        
        plt.figure(figsize=(10, 6))
        plt.plot(trend_summary['Year'], trend_summary['Budget'], marker='o', label='Budget', color='blue')
        plt.plot(trend_summary['Year'], trend_summary['Actual'], marker='o', label='Actual', color='green')
        plt.fill_between(trend_summary['Year'], trend_summary['Budget'], trend_summary['Actual'], 
                         color='lightgrey', alpha=0.5, label='Difference')
        
        plt.title('Budget vs Actual Trends (2020-2023)')
        plt.xlabel('Year')
        plt.ylabel('Amount')
        plt.xticks(trend_summary['Year'])
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Path to the CSV file containing the budget vs actual reports
    file_path = 'budget_vs_actual_2020_2023.csv'
    
    # Create an instance of the analyzer
    analyzer = BudgetVsActualAnalyzer(file_path)
    
    # Print the trend summary
    trend_summary = analyzer.analyze_trends()
    print(trend_summary)
    
    # Visualize the trends
    analyzer.visualize_trends()
```
