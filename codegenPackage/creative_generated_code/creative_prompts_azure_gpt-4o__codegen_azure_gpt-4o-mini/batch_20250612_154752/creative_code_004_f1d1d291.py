"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tektekdunk.blogspot.com
Prompt: Create a script that automates the generation of payroll reports, including transaction details such as account numbers and amounts, as described in the Tek Tek Dunk blog.
Generated: DETERMINISTIC_f1d1d29160f6358b
Batch ID: 20250612_154752
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
from typing import List, Dict

class PayrollReportGenerator:
    def __init__(self, transactions: List[Dict[str, str]], output_dir: str):
        """
        Initializes the PayrollReportGenerator with a list of transactions and output directory.
        
        :param transactions: List of transaction details as dictionaries.
        :param output_dir: Directory to save the generated report.
        """
        self.transactions = transactions
        self.output_dir = output_dir

    def generate_report(self) -> str:
        """
        Generates a payroll report in CSV format based on the provided transactions.
        
        :return: The file path of the generated report.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)  # Create output directory if it doesn't exist

        report_filename = f"payroll_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        report_filepath = os.path.join(self.output_dir, report_filename)

        try:
            with open(report_filepath, mode='w', newline='') as report_file:
                fieldnames = ['Account Number', 'Amount', 'Date']
                writer = csv.DictWriter(report_file, fieldnames=fieldnames)

                writer.writeheader()  # Write CSV header
                for transaction in self.transactions:
                    writer.writerow(transaction)  # Write each transaction

            print(f"Report generated successfully: {report_filepath}")
            return report_filepath

        except Exception as e:
            print(f"Error generating report: {e}")
            raise

def main():
    # Sample transactions for demonstration purposes
    transactions = [
        {'Account Number': '123456789', 'Amount': '1000.00', 'Date': '2023-10-01'},
        {'Account Number': '987654321', 'Amount': '1500.00', 'Date': '2023-10-01'},
        {'Account Number': '555555555', 'Amount': '2000.00', 'Date': '2023-10-01'},
    ]
    
    output_directory = './payroll_reports'  # Specify the output directory

    # Initialize the report generator with transactions and output directory
    report_generator = PayrollReportGenerator(transactions, output_directory)

    try:
        # Generate the payroll report
        report_generator.generate_report()
    except Exception as e:
        print(f"Failed to generate payroll report: {e}")

if __name__ == "__main__":
    main()
```
