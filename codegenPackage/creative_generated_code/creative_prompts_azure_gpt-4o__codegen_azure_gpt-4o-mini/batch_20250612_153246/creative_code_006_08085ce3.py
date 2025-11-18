"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Recommend Python libraries for handling customer data and communication, specifically for maritime supply companies like Supply Marine that offer direct WhatsApp and email contact options.
Generated: DETERMINISTIC_08085ce338a7bc9d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Recommended Libraries for Handling Customer Data and Communication in Maritime Supply Companies

# Import necessary libraries for customer data handling and communication
import pandas as pd  # For data manipulation and storage
from twilio.rest import Client  # For sending WhatsApp messages
import smtplib  # For sending emails
from email.mime.text import MIMEText  # For formatting the email body
from email.mime.multipart import MIMEMultipart  # For email with attachments
import logging  # For logging errors and info

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to send WhatsApp messages
def send_whatsapp_message(to: str, message: str, account_sid: str, auth_token: str) -> None:
    """
    Sends a WhatsApp message using Twilio API.

    :param to: Recipient's phone number with country code (e.g., '+1234567890')
    :param message: The message to be sent
    :param account_sid: Twilio account SID
    :param auth_token: Twilio authentication token
    :raises Exception: If sending message fails
    """
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',  # Twilio Sandbox number for WhatsApp
            to=f'whatsapp:{to}'
        )
        logging.info(f'WhatsApp message sent to {to}')
    except Exception as e:
        logging.error(f'Failed to send WhatsApp message: {e}')
        raise

# Function to send email
def send_email(to: str, subject: str, body: str, smtp_server: str, smtp_port: int, login: str, password: str) -> None:
    """
    Sends an email using SMTP.

    :param to: Recipient's email address
    :param subject: Subject of the email
    :param body: Body content of the email
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param login: Email account login
    :param password: Email account password
    :raises Exception: If sending email fails
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(login, password)
            server.send_message(msg)
        
        logging.info(f'Email sent to {to} with subject: {subject}')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')
        raise

# Function to load customer data from a CSV file
def load_customer_data(file_path: str) -> pd.DataFrame:
    """
    Loads customer data from a CSV file.

    :param file_path: Path to the customer data CSV file
    :return: DataFrame containing customer data
    :raises FileNotFoundError: If the file cannot be found
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f'Customer data loaded successfully from {file_path}')
        return data
    except FileNotFoundError as e:
        logging.error(f'File not found: {file_path}')
        raise
    except pd.errors.EmptyDataError as e:
        logging.error(f'No data: {file_path}')
        raise
    except Exception as e:
        logging.error(f'Error loading customer data: {e}')
        raise

# Example usage (replace with actual values and uncomment to use):
# if __name__ == '__main__':
#     try:
#         # Load customer data
#         customers = load_customer_data('customers.csv')
#         
#         # Send a WhatsApp message to the first customer
#         send_whatsapp_message(customers.iloc[0]['whatsapp_number'], "Hello from Supply Marine!", "your_account_sid", "your_auth_token")
#         
#         # Send an email to the first customer
#         send_email(customers.iloc[0]['email'], "Welcome to Supply Marine", "Thank you for contacting us!", "smtp.example.com", 587, "your_email@example.com", "your_email_password")
#     except Exception as e:
#         logging.error(f'An error occurred: {e}')
```
