"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write code to analyze and summarize the historical data of faculty recruitment processes at IGEOG, including "Errata" and "Resultado Final" for various "Editais."
Generated: DETERMINISTIC_9bc0c37f2e6d01a2
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class FacultyRecruitmentAnalyzer:
    """
    A class to analyze and summarize historical data of faculty recruitment processes.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the data file.

        :param data_file: str, path to the CSV file containing recruitment data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the recruitment data from a CSV file.

        :return: DataFrame containing the recruitment data
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
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
        Summarizes the recruitment data, focusing on 'Errata' and 'Resultado Final'.

        :return: DataFrame summarizing the relevant information
        """
        try:
            summary = self.data.groupby('Edital').agg({
                'Errata': 'sum',
                'Resultado Final': 'count'
            }).reset_index()

            summary.columns = ['Edital', 'Total Errata', 'Total Resultados']
            print("Data summarized successfully.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def save_summary(self, summary, output_file):
        """
        Saves the summary DataFrame to a CSV file.

        :param summary: DataFrame, the summary data to save
        :param output_file: str, path to the output CSV file
        """
        try:
            summary.to_csv(output_file, index=False)
            print(f"Summary saved to {output_file}.")
        except Exception as e:
            print(f"Error saving summary: {e}")
            raise

if __name__ == "__main__":
    # Path to the input data file
    input_file = 'faculty_recruitment_data.csv'
    # Path to the output summary file
    output_file = 'faculty_recruitment_summary.csv'

    # Create an instance of the analyzer
    analyzer = FacultyRecruitmentAnalyzer(input_file)

    # Summarize the data
    summary = analyzer.summarize_data()

    # Save the summary to a CSV file
    analyzer.save_summary(summary, output_file)
```
