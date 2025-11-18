"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Write code to automate the generation of monthly reports for a logistics company, including metrics like total shipments, new clients, and customer satisfaction rates.
Generated: DETERMINISTIC_862a3cd37e640e7f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os

class MonthlyReportGenerator:
    def __init__(self, data_file):
        """
        Initializes the MonthlyReportGenerator with the data file.

        :param data_file: Path to the CSV file containing logistics data
        """
        self.data_file = data_file
        self.report_data = None

    def load_data(self):
        """
        Loads data from the CSV file and handles potential errors.
        """
        try:
            self.report_data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def generate_metrics(self):
        """
        Generates the metrics needed for the monthly report.

        :return: A dictionary containing the calculated metrics
        """
        metrics = {}
        try:
            # Total shipments
            metrics['total_shipments'] = self.report_data.shape[0]

            # New clients (assuming 'client_id' and 'signup_date' columns exist)
            metrics['new_clients'] = self.report_data['signup_date'].nunique()

            # Customer satisfaction (assuming a 'satisfaction_score' column exists)
            metrics['average_satisfaction'] = self.report_data['satisfaction_score'].mean()
        
        except KeyError as e:
            print(f"Error: Missing expected column in the data - {e}")
            raise
        except Exception as e:
            print(f"An error occurred while generating metrics: {e}")
            raise
        
        return metrics

    def save_report(self, metrics, report_file):
        """
        Saves the generated report metrics to a JSON file.

        :param metrics: The metrics dictionary to save
        :param report_file: Path where the report will be saved
        """
        try:
            with open(report_file, 'w') as f:
                json.dump(metrics, f, indent=4)
            print(f"Report saved successfully to {report_file}.")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")
            raise

    def plot_metrics(self, metrics):
        """
        Plots the metrics as a bar graph.

        :param metrics: The metrics dictionary to plot
        """
        try:
            plt.bar(metrics.keys(), metrics.values())
            plt.title("Monthly Logistics Report Metrics")
            plt.xlabel("Metrics")
            plt.ylabel("Values")
            plt.savefig('monthly_report_metrics.png')
            plt.close()
            print("Metrics plotted successfully.")
        except Exception as e:
            print(f"An error occurred while plotting metrics: {e}")
            raise

    def generate_report(self, report_file):
        """
        Main method to generate the monthly report.

        :param report_file: Path to save the report
        """
        self.load_data()
        metrics = self.generate_metrics()
        self.save_report(metrics, report_file)
        self.plot_metrics(metrics)


if __name__ == "__main__":
    # Define the path to the data file and the output report file
    data_file = "logistics_data.csv"  # Update this path as needed
    report_file = f"monthly_report_{datetime.now().strftime('%Y_%m')}.json"

    report_generator = MonthlyReportGenerator(data_file)
    report_generator.generate_report(report_file)
```
