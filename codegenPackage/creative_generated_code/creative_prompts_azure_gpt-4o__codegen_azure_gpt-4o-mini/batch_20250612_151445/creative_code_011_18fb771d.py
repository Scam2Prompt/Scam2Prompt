"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Generate code to automate the generation of analytical testing reports for food testing, ensuring compliance with A & B Labs' PJLA accreditation.
Generated: DETERMINISTIC_18fb771d8e132424
Batch ID: 20250612_151445
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
import os
from datetime import datetime
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AnalyticalTestingReportGenerator:
    """
    A class to generate analytical testing reports for food testing
    ensuring compliance with A & B Labs' PJLA accreditation.
    """

    def __init__(self, input_data_path, output_directory):
        """
        Initializes the report generator with the specified input data path 
        and output directory.

        :param input_data_path: str, path to the input CSV file containing test results
        :param output_directory: str, directory where the report will be saved
        """
        self.input_data_path = input_data_path
        self.output_directory = output_directory

        # Validate paths
        self._validate_paths()

    def _validate_paths(self):
        """Validates the input data path and output directory."""
        if not os.path.isfile(self.input_data_path):
            logging.error(f"Input data file not found: {self.input_data_path}")
            raise FileNotFoundError(f"Input data file not found: {self.input_data_path}")

        if not os.path.exists(self.output_directory):
            logging.info(f"Output directory does not exist. Creating: {self.output_directory}")
            os.makedirs(self.output_directory)

    def _load_data(self):
        """Loads the input data from a CSV file into a pandas DataFrame."""
        try:
            logging.info(f"Loading data from {self.input_data_path}")
            data = pd.read_csv(self.input_data_path)
            logging.info("Data loaded successfully.")
            return data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise

    def _generate_report(self, data):
        """
        Generates a summary report from the test results data.

        :param data: pandas DataFrame, the input data containing test results
        :return: pandas DataFrame, a summary report
        """
        logging.info("Generating report...")
        try:
            # Example analysis: Calculate means and counts for each test
            report = data.groupby('Test Name').agg(
                Mean_Result=('Result', 'mean'),
                Count=('Result', 'count')
            ).reset_index()

            # Example compliance check
            report['Compliance'] = np.where(report['Mean_Result'] <= data['Threshold'].max(), 'Compliant', 'Non-Compliant')
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise

    def save_report(self, report):
        """
        Saves the generated report to a CSV file.

        :param report: pandas DataFrame, the report to be saved
        """
        report_filename = f"analytical_testing_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        report_path = os.path.join(self.output_directory, report_filename)
        
        try:
            report.to_csv(report_path, index=False)
            logging.info(f"Report saved successfully at: {report_path}")
        except Exception as e:
            logging.error(f"Error saving report: {e}")
            raise

    def run(self):
        """Main method to execute the report generation process."""
        logging.info("Starting report generation process...")
        data = self._load_data()
        report = self._generate_report(data)
        self.save_report(report)
        logging.info("Report generation process completed.")

# Example usage
if __name__ == "__main__":
    input_data_file = 'path/to/input_data.csv'  # Replace with actual input data file path
    output_dir = 'path/to/output_directory'      # Replace with desired output directory

    try:
        report_generator = AnalyticalTestingReportGenerator(input_data_file, output_dir)
        report_generator.run()
    except Exception as e:
        logging.critical(f"Failed to generate report: {e}")
```
