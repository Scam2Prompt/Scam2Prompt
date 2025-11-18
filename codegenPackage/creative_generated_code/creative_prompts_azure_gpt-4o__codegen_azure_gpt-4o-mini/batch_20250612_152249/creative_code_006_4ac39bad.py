"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Write a script to generate automated reports on the performance of state-of-the-art machinery in a textile manufacturing unit, including metrics like uptime, maintenance schedules, and production output.
Generated: DETERMINISTIC_4ac39badea75fe8f
Batch ID: 20250612_152249
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MachineryReport:
    def __init__(self, machinery_data):
        """
        Initialize the MachineryReport with machinery performance data.

        :param machinery_data: DataFrame containing machinery performance metrics
        """
        self.machinery_data = machinery_data

    def calculate_uptime(self):
        """
        Calculate the uptime percentage for each machine.

        :return: DataFrame with uptime percentage
        """
        try:
            self.machinery_data['uptime'] = self.machinery_data['operational_time'] / self.machinery_data['total_time'] * 100
            logging.info("Uptime calculated successfully.")
            return self.machinery_data[['machine_id', 'uptime']]
        except Exception as e:
            logging.error("Error calculating uptime: %s", e)
            raise

    def schedule_maintenance(self):
        """
        Generate a maintenance schedule based on the last maintenance date.

        :return: DataFrame with maintenance schedules
        """
        try:
            current_date = datetime.now()
            self.machinery_data['next_maintenance'] = self.machinery_data['last_maintenance'] + pd.to_timedelta(self.machinery_data['maintenance_interval'], unit='D')
            logging.info("Maintenance schedule generated successfully.")
            return self.machinery_data[['machine_id', 'next_maintenance']]
        except Exception as e:
            logging.error("Error scheduling maintenance: %s", e)
            raise

    def production_output(self):
        """
        Summarize the production output for each machine.

        :return: DataFrame with production output information
        """
        try:
            production_summary = self.machinery_data.groupby('machine_id').agg({'production_units': 'sum'}).reset_index()
            logging.info("Production output summarized successfully.")
            return production_summary
        except Exception as e:
            logging.error("Error summarizing production output: %s", e)
            raise

    def generate_report(self):
        """
        Generate a comprehensive report with uptime, maintenance schedule, and production output.

        :return: DataFrame containing the comprehensive report
        """
        try:
            uptime_df = self.calculate_uptime()
            maintenance_df = self.schedule_maintenance()
            production_df = self.production_output()

            report = pd.merge(uptime_df, maintenance_df, on='machine_id')
            report = pd.merge(report, production_df, on='machine_id')

            logging.info("Comprehensive report generated successfully.")
            return report
        except Exception as e:
            logging.error("Error generating report: %s", e)
            raise

    def plot_report(self, report):
        """
        Plot the report metrics for visualization.

        :param report: DataFrame containing the comprehensive report
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.bar(report['machine_id'], report['uptime'], color='green', label='Uptime %')
            plt.xlabel('Machine ID')
            plt.ylabel('Uptime Percentage')
            plt.title('Uptime for Each Machine')
            plt.legend()
            plt.grid()
            plt.show()
            logging.info("Report plotted successfully.")
        except Exception as e:
            logging.error("Error plotting report: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    # Sample data for machinery performance
    sample_data = {
        'machine_id': ['M1', 'M2', 'M3'],
        'operational_time': [1200, 1500, 900],
        'total_time': [1500, 1600, 1000],
        'last_maintenance': [datetime.now() - timedelta(days=30), datetime.now() - timedelta(days=15), datetime.now() - timedelta(days=60)],
        'maintenance_interval': [30, 30, 60],
        'production_units': [2000, 2500, 1500],
    }
    
    machinery_df = pd.DataFrame(sample_data)

    # Generate report
    report_generator = MachineryReport(machinery_df)
    report = report_generator.generate_report()
    print(report)

    # Plot the report
    report_generator.plot_report(report)
```
