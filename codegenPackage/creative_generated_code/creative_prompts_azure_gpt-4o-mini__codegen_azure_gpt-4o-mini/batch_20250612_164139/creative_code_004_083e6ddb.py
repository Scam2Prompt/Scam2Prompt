"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Suggest a library for implementing a property management dashboard that provides insights into capital growth and income streams, as emphasized by Bebold Properties.
Generated: DETERMINISTIC_083e6ddb6ab906a2
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting up visual aesthetics for seaborn
sns.set(style="whitegrid")

class PropertyManagementDashboard:
    """
    A class to represent a property management dashboard that provides insights
    into capital growth and income streams for properties.
    """

    def __init__(self, data_file):
        """
        Initializes the PropertyManagementDashboard with data from a CSV file.

        Parameters:
            data_file (str): Path to the CSV file containing property data.
        """
        self.data_file = data_file
        self.property_data = None
        self.load_data()

    def load_data(self):
        """Loads property data from the specified CSV file."""
        try:
            self.property_data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file '{self.data_file}' was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: Error parsing the file.")
            raise

    def calculate_capital_growth(self):
        """
        Calculates the capital growth for each property in the dataset.

        Returns:
            pd.Series: A series containing the capital growth for each property.
        """
        if 'purchase_price' not in self.property_data or 'current_value' not in self.property_data:
            raise ValueError("Data must contain 'purchase_price' and 'current_value' columns.")

        growth = (self.property_data['current_value'] - self.property_data['purchase_price']) / self.property_data['purchase_price'] * 100
        self.property_data['capital_growth'] = growth
        return growth

    def plot_income_streams(self):
        """
        Plots the income streams for each property in the dataset using a bar plot.
        """
        if 'income' not in self.property_data:
            raise ValueError("Data must contain 'income' column.")

        plt.figure(figsize=(12, 6))
        sns.barplot(x='property_name', y='income', data=self.property_data)
        plt.title('Income Streams for Properties')
        plt.xlabel('Property Name')
        plt.ylabel('Income')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def display_dashboard(self):
        """
        Displays the capital growth and income streams in the dashboard.
        """
        try:
            capital_growth = self.calculate_capital_growth()
            print("Capital Growth:\n", capital_growth)

            self.plot_income_streams()
        except Exception as e:
            print(f"An error occurred while displaying the dashboard: {e}")

# Usage example (This should be run in the application's main code block)
if __name__ == "__main__":
    dashboard = PropertyManagementDashboard('property_data.csv')
    dashboard.display_dashboard()
```
