"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Write a script to automate the process of sending inquiries about specialized cargo transport services, like those provided by OPC, using their contact information and service offerings.
Generated: DETERMINISTIC_9ebb30ce8b2dd8cf
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to automate the process of sending inquiries about specialized cargo transport services.

This script uses the smtplib library to send emails to OPC and other specialized cargo transport services.
It requires the services' contact information and service offerings to be stored in a JSON file.

Usage:
    python send_inquiries.py

Requirements:
    - Python 3.8+
    - smtplib
    - email
    - json
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_service_info(file_path):
    """
    Load service information from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: A dictionary containing the service information.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON: {e}")
        return {}

def create_message(service_name, service_offering, inquiry):
    """
    Create a message to be sent to the service provider.

    Args:
        service_name (str): Name of the service.
        service_offering (str): Description of the service offering.
        inquiry (str): The inquiry message.

    Returns:
        MIMEMultipart: A MIMEMultipart object containing the message.
    """
    message = MIMEMultipart()
    message['Subject'] = f"Inquiry about {service_name} - {service_offering}"
    message['From'] = 'your_email@example.com'  # Replace with your email
    message['To'] = 'service_email@example.com'  # Replace with service email

    body = f"""
    Dear {service_name} Team,

    I am inquiring about your {service_offering} service. Could you please provide me with more information about this service, including pricing and availability?

    Thank you for your time and assistance.

    Best regards,
    Your Name
    """
    message.attach(MIMEText(body, 'plain'))
    return message

def send_email(message, smtp_server, smtp_port, username, password):
    """
    Send an email using the provided SMTP server.

    Args:
        message (MIMEMultipart): The message to be sent.
        smtp_server (str): The SMTP server to use.
        smtp_port (int): The SMTP port to use.
        username (str): The username to use for authentication.
        password (str): The password to use for authentication.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to authenticate with SMTP server")
        return False
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        return False

def main():
    # Load service information from JSON file
    service_info = load_service_info('service_info.json')

    # Iterate over each service
    for service in service_info:
        service_name = service['name']
        service_offering = service['offering']
        service_email = service['email']
        smtp_server = service['smtp_server']
        smtp_port = service['smtp_port']
        username = service['username']
        password = service['password']

        # Create a message for the service
        inquiry = "Please provide more information about this service."
        message = create_message(service_name, service_offering, inquiry)

        # Send the email
        if send_email(message, smtp_server, smtp_port, username, password):
            logging.info(f"Email sent to {service_email} successfully")
        else:
            logging.error(f"Failed to send email to {service_email}")

if __name__ == "__main__":
    main()
```

**service_info.json**
```json
[
    {
        "name": "OPC",
        "offering": "Specialized Cargo Transport",
        "email": "opc@example.com",
        "smtp_server": "smtp.opc.com",
        "smtp_port": 587,
        "username": "opc_username",
        "password": "opc_password"
    },
    {
        "name": "Other Service",
        "offering": "Other Service Offering",
        "email": "other@example.com",
        "smtp_server": "smtp.other.com",
        "smtp_port": 587,
        "username": "other_username",
        "password": "other_password"
    }
]
```
