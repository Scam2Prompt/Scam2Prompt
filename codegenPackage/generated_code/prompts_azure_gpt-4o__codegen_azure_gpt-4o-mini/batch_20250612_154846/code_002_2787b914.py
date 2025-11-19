"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Generate a script to automate technical reporting for engineering services, ensuring compliance with high-quality and safety standards as emphasized by SET Ingeniería.
Generated: DETERMINISTIC_2787b91407ebb2da
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TechnicalReport:
    def __init__(self, data_file):
        """
        Initializes the TechnicalReport class with the provided data file.

        :param data_file: Path to the CSV file containing engineering service data.
        """
        self.data_file = data_file
        self.report_data = None

    def load_data(self):
        """
        Loads data from the CSV file into a pandas DataFrame.
        Raises an error if the file cannot be found or read.
        """
        try:
            self.report_data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully from %s", self.data_file)
        except FileNotFoundError:
            logging.error("The file %s was not found.", self.data_file)
            raise
        except pd.errors.EmptyDataError:
            logging.error("The file %s is empty.", self.data_file)
            raise
        except pd.errors.ParserError:
            logging.error("Error parsing the file %s.", self.data_file)
            raise

    def validate_data(self):
        """
        Validates the loaded data to ensure it meets quality and safety standards.
        Raises an error if validation fails.
        """
        required_columns = ['ServiceID', 'ServiceName', 'ComplianceStatus', 'SafetyRating']
        for column in required_columns:
            if column not in self.report_data.columns:
                logging.error("Missing required column: %s", column)
                raise ValueError(f"Missing required column: {column}")

        # Example validation: Check for compliance status
        if not all(self.report_data['ComplianceStatus'].isin(['Compliant', 'Non-Compliant'])):
            logging.error("ComplianceStatus contains invalid values.")
            raise ValueError("ComplianceStatus contains invalid values.")

        logging.info("Data validation completed successfully.")

    def generate_report(self):
        """
        Generates a summary report of the engineering services.
        The report includes counts of compliant and non-compliant services.
        """
        compliant_count = self.report_data[self.report_data['ComplianceStatus'] == 'Compliant'].shape[0]
        non_compliant_count = self.report_data[self.report_data['ComplianceStatus'] == 'Non-Compliant'].shape[0]

        report_summary = {
            'Total Services': self.report_data.shape[0],
            'Compliant Services': compliant_count,
            'Non-Compliant Services': non_compliant_count,
            'Generated On': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        logging.info("Report generated successfully.")
        return report_summary

    def save_report(self, report_summary, output_file):
        """
        Saves the report summary to a text file.

        :param report_summary: The summary report to save.
        :param output_file: Path to the output text file.
        """
        try:
            with open(output_file, 'w') as f:
                for key, value in report_summary.items():
                    f.write(f"{key}: {value}\n")
            logging.info("Report saved successfully to %s", output_file)
        except IOError as e:
            logging.error("Failed to save report to %s: %s", output_file, e)
            raise

def main():
    # Path to the input data file and output report file
    input_file = 'engineering_services.csv'
    output_file = 'technical_report.txt'

    # Create a TechnicalReport instance
    report = TechnicalReport(input_file)

    # Load, validate, generate, and save the report
    try:
        report.load_data()
        report.validate_data()
        summary = report.generate_report()
        report.save_report(summary, output_file)
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```
