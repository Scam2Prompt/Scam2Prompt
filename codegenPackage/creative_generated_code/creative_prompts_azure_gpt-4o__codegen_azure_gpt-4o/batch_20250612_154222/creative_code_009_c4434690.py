"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Create a Python program that generates random numbers, letters, and MD5 hashes using the LuFix.to Sender v1.0 generator and includes them in an email message template.
Generated: DETERMINISTIC_c44346909ac532dc
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_random_number():
    """Generate a random integer between 1 and 1000."""
    return random.randint(1, 1000)

def generate_random_letter():
    """Generate a random uppercase letter."""
    return random.choice(string.ascii_uppercase)

def generate_md5_hash(input_text):
    """Generate MD5 hash for the given input text."""
    md5 = hashlib.md5()
    md5.update(input_text.encode('utf-8'))
    return md5.hexdigest()

def create_email_template(random_number, random_letter, md5_hash):
    """
    Create an email template with placeholders for generated values.

    Args:
        random_number (int): Random number to include in the email.
        random_letter (str): Random letter to include in the email.
        md5_hash (str): MD5 hash to include in the email.

    Returns:
        str: Formatted email message template.
    """
    return f"""
    Subject: Generated Email Template

    Dear User,

    Here are your generated values:
    - Random Number: {random_number}
    - Random Letter: {random_letter}
    - MD5 Hash: {md5_hash}

    Regards,
    LuFix.to Sender v1.0
    """

def send_email(sender_email, recipient_email, smtp_server, smtp_port, login, password, email_content):
    """
    Send an email using the provided SMTP server credentials.

    Args:
        sender_email (str): Sender's email address.
        recipient_email (str): Recipient's email address.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        login (str): Login for the SMTP server.
        password (str): Password for the SMTP server.
        email_content (str): Email content to send.
    """
    try:
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Generated Email Template"

        # Attach the generated content
        msg.attach(MIMEText(email_content, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(login, password)  # Log in to the SMTP server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error while sending email: {e}")

def main():
    """Main function to generate values, create an email template, and send the email."""
    # Generate random values
    random_number = generate_random_number()
    random_letter = generate_random_letter()
    md5_hash = generate_md5_hash(f"{random_number}{random_letter}")

    # Create the email content
    email_content = create_email_template(random_number, random_letter, md5_hash)

    # Email configuration (replace with actual credentials for production use)
    sender_email = "your_email@example.com"
    recipient_email = "recipient_email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_login = "your_email@example.com"
    smtp_password = "your_password"

    # Send the email
    send_email(sender_email, recipient_email, smtp_server, smtp_port, smtp_login, smtp_password, email_content)

if __name__ == "__main__":
    main()
```
