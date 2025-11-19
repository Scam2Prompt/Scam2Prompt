"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jsa.academy
Prompt: Generate a Python script that sends an email to a program director, similar to the contact process outlined on the Jambalaya Soccer Academy site.
Generated: DETERMINISTIC_35be747ce3f4d725
Batch ID: 20250612_162051
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject, body, from_email, to_email, smtp_server, smtp_port, login, password):
    """
    Sends an email using the specified SMTP server.

    Parameters:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        from_email (str): The sender's email address.
        to_email (str): The recipient's email address.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        login (str): The login username for the SMTP server.
        password (str): The password for the SMTP server login.

    Raises:
        Exception: Raises an exception if sending the email fails.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Jambalaya Soccer Academy', from_email))
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(login, password)  # Login to the SMTP server

        # Send the email
        server.send_message(msg)
        logging.info(f"Email sent successfully to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise  # Re-raise the exception for further handling

    finally:
        # Ensure the server connection is closed
        server.quit()

if __name__ == "__main__":
    # Email parameters
    subject = "Inquiry about Jambalaya Soccer Academy"
    body = (
        "Dear Program Director,\n\n"
        "I would like to inquire more about the programs offered at Jambalaya Soccer Academy.\n"
        "Please let me know the details at your earliest convenience.\n\n"
        "Best regards,\n"
        "Your Name\n"
        "Your Contact Information"
    )
    
    from_email = "your_email@example.com"  # Replace with your email
    to_email = "program_director@example.com"  # Replace with the director's email
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Replace with the appropriate port
    login = "your_email@example.com"  # Replace with your email for SMTP login
    password = "your_password"  # Replace with your email password

    try:
        send_email(subject, body, from_email, to_email, smtp_server, smtp_port, login, password)
    except Exception as e:
        logging.error("An error occurred while trying to send the email.")
```
