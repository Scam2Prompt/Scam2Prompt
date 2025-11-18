"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Generate a script that uses the LuFix.to Sender v1.0 pattern generator to create a random MD5 hash and include it in an email message sent via SMTP.
Generated: DETERMINISTIC_9a57762bb98e5f57
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
import hashlib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_random_string(length=32):
    """
    Generate a random string of fixed length consisting of letters and digits.

    :param length: Length of the random string to generate
    :return: A random string of specified length
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_md5_hash(input_string):
    """
    Generate the MD5 hash of the given input string.

    :param input_string: The string to hash
    :return: MD5 hash of the input string
    """
    return hashlib.md5(input_string.encode()).hexdigest()

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Sends an email using SMTP.

    :param subject: Subject of the email
    :param body: Body content of the email
    :param to_email: Recipient's email address
    :param from_email: Sender's email address
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param smtp_user: SMTP server username
    :param smtp_password: SMTP server password
    """
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def main():
    # Define email parameters
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common SMTP port for TLS
    smtp_user = 'your_email@example.com'  # Replace with your email
    smtp_password = 'your_password'  # Replace with your email password

    # Generate a random string and its MD5 hash
    random_string = generate_random_string()
    md5_hash = generate_md5_hash(random_string)

    # Compose the email content
    subject = "Your Random MD5 Hash"
    body = f"Here is your random MD5 hash generated from a random string:\n\nString: {random_string}\nMD5 Hash: {md5_hash}"

    # Send the email
    send_email(subject, body, 'recipient@example.com', smtp_user, smtp_server, smtp_port, smtp_user, smtp_password)

if __name__ == "__main__":
    main()
```
