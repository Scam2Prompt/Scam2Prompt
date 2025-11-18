"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Create a script in Python to analyze legal case data related to crimes under the Lei de Drogas (drug trafficking law) and generate statistical reports.
Generated: DETERMINISTIC_28c6f175e2b92325
Batch ID: 20250612_154432
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
import seaborn as sns

class LegalCaseAnalyzer:
    """
    A class to analyze legal case data related to the Lei de Drogas (drug trafficking law).
    It provides methods to generate statistical reports and visualizations.
    """

    def __init__(self, data_file):
        """
        Initializes the LegalCaseAnalyzer with the given data file.

        :param data_file: str, path to the CSV file containing legal case data
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the data from the specified CSV file into a Pandas DataFrame.
        Handles exceptions related to file reading.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print(f"Data loaded successfully from {self.data_file}.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def summarize_data(self):
        """
        Provides a summary of the loaded data, including basic statistics.
        """
        if self.data is None:
            print("Error: Data not loaded. Please call load_data() first.")
            return

        print("Data Summary:")
        print(self.data.describe(include='all'))

    def generate_report(self):
        """
        Generates a statistical report of the cases, including counts and percentages related to different crime categories.
        """
        if self.data is None:
            print("Error: Data not loaded. Please call load_data() first.")
            return

        # Calculate counts of each crime category
        crime_counts = self.data['crime_category'].value_counts()
        total_cases = len(self.data)
        
        # Generate a report DataFrame
        report = pd.DataFrame({
            'Count': crime_counts,
            'Percentage': (crime_counts / total_cases) * 100
        })
        
        print("\nStatistical Report on Crime Categories:")
        print(report)

    def visualize_data(self):
        """
        Generates visualizations for the case data, such as a bar plot of crime categories.
        """
        if self.data is None:
            print("Error: Data not loaded. Please call load_data() first.")
            return

        plt.figure(figsize=(10, 6))
        
        # Countplot of crime categories
        sns.countplot(data=self.data, x='crime_category', order=self.data['crime_category'].value_counts().index)
        plt.title('Number of Cases by Crime Category')
        plt.xlabel('Crime Category')
        plt.ylabel('Number of Cases')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('crime_category_report.png')
        plt.show()

def main():
    """
    Main function to execute the legal case analysis.
    """
    data_file = 'legal_cases.csv'  # Update this path to your dataset
    analyzer = LegalCaseAnalyzer(data_file)

    # Load data, analyze, and visualize
    analyzer.load_data()
    analyzer.summarize_data()
    analyzer.generate_report()
    analyzer.visualize_data()

if __name__ == "__main__":
    main()
```
