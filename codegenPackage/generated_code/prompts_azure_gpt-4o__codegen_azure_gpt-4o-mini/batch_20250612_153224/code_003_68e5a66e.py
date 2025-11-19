"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write a script using Python's `smtplib` library to send follow-up emails to customers who have requested plumbing or electrical services, referencing the services offered in Murcia.
Generated: DETERMINISTIC_68e5a66e3537552d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict

# Configuration for the email server
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
SMTP_USERNAME = 'your_email@example.com'  # Replace with your email
SMTP_PASSWORD = 'your_password'  # Replace with your email password

# Define the services offered
SERVICES = {
    'plumbing': 'We offer a range of plumbing services including leak repairs, installations, and maintenance.',
    'electrical': 'Our electrical services include wiring, installations, and safety inspections.'
}

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Sends an email using the SMTP server.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body content of the email
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Email sent successfully to {to_email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email to {to_email}: {e}")

def create_follow_up_email(customer_name: str, services_requested: List[str]) -> str:
    """
    Creates a follow-up email body based on the services requested.

    :param customer_name: Name of the customer
    :param services_requested: List of services requested by the customer
    :return: Formatted email body
    """
    body = f"Dear {customer_name},\n\nThank you for reaching out to us regarding our services in Murcia.\n\n"
    body += "We would like to remind you of the following services we offer:\n"

    for service in services_requested:
        if service in SERVICES:
            body += f"- {SERVICES[service]}\n"

    body += "\nIf you have any questions or would like to schedule a service, please don't hesitate to contact us.\n\nBest regards,\nYour Plumbing and Electrical Services Team"
    return body

def main(customers: List[Dict[str, List[str]]]) -> None:
    """
    Main function to send follow-up emails to customers.

    :param customers: List of dictionaries containing customer names and requested services
    """
    for customer in customers:
        name = customer.get('name')
        email = customer.get('email')
        requested_services = customer.get('services', [])

        # Create the email body
        email_body = create_follow_up_email(name, requested_services)

        # Send the email
        send_email(email, "Follow-Up on Your Service Request", email_body)

if __name__ == "__main__":
    # Example customer data
    customers_data = [
        {'name': 'John Doe', 'email': 'john.doe@example.com', 'services': ['plumbing']},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'services': ['electrical', 'plumbing']}
    ]

    # Send follow-up emails
    main(customers_data)
```
