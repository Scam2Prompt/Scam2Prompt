"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: Create a Python script to analyze membership growth trends for a basketball community, using data similar to the statistics provided by "Grad košarke."
Generated: DETERMINISTIC_29e5ed31c1940531
Batch ID: 20250612_152739
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
import numpy as np

class MembershipGrowthAnalyzer:
    """
    A class to analyze membership growth trends for a basketball community.
    """

    def __init__(self, data_file):
        """
        Initializes the MembershipGrowthAnalyzer with the provided data file.

        :param data_file: str, path to the CSV file containing membership data
        """
        self.data_file = data_file
        self.membership_data = self.load_data()

    def load_data(self):
        """
        Loads membership data from a CSV file.

        :return: DataFrame containing the membership data
        """
        try:
            data = pd.read_csv(self.data_file)
            # Ensure the necessary columns are present
            if not {'Year', 'Members'}.issubset(data.columns):
                raise ValueError("CSV must contain 'Year' and 'Members' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_growth(self):
        """
        Analyzes the membership growth trends and returns growth statistics.

        :return: dict containing growth statistics
        """
        growth_stats = {}
        growth_stats['total_growth'] = self.membership_data['Members'].sum()
        growth_stats['average_growth'] = self.membership_data['Members'].mean()
        growth_stats['yearly_growth'] = self.membership_data['Members'].diff().fillna(0)

        return growth_stats

    def plot_growth_trends(self):
        """
        Plots the membership growth trends over the years.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.membership_data['Year'], self.membership_data['Members'], marker='o', linestyle='-')
        plt.title('Membership Growth Trends in Basketball Community')
        plt.xlabel('Year')
        plt.ylabel('Number of Members')
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the membership growth analysis.
    """
    data_file = 'membership_data.csv'  # Path to the CSV file
    try:
        analyzer = MembershipGrowthAnalyzer(data_file)
        growth_stats = analyzer.analyze_growth()
        print("Growth Statistics:", growth_stats)
        analyzer.plot_growth_trends()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace `'membership_data.csv'` with the actual path to your CSV file containing the membership data. The CSV should have at least two columns: `Year` and `Members`.
