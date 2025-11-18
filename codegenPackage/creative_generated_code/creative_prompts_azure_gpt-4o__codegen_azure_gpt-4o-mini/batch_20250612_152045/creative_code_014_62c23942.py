"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Create a Python script for generating ROI reports, based on the ROI software solutions mentioned by MDA Tech Sys.
Generated: DETERMINISTIC_62c2394271f743a2
Batch ID: 20250612_152045
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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ROIReportGenerator:
    """
    A class to generate Return on Investment (ROI) reports based on input data.
    """

    def __init__(self, data_file: str):
        """
        Initializes the ROIReportGenerator with the specified data file.

        :param data_file: Path to the CSV file containing ROI data
        """
        self.data_file = data_file
        self.data = None

    def load_data(self) -> None:
        """
        Loads the data from the specified CSV file into a DataFrame.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            pd.errors.EmptyDataError: If the file is empty.
            pd.errors.ParserError: If the file cannot be parsed.
        """
        try:
            self.data = pd.read_csv(self.data_file)
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

    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculates the ROI based on the loaded data.

        :return: DataFrame with calculated ROI
        """
        if self.data is None:
            logging.error("Data not loaded. Please load data first.")
            raise ValueError("Data not loaded. Please load data first.")

        # Assuming the DataFrame has 'investment' and 'return' columns
        if 'investment' not in self.data.columns or 'return' not in self.data.columns:
            logging.error("Data must contain 'investment' and 'return' columns.")
            raise ValueError("Data must contain 'investment' and 'return' columns.")

        # Calculate ROI = (Return - Investment) / Investment
        self.data['ROI'] = (self.data['return'] - self.data['investment']) / self.data['investment']
        return self.data[['investment', 'return', 'ROI']]

    def save_report(self, report: pd.DataFrame, output_file: str) -> None:
        """
        Saves the ROI report to a specified output file.

        :param report: DataFrame containing the ROI report
        :param output_file: Path to the output CSV file
        """
        try:
            report.to_csv(output_file, index=False)
            logging.info("Report saved successfully to %s", output_file)
        except Exception as e:
            logging.error("Failed to save report to %s: %s", output_file, str(e))
            raise

def main():
    """
    Main function to execute the ROI report generation process.
    """
    roi_generator = ROIReportGenerator('roi_data.csv')
    
    try:
        roi_generator.load_data()
        roi_report = roi_generator.calculate_roi()
        roi_generator.save_report(roi_report, 'roi_report.csv')
    except Exception as e:
        logging.error("An error occurred during ROI report generation: %s", str(e))

if __name__ == "__main__":
    main()
```
