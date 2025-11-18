"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Generate code to send an automated email notification when a hosting package is activated.
Generated: DETERMINISTIC_87040fcc9d41e7fc
Batch ID: 20250612_154703
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

def send_email_notification(recipient_email, recipient_name, hosting_package_name):
    """
    Sends an automated email notification when a hosting package is activated.

    Args:
        recipient_email (str): The email address of the recipient.
        recipient_name (str): Name of the recipient.
        hosting_package_name (str): Name of the hosting package that was activated.

    Returns:
        None
    """
    try:
        # Email server configuration
        smtp_server = "smtp.gmail.com"  # Change to your SMTP server
        smtp_port = 587  # Typically 587 for TLS or 465 for SSL
        sender_email = "your_email@example.com"  # Replace with your email
        sender_password = "your_password"  # Replace with your email password or app-specific password

        # Email content setup
        subject = f"Hosting Package Activation: {hosting_package_name}"
        body = f"""
        Dear {recipient_name},

        Your hosting package "{hosting_package_name}" has been successfully activated.
        You can now start using your hosting services.

        If you have any questions, feel free to contact our support team.

        Best regards,
        Hosting Company Team
        """

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        logging.info("Connecting to the SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
        server.login(sender_email, sender_password)
        logging.info("Successfully authenticated with the SMTP server.")
        server.sendmail(sender_email, recipient_email, msg.as_string())
        logging.info(f"Email sent successfully to {recipient_email}.")
        server.quit()

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual recipient details
    recipient_email = "recipient_email@example.com"
    recipient_name = "John Doe"
    hosting_package_name = "Premium Hosting Plan"

    send_email_notification(recipient_email, recipient_name, hosting_package_name)
```

> **Note:** Replace `your_email@example.com` and `your_password` with appropriate values for sender credentials. If using Gmail, you may need to enable "Allow less secure apps" or use an app-specific password for better security.
