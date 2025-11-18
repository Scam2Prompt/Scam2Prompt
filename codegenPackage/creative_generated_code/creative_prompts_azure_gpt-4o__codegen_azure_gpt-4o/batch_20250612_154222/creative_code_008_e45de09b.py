"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Develop a Python script to send emails with different priority levels (e.g., high, normal, low) and encoding types (e.g., base64, quoted-printable) as specified on the LuFix.to Sender v1.0 webpage.
Generated: DETERMINISTIC_e45de09b70840411
Batch ID: 20250612_154222
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
import base64

def send_email(smtp_server, port, sender_email, sender_name, recipient_email, subject, body, priority='normal', encoding='base64', password=None):
    """
    Sends an email with specified priority and encoding.

    Parameters:
        smtp_server (str): The SMTP server to use for sending the email.
        port (int): The port to use for the SMTP server.
        sender_email (str): The sender's email address.
        sender_name (str): The sender's name.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The main content of the email.
        priority (str): Priority level of the email ('high', 'normal', 'low'). Default is 'normal'.
        encoding (str): Encoding type ('base64', 'quoted-printable'). Default is 'base64'.
        password (str): Password for the sender's email account. Required if SMTP server needs authentication.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add priority header
        if priority == 'high':
            msg['X-Priority'] = '1'
        elif priority == 'normal':
            msg['X-Priority'] = '3'
        elif priority == 'low':
            msg['X-Priority'] = '5'
        else:
            raise ValueError("Invalid priority level. Use 'high', 'normal', or 'low'.")

        # Encode the message body
        if encoding == 'base64':
            encoded_body = base64.b64encode(body.encode('utf-8')).decode('utf-8')
            msg.attach(MIMEText(encoded_body, 'plain'))
        elif encoding == 'quoted-printable':
            from email.quoprimime import body_encode
            encoded_body = body_encode(body)
            msg.attach(MIMEText(encoded_body, 'plain'))
        else:
            raise ValueError("Invalid encoding type. Use 'base64' or 'quoted-printable'.")

        # Send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Enable encryption
            if password:  # Authenticate if password is provided
                server.login(sender_email, password)
            server.send_message(msg)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Replace with your actual data
    SMTP_SERVER = 'smtp.example.com'
    PORT = 587
    SENDER_EMAIL = 'sender@example.com'
    SENDER_NAME = 'Sender Name'
    RECIPIENT_EMAIL = 'recipient@example.com'
    SUBJECT = 'Test Email'
    BODY = 'This is a test email.'
    PRIORITY = 'high'
    ENCODING = 'base64'
    PASSWORD = 'yourpassword'

    send_email(SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_NAME, RECIPIENT_EMAIL, SUBJECT, BODY, PRIORITY, ENCODING, PASSWORD)
```
