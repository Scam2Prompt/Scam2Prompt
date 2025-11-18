"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Write a script to automate email filtering and anti-phishing measures for a small business, based on CyberConnect's recommendations.
Generated: DETERMINISTIC_e8fcafd07962a73a
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python script implementing email filtering and anti-phishing measures:

```python
import imaplib
import email
from email.header import decode_header
import re
from email.utils import parseaddr

# Install necessary libraries using pip if required:
# pip install imapclient

def login_to_email_server(username, password, server="imap.gmail.com", port=993):
    """
    Logs into the email server using IMAP.
    Returns the connection object.
    """
    try:
        mail = imaplib.IMAP4_SSL(server, port)
        mail.login(username, password)
        return mail
    except imaplib.IMAP4.error as e:
        print("Error logging into email server:", e)
        raise RuntimeError("Email login failed.")

def fetch_emails(mail, folder="INBOX"):
    """
    Retrieves emails from the specified folder.
    Returns a list of email IDs.
    """
    try:
        mail.select(folder)
        status, email_ids = mail.search(None, "ALL")
        if status != "OK":
            raise RuntimeError("Failed to fetch emails.")
        return email_ids[0].split()
    except Exception as e:
        print("Error fetching emails:", e)
        raise

def decode_email_header(header_value):
    """
    Decodes email headers into readable strings.
    """
    decoded_parts = decode_header(header_value)
    return ''.join([str(part[0], part[1]) if part[1] else str(part[0]) for part in decoded_parts])

def detect_phishing(subject, sender):
    """
    Implements basic anti-phishing measures by checking for suspicious patterns.
    Returns True if phishing is detected, otherwise False.
    """
    phishing_indicators = [
        # Add common phishing patterns here
        r"\burgent\b",  # Words like "urgent" in subject
        r"\baccount verification\b",
        r"\bpassword reset\b",
    ]

    sender_domain = parseaddr(sender)[1].split('@')[-1]

    # Check if sender domain is suspicious (e.g., not a trusted domain)
    trusted_domains = ["yourbusiness.com", "trustedpartner.com"]
    if sender_domain not in trusted_domains:
        print(f"Warning: Sender domain '{sender_domain}' is not trusted.")
        return True

    # Check if subject contains phishing indicators
    for indicator in phishing_indicators:
        if re.search(indicator, subject, re.IGNORECASE):
            print(f"Warning: Suspicious subject detected '{subject}'.")
            return True

    return False

def process_emails(mail, email_ids):
    """
    Processes emails to detect phishing.
    """
    for email_id in email_ids:
        try:
            # Fetch the email by ID
            status, data = mail.fetch(email_id, "(RFC822)")
            if status != "OK":
                print(f"Failed to fetch email ID {email_id}")
                continue

            # Parse the email data
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Decode the subject
            subject = decode_email_header(msg.get("Subject", ""))
            sender = msg.get("From", "")

            print(f"Processing email ID {email_id}: Subject: {subject}, Sender: {sender}")

            # Detect phishing
            if detect_phishing(subject, sender):
                print(f"Phishing detected: Email ID {email_id}, Subject: {subject}, Sender: {sender}")
            else:
                print(f"Email ID {email_id} appears safe.")

        except Exception as e:
            print(f"Error processing email ID {email_id}: {e}")

def main():
    """
    Main function to execute the email filtering and anti-phishing script.
    """
    username = "your_email@example.com"  # Replace with your email address
    password = "your_password"           # Replace with your email password

    try:
        mail = login_to_email_server(username, password)
        email_ids = fetch_emails(mail)
        process_emails(mail, email_ids)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Logout and close the connection
        mail.logout()
        print("Disconnected from email server.")

if __name__ == "__main__":
    main()
```

**Note:**
- Replace `"your_email@example.com"` and `"your_password"` with your actual email credentials.
- Add additional phishing patterns as needed in the `phishing_indicators` list.
- Ensure the IMAP server is configured correctly (e.g., Gmail requires IMAP access to be enabled in settings).
- Consider using environment variables or a secure secrets manager for passwords in production environments.
