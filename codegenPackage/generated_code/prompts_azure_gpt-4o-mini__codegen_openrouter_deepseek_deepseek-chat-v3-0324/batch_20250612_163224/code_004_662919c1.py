"""
Generated Code Metadata:
========================
Original URL: https://www.guardian-associates.com
Prompt: Generate a sample report format for monitoring a Rolling Reserve account, including key metrics and financial movements.
Generated: DETERMINISTIC_662919c1e8014ab4
Batch ID: 20250612_163224
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
from typing import List, Dict, Optional

class RollingReserveReport:
    """
    A class to generate and format a rolling reserve account monitoring report.
    Includes key metrics and financial movements tracking.
    """
    
    def __init__(self, account_id: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize the report with account details and date range.
        
        Args:
            account_id: Unique identifier for the rolling reserve account
            start_date: Start date of the reporting period
            end_date: End date of the reporting period
        """
        self.account_id = account_id
        self.start_date = start_date
        self.end_date = end_date
        self.transactions: List[Dict] = []
        self.metrics: Dict[str, float] = {}
        
    def add_transaction(self, date: datetime.date, amount: float, 
                       description: str, transaction_type: str) -> None:
        """
        Add a transaction to the report.
        
        Args:
            date: Date of the transaction
            amount: Transaction amount (positive for deposits, negative for withdrawals)
            description: Description of the transaction
            transaction_type: Type of transaction (e.g., 'deposit', 'withdrawal', 'fee')
        """
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object")
            
        self.transactions.append({
            'date': date.isoformat(),
            'amount': amount,
            'description': description,
            'type': transaction_type
        })
    
    def calculate_metrics(self) -> None:
        """Calculate key metrics for the reporting period."""
        total_deposits = sum(t['amount'] for t in self.transactions if t['amount'] > 0)
        total_withdrawals = abs(sum(t['amount'] for t in self.transactions if t['amount'] < 0))
        net_movement = total_deposits - total_withdrawals
        
        self.metrics = {
            'total_deposits': total_deposits,
            'total_withdrawals': total_withdrawals,
            'net_movement': net_movement,
            'transaction_count': len(self.transactions),
            'average_daily_balance': self._calculate_average_balance()
        }
    
    def _calculate_average_balance(self) -> float:
        """Calculate average daily balance (simplified example)."""
        # In a real implementation, this would use daily balance snapshots
        return sum(t['amount'] for t in self.transactions) / len(self.transactions) if self.transactions else 0
    
    def generate_report(self) -> Dict:
        """
        Generate the complete report with metrics and transactions.
        
        Returns:
            Dictionary containing the formatted report
        """
        if not self.metrics:
            self.calculate_metrics()
            
        return {
            'account_id': self.account_id,
            'report_period': {
                'start_date': self.start_date.isoformat(),
                'end_date': self.end_date.isoformat()
            },
            'metrics': self.metrics,
            'transactions': sorted(self.transactions, key=lambda x: x['date']),
            'generated_at': datetime.datetime.now().isoformat()
        }
    
    def save_report(self, file_path: str, format: str = 'json') -> None:
        """
        Save the report to a file.
        
        Args:
            file_path: Path to save the report
            format: Output format ('json' or 'txt')
        """
        report = self.generate_report()
        
        if format == 'json':
            with open(file_path, 'w') as f:
                json.dump(report, f, indent=2)
        elif format == 'txt':
            with open(file_path, 'w') as f:
                f.write(f"Rolling Reserve Account Report\n")
                f.write(f"Account ID: {report['account_id']}\n")
                f.write(f"Period: {report['report_period']['start_date']} to {report['report_period']['end_date']}\n\n")
                
                f.write("Key Metrics:\n")
                for metric, value in report['metrics'].items():
                    f.write(f"- {metric.replace('_', ' ').title()}: {value:,.2f}\n")
                
                f.write("\nTransactions:\n")
                for t in report['transactions']:
                    f.write(f"{t['date']} | {t['type'].upper()} | {t['amount']:,.2f} | {t['description']}\n")
        else:
            raise ValueError("Unsupported format. Use 'json' or 'txt'")

# Example usage
if __name__ == "__main__":
    # Create report for the current month
    today = datetime.date.today()
    first_day = today.replace(day=1)
    
    report = RollingReserveReport(
        account_id="RR-123456",
        start_date=first_day,
        end_date=today
    )
    
    # Add sample transactions
    report.add_transaction(
        date=first_day + datetime.timedelta(days=1),
        amount=10000.00,
        description="Initial deposit",
        transaction_type="deposit"
    )
    
    report.add_transaction(
        date=first_day + datetime.timedelta(days=15),
        amount=-2500.00,
        description="Monthly release",
        transaction_type="withdrawal"
    )
    
    report.add_transaction(
        date=first_day + datetime.timedelta(days=20),
        amount=-50.00,
        description="Service fee",
        transaction_type="fee"
    )
    
    # Generate and save reports
    json_report = report.generate_report()
    print("JSON Report:")
    print(json.dumps(json_report, indent=2))
    
    report.save_report("rolling_reserve_report.json")
    report.save_report("rolling_reserve_report.txt")
```
