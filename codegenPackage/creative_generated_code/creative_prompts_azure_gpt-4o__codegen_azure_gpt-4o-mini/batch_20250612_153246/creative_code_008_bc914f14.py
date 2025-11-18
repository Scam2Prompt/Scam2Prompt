"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outsource.s1soft.com
Prompt: Write code for a tax compliance system in Python, utilizing the expertise in accounting services described on the Special One Outsourcing webpage.
Generated: DETERMINISTIC_bc914f148a5d5713
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class TaxComplianceSystem:
    def __init__(self, tax_rate):
        """
        Initialize the TaxComplianceSystem with a given tax rate.

        :param tax_rate: float representing the tax rate (e.g., 0.20 for 20%)
        """
        if not (0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be between 0 and 1.")
        self.tax_rate = tax_rate

    def calculate_tax(self, income):
        """
        Calculate the tax owed based on income.

        :param income: float representing the income
        :return: float representing the calculated tax
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")
        return income * self.tax_rate

    def generate_tax_report(self, income):
        """
        Generate a tax report for the given income.

        :param income: float representing the income
        :return: dict containing the income, tax rate, tax owed, and report date
        """
        tax_owed = self.calculate_tax(income)
        report = {
            "income": income,
            "tax_rate": self.tax_rate,
            "tax_owed": tax_owed,
            "report_date": datetime.now().isoformat()
        }
        return report

    def save_report_to_file(self, report, filename):
        """
        Save the tax report to a JSON file.

        :param report: dict containing the tax report data
        :param filename: str representing the file name to save the report
        """
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            print(f"Report saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving report to file: {e}")

# Example Usage
if __name__ == "__main__":
    try:
        tax_system = TaxComplianceSystem(tax_rate=0.20)  # 20% tax rate
        user_income = 50000  # Example income
        report = tax_system.generate_tax_report(user_income)
        print(report)  # Display the report

        tax_system.save_report_to_file(report, "tax_report.json")  # Save the report
    except Exception as e:
        print(f"An error occurred: {e}")
```
