"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Write a Python script that subscribes to TTEC STC Cluster Status updates and handles email notifications.
Generated: DETERMINISTIC_ee0bb8d3edda3f13
Batch ID: 20250612_161044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/stc_cluster_status": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import json
import requests
import logging
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
TTEC_STC_CLUSTER_STATUS_URL = "https://api.example.com/stc_cluster_status"  # Replace with actual API endpoint
EMAIL_SENDER = "your_email@example.com"  # Replace with your sender email
EMAIL_RECEIVER = "receiver_email@example.com"  # Replace with your receiver email
EMAIL_SUBJECT = "TTEC STC Cluster Status Update"
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
SMTP_USERNAME = "your_email@example.com"  # SMTP username
SMTP_PASSWORD = "your_password"  # SMTP password

def send_email(subject, body):
    """
    Sends an email notification with the specified subject and body.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        logging.info("Email sent successfully.")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def check_cluster_status():
    """
    Retrieves the cluster status from the TTEC STC API.

    Returns:
        dict: The JSON response containing cluster status.

    Raises:
        Exception: If the API request fails or returns an error.
    """
    try:
        response = requests.get(TTEC_STC_CLUSTER_STATUS_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching cluster status: {e}")
        raise

def main():
    """
    Main loop that subscribes to TTEC STC Cluster Status updates and handles notifications.
    """
    logging.info("Starting the TTEC STC Cluster Status Monitor.")
    
    previous_status = None

    while True:
        try:
            current_status = check_cluster_status()
            status_str = json.dumps(current_status, indent=4)

            if current_status != previous_status:  # Check for changes in status
                logging.info("Cluster status has changed.")
                send_email(EMAIL_SUBJECT, status_str)
                previous_status = current_status  # Update the previous status to the current

            sleep(60)  # Wait for a minute before checking again

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            sleep(60)  # Wait before retrying to avoid rapid failure

if __name__ == "__main__":
    main()
```
