"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Write code to generate monthly reports for residential block administration, including maintenance, cleaning, and financial updates, as described in BlocPrest's offerings.
Generated: DETERMINISTIC_b31c01504a500e06
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import List, Dict

class MonthlyReport:
    def __init__(self, block_name: str, month: int, year: int):
        """
        Initialize the MonthlyReport with block name, month, and year.
        
        :param block_name: Name of the residential block
        :param month: Month for the report (1-12)
        :param year: Year for the report
        """
        self.block_name = block_name
        self.month = month
        self.year = year
        self.maintenance_updates = []
        self.cleaning_updates = []
        self.financial_updates = {}

    def add_maintenance_update(self, update: str):
        """
        Add a maintenance update to the report.
        
        :param update: Description of the maintenance update
        """
        self.maintenance_updates.append(update)

    def add_cleaning_update(self, update: str):
        """
        Add a cleaning update to the report.
        
        :param update: Description of the cleaning update
        """
        self.cleaning_updates.append(update)

    def set_financial_update(self, financial_data: Dict[str, float]):
        """
        Set the financial updates for the report.
        
        :param financial_data: Dictionary containing financial information
        """
        self.financial_updates = financial_data

    def generate_report(self) -> Dict:
        """
        Generate the monthly report as a dictionary.
        
        :return: A dictionary representation of the report
        """
        report = {
            "block_name": self.block_name,
            "report_date": datetime.date(self.year, self.month, 1).strftime("%B %Y"),
            "maintenance_updates": self.maintenance_updates,
            "cleaning_updates": self.cleaning_updates,
            "financial_updates": self.financial_updates
        }
        return report

    def save_report(self, directory: str):
        """
        Save the report to a JSON file in the specified directory.
        
        :param directory: Directory where the report will be saved
        """
        report_data = self.generate_report()
        filename = f"{self.block_name.replace(' ', '_')}_report_{self.year}_{self.month}.json"
        file_path = os.path.join(directory, filename)

        try:
            with open(file_path, 'w') as report_file:
                json.dump(report_data, report_file, indent=4)
            print(f"Report saved successfully: {file_path}")
        except IOError as e:
            print(f"Error saving report: {e}")

# Example usage
if __name__ == "__main__":
    # Create a monthly report for a residential block
    report = MonthlyReport(block_name="Greenwood Block", month=10, year=2023)
    
    # Add updates
    report.add_maintenance_update("Repaired the main entrance gate.")
    report.add_cleaning_update("Completed deep cleaning of common areas.")
    report.set_financial_update({
        "total_income": 5000.00,
        "total_expenses": 3000.00,
        "net_profit": 2000.00
    })
    
    # Save the report to the specified directory
    report.save_report(directory="reports")
```
