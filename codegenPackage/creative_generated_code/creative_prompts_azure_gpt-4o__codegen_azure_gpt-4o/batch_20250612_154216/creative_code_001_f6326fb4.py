"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cira.com.fj
Prompt: Generate a script to automate email requests to customercare@cira.com.fj for obtaining personal credit files, including handling responses and parsing credit report data.
Generated: DETERMINISTIC_f6326fb43946de32
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import imaplib
import email
import re
import os

# Configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
IMAP_SERVER = 'imap.example.com'  # Replace with your IMAP server
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'          # Replace with your email password
CUSTOMER_CARE_EMAIL = 'customercare@cira.com.fj'

def send_email_request():
    """
    Sends an email request to customer care for obtaining personal credit files.
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = 'Request for Personal Credit File'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = CUSTOMER_CARE_EMAIL
        msg.set_content("""
        Dear Customer Care,

        I am writing to request a copy of my personal credit file. Please let me know if you require any additional information to process this request.

        Thank you,
        [Your Name]
        """)

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, 587) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email request sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def fetch_email_responses():
    """
    Connects to the email server and fetches responses from customer care.
    Parses the credit report data from the response emails.
    """
    try:
        # Connect to the IMAP server
        with imaplib.IMAP4_SSL(IMAP_SERVER) as imap:
            imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            imap.select('inbox')  # Select the inbox folder

            # Search for emails from customer care
            status, messages = imap.search(None, f'FROM "{CUSTOMER_CARE_EMAIL}"')
            if status != 'OK':
                print("No messages found.")
                return

            # Process each email
            for num in messages[0].split():
                status, data = imap.fetch(num, '(RFC822)')
                if status != 'OK':
                    print(f"Failed to fetch email ID {num}.")
                    continue

                # Parse the email content
                raw_email = data[0][1]
                msg = email.message_from_bytes(raw_email)

                # Extract the body content
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True).decode()
                            parse_credit_report(body)
                else:
                    body = msg.get_payload(decode=True).decode()
                    parse_credit_report(body)

            print("Finished processing all responses.")
    except Exception as e:
        print(f"Error fetching emails: {e}")

def parse_credit_report(email_body):
    """
    Parses credit report data from the email body content.
    """
    try:
        # Example: Extract numeric credit score using regex
        credit_score_pattern = r"Credit Score: (\d+)"
        match = re.search(credit_score_pattern, email_body)
        if match:
            credit_score = match.group(1)
            print(f"Credit Score: {credit_score}")
        else:
            print("No credit score found in the email.")
    except Exception as e:
        print(f"Error parsing credit report: {e}")

if __name__ == "__main__":
    # Automate the email request and response handling
    send_email_request()
    fetch_email_responses()
```

**Note:** Replace placeholders (`SMTP_SERVER`, `IMAP_SERVER`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD`) with actual values. Ensure that sensitive data (like passwords) are stored securely using environment variables or secure vaults in production environments.
