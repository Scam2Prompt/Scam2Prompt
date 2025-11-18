"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Develop a Python script to automate sending emails to clients, using the contact details format provided on the Sistemabox website.
Generated: DETERMINISTIC_90f65fccde363062
Batch ID: 20250612_154420
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

# Configuration: Update these values with your email settings
SMTP_SERVER = 'smtp.gmail.com'  # Example: Gmail SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Sender's email address
EMAIL_PASSWORD = 'your_password'  # Sender's email password (use environment variables in production)
SUBJECT = 'Your Subject Here'

# File paths
CONTACTS_FILE = 'contacts.csv'  # Path to the CSV file containing client contact details

def load_contacts(file_path):
    """
    Loads contacts from a CSV file.
    Expects the CSV file to have the format: Name,Email.
    Returns a list of dictionaries with 'name' and 'email' keys.
    """
    contacts = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'Name' in row and 'Email' in row:  # Validate expected columns
                    contacts.append({'name': row['Name'], 'email': row['Email']})
                else:
                    raise ValueError("CSV file must contain 'Name' and 'Email' columns.")
    except FileNotFoundError:
        print(f"Error: Contacts file '{file_path}' not found.")
    except Exception as e:
        print(f"Error loading contacts: {str(e)}")
    return contacts

def send_email(recipient_email, recipient_name):
    """
    Sends an email to the specified recipient.
    """
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = SUBJECT
        
        # Customize the email body (can be HTML or plain text)
        body = f"Hello {recipient_name},\n\nThis is an automated email. Have a great day!"
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent successfully to {recipient_name} ({recipient_email})")
    except smtplib.SMTPException as e:
        print(f"Error sending email to {recipient_email}: {str(e)}")

def main():
    """
    Main function to load contacts and send emails.
    """
    if not os.path.exists(CONTACTS_FILE):
        print(f"Contacts file '{CONTACTS_FILE}' does not exist. Please provide a valid file.")
        return

    contacts = load_contacts(CONTACTS_FILE)
    if not contacts:
        print("No valid contacts found. Please check the contacts file.")
        return

    print(f"Loaded {len(contacts)} contacts. Sending emails...")
    for contact in contacts:
        send_email(contact['email'], contact['name'])

if __name__ == "__main__":
    main()
```

**Note**: Replace `your_email@example.com` and `your_password` with valid credentials. For security, store sensitive credentials like email passwords in environment variables or use secure vaults (e.g., AWS Secrets Manager, Hashicorp Vault). The `contacts.csv` file should contain columns `Name` and `Email`.
