"""
Generated Code Metadata:
========================
Original URL: https://www.optimism.rs
Prompt: Create a script to send an automated email inquiry to info@domainnames.rs about purchasing a domain, using the example domains listed on optimism.rs.
Generated: DETERMINISTIC_508eebdb46fbf5a2
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

# Function to send an email inquiry
def send_email(subject: str, body: str, to_email: str, from_email: str, smtp_server: str, smtp_port: int, password: str) -> None:
    """
    Sends an email using the specified SMTP server.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param to_email: Recipient's email address
    :param from_email: Sender's email address
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param password: Password for the sender's email account
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(from_email, password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Email configuration
    SMTP_SERVER = 'smtp.your-email-provider.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    FROM_EMAIL = 'your-email@example.com'  # Replace with your email
    PASSWORD = 'your-email-password'  # Replace with your email password
    TO_EMAIL = 'info@domainnames.rs'  # Recipient's email address

    # Example domains to inquire about
    example_domains: List[str] = [
        'example1.optimism.rs',
        'example2.optimism.rs',
        'example3.optimism.rs'
    ]

    # Create the email subject and body
    subject = "Inquiry about Domain Purchase"
    body = "Hello,\n\nI would like to inquire about purchasing the following domains:\n" + "\n".join(example_domains) + "\n\nThank you!"

    # Send the email
    send_email(subject, body, TO_EMAIL, FROM_EMAIL, SMTP_SERVER, SMTP_PORT, PASSWORD)
```
