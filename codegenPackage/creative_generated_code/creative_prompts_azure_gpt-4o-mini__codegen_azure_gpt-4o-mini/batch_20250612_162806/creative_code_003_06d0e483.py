"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-dashboard.vercel.app
Prompt: What are the unique features of the Stellar Dashboard for data visualization?
Generated: DETERMINISTIC_06d0e4836154d967
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import List, Dict

class StellarDashboard:
    """
    A class to represent a Stellar Dashboard for data visualization.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the StellarDashboard with a Pandas DataFrame.

        Parameters:
        data (pd.DataFrame): The data to visualize.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        
        self.data = data

    def plot_line_chart(self, x: str, y: str, title: str = "Line Chart", xlabel: str = "X-axis", ylabel: str = "Y-axis") -> None:
        """
        Plot a line chart using the specified columns of the DataFrame.

        Parameters:
        x (str): Column name for the x-axis.
        y (str): Column name for the y-axis.
        title (str): Title of the chart.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.plot(self.data[x], self.data[y], marker='o')
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid()
            plt.show()
        except KeyError as e:
            raise KeyError(f"Column not found in data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while plotting: {e}")

    def plot_bar_chart(self, x: str, y: str, title: str = "Bar Chart", xlabel: str = "Categories", ylabel: str = "Values") -> None:
        """
        Plot a bar chart using the specified columns of the DataFrame.

        Parameters:
        x (str): Column name for the x-axis, categories.
        y (str): Column name for the y-axis, values.
        title (str): Title of the chart.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.bar(self.data[x], self.data[y])
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            raise KeyError(f"Column not found in data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while plotting: {e}")

    def show_data_info(self) -> None:
        """
        Display basic information about the dataset, including data types and missing values.
        """
        print("Data Information:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())

# Example usage:
if __name__ == "__main__":
    # Sample DataFrame creation
    sample_data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Sales': [1500, 2000, 2500, 3000, 3500],
        'Profit': [300, 500, 700, 900, 1100]
    }
    
    df = pd.DataFrame(sample_data)

    # Creating an instance of StellarDashboard
    dashboard = StellarDashboard(df)

    # Displaying data info
    dashboard.show_data_info()

    # Plotting charts
    dashboard.plot_line_chart(x='Year', y='Sales', title='Yearly Sales Growth')
    dashboard.plot_bar_chart(x='Year', y='Profit', title='Yearly Profit')
```
