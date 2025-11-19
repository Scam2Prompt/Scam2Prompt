"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Write a Python script to generate reports on ISO 9001:2015 certification compliance for packaging products, inspired by Osku's certification achievements.
Generated: DETERMINISTIC_0dc7f2d0120dcd29
Batch ID: 20250612_151610
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

class ISO9001ReportGenerator:
    """
    A class to generate reports on ISO 9001:2015 certification compliance for packaging products.
    """

    def __init__(self, data_file):
        """
        Initializes the report generator with the provided data file.

        :param data_file: Path to the CSV file containing packaging product data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads data from the CSV file into a pandas DataFrame.
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

    def generate_report(self):
        """
        Generates a compliance report based on the loaded data.
        
        :return: A DataFrame containing the compliance report.
        """
        if self.data is None:
            logging.error("Data not loaded. Please call load_data() first.")
            raise ValueError("Data not loaded.")

        # Check for required columns
        required_columns = ['Product ID', 'Product Name', 'Compliance Status', 'Last Audit Date']
        for column in required_columns:
            if column not in self.data.columns:
                logging.error("Missing required column: %s", column)
                raise ValueError(f"Missing required column: {column}")

        # Filter compliant products
        compliant_products = self.data[self.data['Compliance Status'] == 'Compliant']
        logging.info("Found %d compliant products.", len(compliant_products))

        # Generate report summary
        report_summary = {
            'Total Products': len(self.data),
            'Compliant Products': len(compliant_products),
            'Non-Compliant Products': len(self.data) - len(compliant_products),
            'Report Date': datetime.now().strftime('%Y-%m-%d')
        }

        return compliant_products, report_summary

    def save_report(self, compliant_products, report_summary, output_file):
        """
        Saves the compliant products and report summary to an Excel file.

        :param compliant_products: DataFrame of compliant products.
        :param report_summary: Dictionary containing the report summary.
        :param output_file: Path to the output Excel file.
        """
        try:
            with pd.ExcelWriter(output_file) as writer:
                compliant_products.to_excel(writer, sheet_name='Compliant Products', index=False)
                summary_df = pd.DataFrame([report_summary])
                summary_df.to_excel(writer, sheet_name='Report Summary', index=False)
            logging.info("Report saved successfully to %s", output_file)
        except Exception as e:
            logging.error("Failed to save report: %s", e)
            raise

def main():
    """
    Main function to execute the report generation process.
    """
    data_file = 'packaging_products.csv'  # Input CSV file path
    output_file = 'iso9001_compliance_report.xlsx'  # Output Excel file path

    report_generator = ISO9001ReportGenerator(data_file)

    try:
        report_generator.load_data()
        compliant_products, report_summary = report_generator.generate_report()
        report_generator.save_report(compliant_products, report_summary, output_file)
    except Exception as e:
        logging.error("An error occurred during report generation: %s", e)

if __name__ == "__main__":
    main()
```
