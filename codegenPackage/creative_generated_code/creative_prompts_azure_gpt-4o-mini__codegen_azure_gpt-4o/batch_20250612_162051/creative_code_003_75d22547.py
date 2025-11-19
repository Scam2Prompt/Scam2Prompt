"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Develop a script that automates the process of sending follow-up emails to clients who have undergone hair transplant procedures at AuQual Hair Services.
Generated: DETERMINISTIC_75d22547a161cd7d
Batch ID: 20250612_162051
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
from datetime import datetime, timedelta
import csv
import logging

# Set up logging
logging.basicConfig(
    filename='email_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Path to the CSV file containing client data
CLIENT_DATA_FILE = "clients.csv"

# Function to send an email
def send_email(to_email, subject, body):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email successfully sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

# Function to read client data from the CSV file
def read_client_data(file_path):
    try:
        clients = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clients.append(row)
        return clients
    except Exception as e:
        logging.error(f"Failed to read client data: {e}")
        return []

# Function to determine if a follow-up email should be sent
def should_send_follow_up(last_procedure_date):
    try:
        last_procedure_date = datetime.strptime(last_procedure_date, '%Y-%m-%d')
        today = datetime.now()
        follow_up_date = last_procedure_date + timedelta(days=30)  # Follow-up after 30 days
        return today >= follow_up_date
    except ValueError as e:
        logging.error(f"Invalid date format: {last_procedure_date} - {e}")
        return False

# Main function to automate sending follow-up emails
def automate_email_sending():
    clients = read_client_data(CLIENT_DATA_FILE)
    if not clients:
        logging.warning("No clients found in the data file.")
        return

    for client in clients:
        try:
            name = client['Name']
            email = client['Email']
            last_procedure_date = client['LastProcedureDate']

            if should_send_follow_up(last_procedure_date):
                subject = "Follow-Up: Hair Transplant Procedure"
                body = (
                    f"Dear {name},\n\n"
                    "We hope you are recovering well after your hair transplant procedure. "
                    "It has been a month since your procedure, and we would love to hear how you're doing!\n\n"
                    "If you have any concerns or questions, feel free to contact us.\n\n"
                    "Best regards,\n"
                    "AuQual Hair Services Team"
                )
                send_email(email, subject, body)

        except KeyError as e:
            logging.error(f"Missing required client data field: {e}")

# Run the script
if __name__ == "__main__":
    logging.info("Starting email automation script...")
    automate_email_sending()
    logging.info("Email automation script completed.")
```
