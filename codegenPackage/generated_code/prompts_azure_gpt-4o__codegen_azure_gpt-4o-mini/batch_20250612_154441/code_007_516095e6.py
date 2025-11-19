"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Create a Python script to compare the mechanical properties of treated eucalyptus wood versus untreated native woods, as discussed on Trattar Madeiras' website.
Generated: DETERMINISTIC_516095e6529a8da3
Batch ID: 20250612_154441
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

class WoodComparison:
    """
    A class to compare the mechanical properties of treated eucalyptus wood
    versus untreated native woods.
    """

    def __init__(self, treated_data: str, untreated_data: str):
        """
        Initializes the WoodComparison class with file paths for treated and untreated wood data.

        :param treated_data: Path to the CSV file containing treated eucalyptus wood data.
        :param untreated_data: Path to the CSV file containing untreated native woods data.
        """
        self.treated_data = treated_data
        self.untreated_data = untreated_data
        self.treated_df = None
        self.untreated_df = None

    def load_data(self):
        """
        Loads the treated and untreated wood data from CSV files into pandas DataFrames.
        """
        try:
            self.treated_df = pd.read_csv(self.treated_data)
            self.untreated_df = pd.read_csv(self.untreated_data)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the file paths.")
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
        except pd.errors.ParserError:
            print("Error: Could not parse the data. Please check the file format.")

    def compare_properties(self):
        """
        Compares the mechanical properties of treated eucalyptus wood with untreated native woods.
        """
        if self.treated_df is None or self.untreated_df is None:
            print("Data not loaded. Please call load_data() first.")
            return

        # Assuming the DataFrames have a 'Property' column and a 'Value' column
        properties = self.treated_df['Property'].unique()
        comparison_df = pd.DataFrame(columns=['Property', 'Treated', 'Untreated'])

        for prop in properties:
            treated_value = self.treated_df.loc[self.treated_df['Property'] == prop, 'Value'].mean()
            untreated_value = self.untreated_df.loc[self.untreated_df['Property'] == prop, 'Value'].mean()
            comparison_df = comparison_df.append({'Property': prop, 'Treated': treated_value, 'Untreated': untreated_value}, ignore_index=True)

        return comparison_df

    def plot_comparison(self, comparison_df):
        """
        Plots the comparison of mechanical properties between treated and untreated woods.

        :param comparison_df: DataFrame containing the comparison data.
        """
        comparison_df.set_index('Property').plot(kind='bar', figsize=(10, 6))
        plt.title('Comparison of Mechanical Properties')
        plt.ylabel('Value')
        plt.xlabel('Properties')
        plt.xticks(rotation=45)
        plt.legend(title='Wood Type')
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the wood comparison analysis.
    """
    treated_file = 'treated_eucalyptus.csv'  # Path to treated eucalyptus data
    untreated_file = 'untreated_native_woods.csv'  # Path to untreated native woods data

    wood_comparison = WoodComparison(treated_file, untreated_file)
    wood_comparison.load_data()
    comparison_df = wood_comparison.compare_properties()

    if comparison_df is not None:
        print(comparison_df)
        wood_comparison.plot_comparison(comparison_df)

if __name__ == "__main__":
    main()
```
