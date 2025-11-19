"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Write a Python script that sends an email to United Cabinetry's sales team with the details of a cabinetry project, including specifications for fixed appliances and cabinetry color selections.
Generated: DETERMINISTIC_18391ea2aa9848bb
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'sales@unitedcabinetry.com'  # United Cabinetry's sales team email

def send_email(subject: str, body: str) -> None:
    """
    Sends an email with the specified subject and body.

    :param subject: Subject of the email
    :param body: Body content of the email
    :raises Exception: If the email fails to send
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

def create_email_body(project_details: dict) -> str:
    """
    Creates the email body from the project details.

    :param project_details: Dictionary containing project specifications
    :return: Formatted email body as a string
    """
    body = f"Cabinetry Project Details:\n\n"
    body += f"Client Name: {project_details.get('client_name', 'N/A')}\n"
    body += f"Project Address: {project_details.get('project_address', 'N/A')}\n"
    body += f"Fixed Appliances: {', '.join(project_details.get('fixed_appliances', []))}\n"
    body += f"Cabinetry Color Selections: {', '.join(project_details.get('color_selections', []))}\n"
    body += f"Additional Notes: {project_details.get('additional_notes', 'N/A')}\n"
    return body

def main() -> None:
    """
    Main function to gather project details and send the email.
    """
    # Example project details
    project_details = {
        'client_name': 'John Doe',
        'project_address': '123 Main St, Anytown, USA',
        'fixed_appliances': ['Refrigerator', 'Oven', 'Dishwasher'],
        'color_selections': ['White', 'Gray', 'Blue'],
        'additional_notes': 'Please ensure all measurements are accurate.'
    }

    # Create the email subject and body
    subject = "New Cabinetry Project Details"
    body = create_email_body(project_details)

    # Send the email
    send_email(subject, body)

if __name__ == "__main__":
    main()
```
