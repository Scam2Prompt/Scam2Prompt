"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Create a Python script for generating ROI reports, based on the ROI software solutions mentioned by MDA Tech Sys.
Generated: DETERMINISTIC_62c2394271f743a2
Batch ID: 20250612_152045
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ROIReportGenerator:
    """
    A class to generate ROI reports based on input data.
    """

    def __init__(self, data_file):
        """
        Initializes the ROIReportGenerator with a data file.

        :param data_file: Path to the CSV file containing ROI data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the ROI data from the specified CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def calculate_roi(self):
        """
        Calculates the ROI for each entry in the data.

        :return: A DataFrame with calculated ROI.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data first.")
            raise ValueError("Data not loaded.")

        # Assuming the data has 'gain' and 'cost' columns
        try:
            self.data['ROI'] = (self.data['gain'] - self.data['cost']) / self.data['cost'] * 100
            logging.info("ROI calculated successfully.")
            return self.data[['gain', 'cost', 'ROI']]
        except KeyError as e:
            logging.error(f"Missing expected column in data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while calculating ROI: {e}")
            raise

    def save_report(self, output_file):
        """
        Saves the ROI report to a specified CSV file.

        :param output_file: Path to the output CSV file.
        """
        try:
            report = self.calculate_roi()
            report.to_csv(output_file, index=False)
            logging.info(f"Report saved successfully to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while saving the report: {e}")
            raise

def main():
    """
    Main function to execute the ROI report generation.
    """
    input_file = 'roi_data.csv'  # Input CSV file with ROI data
    output_file = f'roi_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'  # Output file with timestamp

    roi_report_generator = ROIReportGenerator(input_file)

    try:
        roi_report_generator.load_data()
        roi_report_generator.save_report(output_file)
    except Exception as e:
        logging.error(f"Failed to generate ROI report: {e}")

if __name__ == "__main__":
    main()
```
