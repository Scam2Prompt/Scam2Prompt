"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write code to analyze trends in charitable giving by the Armourers & Brasiers' Company over the last decade, using historical data.
Generated: DETERMINISTIC_3bd1f14ddda041bd
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CharitableGivingAnalyzer:
    """
    A class to analyze trends in charitable giving by the Armourers & Brasiers' Company.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the given data file.

        :param data_file: str, path to the CSV file containing historical giving data
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the charitable giving data from a CSV file into a pandas DataFrame.
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
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by converting date columns and handling missing values.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Convert 'date' column to datetime
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')

        # Drop rows with missing values in critical columns
        self.data.dropna(subset=['date', 'amount'], inplace=True)

        # Extract year from date for analysis
        self.data['year'] = self.data['date'].dt.year

    def analyze_trends(self):
        """
        Analyzes trends in charitable giving over the years and visualizes the results.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Group by year and sum the amounts
        trend_data = self.data.groupby('year')['amount'].sum().reset_index()

        # Plotting the trends
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=trend_data, x='year', y='amount', marker='o')
        plt.title("Trends in Charitable Giving Over the Last Decade")
        plt.xlabel("Year")
        plt.ylabel("Total Amount Given (£)")
        plt.xticks(trend_data['year'], rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Path to the CSV file containing historical charitable giving data
    data_file_path = 'charitable_giving_data.csv'

    # Create an instance of the analyzer
    analyzer = CharitableGivingAnalyzer(data_file_path)

    # Load, preprocess, and analyze the data
    try:
        analyzer.load_data()
        analyzer.preprocess_data()
        analyzer.analyze_trends()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
