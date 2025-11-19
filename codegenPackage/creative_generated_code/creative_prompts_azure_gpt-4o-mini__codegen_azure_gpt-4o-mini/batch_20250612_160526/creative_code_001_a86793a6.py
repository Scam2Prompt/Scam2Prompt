"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartenoir.org
Prompt: Write a Python script that automates the reporting of safety compliance metrics for a project, inspired by the methodologies used by Carte Noir Consulting.
Generated: DETERMINISTIC_a86793a665eb6442
Batch ID: 20250612_160526
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
logging.basicConfig(
    filename='safety_compliance_report.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class SafetyComplianceMetrics:
    def __init__(self, data_file: str):
        """
        Initialize the SafetyComplianceMetrics with the data file.
        
        :param data_file: Path to the CSV file containing safety compliance data.
        """
        self.data_file = data_file
        self.df = None

    def load_data(self):
        """
        Load the CSV data into a Pandas DataFrame.
        """
        try:
            self.df = pd.read_csv(self.data_file)
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

    def calculate_metrics(self):
        """
        Calculate safety compliance metrics from the DataFrame.
        
        :return: A dictionary containing compliance metrics.
        """
        if self.df is None:
            logging.error("DataFrame is not loaded. Please load the data first.")
            raise ValueError("DataFrame is not loaded.")

        metrics = {
            "total_incidents": self.df['incident'].count(),
            "total_compliance": self.df[self.df['compliant'] == True].shape[0],
            "compliance_rate": self.df['compliant'].mean() * 100,
        }
        logging.info("Metrics calculated: %s", metrics)
        return metrics

    def generate_report(self, metrics):
        """
        Generate a compliance report based on calculated metrics.
        
        :param metrics: A dictionary of calculated compliance metrics.
        """
        report_date = datetime.now().strftime('%Y-%m-%d')
        report_content = (f"Safety Compliance Report - {report_date}\n"
                          f"---------------------------------\n"
                          f"Total Incidents: {metrics['total_incidents']}\n"
                          f"Total Compliant: {metrics['total_compliance']}\n"
                          f"Compliance Rate: {metrics['compliance_rate']:.2f}%\n")
        
        report_file = f"safety_compliance_report_{report_date}.txt"
        with open(report_file, 'w') as f:
            f.write(report_content)
        logging.info("Report generated: %s", report_file)

def main():
    """
    Main function to execute safety compliance reporting.
    """
    data_file = 'safety_data.csv'  # Specify the path to your data file
    metrics_calculator = SafetyComplianceMetrics(data_file)

    try:
        metrics_calculator.load_data()
        metrics = metrics_calculator.calculate_metrics()
        metrics_calculator.generate_report(metrics)
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```
