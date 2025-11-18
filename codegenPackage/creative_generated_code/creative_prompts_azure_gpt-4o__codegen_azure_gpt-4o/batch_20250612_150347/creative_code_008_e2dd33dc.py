"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Write code to generate annual tax reports for businesses, incorporating optimization techniques described by Arbitum Consulting.
Generated: DETERMINISTIC_e2dd33dc18f929dd
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime

class TaxReportGenerator:
    """
    A class to generate annual tax reports for businesses with optimization techniques 
    described by Arbitum Consulting.

    Attributes:
        businesses (list): A list of business data dictionaries.
        output_dir (str): Directory where reports will be saved.
    """

    def __init__(self, businesses, output_dir="tax_reports"):
        """
        Initialize the TaxReportGenerator with business data and output directory.

        Args:
            businesses (list): List of business data dictionaries.
            output_dir (str): Directory where reports will be saved.
        """
        self.businesses = businesses
        self.output_dir = output_dir
        self._initialize_output_dir()

    def _initialize_output_dir(self):
        """Create the output directory if it doesn't exist."""
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory {self.output_dir}: {e}")

    def _calculate_tax(self, revenue, expenses, tax_rate):
        """
        Calculate the tax owed based on revenue, expenses, and tax rate.

        Args:
            revenue (float): Total revenue earned by the business.
            expenses (float): Total expenses incurred by the business.
            tax_rate (float): Applicable tax rate.

        Returns:
            float: Tax amount owed.
        """
        # Basic validation
        if revenue < 0 or expenses < 0 or not (0 <= tax_rate <= 1):
            raise ValueError("Invalid input for tax calculation.")
        taxable_income = max(revenue - expenses, 0)  # Ensure taxable income is not negative
        return taxable_income * tax_rate

    def generate_report(self, tax_rate=0.25):
        """
        Generate annual tax reports for each business and save as CSV files.

        Args:
            tax_rate (float): The applicable tax rate. Default is 25% (0.25).
        """
        for business in self.businesses:
            try:
                # Extract business information
                business_name = business.get("name", "Unknown Business")
                revenue = business.get("revenue", 0)
                expenses = business.get("expenses", 0)

                # Validate inputs
                if not isinstance(revenue, (int, float)) or not isinstance(expenses, (int, float)):
                    raise ValueError(f"Invalid data types for business '{business_name}'.")

                # Calculate tax owed
                tax_owed = self._calculate_tax(revenue, expenses, tax_rate)

                # Prepare report data
                report_data = [
                    ["Business Name", business_name],
                    ["Revenue", f"${revenue:,.2f}"],
                    ["Expenses", f"${expenses:,.2f}"],
                    ["Tax Rate", f"{tax_rate * 100:.2f}%"],
                    ["Tax Owed", f"${tax_owed:,.2f}"],
                ]

                # Generate filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{business_name.replace(' ', '_')}_Tax_Report_{timestamp}.csv"
                filepath = os.path.join(self.output_dir, filename)

                # Write report to CSV file
                with open(filepath, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(report_data)

                print(f"Tax report generated for '{business_name}': {filepath}")

            except Exception as e:
                print(f"Error generating report for business '{business.get('name', 'Unknown')}': {e}")

# Example usage
if __name__ == "__main__":
    # Sample business data
    businesses = [
        {"name": "ABC Corp", "revenue": 1000000, "expenses": 400000},
        {"name": "XYZ LLC", "revenue": 750000, "expenses": 300000},
        {"name": "Invalid Data Inc", "revenue": "invalid", "expenses": 200000},  # Invalid data example
    ]

    # Initialize the TaxReportGenerator
    generator = TaxReportGenerator(businesses)

    # Generate tax reports
    generator.generate_report()
```
