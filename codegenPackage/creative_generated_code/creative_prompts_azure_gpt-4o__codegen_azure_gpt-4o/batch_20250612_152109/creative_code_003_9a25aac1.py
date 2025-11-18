"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Write a script to automate sending service reminders to customers based on their car's minor or major service intervals, as outlined on Mechanics.ae.
Generated: DETERMINISTIC_9a25aac109b9fb4f
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib  # Library for sending emails
from email.mime.text import MIMEText  # Create email content
from email.mime.multipart import MIMEMultipart  # Create multi-part emails (e.g., with subject and body)
from datetime import datetime, timedelta  # For date calculations
import csv  # For reading customer data from a CSV file
import logging  # For logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("service_reminder.log"), logging.StreamHandler()]
)

# Email configuration (adjust these as needed)
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Service intervals (in days)
MINOR_SERVICE_INTERVAL = 180  # 6 months
MAJOR_SERVICE_INTERVAL = 365  # 12 months

# File containing customer data
CUSTOMER_DATA_FILE = "customers.csv"

def read_customer_data(file_path):
    """
    Reads customer data from a CSV file.
    The file should contain columns: Name, Email, LastServiceDate.
    
    :param file_path: Path to the CSV file
    :return: List of customer records (dicts)
    """
    try:
        customers = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers.append({
                    "name": row["Name"],
                    "email": row["Email"],
                    "last_service_date": datetime.strptime(row["LastServiceDate"], "%Y-%m-%d")
                })
        logging.info("Successfully read customer data.")
        return customers
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading customer data: {e}")
        raise

def send_reminder_email(customer, service_type):
    """
    Sends a service reminder email to a customer.
    
    :param customer: Customer record (dict containing name, email, and last service date)
    :param service_type: Type of service ("minor" or "major")
    """
    try:
        # Create email content
        subject = f"Reminder: Time for Your {service_type.capitalize()} Service!"
        body = (
            f"Dear {customer['name']},\n\n"
            f"It has been {MINOR_SERVICE_INTERVAL if service_type == 'minor' else MAJOR_SERVICE_INTERVAL} days since your last car service.\n"
            f"This is a friendly reminder to schedule your {service_type} service with us.\n\n"
            "Best regards,\n"
            "Mechanics.ae"
        )
        
        # Email setup
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USERNAME
        msg["To"] = customer["email"]
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        
        logging.info(f"Email sent successfully to {customer['email']}.")
    except Exception as e:
        logging.error(f"Failed to send email to {customer['email']}: {e}")

def calculate_service_due(customers):
    """
    Checks which customers are due for a service reminder.
    
    :param customers: List of customer records
    """
    today = datetime.today()
    for customer in customers:
        days_since_service = (today - customer["last_service_date"]).days
        if days_since_service >= MAJOR_SERVICE_INTERVAL:
            send_reminder_email(customer, "major")
        elif days_since_service >= MINOR_SERVICE_INTERVAL:
            send_reminder_email(customer, "minor")

def main():
    """
    Main function to send service reminders to customers.
    """
    try:
        logging.info("Starting service reminder script...")
        customers = read_customer_data(CUSTOMER_DATA_FILE)
        calculate_service_due(customers)
        logging.info("Service reminder script completed.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
