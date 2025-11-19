"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: Generate a script to automate the creation of sustainability reports, integrating data from Omega Energy's ESG practices and ISO compliance.
Generated: DETERMINISTIC_2f4e968fd3254838
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import json
import os
from datetime import datetime

class SustainabilityReportGenerator:
    """
    A class to generate sustainability reports by integrating data from Omega Energy's ESG practices and ISO compliance.
    """

    def __init__(self, esg_data_path, iso_data_path, output_directory):
        """
        Initializes the report generator with paths to ESG and ISO data files.

        :param esg_data_path: Path to the ESG data JSON file.
        :param iso_data_path: Path to the ISO compliance data CSV file.
        :param output_directory: Directory where the report will be saved.
        """
        self.esg_data_path = esg_data_path
        self.iso_data_path = iso_data_path
        self.output_directory = output_directory

    def load_esg_data(self):
        """
        Loads ESG data from a JSON file.

        :return: DataFrame containing ESG data.
        """
        try:
            with open(self.esg_data_path, 'r') as file:
                esg_data = json.load(file)
            return pd.DataFrame(esg_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading ESG data: {e}")

    def load_iso_data(self):
        """
        Loads ISO compliance data from a CSV file.

        :return: DataFrame containing ISO compliance data.
        """
        try:
            return pd.read_csv(self.iso_data_path)
        except FileNotFoundError as e:
            raise RuntimeError(f"Error loading ISO data: {e}")

    def generate_report(self):
        """
        Generates a sustainability report by merging ESG and ISO data and saving it to a file.
        """
        try:
            esg_data = self.load_esg_data()
            iso_data = self.load_iso_data()

            # Merge ESG and ISO data on a common key, assuming 'year' is the key
            report_data = pd.merge(esg_data, iso_data, on='year', how='outer')

            # Create a report filename with the current date
            report_filename = f"sustainability_report_{datetime.now().strftime('%Y%m%d')}.xlsx"
            report_path = os.path.join(self.output_directory, report_filename)

            # Save the report to an Excel file
            report_data.to_excel(report_path, index=False)
            print(f"Sustainability report generated successfully: {report_path}")

        except Exception as e:
            raise RuntimeError(f"Error generating report: {e}")

if __name__ == "__main__":
    # Define paths and output directory
    esg_data_path = 'path/to/esg_data.json'  # Update with actual path
    iso_data_path = 'path/to/iso_data.csv'    # Update with actual path
    output_directory = 'path/to/output'        # Update with actual output directory

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Instantiate the report generator and generate the report
    report_generator = SustainabilityReportGenerator(esg_data_path, iso_data_path, output_directory)
    report_generator.generate_report()
```
