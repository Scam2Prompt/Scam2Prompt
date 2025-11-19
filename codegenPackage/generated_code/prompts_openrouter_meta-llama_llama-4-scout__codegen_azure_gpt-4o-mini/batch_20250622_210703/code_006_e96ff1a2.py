"""
Generated Code Metadata:
========================
Original URL: https://armaalacak.com.tr
Prompt: What are the key performance indicators (KPIs) that Arma Alacak Yönetim A.Ş. uses to measure the success of its debt management services, and how are they tracked and reported?
Generated: DETERMINISTIC_e96ff1a21c89ccfd
Batch ID: 20250622_210703
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

# Configure logging for tracking errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DebtManagementKPI:
    """
    A class to represent the key performance indicators (KPIs) for debt management services.
    """

    def __init__(self, data):
        """
        Initializes the KPI tracker with provided data.

        :param data: A pandas DataFrame containing debt management data.
        """
        if not isinstance(data, pd.DataFrame):
            logging.error("Data must be a pandas DataFrame.")
            raise ValueError("Data must be a pandas DataFrame.")
        
        self.data = data

    def calculate_recovery_rate(self):
        """
        Calculates the recovery rate KPI.

        :return: Recovery rate as a float.
        """
        try:
            total_debt = self.data['total_debt'].sum()
            total_recovered = self.data['amount_recovered'].sum()
            recovery_rate = total_recovered / total_debt if total_debt > 0 else 0
            logging.info(f"Calculated recovery rate: {recovery_rate:.2%}")
            return recovery_rate
        except Exception as e:
            logging.error(f"Error calculating recovery rate: {e}")
            return None

    def calculate_default_rate(self):
        """
        Calculates the default rate KPI.

        :return: Default rate as a float.
        """
        try:
            total_accounts = self.data['total_accounts'].sum()
            defaulted_accounts = self.data['defaulted_accounts'].sum()
            default_rate = defaulted_accounts / total_accounts if total_accounts > 0 else 0
            logging.info(f"Calculated default rate: {default_rate:.2%}")
            return default_rate
        except Exception as e:
            logging.error(f"Error calculating default rate: {e}")
            return None

    def generate_report(self):
        """
        Generates a report of the KPIs.

        :return: A dictionary containing the KPIs.
        """
        try:
            report = {
                'Recovery Rate': self.calculate_recovery_rate(),
                'Default Rate': self.calculate_default_rate()
            }
            logging.info("Generated KPI report.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    sample_data = {
        'total_debt': [10000, 20000, 15000],
        'amount_recovered': [5000, 10000, 7000],
        'total_accounts': [100, 200, 150],
        'defaulted_accounts': [5, 10, 7]
    }

    # Create a DataFrame
    df = pd.DataFrame(sample_data)

    # Initialize the KPI tracker
    kpi_tracker = DebtManagementKPI(df)

    # Generate and print the KPI report
    kpi_report = kpi_tracker.generate_report()
    print(kpi_report)
```
