"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Write a Python script that automates the process of collecting client testimonials for a digital branding agency.
Generated: DETERMINISTIC_492f8a1d7bede40c
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
import csv
import os
import logging
from datetime import datetime

# Setup logging
LOG_FILE = "testimonial_request.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_password"  # Use environment variables for security

# Testimonial request template
EMAIL_SUBJECT = "We'd love to hear your feedback!"
EMAIL_BODY = """
Hi {client_name},

Thank you for working with us at [Your Digital Branding Agency Name]. 
We'd greatly appreciate it if you could share your experience with us 
by providing a testimonial. Your feedback helps us grow and serve our clients better.

Please reply to this email with your testimonial, or click the link below to fill out the form:
[Insert Testimonial Form Link]

Thank you for your time!

Best regards,
[Your Name]
"""

# File paths
CLIENTS_CSV_FILE = "clients.csv"

def load_client_emails(csv_file):
    """
    Load client names and email addresses from a CSV file.
    :param csv_file: Path to the CSV file containing client data.
    :return: List of client dictionaries with 'name' and 'email' keys.
    """
    clients = []
    if not os.path.exists(csv_file):
        logging.error(f"File not found: {csv_file}")
        raise FileNotFoundError(f"CSV file '{csv_file}' not found.")
    
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "name" in row and "email" in row:
                clients.append({"name": row["name"], "email": row["email"]})
            else:
                logging.warning("Invalid data format in CSV file.")
    return clients

def send_email(client_name, client_email):
    """
    Send an email request for a testimonial to a client.
    :param client_name: Name of the client.
    :param client_email: Email address of the client.
    """
    try:
        # Create email message
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = client_email
        message["Subject"] = EMAIL_SUBJECT

        # Personalize email body
        personalized_body = EMAIL_BODY.format(client_name=client_name)
        message.attach(MIMEText(personalized_body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(message)
        
        logging.info(f"Email successfully sent to {client_email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {client_email}: {e}")

def main():
    """
    Main function to load client data and send testimonial request emails.
    """
    try:
        logging.info("Testimonial request process started.")
        
        # Load client data from CSV
        clients = load_client_emails(CLIENTS_CSV_FILE)
        if not clients:
            logging.warning("No clients found in the CSV file.")
            return

        # Send emails to all clients
        for client in clients:
            send_email(client["name"], client["email"])
        
        logging.info("Testimonial request process completed.")
    except Exception as e:
        logging.error(f"An error occurred in the process: {e}")

if __name__ == "__main__":
    main()
```
