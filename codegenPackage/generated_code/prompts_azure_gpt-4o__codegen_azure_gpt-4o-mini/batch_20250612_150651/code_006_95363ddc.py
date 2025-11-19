"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a program to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust, including metrics for educational outcomes and research advancements.
Generated: DETERMINISTIC_95363ddc294af343
Batch ID: 20250612_150651
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrantReportGenerator:
    def __init__(self, data_file: str):
        """
        Initializes the GrantReportGenerator with the provided data file.

        :param data_file: Path to the CSV file containing grant data.
        """
        self.data_file = data_file
        self.grant_data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads grant data from a CSV file.

        :return: A pandas DataFrame containing the grant data.
        """
        try:
            data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
            return data
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def generate_report(self) -> Dict[str, float]:
        """
        Generates a report on the impact of grants.

        :return: A dictionary containing metrics for educational outcomes and research advancements.
        """
        try:
            # Calculate metrics
            total_grants = len(self.grant_data)
            total_funding = self.grant_data['amount'].sum()
            avg_outcome_score = self.grant_data['outcome_score'].mean()

            report = {
                'Total Grants': total_grants,
                'Total Funding': total_funding,
                'Average Outcome Score': avg_outcome_score
            }

            logging.info("Report generated successfully.")
            return report
        except KeyError as e:
            logging.error(f"Missing expected column in data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while generating the report: {e}")
            raise

    def save_report(self, report: Dict[str, float], output_file: str) -> None:
        """
        Saves the generated report to a specified output file.

        :param report: The report data to save.
        :param output_file: The path to the output file.
        """
        try:
            report_df = pd.DataFrame(report.items(), columns=['Metric', 'Value'])
            report_df.to_csv(output_file, index=False)
            logging.info(f"Report saved successfully to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while saving the report: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        generator = GrantReportGenerator('grant_data.csv')
        report = generator.generate_report()
        generator.save_report(report, 'grant_report.csv')
    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
```
