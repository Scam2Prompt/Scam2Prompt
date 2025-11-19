"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Generate a sample code for automating the process of sending enquiries for spares and consumables to Aayra International Limited using their contact information.
Generated: DETERMINISTIC_ef4c1ad6fd4ddf53
Batch ID: 20250622_210650
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

def send_enquiry(to_email, subject, body, from_email, smtp_server, smtp_port, login, password):
    """
    Sends an enquiry email to the specified recipient.

    Parameters:
    to_email (str): Recipient's email address.
    subject (str): Subject of the email.
    body (str): Body of the email.
    from_email (str): Sender's email address.
    smtp_server (str): SMTP server address.
    smtp_port (int): SMTP server port.
    login (str): Login username for the SMTP server.
    password (str): Password for the SMTP server.

    Returns:
    None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)  # Log in to the server
            server.send_message(message)  # Send the email
            print(f"Enquiry email sent successfully to {to_email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Configuration for sending the email
to_email = "contact@aayrainternational.com"  # Aayra International Limited's contact email
subject = "Enquiry for Spares and Consumables"
body = """
Dear Aayra International Limited,

I am writing to inquire about the availability and pricing of spares and consumables. 
Please provide detailed information regarding the products you offer, including catalogs, pricing, and delivery options.

Looking forward to your response.

Best regards,
[Your Name]
[Your Contact Information]
"""
from_email = "your_email@example.com"  # Replace with your email address
smtp_server = "smtp.example.com"  # Replace with your SMTP server
smtp_port = 587  # Common SMTP port for TLS
login = "your_email@example.com"  # Replace with your email login
password = "your_password"  # Replace with your email password

# Send the enquiry email
send_enquiry(to_email, subject, body, from_email, smtp_server, smtp_port, login, password)
```
