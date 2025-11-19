"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Write a Python script that automates the process of connecting with suppliers for an e-commerce business, as suggested by FinishDrop's business model.
Generated: DETERMINISTIC_ce509757d27b851f
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import csv
import os

# Configuration for email server and sender details
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",  # Change this if using a different provider
    "port": 587,
    "sender_email": "your_email@example.com",
    "sender_password": "your_password",  # Use environment variables in production
}

# CSV file containing supplier contact details
SUPPLIER_CSV_FILE = "suppliers.csv"

# Email subject and template
EMAIL_SUBJECT = "Partnership Opportunity with [Your E-commerce Business]"
EMAIL_TEMPLATE = """
Dear {supplier_name},

I hope this email finds you well. My name is [Your Name], and I represent [Your E-commerce Business]. 
We are a growing e-commerce platform specializing in [your niche/products], and we're looking to partner with reliable suppliers like yourself.

We believe your products align perfectly with our target customers, and we'd love to discuss how we can work together.

Please let us know your availability for a quick call or meeting to explore this opportunity further.

Looking forward to hearing from you.

Best regards,
[Your Name]
[Your Contact Information]
"""

def read_suppliers_from_csv(csv_file):
    """
    Reads supplier contact data from a CSV file.
    
    :param csv_file: Path to the CSV file containing supplier data.
    :return: List of dictionaries, each containing supplier name and email.
    """
    suppliers = []
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'Supplier Name' in row and 'Email' in row:
                    suppliers.append({
                        'name': row['Supplier Name'],
                        'email': row['Email']
                    })
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' does not exist.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return suppliers

def send_email(smtp_details, recipient_email, recipient_name):
    """
    Sends an email to a supplier.
    
    :param smtp_details: Dictionary containing SMTP server configuration.
    :param recipient_email: Email address of the recipient.
    :param recipient_name: Name of the recipient.
    :return: None
    """
    try:
        # Establish connection to SMTP server
        server = smtplib.SMTP(smtp_details["smtp_server"], smtp_details["port"])
        server.starttls()  # Upgrade connection to secure encryption
        server.login(smtp_details["sender_email"], smtp_details["sender_password"])
        
        # Create email content
        msg = MIMEMultipart()
        msg["From"] = smtp_details["sender_email"]
        msg["To"] = recipient_email
        msg["Subject"] = EMAIL_SUBJECT
        
        # Personalize and attach the message body
        body = EMAIL_TEMPLATE.format(supplier_name=recipient_name)
        msg.attach(MIMEText(body, "plain"))
        
        # Send the email
        server.sendmail(smtp_details["sender_email"], recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_name} ({recipient_email})")
        
    except smtplib.SMTPException as smtp_err:
        print(f"Error sending email to {recipient_email}: {smtp_err}")
    except Exception as general_err:
        print(f"Unexpected error: {general_err}")
    finally:
        # Ensure connection closes
        server.quit()

def main():
    """
    Main function to automate supplier email outreach.
    """
    suppliers = read_suppliers_from_csv(SUPPLIER_CSV_FILE)
    if not suppliers:
        print("No suppliers found. Please check your CSV file.")
        return
    
    print(f"Found {len(suppliers)} suppliers. Starting email outreach...")
    for supplier in suppliers:
        if 'email' in supplier and 'name' in supplier:
            send_email(EMAIL_CONFIG, supplier['email'], supplier['name'])
        else:
            print(f"Skipping supplier due to missing information: {supplier}")

if __name__ == "__main__":
    # Ensure email password is fetched securely (e.g., environment variable)
    EMAIL_CONFIG["sender_password"] = os.getenv("EMAIL_PASSWORD")
    if not EMAIL_CONFIG["sender_password"]:
        print("Error: Email password not provided. Set EMAIL_PASSWORD environment variable.")
    else:
        main()
```
