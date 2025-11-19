"""
Generated Code Metadata:
========================
Original URL: https://prupim.com
Prompt: Generate a sample Bacs payment file format that can be used with Perfect Payrolls for making electronic payments to employees and HMRC.
Generated: DETERMINISTIC_0abab25d094d1a72
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_bacs_payment_file(file_name, payments):
    """
    Generates a BACS payment file for electronic payments.

    Args:
        file_name (str): The name of the output file.
        payments (list of dict): A list of payment records. Each record should contain:
            - 'account_name' (str): Name of the payee's account.
            - 'sort_code' (str): Sort code of the payee's bank.
            - 'account_number' (str): Account number of the payee's bank.
            - 'amount' (float): Payment amount in pounds.
            - 'reference' (str): Payment reference.

    Returns:
        None
    """
    try:
        # Validate input
        if not isinstance(file_name, str) or not file_name.endswith(".txt"):
            raise ValueError("File name must be a string ending with '.txt'.")
        if not isinstance(payments, list) or not all(isinstance(p, dict) for p in payments):
            raise ValueError("Payments must be a list of dictionaries.")

        # Header section
        header = "BACS PAYMENT FILE\n"
        header += f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        header += "----------------------------------------\n"

        # Payment records
        payment_lines = []
        for payment in payments:
            # Validate payment fields
            if not all(key in payment for key in ['account_name', 'sort_code', 'account_number', 'amount', 'reference']):
                raise ValueError("Each payment record must contain 'account_name', 'sort_code', 'account_number', 'amount', and 'reference'.")
            if len(payment['sort_code']) != 6 or not payment['sort_code'].isdigit():
                raise ValueError("Sort code must be a 6-digit numeric string.")
            if len(payment['account_number']) != 8 or not payment['account_number'].isdigit():
                raise ValueError("Account number must be an 8-digit numeric string.")
            if not isinstance(payment['amount'], (int, float)) or payment['amount'] <= 0:
                raise ValueError("Amount must be a positive number.")
            if not isinstance(payment['reference'], str) or len(payment['reference']) > 18:
                raise ValueError("Reference must be a string with a maximum length of 18 characters.")

            # Format payment line
            payment_line = f"{payment['account_name']:<18} {payment['sort_code']} {payment['account_number']} {payment['amount']:.2f} {payment['reference'][:18]}"
            payment_lines.append(payment_line)

        # Footer section
        footer = "----------------------------------------\n"
        footer += f"Total Payments: {len(payments)}\n"

        # Write to file
        with open(file_name, "w") as file:
            file.write(header)
            file.write("\n".join(payment_lines))
            file.write("\n")
            file.write(footer)

        print(f"BACS payment file '{file_name}' generated successfully.")

    except Exception as e:
        print(f"Error generating BACS payment file: {e}")


# Example usage
if __name__ == "__main__":
    payments = [
        {
            "account_name": "John Doe",
            "sort_code": "123456",
            "account_number": "12345678",
            "amount": 1500.50,
            "reference": "Salary Oct"
        },
        {
            "account_name": "Jane Smith",
            "sort_code": "654321",
            "account_number": "87654321",
            "amount": 1200.75,
            "reference": "Salary Oct"
        },
        {
            "account_name": "HMRC",
            "sort_code": "111222",
            "account_number": "33344455",
            "amount": 500.00,
            "reference": "Tax Payment"
        }
    ]

    generate_bacs_payment_file("bacs_payment_file.txt", payments)
```
