"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Suggest a Python library or framework for generating compliance reports that adhere to NBR, NHBRC, and local authority regulations, as mentioned by TWM Associates.
Generated: DETERMINISTIC_ab7d5ca190c898f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime

class ComplianceReportGenerator:
    """
    A class to generate compliance reports that adhere to NBR, NHBRC, and local authority regulations.
    """

    def __init__(self, data_source):
        """
        Initializes the ComplianceReportGenerator with a data source.

        Parameters:
        data_source (str): The file path to the CSV file containing compliance data.
        """
        self.data_source = data_source
        self.df = self.load_data()

    def load_data(self):
        """
        Loads compliance data from the specified CSV file.

        Returns:
        pd.DataFrame: A DataFrame containing the compliance data.

        Raises:
        FileNotFoundError: If the data source file does not exist.
        pd.errors.EmptyDataError: If the data source file is empty.
        """
        try:
            data = pd.read_csv(self.data_source)
            return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data source not found: {self.data_source}") from e
        except pd.errors.EmptyDataError as e:
            raise ValueError("No data found in the provided file.") from e

    def generate_report(self):
        """
        Generates a compliance report based on the loaded data.

        Returns:
        str: A string representation of the compliance report.
        """
        report = "Compliance Report\n"
        report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        report += f"Total Entries: {len(self.df)}\n\n"
        
        # Group by regulations and count entries
        regulations_count = self.df.groupby('Regulation').size()
        report += "Entries per Regulation:\n"
        for regulation, count in regulations_count.items():
            report += f"{regulation}: {count}\n"

        return report

    def save_report(self, report, output_file):
        """
        Saves the compliance report to a specified output file.

        Parameters:
        report (str): The compliance report to save.
        output_file (str): The file path to save the report.
        """
        try:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"Report saved successfully to {output_file}")
        except IOError as e:
            raise IOError(f"An error occurred while saving the report to {output_file}") from e


# Example usage
if __name__ == "__main__":
    try:
        # Path to the CSV file containing compliance data
        data_source = 'compliance_data.csv'
        
        # Create an instance of the report generator
        report_generator = ComplianceReportGenerator(data_source)
        
        # Generate the compliance report
        report = report_generator.generate_report()
        
        # Save the report to a file
        report_generator.save_report(report, 'compliance_report.txt')
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
