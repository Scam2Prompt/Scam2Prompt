"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write code to generate a logistics report for automotive and aerospace industries, using Uniair Cargo’s tailored solutions for these sectors.
Generated: DETERMINISTIC_aa0079215ec9ac26
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogisticsReport:
    def __init__(self, data_source: str):
        """
        Initializes the LogisticsReport class with a data source.

        :param data_source: Path to the data source (CSV file) containing logistics data
        """
        self.data_source = data_source
        self.data = None

    def load_data(self):
        """
        Loads the logistics data from the specified CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_source)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_source}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def generate_report(self):
        """
        Generates a logistics report filtered by automotive and aerospace industries.

        :return: A pandas DataFrame containing the filtered report
        """
        if self.data is None:
            logging.error("Data not loaded. Please load data before generating the report.")
            raise ValueError("Data not loaded.")

        try:
            # Filter data for automotive and aerospace sectors
            filtered_data = self.data[self.data['Industry'].isin(['Automotive', 'Aerospace'])]

            # Calculate summary statistics
            summary = filtered_data.groupby('Industry').agg({
                'Shipment_Weight': 'sum',
                'Cost': 'sum',
                'Delivery_Time': 'mean'
            }).reset_index()

            logging.info("Report generated successfully.")
            return summary
        except KeyError as e:
            logging.error(f"Missing expected column in data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while generating the report: {e}")
            raise

    def save_report(self, report: pd.DataFrame, output_file: str):
        """
        Saves the generated report to a specified CSV file.

        :param report: The report DataFrame to save
        :param output_file: The path to the output CSV file
        """
        try:
            report.to_csv(output_file, index=False)
            logging.info(f"Report saved to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while saving the report: {e}")
            raise

def main():
    """
    Main function to execute the logistics report generation.
    """
    report_generator = LogisticsReport(data_source='logistics_data.csv')

    try:
        report_generator.load_data()
        report = report_generator.generate_report()
        report_generator.save_report(report, output_file=f'logistics_report_{datetime.now().strftime("%Y%m%d")}.csv')
    except Exception as e:
        logging.error(f"An error occurred in the report generation process: {e}")

if __name__ == "__main__":
    main()
```
