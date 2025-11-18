"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secure-fkcbank.com
Prompt: Create a program that generates eStatements for customers, inspired by the environmentally-friendly and secure eStatements service described on First Keystone Community Bank's website.
Generated: DETERMINISTIC_8d66545961282ed2
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
from datetime import datetime
from fpdf import FPDF

# Constants
OUTPUT_DIR = "eStatements"
CUSTOMER_DATA_FILE = "customers.csv"  # Assumes a CSV file with customer data
LOG_FILE = "generation_log.txt"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def log_message(message):
    """Logs a message to the log file."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()}: {message}\n")

def generate_estatement(customer, statement_data):
    """
    Generates a PDF eStatement for a customer.
    
    :param customer: Dictionary containing customer information.
    :param statement_data: List of dictionaries containing statement transactions.
    :return: None
    """
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)

        # Title
        pdf.cell(0, 10, "Customer eStatement", 0, 1, "C")
        
        # Customer Information
        pdf.set_font("Arial", "", 10)
        pdf.cell(0, 10, f"Customer Name: {customer['Name']}", 0, 1)
        pdf.cell(0, 10, f"Account Number: {customer['Account Number']}", 0, 1)
        pdf.cell(0, 10, f"Email: {customer['Email']}", 0, 1)
        pdf.cell(0, 10, f"Statement Date: {datetime.now().strftime('%Y-%m-%d')}", 0, 1)
        pdf.cell(0, 10, "", 0, 1)  # Blank line
        
        # Statement Transactions
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 10, "Transactions:", 0, 1)
        pdf.set_font("Arial", "", 10)
        for transaction in statement_data:
            pdf.cell(0, 10, f"{transaction['Date']} - {transaction['Description']}: ${transaction['Amount']}", 0, 1)

        # Save PDF to file
        filename = f"{customer['Account Number']}_eStatement_{datetime.now().strftime('%Y%m%d')}.pdf"
        filepath = os.path.join(OUTPUT_DIR, filename)
        pdf.output(filepath)
        log_message(f"eStatement generated successfully for {customer['Name']} at {filepath}")
    except Exception as e:
        log_message(f"Error generating eStatement for {customer['Name']}: {str(e)}")

def load_customer_data(file_path):
    """
    Loads customer data from a CSV file.
    
    :param file_path: Path to the CSV file containing customer data.
    :return: List of dictionaries with customer information.
    """
    try:
        customers = []
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers.append(row)
        log_message("Customer data loaded successfully.")
        return customers
    except Exception as e:
        log_message(f"Error loading customer data: {str(e)}")
        return []

def main():
    """
    Main function to drive the eStatement generation process.
    """
    customers = load_customer_data(CUSTOMER_DATA_FILE)
    if not customers:
        log_message("No customer data available. Exiting.")
        return

    # Placeholder for transaction data - In production, fetch real data from a database or API
    transaction_data = [
        {"Date": "2023-10-01", "Description": "Deposit", "Amount": "1000.00"},
        {"Date": "2023-10-03", "Description": "Withdrawal", "Amount": "500.00"},
        {"Date": "2023-10-05", "Description": "Purchase", "Amount": "200.00"},
    ]

    for customer in customers:
        generate_estatement(customer, transaction_data)

if __name__ == "__main__":
    main()
```
