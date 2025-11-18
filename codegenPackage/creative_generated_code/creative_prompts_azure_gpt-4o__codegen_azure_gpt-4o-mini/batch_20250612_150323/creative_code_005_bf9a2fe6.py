"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Write a Python script to analyze e-commerce sales growth trends, inspired by Metamark's insights on the 20% annual growth in online sales.
Generated: DETERMINISTIC_bf9a2fe6802ea7d3
Batch ID: 20250612_150323
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

class SalesGrowthAnalyzer:
    """
    A class to analyze e-commerce sales growth trends.
    """

    def __init__(self, sales_data: str):
        """
        Initializes the SalesGrowthAnalyzer with sales data from a CSV file.

        :param sales_data: Path to the CSV file containing sales data.
        """
        self.sales_data = sales_data
        self.df = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads sales data from a CSV file into a DataFrame.

        :return: Pandas DataFrame containing the sales data.
        """
        try:
            df = pd.read_csv(self.sales_data)
            df['Date'] = pd.to_datetime(df['Date'])
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.sales_data} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_growth(self) -> pd.DataFrame:
        """
        Calculates the year-over-year growth of sales.

        :return: DataFrame containing the sales and growth percentages.
        """
        self.df.set_index('Date', inplace=True)
        yearly_sales = self.df.resample('Y').sum()
        yearly_sales['Growth (%)'] = yearly_sales['Sales'].pct_change() * 100
        return yearly_sales

    def plot_growth(self, growth_data: pd.DataFrame):
        """
        Plots the year-over-year sales growth.

        :param growth_data: DataFrame containing sales and growth data.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(growth_data.index, growth_data['Sales'], marker='o', label='Sales')
        plt.plot(growth_data.index, growth_data['Growth (%)'], marker='o', label='Growth (%)', color='orange')
        plt.title('E-commerce Sales Growth Trends')
        plt.xlabel('Year')
        plt.ylabel('Sales and Growth (%)')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

    def analyze(self):
        """
        Executes the analysis of sales growth trends.
        """
        growth_data = self.calculate_growth()
        print(growth_data)
        self.plot_growth(growth_data)


if __name__ == "__main__":
    # Specify the path to the sales data CSV file
    sales_data_path = 'sales_data.csv'

    # Initialize the SalesGrowthAnalyzer
    analyzer = SalesGrowthAnalyzer(sales_data_path)

    # Perform the analysis
    analyzer.analyze()
```
