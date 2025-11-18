"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Create a Python program to manage preventive, administrative, extrajudicial, and judicial debt collection processes, inspired by the cobranzas services described on SIF's site.
Generated: DETERMINISTIC_9303c9821654e6a5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging to output to a file
logging.basicConfig(filename='debt_collection.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DebtCollection:
    """Class to manage various debt collection processes."""

    def __init__(self):
        """Initialize a dictionary to hold debt records."""
        self.debts = {}

    def add_debt(self, debtor_name, amount, due_date):
        """Add a new debt record.

        Args:
            debtor_name (str): Name of the debtor.
            amount (float): Amount owed.
            due_date (datetime.date): Due date for the payment.
        """
        if debtor_name in self.debts:
            logging.warning(f'Debt for {debtor_name} already exists. Not adding duplicate.')
            return

        self.debts[debtor_name] = {
            'amount': amount,
            'due_date': due_date,
            'status': 'pending'
        }
        logging.info(f'Debt added for {debtor_name}: {amount} due by {due_date}.')

    def mark_as_paid(self, debtor_name):
        """Mark a debt as paid.

        Args:
            debtor_name (str): Name of the debtor.

        Raises:
            ValueError: If the debtor does not exist.
        """
        if debtor_name not in self.debts:
            logging.error(f'Debtor {debtor_name} does not exist.')
            raise ValueError(f'Debtor {debtor_name} does not exist.')

        self.debts[debtor_name]['status'] = 'paid'
        logging.info(f'Debt for {debtor_name} marked as paid.')

    def overdue_debts(self):
        """Get a list of overdue debts.

        Returns:
            list: List of debtor names with overdue debts.
        """
        today = datetime.date.today()
        overdue = [
            debtor for debtor, details in self.debts.items()
            if details['due_date'] < today and details['status'] == 'pending'
        ]
        logging.info(f'Overdue debts retrieved: {overdue}.')
        return overdue

    def generate_report(self):
        """Generate a report of all debts.

        Returns:
            str: A formatted string of the debt report.
        """
        report_lines = ["Debt Collection Report:\n"]
        for debtor, details in self.debts.items():
            report_lines.append(f"Debtor: {debtor}, Amount: {details['amount']}, "
                                f"Due Date: {details['due_date']}, Status: {details['status']}")
        report = "\n".join(report_lines)
        logging.info('Debt report generated.')
        return report

# Example Usage
if __name__ == "__main__":
    collector = DebtCollection()
    collector.add_debt("John Doe", 1500.00, datetime.date(2023, 12, 31))
    collector.add_debt("Jane Smith", 2500.00, datetime.date(2023, 11, 30))

    print(collector.generate_report())

    # Simulating a payment
    try:
        collector.mark_as_paid("John Doe")
    except ValueError as e:
        print(e)

    # Check overdue debts
    print("Overdue debts:", collector.overdue_debts())
```
