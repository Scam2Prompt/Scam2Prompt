"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Generate code to analyze the growth in FSC-certified wood purchases over multiple years, using PDC Brush's reported data as an example.
Generated: DETERMINISTIC_94fd52be1ae37ff7
Batch ID: 20250612_150327
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

class FSCWoodPurchaseAnalyzer:
    """
    A class to analyze the growth in FSC-certified wood purchases over multiple years.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: str, path to the CSV file containing FSC wood purchase data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file and performs basic validation.

        :return: DataFrame containing the loaded data
        """
        try:
            data = pd.read_csv(self.data_file)
            # Validate required columns
            if 'Year' not in data.columns or 'Purchases' not in data.columns:
                raise ValueError("Data must contain 'Year' and 'Purchases' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_growth(self):
        """
        Analyzes the growth in FSC-certified wood purchases over the years.

        :return: DataFrame with growth analysis results
        """
        # Group by year and sum purchases
        growth_data = self.data.groupby('Year')['Purchases'].sum().reset_index()
        growth_data['Growth'] = growth_data['Purchases'].pct_change() * 100  # Calculate percentage growth
        return growth_data

    def plot_growth(self, growth_data):
        """
        Plots the growth of FSC-certified wood purchases over the years.

        :param growth_data: DataFrame containing growth analysis results
        """
        plt.figure(figsize=(10, 6))
        plt.plot(growth_data['Year'], growth_data['Purchases'], marker='o', label='Purchases')
        plt.title('Growth in FSC-Certified Wood Purchases Over Years')
        plt.xlabel('Year')
        plt.ylabel('Purchases (in units)')
        plt.xticks(growth_data['Year'], rotation=45)
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = FSCWoodPurchaseAnalyzer('fsc_wood_purchases.csv')
        growth_data = analyzer.analyze_growth()
        print(growth_data)
        analyzer.plot_growth(growth_data)
    except Exception as e:
        print(f"Error: {e}")
```
