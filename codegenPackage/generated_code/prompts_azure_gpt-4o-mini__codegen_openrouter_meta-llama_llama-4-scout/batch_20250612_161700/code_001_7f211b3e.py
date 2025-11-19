"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: Write a Python script that automates sending thank-you emails to donors of a charity organization, inspired by the gratitude expressed by Amma Parivaar Orphanage.
Generated: DETERMINISTIC_7f211b3ee87ef491
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import getpass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_thank_you_email(subject, message, from_addr, to_addr, password, smtp_server, smtp_port):
    """
    Send a thank-you email to a donor.

    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.
        smtp_server (str): The SMTP server to use.
        smtp_port (int): The SMTP port to use.

    Returns:
        None
    """

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Set up the SMTP server
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            # Log in to the SMTP server
            server.login(from_addr, password)

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Subject'] = subject

            # Attach the message to the email
            msg.attach(MIMEText(message, 'plain'))

            # Send the email
            server.sendmail(from_addr, to_addr, msg.as_string())

            logging.info(f"Email sent to {to_addr}")

    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to log in to the SMTP server. Check your email and password.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Get user input
    from_addr = input("Enter the sender's email address: ")
    password = getpass.getpass("Enter the sender's email password: ")
    smtp_server = input("Enter the SMTP server: ")
    smtp_port = int(input("Enter the SMTP port: "))

    # Define the email subject and message
    subject = "Thank You for Your Donation"
    message = """
Dear valued donor,

We at Amma Parivaar Orphanage would like to extend our heartfelt gratitude for your generous donation.
Your support will help us provide a better life for the children in our care.

Thank you for your kindness and compassion.

Best regards,
Amma Parivaar Orphanage
"""

    # Define the recipient's email address
    donors = [
        "donor1@example.com",
        "donor2@example.com",
        # Add more donors here
    ]

    # Send emails to donors
    for donor in donors:
        send_thank_you_email(subject, message, from_addr, donor, password, smtp_server, smtp_port)

if __name__ == "__main__":
    main()
```
