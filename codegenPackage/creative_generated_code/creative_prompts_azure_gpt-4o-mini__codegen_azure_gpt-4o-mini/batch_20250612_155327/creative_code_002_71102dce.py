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
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Constants for email configuration
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USER = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

# Function to load billing data from a JSON file
def load_billing_data(file_path):
    """Load billing data from a specified JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Billing data file not found.")
    
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError("Error decoding JSON data: " + str(e))

# Function to generate an invoice
def generate_invoice(billing_info):
    """Generate a formatted invoice string from billing information."""
    invoice_lines = []
    invoice_lines.append("Invoice Date: {}\n".format(datetime.now().strftime("%Y-%m-%d")))
    invoice_lines.append("Customer: {}\n".format(billing_info['customer_name']))
    invoice_lines.append("Items:\n")
    
    total_amount = 0.0
    for item in billing_info['items']:
        line_total = item['quantity'] * item['price']
        total_amount += line_total
        invoice_lines.append(" - {}: {} x ${:.2f} = ${:.2f}\n".format(
            item['description'], item['quantity'], item['price'], line_total))
    
    invoice_lines.append("\nTotal Amount Due: ${:.2f}\n".format(total_amount))
    return ''.join(invoice_lines)

# Function to send the invoice via email
def send_invoice_email(to_email, invoice_content):
    """Send the generated invoice to the specified email address."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = to_email
    msg['Subject'] = "Your Invoice"

    msg.attach(MIMEText(invoice_content, 'plain'))
    
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Invoice sent successfully to {}".format(to_email))
    except Exception as e:
        raise RuntimeError("Failed to send email: " + str(e))

# Main function to execute billing automation
def automate_billing(file_path, customer_email):
    """Automate the billing process by loading data, generating, and sending an invoice."""
    try:
        billing_info = load_billing_data(file_path)
        invoice_content = generate_invoice(billing_info)
        send_invoice_email(customer_email, invoice_content)
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print("Error during billing process: " + str(e))

# Runner code
if __name__ == "__main__":
    # Specify the path to the billing data file and the customer's email
    billing_data_file = 'billing_data.json'
    customer_email = 'customer@example.com'
    
    # Execute the billing automation process
    automate_billing(billing_data_file, customer_email)
```

Make sure to replace `smtp.example.com`, `your_email@example.com`, and `your_email_password` with actual values appropriate for your email configuration and update the `billing_data_file` and `customer_email` variables as needed.
