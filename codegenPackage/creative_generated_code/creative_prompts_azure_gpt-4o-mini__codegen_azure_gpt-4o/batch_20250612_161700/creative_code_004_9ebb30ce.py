"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write a script to automate the process of sending inquiries about specialized cargo transport services, like those provided by OPC, using their contact information and service offerings.
Generated: DETERMINISTIC_9ebb30ce8b2dd8cf
Batch ID: 20250612_161700
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

def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.

    Args:
        smtp_server (str): SMTP server address.
        port (int): Port number for the SMTP server.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body content.

    Returns:
        None
    """
    try:
        # Set up the MIME structure for the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Enable secure connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")


def load_contact_info(csv_file):
    """
    Loads contact information from a CSV file.

    Args:
        csv_file (str): Path to the CSV file containing contact information.

    Returns:
        list: List of dictionaries containing contact information.
    """
    contacts = []
    try:
        # Read the CSV file and parse contact information
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)

        print(f"Successfully loaded {len(contacts)} contacts from {csv_file}")
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except Exception as e:
        print(f"Failed to load contacts from {csv_file}. Error: {e}")

    return contacts


def main():
    """
    Main function to automate the process of sending inquiries.

    Args:
        None

    Returns:
        None
    """
    # Configuration settings
    smtp_server = "smtp.example.com"  # Replace with your SMTP server address
    port = 587  # Commonly used port for SMTP
    sender_email = "youremail@example.com"  # Replace with your email address
    sender_password = "yourpassword"  # Replace with your email password
    subject = "Inquiry About Specialized Cargo Transport Services"
    body_template = """
    Dear {name},

    I am writing to inquire about your specialized cargo transport services. We are looking for reliable and efficient solutions tailored to our unique needs.

    Please provide more information regarding your offerings, pricing, and availability.

    Thank you and looking forward to your response.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Path to the CSV file containing contact information
    csv_file = "contact_info.csv"

    # Load contacts from the CSV file
    contacts = load_contact_info(csv_file)

    # Send inquiries to each contact
    for contact in contacts:
        if 'email' in contact and 'name' in contact:
            recipient_email = contact['email']
            name = contact['name']
            body = body_template.format(name=name)
            send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body)
        else:
            print("Invalid contact information. Skipping...")

if __name__ == "__main__":
    main()
```
