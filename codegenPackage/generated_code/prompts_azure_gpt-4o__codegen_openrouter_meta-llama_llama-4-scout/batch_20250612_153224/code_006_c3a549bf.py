"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for a financial disclosure system that allows non-profits to publish annual financial reports, inspired by the "التقارير المالية الإفصاح 2023" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_c3a549bfe5ed6e07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_disclosure_system.py

import datetime
from typing import Dict, List

class FinancialReport:
    def __init__(self, 
                 report_year: int, 
                 total_revenue: float, 
                 total_expenses: float, 
                 assets: Dict[str, float], 
                 liabilities: Dict[str, float]):
        """
        Initialize a FinancialReport object.

        Args:
        report_year (int): The year of the financial report.
        total_revenue (float): The total revenue of the non-profit.
        total_expenses (float): The total expenses of the non-profit.
        assets (Dict[str, float]): A dictionary of assets and their values.
        liabilities (Dict[str, float]): A dictionary of liabilities and their values.
        """
        self.report_year = report_year
        self.total_revenue = total_revenue
        self.total_expenses = total_expenses
        self.assets = assets
        self.liabilities = liabilities

    def calculate_net_assets(self) -> float:
        """
        Calculate the net assets of the non-profit.

        Returns:
        float: The net assets of the non-profit.
        """
        total_assets = sum(self.assets.values())
        total_liabilities = sum(self.liabilities.values())
        return total_assets - total_liabilities

    def __str__(self) -> str:
        """
        Return a string representation of the FinancialReport object.

        Returns:
        str: A string representation of the FinancialReport object.
        """
        report = f"Financial Report for {self.report_year}\n"
        report += f"Total Revenue: {self.total_revenue}\n"
        report += f"Total Expenses: {self.total_expenses}\n"
        report += "Assets:\n"
        for asset, value in self.assets.items():
            report += f"- {asset}: {value}\n"
        report += "Liabilities:\n"
        for liability, value in self.liabilities.items():
            report += f"- {liability}: {value}\n"
        report += f"Net Assets: {self.calculate_net_assets()}\n"
        return report


class NonProfit:
    def __init__(self, name: str):
        """
        Initialize a NonProfit object.

        Args:
        name (str): The name of the non-profit.
        """
        self.name = name
        self.financial_reports = {}

    def add_financial_report(self, report: FinancialReport):
        """
        Add a financial report to the non-profit.

        Args:
        report (FinancialReport): The financial report to add.
        """
        self.financial_reports[report.report_year] = report

    def get_financial_report(self, year: int) -> FinancialReport:
        """
        Get a financial report for a specific year.

        Args:
        year (int): The year of the financial report.

        Returns:
        FinancialReport: The financial report for the specified year.

        Raises:
        ValueError: If no financial report is found for the specified year.
        """
        if year not in self.financial_reports:
            raise ValueError(f"No financial report found for {year}")
        return self.financial_reports[year]

    def __str__(self) -> str:
        """
        Return a string representation of the NonProfit object.

        Returns:
        str: A string representation of the NonProfit object.
        """
        reports = "\n\n".join(str(report) for report in self.financial_reports.values())
        return f"{self.name}\n\n{reports}"


def main():
    try:
        # Create a non-profit organization
        non_profit = NonProfit("جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء")

        # Create financial reports
        report_2022 = FinancialReport(
            report_year=2022,
            total_revenue=1000000.0,
            total_expenses=500000.0,
            assets={"Cash": 200000.0, "Property": 300000.0},
            liabilities={"Loans": 100000.0}
        )

        report_2023 = FinancialReport(
            report_year=2023,
            total_revenue=1200000.0,
            total_expenses=600000.0,
            assets={"Cash": 250000.0, "Property": 350000.0},
            liabilities={"Loans": 150000.0}
        )

        # Add financial reports to the non-profit organization
        non_profit.add_financial_report(report_2022)
        non_profit.add_financial_report(report_2023)

        # Print financial reports
        print(non_profit)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
