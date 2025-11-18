"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Generate a script to automate the creation of sustainability reports, integrating data from Omega Energy's ESG practices and ISO compliance.
Generated: DETERMINISTIC_2f4e968fd3254838
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='sustainability_report.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class SustainabilityReport:
    """A class to generate sustainability reports from ESG practices and ISO compliance data."""
    
    def __init__(self, esg_data_path, iso_data_path):
        """
        Initializes the SustainabilityReport class with ESG and ISO data.
        
        Args:
            esg_data_path (str): Path to the ESG data file (CSV).
            iso_data_path (str): Path to the ISO compliance data file (CSV).
        """
        self.esg_data_path = esg_data_path
        self.iso_data_path = iso_data_path
        self.esg_data = None
        self.iso_data = None

    def load_data(self):
        """Loads ESG and ISO data from specified CSV files."""
        try:
            self.esg_data = pd.read_csv(self.esg_data_path)
            logging.info("ESG data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"ESG data file not found: {self.esg_data_path}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading ESG data: {e}")
            raise

        try:
            self.iso_data = pd.read_csv(self.iso_data_path)
            logging.info("ISO data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"ISO data file not found: {self.iso_data_path}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading ISO data: {e}")
            raise

    def generate_report(self):
        """Generates a sustainability report by integrating ESG and ISO data."""
        # Check if data is loaded
        if self.esg_data is None or self.iso_data is None:
            logging.error("Data not loaded. Please load the data first.")
            raise ValueError("Data not loaded.")

        # Merging the ESG and ISO data on a common key (assuming a 'Company' column exists)
        try:
            report_data = pd.merge(self.esg_data, self.iso_data, on='Company', how='inner')
            logging.info("Data merged successfully.")
        except KeyError as e:
            logging.error(f"Key error during merging: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while merging data: {e}")
            raise

        return report_data

    def save_report(self, report_data, output_path):
        """Saves the generated report to a specified file.
        
        Args:
            report_data (DataFrame): The report data to save.
            output_path (str): The file path where the report will be saved (CSV).
        """
        try:
            report_data.to_csv(output_path, index=False)
            logging.info(f"Sustainability report saved successfully at: {output_path}")
        except Exception as e:
            logging.error(f"An error occurred while saving the report: {e}")
            raise


def main():
    """Main function to execute the report generation process."""
    esg_file_path = 'esg_data.csv'  # Replace with actual ESG data file path
    iso_file_path = 'iso_data.csv'   # Replace with actual ISO data file path
    output_file_path = f'sustainability_report_{datetime.now().strftime("%Y%m%d")}.csv'

    report_generator = SustainabilityReport(esg_file_path, iso_file_path)

    try:
        report_generator.load_data()
        report_data = report_generator.generate_report()
        report_generator.save_report(report_data, output_file_path)
        logging.info("Sustainability report generation completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during report generation: {e}")


if __name__ == "__main__":
    main()
```
