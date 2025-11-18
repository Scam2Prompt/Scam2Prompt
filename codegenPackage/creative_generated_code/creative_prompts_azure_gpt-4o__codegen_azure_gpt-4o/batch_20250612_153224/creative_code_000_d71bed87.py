"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write a Python script to send automated email notifications to customers about reverse osmosis system maintenance schedules, using the email address provided on the webpage (`felipemi.f@gmail.com`).
Generated: DETERMINISTIC_d71bed873b50197c
Batch ID: 20250612_153224
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
from email.utils import formataddr
import traceback

# Configuration for the email server
SMTP_SERVER = "smtp.gmail.com"  # Use Gmail's SMTP server
SMTP_PORT = 587                 # Port for TLS
SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
SENDER_NAME = "Maintenance Notifications"
SENDER_PASSWORD = "your_password"      # Replace with your email password or app-specific password

# Customer email address (retrieved from the webpage)
CUSTOMER_EMAIL = "felipemi.f@gmail.com"

def send_email_notification():
    """
    Sends an automated email notifying customers about reverse osmosis system maintenance schedules.
    """
    try:
        # Create the email content
        subject = "Reverse Osmosis System Maintenance Schedule"
        body = """
        Dear Customer,

        This is a friendly reminder regarding the maintenance schedule for your reverse osmosis system.

        Please ensure the system is serviced every 6 months to ensure optimal performance and water quality.
        If you have any questions, feel free to contact us.

        Best regards,
        Your Maintenance Team
        """

        # Create MIME message
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = CUSTOMER_EMAIL
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to secure encrypted TLS
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Send the email
        server.sendmail(SENDER_EMAIL, CUSTOMER_EMAIL, msg.as_string())
        print("Email sent successfully!")

        # Close the connection
        server.quit()

    except Exception as e:
        # Handle exceptions and print details for debugging
        print("An error occurred while trying to send the email.")
        print(traceback.format_exc())

if __name__ == "__main__":
    send_email_notification()
```

**Note**: Ensure you replace `your_email@gmail.com` and `your_password` with your actual email credentials. For security purposes, consider using environment variables or a secure credentials manager to store sensitive data like email passwords. Additionally, if using Gmail, enable "Less secure app access" or generate an app-specific password.
