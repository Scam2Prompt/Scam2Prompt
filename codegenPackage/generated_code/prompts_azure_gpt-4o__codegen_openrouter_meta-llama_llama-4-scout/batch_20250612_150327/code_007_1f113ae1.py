"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Provide code examples for generating reports on ethical trading compliance, similar to PDC Brush's initiatives.
Generated: DETERMINISTIC_1f113ae1494b73a5
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime

class EthicalTradingComplianceReport:
    def __init__(self, trades, suppliers):
        """
        Initialize the report generator with trades and suppliers data.

        Args:
            trades (list): List of trades with 'date', 'supplier_id', 'product', and 'price' columns.
            suppliers (list): List of suppliers with 'id', 'name', and 'country' columns.
        """
        self.trades = pd.DataFrame(trades)
        self.suppliers = pd.DataFrame(suppliers)

    def generate_compliance_report(self):
        """
        Generate a report on ethical trading compliance.

        Returns:
            pd.DataFrame: Report with 'supplier_name', 'product', 'total_trades', and 'total_value' columns.
        """
        # Merge trades and suppliers data
        merged_data = pd.merge(self.trades, self.suppliers, left_on='supplier_id', right_on='id')

        # Group by supplier name, product, and calculate total trades and total value
        report = merged_data.groupby(['supplier_name', 'product']).agg({
            'date': 'count',
            'price': 'sum'
        }).reset_index()

        # Rename columns
        report.columns = ['supplier_name', 'product', 'total_trades', 'total_value']

        return report

    def check_for_high_risk_suppliers(self):
        """
        Check for high-risk suppliers based on their country.

        Returns:
            list: List of high-risk suppliers.
        """
        # Define high-risk countries
        high_risk_countries = ['Country A', 'Country B']

        # Filter high-risk suppliers
        high_risk_suppliers = self.suppliers[self.suppliers['country'].isin(high_risk_countries)]

        return high_risk_suppliers.to_dict('records')

    def check_for_unusual_trades(self):
        """
        Check for unusual trades based on their price.

        Returns:
            list: List of unusual trades.
        """
        # Define the threshold for unusual trades
        threshold = 1000

        # Filter unusual trades
        unusual_trades = self.trades[self.trades['price'] > threshold]

        return unusual_trades.to_dict('records')


def main():
    try:
        # Example usage
        trades = [
            {'date': datetime(2022, 1, 1), 'supplier_id': 1, 'product': 'Product A', 'price': 500},
            {'date': datetime(2022, 1, 2), 'supplier_id': 1, 'product': 'Product A', 'price': 600},
            {'date': datetime(2022, 1, 3), 'supplier_id': 2, 'product': 'Product B', 'price': 1500},
        ]

        suppliers = [
            {'id': 1, 'name': 'Supplier A', 'country': 'Country C'},
            {'id': 2, 'name': 'Supplier B', 'country': 'Country A'},
        ]

        report_generator = EthicalTradingComplianceReport(trades, suppliers)
        compliance_report = report_generator.generate_compliance_report()
        high_risk_suppliers = report_generator.check_for_high_risk_suppliers()
        unusual_trades = report_generator.check_for_unusual_trades()

        print("Compliance Report:")
        print(compliance_report)
        print("\nHigh-Risk Suppliers:")
        print(high_risk_suppliers)
        print("\nUnusual Trades:")
        print(unusual_trades)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
