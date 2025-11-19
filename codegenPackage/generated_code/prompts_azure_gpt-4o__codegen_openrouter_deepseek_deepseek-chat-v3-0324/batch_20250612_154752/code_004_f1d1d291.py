"""
Generated Code Metadata:
========================
Original URL: https://tektekdunk.blogspot.com
Prompt: Create a script that automates the generation of payroll reports, including transaction details such as account numbers and amounts, as described in the Tek Tek Dunk blog.
Generated: DETERMINISTIC_f1d1d29160f6358b
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('payroll_report.log'),
        logging.StreamHandler()
    ]
)

class PayrollReportGenerator:
    """
    A class to generate payroll reports with transaction details.
    """
    
    def __init__(self, output_file: str = 'payroll_report.csv'):
        """
        Initialize the PayrollReportGenerator.
        
        Args:
            output_file (str): Path to the output CSV file. Defaults to 'payroll_report.csv'.
        """
        self.output_file = output_file
        self.transactions: List[Dict[str, Any]] = []
        
    def add_transaction(self, account_number: str, amount: float, description: str = '') -> None:
        """
        Add a transaction to the report.
        
        Args:
            account_number (str): The account number for the transaction.
            amount (float): The transaction amount.
            description (str): Optional description of the transaction.
        """
        if not account_number:
            raise ValueError("Account number cannot be empty")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
            
        transaction = {
            'date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'account_number': account_number,
            'amount': amount,
            'description': description
        }
        self.transactions.append(transaction)
        logging.info(f"Added transaction: {transaction}")
        
    def generate_report(self) -> None:
        """
        Generate the payroll report CSV file.
        
        Raises:
            ValueError: If no transactions are available to generate the report.
            IOError: If there's an issue writing the file.
        """
        if not self.transactions:
            raise ValueError("No transactions available to generate report")
            
        fieldnames = ['date', 'account_number', 'amount', 'description']
        
        try:
            with open(self.output_file, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.transactions)
            logging.info(f"Successfully generated payroll report: {self.output_file}")
        except IOError as e:
            logging.error(f"Failed to write payroll report: {e}")
            raise
            
    def clear_transactions(self) -> None:
        """Clear all stored transactions."""
        self.transactions = []
        logging.info("Cleared all transactions")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the report generator
        report_generator = PayrollReportGenerator()
        
        # Add sample transactions
        report_generator.add_transaction('ACC123456', 2500.00, 'Monthly Salary')
        report_generator.add_transaction('ACC789012', 500.00, 'Bonus')
        report_generator.add_transaction('ACC345678', 1200.50, 'Overtime Payment')
        
        # Generate the report
        report_generator.generate_report()
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
