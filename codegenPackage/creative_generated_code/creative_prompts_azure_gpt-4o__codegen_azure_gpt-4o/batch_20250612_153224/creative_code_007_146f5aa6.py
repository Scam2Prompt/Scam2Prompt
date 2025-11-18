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

# Constants
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "felipemi.f@gmail.com"
PASSWORD = "your_password"  # Replace with your actual password
CATEGORY_KEYWORDS = {
    "plumbing": ["pipe", "leak", "water", "clog"],
    "electrical work": ["electric", "wire", "power", "outlet"],
    "appliance repair": ["appliance", "fridge", "washer", "dryer"]
}

def connect_to_email_server(imap_server, email_account, password):
    """
    Connect to the email server and return the IMAP connection object.
    """
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_account, password)
        return mail
    except Exception as e:
        print(f"Error connecting to email server: {e}")
        return None

def fetch_emails(mail):
    """
    Fetch emails from the inbox folder.
    """
    try:
        mail.select("inbox")
        status, messages = mail.search(None, "ALL")
        if status != "OK":
            print("Error fetching emails.")
            return []
        
        # Get the list of email IDs
        email_ids = messages[0].split()
        return email_ids
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []

def parse_email(mail, email_id):
    """
    Parse an individual email and extract content.
    """
    try:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        if status != "OK":
            print(f"Error fetching email ID {email_id}")
            return None
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                
                # Extract email body
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            return subject, body
                else:
                    body = msg.get_payload(decode=True).decode()
                    return subject, body
        return None
    except Exception as e:
        print(f"Error parsing email ID {email_id}: {e}")
        return None

def categorize_inquiry(subject, body):
    """
    Categorize an email inquiry based on keywords.
    """
    content = (subject + " " + body).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", content):
                return category
    return "uncategorized"

def main():
    # Connect to email server
    mail = connect_to_email_server(IMAP_SERVER, EMAIL_ACCOUNT, PASSWORD)
    if not mail:
        return
    
    # Fetch emails
    email_ids = fetch_emails(mail)
    if not email_ids:
        print("No emails found.")
        return
    
    print("Categorizing customer inquiries:")
    for email_id in email_ids:
        parsed_email = parse_email(mail, email_id)
        if parsed_email:
            subject, body = parsed_email
            category = categorize_inquiry(subject, body)
            print(f"Subject: {subject}")
            print(f"Category: {category}")
            print("-" * 40)
    
    # Close the connection
    mail.logout()

if __name__ == "__main__":
    main()
```
