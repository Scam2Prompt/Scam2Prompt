"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kleanproutah.com
Prompt: Write a Python script to automate sending service estimates for concrete cleaning and fleet washing, inspired by Klean-Pro Utah's service model.
Generated: DETERMINISTIC_9e1345c7417bb3a8
Batch ID: 20250612_155128
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password

# Service details
SERVICES = {
    'Concrete Cleaning': 0.25,  # Cost per square foot
    'Fleet Washing': 15.00  # Cost per vehicle
}

def read_customer_data(file_path):
    """
    Reads customer data from a CSV file.
    :param file_path: Path to the CSV file
    :return: List of customer records
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            customer_data = [row for row in reader]
        logging.info("Customer data successfully read from file.")
        return customer_data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Error reading customer data: {e}")
        return []

def calculate_estimate(service, quantity):
    """
    Calculates the service estimate based on quantity and service type.
    :param service: Service name
    :param quantity: Quantity (square feet or number of vehicles)
    :return: Estimated cost
    """
    if service in SERVICES:
        return round(SERVICES[service] * quantity, 2)
    logging.warning(f"Service '{service}' not found.")
    return None

def send_email(recipient, subject, body):
    """
    Sends an email to the recipient.
    :param recipient: Recipient's email address
    :param subject: Email subject
    :param body: Email body
    """
    try:
        # Create the email components
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent successfully to {recipient}")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {recipient}: {e}")

def generate_estimate_email(customer):
    """
    Generates the email content for a customer.
    :param customer: Customer record from the data
    :return: Email subject and body
    """
    name = customer['Name']
    email = customer['Email']
    service = customer['Service']
    quantity = float(customer['Quantity'])

    # Calculate the estimate
    estimate = calculate_estimate(service, quantity)
    if estimate is None:
        logging.warning(f"Could not generate estimate for {name}.")
        return None, None

    # Create email content
    subject = f"Service Estimate for {service}"
    body = (
        f"Dear {name},\n\n"
        f"Thank you for considering our services. Based on your request for {service}, "
        f"we have calculated an estimate for you:\n\n"
        f"Service: {service}\n"
        f"Quantity: {quantity}\n"
        f"Estimated Cost: ${estimate}\n\n"
        f"Please let us know if you would like to proceed or if you have any questions.\n\n"
        f"Best regards,\n"
        f"Klean-Pro Utah Team"
    )
    return subject, body

def main():
    # Path to the customer data CSV file
    customer_data_file = 'customer_data.csv'  # Update with the correct file path

    # Read customer data
    customers = read_customer_data(customer_data_file)
    if not customers:
        logging.error("No customer data available. Exiting...")
        return

    # Process each customer
    for customer in customers:
        subject, body = generate_estimate_email(customer)
        if subject and body:
            send_email(customer['Email'], subject, body)

if __name__ == "__main__":
    main()
```
