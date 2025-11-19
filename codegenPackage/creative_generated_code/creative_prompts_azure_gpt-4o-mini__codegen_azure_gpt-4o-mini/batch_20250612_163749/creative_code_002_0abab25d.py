"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Generate a sample Bacs payment file format that can be used with Perfect Payrolls for making electronic payments to employees and HMRC.
Generated: DETERMINISTIC_0abab25d094d1a72
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
import os

class BacsPaymentFile:
    """
    Class to generate a BACS payment file for employee payments and HMRC.
    """

    def __init__(self, filename):
        """
        Initializes the BacsPaymentFile with the given filename.

        Args:
            filename (str): The name of the file to be created.
        """
        self.filename = filename
        self.payments = []

    def add_payment(self, employee_id, employee_name, account_number, sort_code, amount):
        """
        Adds a payment entry to the payment list.

        Args:
            employee_id (str): Unique identifier for the employee.
            employee_name (str): Name of the employee.
            account_number (str): Employee's bank account number.
            sort_code (str): Employee's bank sort code.
            amount (float): Amount to be paid to the employee.
        """
        self.payments.append({
            "employee_id": employee_id,
            "employee_name": employee_name,
            "account_number": account_number,
            "sort_code": sort_code,
            "amount": amount
        })

    def generate_file(self):
        """
        Generates the BACS payment file in CSV format.

        Raises:
            Exception: If the file cannot be created or written to.
        """
        header = ["Employee ID", "Employee Name", "Account Number", "Sort Code", "Amount", "Date"]
        
        # Validate that payments are added before generating the file
        if not self.payments:
            raise ValueError("No payments to write to the file.")

        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)

                for payment in self.payments:
                    row = [
                        payment["employee_id"],
                        payment["employee_name"],
                        payment["account_number"],
                        payment["sort_code"],
                        f"{payment['amount']:.2f}",
                        datetime.now().strftime('%Y-%m-%d')
                    ]
                    writer.writerow(row)
            print(f"BACS payment file '{self.filename}' generated successfully.")
        except Exception as e:
            raise Exception(f"Failed to create BACS payment file: {str(e)}")

if __name__ == "__main__":
    # Example usage of the BacsPaymentFile class
    try:
        bacs_file = BacsPaymentFile("bacs_payments.csv")
        bacs_file.add_payment("E123", "John Doe", "12345678", "12-34-56", 1500.00)
        bacs_file.add_payment("E124", "Jane Smith", "87654321", "65-43-21", 1800.50)
        bacs_file.generate_file()

    except Exception as e:
        print(f"Error: {str(e)}")
```
