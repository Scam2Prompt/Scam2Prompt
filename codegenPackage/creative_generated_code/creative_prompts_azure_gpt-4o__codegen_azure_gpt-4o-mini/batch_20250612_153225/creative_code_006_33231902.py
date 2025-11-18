"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Create a script to automate customer support inquiries for sealing system products, integrating the contact details and global export information from Silver Seals.
Generated: DETERMINISTIC_33231902fd94a061
Batch ID: 20250612_153225
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
import csv
import os

# Define constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Change to your SMTP server
SMTP_PORT = 587  # SMTP port (usually 587 for TLS)
USERNAME = 'your_email@example.com'  # Your email
PASSWORD = 'your_email_password'  # Your email password

# Define the path for the CSV file containing customer inquiries
CSV_FILE_PATH = 'customer_inquiries.csv'

def read_customer_inquiries(csv_file):
    """
    Reads customer inquiries from a CSV file.
    
    Args:
        csv_file (str): Path to the CSV file.
        
    Returns:
        list: A list of dictionaries containing customer inquiry details.
    """
    inquiries = []
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inquiries.append(row)
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return inquiries

def send_email(recipient, subject, body):
    """
    Sends an email to the specified recipient.
    
    Args:
        recipient (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body of the email.
        
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")
        return False

def process_inquiries(inquiries):
    """
    Processes customer inquiries and sends email responses.
    
    Args:
        inquiries (list): List of customer inquiry dictionaries.
    """
    for inquiry in inquiries:
        recipient = inquiry.get('email')
        subject = "Re: Your Inquiry about Sealing Systems"
        body = f"Dear {inquiry.get('name')},\n\nThank you for your inquiry about our sealing system products. " \
               f"We will get back to you shortly with the necessary information.\n\nBest regards,\n" \
               f"Silver Seals Support Team"
        
        if recipient:
            success = send_email(recipient, subject, body)
            if success:
                print(f"Email sent successfully to {recipient}.")
            else:
                print(f"Failed to send email to {recipient}.")
        else:
            print("No email address provided in the inquiry.")

def main():
    """
    Main function to automate customer support inquiries.
    """
    inquiries = read_customer_inquiries(CSV_FILE_PATH)
    if inquiries:
        process_inquiries(inquiries)
    else:
        print("No inquiries to process.")

if __name__ == "__main__":
    main()
```
