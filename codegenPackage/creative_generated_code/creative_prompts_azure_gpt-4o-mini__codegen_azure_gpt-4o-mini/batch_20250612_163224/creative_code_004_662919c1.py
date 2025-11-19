"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.guardian-associates.com
Prompt: Generate a sample report format for monitoring a Rolling Reserve account, including key metrics and financial movements.
Generated: DETERMINISTIC_662919c1e8014ab4
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime

class RollingReserveReport:
    """
    A class to generate a rolling reserve account report.
    """

    def __init__(self, reserve_data):
        """
        Initializes the RollingReserveReport with reserve data.

        :param reserve_data: A DataFrame containing reserve transaction data
        """
        if not isinstance(reserve_data, pd.DataFrame):
            raise ValueError("reserve_data must be a pandas DataFrame.")
        
        self.reserve_data = reserve_data

    def calculate_metrics(self):
        """
        Calculates key metrics for the rolling reserve.

        :return: A dictionary containing key metrics
        """
        metrics = {}
        try:
            metrics['total_deposits'] = self.reserve_data[self.reserve_data['transaction_type'] == 'deposit']['amount'].sum()
            metrics['total_withdrawals'] = self.reserve_data[self.reserve_data['transaction_type'] == 'withdrawal']['amount'].sum()
            metrics['current_balance'] = metrics['total_deposits'] - metrics['total_withdrawals']
            metrics['transaction_count'] = self.reserve_data.shape[0]
            metrics['average_transaction'] = self.reserve_data['amount'].mean()

            # Additional metrics can be calculated as needed
            
        except Exception as e:
            print(f"Error calculating metrics: {e}")
            raise
        
        return metrics

    def generate_report(self):
        """
        Generates a report of the rolling reserve account.

        :return: A formatted string of the report
        """
        metrics = self.calculate_metrics()
        
        report = f"Rolling Reserve Account Report - {datetime.now().strftime('%Y-%m-%d')}\n"
        report += "=" * 50 + "\n"
        report += f"Total Deposits: ${metrics['total_deposits']:.2f}\n"
        report += f"Total Withdrawals: ${metrics['total_withdrawals']:.2f}\n"
        report += f"Current Balance: ${metrics['current_balance']:.2f}\n"
        report += f"Total Transactions: {metrics['transaction_count']}\n"
        report += f"Average Transaction Amount: ${metrics['average_transaction']:.2f}\n"
        report += "=" * 50 + "\n"

        return report

# Example usage
if __name__ == "__main__":
    # Sample data for rolling reserve transactions
    data = {
        'transaction_type': ['deposit', 'withdrawal', 'deposit', 'withdrawal'],
        'amount': [1000.00, 500.00, 2000.00, 300.00],
        'date': pd.to_datetime(['2023-01-01', '2023-01-10', '2023-01-15', '2023-01-20'])
    }
    
    reserve_data = pd.DataFrame(data)

    try:
        report_generator = RollingReserveReport(reserve_data)
        report = report_generator.generate_report()
        print(report)
    except Exception as e:
        print(f"Failed to generate report: {e}")
```
