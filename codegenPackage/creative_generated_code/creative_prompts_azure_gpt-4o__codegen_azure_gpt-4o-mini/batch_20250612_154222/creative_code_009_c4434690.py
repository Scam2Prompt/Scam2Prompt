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

def generate_random_number(min_val=0, max_val=100):
    """Generates a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)

def generate_random_letter():
    """Generates a random uppercase letter."""
    return random.choice(string.ascii_uppercase)

def generate_md5_hash(input_string):
    """Generates an MD5 hash for the given input string."""
    return hashlib.md5(input_string.encode()).hexdigest()

def create_email_message(to_email, subject, body):
    """Creates an email message with the given parameters."""
    message = MIMEMultipart()
    message['From'] = 'sender@example.com'
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    return message

def send_email(server, port, username, password, message):
    """Sends an email using the specified SMTP server settings."""
    try:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls()  # Upgrade to secure connection
            smtp.login(username, password)
            smtp.send_message(message)
            print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

def main():
    """Main function to generate random data and send an email."""
    # Generate random number, letter, and MD5 hash
    random_number = generate_random_number()
    random_letter = generate_random_letter()
    md5_hash = generate_md5_hash(f"{random_number}{random_letter}")

    # Create email content
    subject = "Your Random Data"
    body = (f"Random Number: {random_number}\n"
            f"Random Letter: {random_letter}\n"
            f"MD5 Hash: {md5_hash}")

    # Set up email details
    to_email = "recipient@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_username"
    smtp_password = "your_password"

    # Create the email message
    email_message = create_email_message(to_email, subject, body)

    # Send the email
    send_email(smtp_server, smtp_port, smtp_username, smtp_password, email_message)

if __name__ == "__main__":
    main()
```
