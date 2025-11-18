"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantaxbonk.network
Prompt: Write a function to send automated alerts when a "MantaxBonk" service exceeds its bandwidth limit.
Generated: DETERMINISTIC_d48b62870db3d07e
Batch ID: 20250612_151343
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_alert_email(recipient_email, service_name, usage, limit):
    """
    Sends an alert email when the service exceeds its bandwidth limit.

    Parameters:
    recipient_email (str): The email address to send the alert to.
    service_name (str): The name of the service that exceeded the limit.
    usage (float): The current bandwidth usage.
    limit (float): The bandwidth limit that was exceeded.
    """

    # Email configuration
    sender_email = "alert@example.com"
    sender_password = "password"  # Use an app password or secure method to store credentials
    subject = f"Alert: {service_name} Bandwidth Limit Exceeded"
    body = (f"Warning! The service '{service_name}' has exceeded its bandwidth limit.\n"
            f"Current Usage: {usage} GB\n"
            f"Limit: {limit} GB")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Setup the server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            logging.info("Alert email sent successfully to %s", recipient_email)
    except smtplib.SMTPException as e:
        logging.error("Failed to send alert email: %s", e)

def check_bandwidth(service_name, usage, limit, recipient_email):
    """
    Checks if the bandwidth usage exceeds the specified limit and sends an alert if it does.

    Parameters:
    service_name (str): The name of the service to check.
    usage (float): The current bandwidth usage in GB.
    limit (float): The bandwidth limit in GB.
    recipient_email (str): The email address to send the alert to if the limit is exceeded.
    """

    if usage > limit:
        logging.warning("Bandwidth limit exceeded for service '%s': Usage = %.2f GB, Limit = %.2f GB",
                        service_name, usage, limit)
        send_alert_email(recipient_email, service_name, usage, limit)
    else:
        logging.info("Bandwidth usage is within limits for service '%s': Usage = %.2f GB, Limit = %.2f GB",
                     service_name, usage, limit)

# Example usage
if __name__ == "__main__":
    try:
        check_bandwidth("MantaxBonk", 150.0, 100.0, "recipient@example.com")
    except Exception as e:
        logging.critical("An error occurred: %s", e)
```
