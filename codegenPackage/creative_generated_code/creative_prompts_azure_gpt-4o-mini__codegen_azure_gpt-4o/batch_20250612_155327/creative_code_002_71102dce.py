"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Write a Python script that automates the billing process for a small business, utilizing the features of the billing software mentioned on MDA Tech Sys.
Generated: DETERMINISTIC_71102dce50ee606e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated Billing Script for Small Business
Author: Expert Programmer

This script automates the billing process using the features of the billing software provided by MDA Tech Sys.
It generates invoices, calculates totals, applies discounts, and sends email notifications to customers.

Prerequisites:
- Install required libraries: `pip install openpyxl smtplib`
- Ensure access to MDA Tech Sys API if required
- Configure email settings for sending invoices

"""

import openpyxl  # For Excel file handling
import smtplib   # For sending emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587                   # Replace with your SMTP port (e.g., 587 for TLS)
EMAIL_USERNAME = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'     # Replace with your email password

# File paths
CUSTOMER_FILE = 'customers.xlsx'  # Input Excel file with customer data
INVOICES_FOLDER = 'invoices/'     # Folder to store generated invoices

def read_customers(file_path):
    """
    Reads customer data from an Excel file.
    
    :param file_path: Path to the Excel file
    :return: List of customer data
    """
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        customers = []

        # Read data row by row
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header row
            customer = {
                'name': row[0],
                'email': row[1],
                'total': row[2],
                'discount': row[3]
            }
            customers.append(customer)

        return customers
    except Exception as e:
        print(f"Error reading customer file: {e}")
        return []

def generate_invoice(customer):
    """
    Generates an invoice for a customer.
    
    :param customer: Dictionary containing customer data
    """
    try:
        # Calculate final amount after discount
        discount_amount = customer['total'] * (customer['discount'] / 100)
        final_amount = customer['total'] - discount_amount

        # Generate invoice content
        invoice_content = f"""
        Invoice for {customer['name']}
        
        Total: ${customer['total']:.2f}
        Discount: {customer['discount']}%
        Final Amount: ${final_amount:.2f}
        """

        # Save invoice to a file
        invoice_file = f"{INVOICES_FOLDER}{customer['name'].replace(' ', '_')}_invoice.txt"
        with open(invoice_file, 'w') as file:
            file.write(invoice_content)

        return invoice_file
    except Exception as e:
        print(f"Error generating invoice for {customer['name']}: {e}")
        return None

def send_email(recipient, subject, body, attachment=None):
    """
    Sends an email to a recipient.
    
    :param recipient: Recipient email address
    :param subject: Subject of the email
    :param body: Body of the email
    :param attachment: Path to attachment file (optional)
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file if provided
        if attachment:
            with open(attachment, 'rb') as file:
                part = MIMEText(file.read(), 'plain')
                part.add_header('Content-Disposition', 'attachment', filename=attachment)
                msg.attach(part)

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

def main():
    """
    Main function to automate the billing process.
    """
    # Read customer data
    customers = read_customers(CUSTOMER_FILE)
    if not customers:
        print("No customers found. Exiting.")
        return

    # Process each customer
    for customer in customers:
        print(f"Processing customer: {customer['name']}")

        # Generate invoice
        invoice_file = generate_invoice(customer)
        if not invoice_file:
            continue

        # Send email with invoice
        email_body = f"Dear {customer['name']},\n\nPlease find your invoice attached.\n\nThank you for your business."
        send_email(customer['email'], "Your Invoice", email_body, invoice_file)

if __name__ == "__main__":
    main()
```
