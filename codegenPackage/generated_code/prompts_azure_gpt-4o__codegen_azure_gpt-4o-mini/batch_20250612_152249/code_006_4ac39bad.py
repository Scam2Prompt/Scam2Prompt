"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a script to generate automated reports on the performance of state-of-the-art machinery in a textile manufacturing unit, including metrics like uptime, maintenance schedules, and production output.
Generated: DETERMINISTIC_4ac39badea75fe8f
Batch ID: 20250612_152249
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
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MachineryReport:
    def __init__(self, machinery_data):
        """
        Initialize the MachineryReport with machinery data.

        :param machinery_data: DataFrame containing machinery performance data
        """
        self.machinery_data = machinery_data

    def calculate_uptime(self):
        """
        Calculate the uptime percentage of the machinery.

        :return: Uptime percentage
        """
        try:
            total_time = self.machinery_data['operational_time'].sum()
            downtime = self.machinery_data['downtime'].sum()
            uptime = (total_time - downtime) / total_time * 100
            logging.info(f"Calculated uptime: {uptime:.2f}%")
            return uptime
        except Exception as e:
            logging.error("Error calculating uptime: %s", e)
            return None

    def maintenance_schedule(self):
        """
        Generate a maintenance schedule based on the machinery data.

        :return: DataFrame with maintenance schedule
        """
        try:
            maintenance_df = self.machinery_data[self.machinery_data['needs_maintenance'] == True]
            logging.info("Generated maintenance schedule.")
            return maintenance_df[['machine_id', 'next_maintenance_date']]
        except Exception as e:
            logging.error("Error generating maintenance schedule: %s", e)
            return None

    def production_output(self):
        """
        Calculate total production output.

        :return: Total production output
        """
        try:
            total_output = self.machinery_data['production_output'].sum()
            logging.info(f"Total production output: {total_output}")
            return total_output
        except Exception as e:
            logging.error("Error calculating production output: %s", e)
            return None

    def generate_report(self):
        """
        Generate a comprehensive report of machinery performance.

        :return: Dictionary containing uptime, maintenance schedule, and production output
        """
        try:
            report = {
                'uptime_percentage': self.calculate_uptime(),
                'maintenance_schedule': self.maintenance_schedule(),
                'total_production_output': self.production_output()
            }
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error("Error generating report: %s", e)
            return None

# Sample data for testing
if __name__ == "__main__":
    # Create a sample DataFrame with machinery performance data
    data = {
        'machine_id': [1, 2, 3],
        'operational_time': [1000, 950, 1100],
        'downtime': [50, 30, 20],
        'needs_maintenance': [False, True, False],
        'next_maintenance_date': [None, datetime.date(2023, 11, 15), None],
        'production_output': [5000, 4500, 6000]
    }
    
    machinery_data = pd.DataFrame(data)

    # Create a MachineryReport instance
    report_generator = MachineryReport(machinery_data)

    # Generate the report
    report = report_generator.generate_report()
    print(report)
```
