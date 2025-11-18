"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Write a script to automate the generation of annual reports summarizing the association's achievements, including metrics like programs executed, beneficiaries reached, and partnerships established.
Generated: DETERMINISTIC_dbc42e17b67531eb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import os
from datetime import datetime

class AnnualReportGenerator:
    def __init__(self, data_file: str):
        """
        Initializes the AnnualReportGenerator with the specified data file.

        :param data_file: The path to the CSV file containing the organization's data.
        """
        self.data_file = data_file
        self.report_data = None

    def load_data(self):
        """
        Loads data from the CSV file into a pandas DataFrame.
        Handles errors if the file does not exist or cannot be read.
        """
        try:
            self.report_data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: Error parsing the file.")
            raise

    def generate_summary(self) -> dict:
        """
        Generates a summary of the association's achievements.

        :return: A dictionary containing the summary metrics.
        """
        if self.report_data is None:
            raise ValueError("Data not loaded. Please call load_data() first.")

        summary = {
            "total_programs_executed": self.report_data['programs_executed'].sum(),
            "total_beneficiaries_reached": self.report_data['beneficiaries_reached'].sum(),
            "total_partnerships_established": self.report_data['partnerships_established'].sum(),
            "report_generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return summary

    def export_report(self, summary: dict, output_file: str):
        """
        Exports the summary report to a text file.

        :param summary: The summary dictionary to write to the file.
        :param output_file: The path where the report will be saved.
        """
        try:
            with open(output_file, 'w') as file:
                for key, value in summary.items():
                    file.write(f"{key}: {value}\n")
            print(f"Report successfully exported to {output_file}.")
        except IOError as e:
            print(f"Error writing to file {output_file}: {e}")
            raise

    def run(self, output_file: str):
        """
        Executes the report generation process.

        :param output_file: The path where the report will be saved.
        """
        self.load_data()
        summary = self.generate_summary()
        self.export_report(summary, output_file)

if __name__ == "__main__":
    # Replace 'association_data.csv' with the actual data file path
    data_file_path = 'association_data.csv'
    output_report_path = 'annual_report.txt'

    report_generator = AnnualReportGenerator(data_file_path)
    try:
        report_generator.run(output_report_path)
    except Exception as e:
        print(f"An error occurred during report generation: {e}")
```

Make sure you have a `CSV` file named `association_data.csv` with the required columns (`programs_executed`, `beneficiaries_reached`, `partnerships_established`) in the same directory as the script to execute it successfully.
