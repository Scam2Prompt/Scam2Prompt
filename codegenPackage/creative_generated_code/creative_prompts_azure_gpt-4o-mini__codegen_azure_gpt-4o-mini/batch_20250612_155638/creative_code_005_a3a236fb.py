"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tracingiallc.com
Prompt: Describe how to develop a report generation tool for documenting cryptocurrency fraud cases, following the example of Tracingia LLC's investigative reports.
Generated: DETERMINISTIC_a3a236fbbc0a3f87
Batch ID: 20250612_155638
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
import os
from datetime import datetime

class FraudReportGenerator:
    """
    A class to generate reports documenting cryptocurrency fraud cases.
    """

    def __init__(self, data_file: str):
        """
        Initialize the FraudReportGenerator with the path to the data file.
        
        :param data_file: Path to the CSV file containing fraud case data.
        """
        self.data_file = data_file
        self.fraud_cases = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Load the fraud case data from a CSV file.

        :return: DataFrame containing the fraud case data.
        :raises FileNotFoundError: If the data file does not exist.
        :raises pd.errors.EmptyDataError: If the data file is empty.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file not found: {self.data_file}")
        
        try:
            data = pd.read_csv(self.data_file)
            return data
        except pd.errors.EmptyDataError:
            raise ValueError("Data file is empty")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def generate_report(self, output_file: str):
        """
        Generate a report of fraud cases in a structured format.
        
        :param output_file: Path to the output JSON file where the report will be saved.
        :raises Exception: If the report generation fails.
        """
        report_data = {
            "report_generated_at": datetime.now().isoformat(),
            "total_cases": len(self.fraud_cases),
            "fraud_cases": self.fraud_cases.to_dict(orient='records')
        }

        try:
            with open(output_file, 'w') as f:
                json.dump(report_data, f, indent=4)
            print(f"Report successfully generated: {output_file}")
        except Exception as e:
            raise Exception(f"An error occurred while generating the report: {e}")

def main():
    """
    Main function to execute the report generation tool.
    """
    data_file = 'fraud_cases.csv'  # Path to the CSV file containing fraud case data
    output_file = 'fraud_report.json'  # Output JSON report file

    try:
        report_generator = FraudReportGenerator(data_file)
        report_generator.generate_report(output_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
