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
import datetime

def generate_bacs_file(filename, payments):
    """
    Generate a BACS payment file in CSV format for Perfect Payrolls.
    
    Args:
        filename (str): The name of the file to save the BACS data.
        payments (list of dict): A list of payment records. Each record is a dictionary with:
            - 'account_name': Name of the account holder (Max length: 18 characters)
            - 'account_number': Bank account number (8 digits)
            - 'sort_code': Bank sort code (6 digits, formatted as "XX-XX-XX")
            - 'payment_amount': Payment amount (float, in pounds)
            - 'reference': Payment reference (Max length: 18 characters)
    
    Raises:
        ValueError: If any payment record contains invalid data.
    """
    # Validate payments
    for payment in payments:
        if len(payment['account_name']) > 18:
            raise ValueError("Account name exceeds 18 characters.")
        if len(payment['account_number']) != 8 or not payment['account_number'].isdigit():
            raise ValueError("Account number must be 8 digits.")
        if len(payment['sort_code']) != 8 or not all(part.isdigit() for part in payment['sort_code'].split('-')):
            raise ValueError("Sort code must be in the format XX-XX-XX.")
        if not isinstance(payment['payment_amount'], (int, float)) or payment['payment_amount'] <= 0:
            raise ValueError("Payment amount must be a positive number.")
        if len(payment['reference']) > 18:
            raise ValueError("Reference exceeds 18 characters.")
    
    # Define header and file structure
    header = ['Account Name', 'Account Number', 'Sort Code', 'Payment Amount', 'Reference', 'Payment Date']
    today = datetime.date.today().strftime("%d/%m/%Y")
    
    # Write CSV
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            
            for payment in payments:
                writer.writerow([
                    payment['account_name'],
                    payment['account_number'],
                    payment['sort_code'],
                    f"{payment['payment_amount']:.2f}",  # Format amount to 2 decimal places
                    payment['reference'],
                    today
                ])
    except OSError as e:
        raise RuntimeError(f"Failed to write BACS file: {e}")

# Example usage
if __name__ == "__main__":
    # Sample payment records
    payments = [
        {
            'account_name': 'John Doe',
            'account_number': '12345678',
            'sort_code': '12-34-56',
            'payment_amount': 1500.75,
            'reference': 'Payroll001'
        },
        {
            'account_name': 'Jane Smith',
            'account_number': '87654321',
            'sort_code': '65-43-21',
            'payment_amount': 1200.50,
            'reference': 'Payroll002'
        }
    ]
    
    try:
        generate_bacs_file("bacs_payment_file.csv", payments)
        print("BACS payment file generated successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
