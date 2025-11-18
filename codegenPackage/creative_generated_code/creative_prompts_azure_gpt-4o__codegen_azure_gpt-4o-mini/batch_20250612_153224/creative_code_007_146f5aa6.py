"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Generate Python code to parse customer inquiries from an email inbox (e.g., `felipemi.f@gmail.com`) and categorize them into service types like plumbing, electrical work, or appliance repair.
Generated: DETERMINISTIC_146f5aa6fb146117
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import imaplib
import email
from email.header import decode_header
import re
from collections import defaultdict

# Define constants for email credentials and service categories
EMAIL_ACCOUNT = 'felipemi.f@gmail.com'
EMAIL_PASSWORD = 'your_password_here'  # Use environment variables for sensitive data
SERVICE_CATEGORIES = {
    'plumbing': r'\bplumb(ing|er)?\b',
    'electrical': r'\belectr(ical|ician)?\b',
    'appliance repair': r'\bappliance(s)? repair\b',
}

def connect_to_email(account, password):
    """Connect to the email server and log in to the account."""
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(account, password)
        return mail
    except imaplib.IMAP4.error as e:
        print(f"Failed to connect to email: {e}")
        raise

def fetch_emails(mail):
    """Fetch unread emails from the inbox."""
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    email_ids = data[0].split()
    emails = []
    
    for email_id in email_ids:
        result, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        emails.append(msg)
    
    return emails

def decode_email_subject(subject):
    """Decode the email subject into a readable format."""
    decoded_subject = decode_header(subject)
    subject_parts = []
    
    for part, encoding in decoded_subject:
        if isinstance(part, bytes):
            part = part.decode(encoding if encoding else 'utf-8')
        subject_parts.append(part)
    
    return ''.join(subject_parts)

def categorize_inquiry(content):
    """Categorize the email inquiry based on predefined service categories."""
    categories = defaultdict(list)
    
    for service, pattern in SERVICE_CATEGORIES.items():
        if re.search(pattern, content, re.IGNORECASE):
            categories[service].append(content)
    
    return categories

def main():
    """Main function to parse customer inquiries from the email inbox."""
    try:
        mail = connect_to_email(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        emails = fetch_emails(mail)

        for msg in emails:
            subject = decode_email_subject(msg['Subject'])
            content = msg.get_payload(decode=True).decode('utf-8') if msg.is_multipart() else msg.get_payload()
            categories = categorize_inquiry(content)

            if categories:
                print(f"Email Subject: {subject}")
                for service, inquiries in categories.items():
                    print(f"Categorized under '{service}':")
                    for inquiry in inquiries:
                        print(f"- {inquiry}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mail.logout()

if __name__ == "__main__":
    main()
```
