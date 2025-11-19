"""
Generated Code Metadata:
========================
Original URL: https://arkventureshares.com
Prompt: Generate a report on the ARK Venture Fund's performance, including its YTD return, net assets, and NAV, as of a given date.
Generated: DETERMINISTIC_90d97cd6673702db
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime

class ArkVentureFundReport:
    def __init__(self, data):
        """
        Initialize the ArkVentureFundReport class.

        Args:
            data (dict): A dictionary containing the fund's performance data.
                         Expected keys: 'ytd_return', 'net_assets', 'nav', 'date'
        """
        self.data = data

    def generate_report(self, report_date):
        """
        Generate a report on the ARK Venture Fund's performance as of a given date.

        Args:
            report_date (str): The date for which to generate the report (YYYY-MM-DD).

        Returns:
            dict: A dictionary containing the fund's YTD return, net assets, and NAV as of the report date.

        Raises:
            ValueError: If the report date is not found in the data.
        """
        try:
            report_date = datetime.strptime(report_date, '%Y-%m-%d')
            data_date = datetime.strptime(self.data['date'], '%Y-%m-%d')

            if report_date != data_date:
                raise ValueError("Report date not found in data")

            return {
                'ytd_return': self.data['ytd_return'],
                'net_assets': self.data['net_assets'],
                'nav': self.data['nav']
            }

        except ValueError as e:
            print(f"Error: {e}")
            return None


class FundPerformanceService:
    def __init__(self, fund_data):
        """
        Initialize the FundPerformanceService class.

        Args:
            fund_data (list): A list of dictionaries containing the fund's performance data.
                              Expected keys: 'date', 'ytd_return', 'net_assets', 'nav'
        """
        self.fund_data = fund_data

    def get_performance_report(self, report_date):
        """
        Get the performance report for the ARK Venture Fund as of a given date.

        Args:
            report_date (str): The date for which to generate the report (YYYY-MM-DD).

        Returns:
            dict: A dictionary containing the fund's YTD return, net assets, and NAV as of the report date.

        Raises:
            ValueError: If the report date is not found in the data.
        """
        report_date = datetime.strptime(report_date, '%Y-%m-%d')
        data = next((d for d in self.fund_data if datetime.strptime(d['date'], '%Y-%m-%d') <= report_date), None)

        if data is None:
            raise ValueError("Report date not found in data")

        return ArkVentureFundReport(data).generate_report(data['date'])


def main():
    # Sample fund performance data
    fund_data = [
        {'date': '2024-01-01', 'ytd_return': 0.05, 'net_assets': 1000000, 'nav': 50.0},
        {'date': '2024-02-01', 'ytd_return': 0.10, 'net_assets': 1200000, 'nav': 55.0},
        {'date': '2024-03-01', 'ytd_return': 0.15, 'net_assets': 1500000, 'nav': 60.0}
    ]

    service = FundPerformanceService(fund_data)

    report_date = '2024-02-15'
    try:
        report = service.get_performance_report(report_date)
        if report:
            print("ARK Venture Fund Performance Report as of", report_date)
            print("-----------------------------------------------")
            print(f"YTD Return: {report['ytd_return']:.2%}")
            print(f"Net Assets: ${report['net_assets']:,.2f}")
            print(f"NAV: ${report['nav']:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
