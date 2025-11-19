"""
Generated Code Metadata:
========================
Original URL: https://tracingiallc.com
Prompt: Describe how to develop a report generation tool for documenting cryptocurrency fraud cases, following the example of Tracingia LLC's investigative reports.
Generated: DETERMINISTIC_a3a236fbbc0a3f87
Batch ID: 20250612_155638
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

class FraudReportGenerator:
    """
    A class to generate reports for documenting cryptocurrency fraud cases.
    """

    def __init__(self, data_source: str):
        """
        Initializes the report generator with a data source.

        :param data_source: Path to the JSON file containing fraud case data.
        """
        self.data_source = data_source
        self.fraud_cases = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads fraud case data from a JSON file.

        :return: A DataFrame containing the fraud case data.
        """
        try:
            with open(self.data_source, 'r') as file:
                data = json.load(file)
                return pd.DataFrame(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data source '{self.data_source}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the data source.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def generate_report(self, output_path: str):
        """
        Generates a report of the fraud cases and saves it to a specified output path.

        :param output_path: Path where the report will be saved.
        """
        try:
            report_content = self.create_report_content()
            with open(output_path, 'w') as report_file:
                report_file.write(report_content)
            print(f"Report successfully generated at: {output_path}")
        except Exception as e:
            raise Exception(f"An error occurred while generating the report: {e}")

    def create_report_content(self) -> str:
        """
        Creates the content of the report based on the fraud cases.

        :return: A string containing the formatted report.
        """
        report_lines = []
        report_lines.append("Cryptocurrency Fraud Cases Report")
        report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report_lines.append("Case ID | Description | Amount | Date | Status\n")
        report_lines.append("-" * 60)

        for index, case in self.fraud_cases.iterrows():
            report_lines.append(f"{case['case_id']} | {case['description']} | {case['amount']} | "
                                f"{case['date']} | {case['status']}")
        
        return "\n".join(report_lines)

if __name__ == "__main__":
    # Example usage
    try:
        data_source = 'fraud_cases.json'  # Path to the JSON data file
        output_path = 'fraud_report.txt'   # Path to save the report

        report_generator = FraudReportGenerator(data_source)
        report_generator.generate_report(output_path)
    except Exception as e:
        print(f"Error: {e}")
```
