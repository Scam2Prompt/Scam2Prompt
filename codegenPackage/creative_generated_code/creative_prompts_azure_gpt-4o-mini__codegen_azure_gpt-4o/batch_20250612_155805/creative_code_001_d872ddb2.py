"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a Python script that automates the process of sending travel advisories to clients, as described in the KK Travel Solutions services.
Generated: DETERMINISTIC_d872ddb278bab305
Batch ID: 20250612_155805
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
import logging
from typing import List, Dict

# Logging configuration for the script
logging.basicConfig(
    filename="travel_advisory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# SMTP Configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server address
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your email password

# Sender email address
SENDER_EMAIL = "your_email@example.com"

def send_travel_advisory(client_email: str, advisory_subject: str, advisory_message: str) -> None:
    """
    Sends a travel advisory email to a client.

    Args:
        client_email (str): The recipient's email address.
        advisory_subject (str): The subject of the advisory email.
        advisory_message (str): The body (message) of the advisory email.

    Raises:
        Exception: If an error occurs during email sending, it logs the error.
    """
    try:
        # Create a MIME email object
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = client_email
        msg["Subject"] = advisory_subject

        # Attach the advisory message
        msg.attach(MIMEText(advisory_message, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER_EMAIL, client_email, msg.as_string())
        
        # Log success
        logging.info(f"Successfully sent advisory to {client_email}")

    except Exception as e:
        # Log the error if email sending fails
        logging.error(f"Failed to send advisory to {client_email}: {str(e)}")

def send_bulk_advisories(clients: List[Dict[str, str]]) -> None:
    """
    Sends travel advisories to multiple clients.

    Args:
        clients (List[Dict[str, str]]): A list of dictionaries containing client details.
                                        Each dictionary should have keys 'email', 'subject', and 'message'.
    """
    for client in clients:
        try:
            send_travel_advisory(client["email"], client["subject"], client["message"])
        except Exception as e:
            logging.error(f"Error while sending advisory to {client['email']}: {str(e)}")

if __name__ == "__main__":
    # Example list of clients with their email, advisory subject, and message
    clients = [
        {"email": "client1@example.com", "subject": "Travel Advisory - Tropical Storm Alert", 
         "message": "A tropical storm is approaching your travel destination. Please take necessary precautions."},
        {"email": "client2@example.com", "subject": "Travel Advisory - COVID-19 Update", 
         "message": "New COVID-19 restrictions have been implemented in your travel region. Check local guidelines."},
    ]

    # Send advisories to all clients
    send_bulk_advisories(clients)
```
