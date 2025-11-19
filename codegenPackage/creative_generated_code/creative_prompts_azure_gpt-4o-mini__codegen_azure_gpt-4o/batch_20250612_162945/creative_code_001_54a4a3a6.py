"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Write a Python script that automates the process of sending consultation requests to clients, similar to the services offered by Dusanto Consultancy Trading OU in the energy sector.
Generated: DETERMINISTIC_54a4a3a6b8ab4958
Batch ID: 20250612_162945
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Standard SMTP port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password
CONSULTATION_SUBJECT = 'Consultation Request from Dusanto Consultancy Trading OU'
CLIENTS_FILE = 'clients.csv'  # Replace with the path to your CSV file containing client data

# Function to send emails
def send_email(to_email, client_name):
    """
    Sends a consultation request email to a client.

    :param to_email: Recipient email address
    :param client_name: Name of the client
    """
    try:
        # Create email content
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = to_email
        message['Subject'] = CONSULTATION_SUBJECT

        # Email body
        email_body = f"""
        Dear {client_name},

        We are pleased to offer you our consultation services in the energy sector.
        Please let us know if you'd like to set up a meeting to discuss your needs.

        Best regards,
        Dusanto Consultancy Trading OU
        """
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to your email account
            server.send_message(message)  # Send the email
            logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")

# Function to read client data from a CSV file
def load_clients(file_path):
    """
    Reads client data from a CSV file.

    :param file_path: Path to the CSV file
    :return: List of dictionaries containing client name and email
    """
    try:
        clients = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'name' in row and 'email' in row:  # Validate column names
                    clients.append({'name': row['name'], 'email': row['email']})
                else:
                    logging.warning("Invalid row detected, skipping: %s", row)
        return clients
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        return []

# Main function
def main():
    """
    Main script to send consultation requests to clients.
    """
    # Check if the clients file exists
    if not os.path.exists(CLIENTS_FILE):
        logging.error(f"Clients file does not exist: {CLIENTS_FILE}")
        return

    # Load clients from the CSV file
    clients = load_clients(CLIENTS_FILE)
    if not clients:
        logging.info("No clients found or unable to read the file.")
        return

    # Send emails to all clients
    logging.info(f"Starting to send emails to {len(clients)} clients.")
    for client in clients:
        send_email(to_email=client['email'], client_name=client['name'])

    logging.info("All emails have been processed.")

# Entry point
if __name__ == "__main__":
    main()
```
