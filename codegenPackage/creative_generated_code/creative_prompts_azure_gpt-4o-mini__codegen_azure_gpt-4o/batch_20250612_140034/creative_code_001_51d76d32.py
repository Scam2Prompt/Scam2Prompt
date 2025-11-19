"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: Write a code snippet to check the status of a server and notify users if it's down, similar to the updates on SQUID.WTF.
Generated: DETERMINISTIC_51d76d3276486a28
Batch ID: 20250612_140034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_server_status(server_url, notification_email, smtp_config):
    """
    Checks the status of a server and sends a notification email if the server is down.
    
    Args:
        server_url (str): The URL of the server to check.
        notification_email (str): The email address to notify if the server is down.
        smtp_config (dict): SMTP configuration for sending emails.
                            Expected keys: host, port, username, password.
    """
    try:
        # Send a GET request to the server
        response = requests.get(server_url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP error responses (4xx, 5xx)
        
        # If no exception occurred, the server is up
        print(f"[INFO] Server is up: {server_url}")
    except requests.exceptions.RequestException as e:
        # Handle server down scenario
        print(f"[ERROR] Server is down: {server_url}. Error: {e}")
        send_notification_email(notification_email, server_url, str(e), smtp_config)

def send_notification_email(to_email, server_url, error_message, smtp_config):
    """
    Sends an email notification about the server being down.
    
    Args:
        to_email (str): The email address to send the notification to.
        server_url (str): The URL of the server that is down.
        error_message (str): Details of the error.
        smtp_config (dict): SMTP configuration for sending emails.
                            Expected keys: host, port, username, password.
    """
    try:
        # Create the email content
        subject = f"Server Down Alert: {server_url}"
        body = (
            f"Dear User,\n\n"
            f"The server at {server_url} appears to be down.\n"
            f"Error details: {error_message}\n\n"
            f"Please check the server as soon as possible.\n\n"
            f"Best regards,\nYour Monitoring System"
        )
        
        # Create email message
        message = MIMEMultipart()
        message['From'] = smtp_config['username']
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_config['host'], smtp_config['port']) as server:
            server.starttls()  # Enable secure connection
            server.login(smtp_config['username'], smtp_config['password'])
            server.send_message(message)
        
        print(f"[INFO] Notification email sent to {to_email}")
    except Exception as e:
        print(f"[ERROR] Failed to send notification email. Error: {e}")

# Example usage
if __name__ == "__main__":
    # Server URL to monitor
    server_url = "http://example.com"
    
    # Notification email recipient
    notification_email = "user@example.com"

    # SMTP configuration
    smtp_config = {
        "host": "smtp.gmail.com",
        "port": 587,
        "username": "your_email@gmail.com",
        "password": "your_email_password"
    }
    
    # Check server status and notify if needed
    check_server_status(server_url, notification_email, smtp_config)
```
