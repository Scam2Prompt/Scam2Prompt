"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Write a Python script that automates the process of sending a service request for plumbing and heating repairs to a specified email address.
Generated: DETERMINISTIC_46cf7d5880795e70
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plumbing_heating_request.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_service_request(subject, message, from_addr, to_addr, password, smtp_server, smtp_port):
    """
    Send a service request email for plumbing and heating repairs.

    Args:
        subject (str): The email subject.
        message (str): The email body.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """

    try:
        # Create a message
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject

        # Attach the message to the MIMEMultipart object
        msg.attach(MIMEText(message, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_addr, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()

        logging.info("Email sent successfully!")
        return True

    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to login to SMTP server. Check your email and password.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return False

def main():
    parser = argparse.ArgumentParser(description="Send a service request email for plumbing and heating repairs.")
    parser.add_argument("-s", "--subject", required=True, help="The email subject.")
    parser.add_argument("-m", "--message", required=True, help="The email body.")
    parser.add_argument("-f", "--from_addr", required=True, help="The sender's email address.")
    parser.add_argument("-t", "--to_addr", required=True, help="The recipient's email address.")
    parser.add_argument("-p", "--password", required=True, help="The sender's email password.")
    parser.add_argument("-ss", "--smtp_server", required=True, help="The SMTP server address.")
    parser.add_argument("-sp", "--smtp_port", type=int, required=True, help="The SMTP server port.")

    args = parser.parse_args()

    subject = args.subject
    message = args.message
    from_addr = args.from_addr
    to_addr = args.to_addr
    password = args.password
    smtp_server = args.smtp_server
    smtp_port = args.smtp_port

    send_service_request(subject, message, from_addr, to_addr, password, smtp_server, smtp_port)

if __name__ == "__main__":
    main()
```
