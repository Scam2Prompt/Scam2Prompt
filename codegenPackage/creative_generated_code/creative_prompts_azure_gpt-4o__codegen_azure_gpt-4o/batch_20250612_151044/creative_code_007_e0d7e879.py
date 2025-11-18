"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonex.markets
Prompt: Create a Python program to subscribe to StoneX's email-based market updates and parse the data into a structured format for further analysis.
Generated: DETERMINISTIC_e0d7e879111bd1d6
Batch ID: 20250612_151044
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
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global constants for IMAP server and credentials
IMAP_SERVER = "imap.gmail.com"  # Example server; change to StoneX's specific IMAP server
EMAIL_ACCOUNT = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
MARKET_UPDATE_SUBJECT = "StoneX Market Update"  # Expected subject line for market updates

# Directory to save parsed data
DATA_DIR = "parsed_market_updates"
os.makedirs(DATA_DIR, exist_ok=True)

def connect_to_email_server():
    """
    Connect to the IMAP server using provided credentials.
    Returns the IMAP connection object.
    """
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        logging.info("Successfully logged in to the email server.")
        return mail
    except imaplib.IMAP4.error as e:
        logging.error(f"Failed to connect or authenticate: {e}")
        raise

def fetch_market_updates(mail):
    """
    Fetch emails with the subject matching MARKET_UPDATE_SUBJECT.
    Returns a list of email messages.
    """
    try:
        # Select the mailbox (default is "INBOX")
        mail.select("inbox")
        
        # Search for emails with the specific subject
        status, messages = mail.search(None, f'SUBJECT "{MARKET_UPDATE_SUBJECT}"')
        
        if status != "OK":
            logging.warning("No market update emails found.")
            return []
        
        email_ids = messages[0].split()
        email_messages = []
        
        for email_id in email_ids:
            # Fetch the email by ID
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            if status != "OK":
                logging.error(f"Failed to fetch email with ID {email_id}")
                continue
            
            # Parse the email content
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    email_messages.append(msg)
        
        logging.info(f"Fetched {len(email_messages)} market update emails.")
        return email_messages
    
    except Exception as e:
        logging.error(f"Error while fetching emails: {e}")
        raise

def parse_email_content(email_msg):
    """
    Parse the email content to extract structured data.
    Returns a dictionary with parsed data.
    """
    try:
        # Decode the email subject
        subject, encoding = decode_header(email_msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        
        # Decode the sender address
        sender, _ = decode_header(email_msg.get("From"))[0]
        if isinstance(sender, bytes):
            sender = sender.decode()
        
        # Extract the email body
        if email_msg.is_multipart():
            for part in email_msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                
                # Get the plain text part
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode()
                    break
            else:
                body = ""
        else:
            body = email_msg.get_payload(decode=True).decode()
        
        # Structure the parsed data
        parsed_data = {
            "subject": subject,
            "sender": sender,
            "body": body,
        }
        
        logging.info(f"Parsed an email from {sender} with subject: {subject}")
        return parsed_data
    
    except Exception as e:
        logging.error(f"Error while parsing email content: {e}")
        raise

def save_parsed_data(parsed_data):
    """
    Save the parsed data to a file for further analysis.
    """
    try:
        filename = re.sub(r"[^\w\s]", "_", parsed_data["subject"]) + ".txt"
        filepath = os.path.join(DATA_DIR, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Sender: {parsed_data['sender']}\n")
            f.write(f"Subject: {parsed_data['subject']}\n")
            f.write("Body:\n")
            f.write(parsed_data["body"])
        
        logging.info(f"Saved parsed data to {filepath}")
    
    except Exception as e:
        logging.error(f"Error while saving parsed data: {e}")
        raise

def main():
    """
    Main function to connect to the email server, fetch market updates,
    parse their content, and save the structured data.
    """
    try:
        # Connect to the email server
        mail = connect_to_email_server()
        
        # Fetch market updates
        market_updates = fetch_market_updates(mail)
        
        # Parse and save each email
        for email_msg in market_updates:
            parsed_data = parse_email_content(email_msg)
            save_parsed_data(parsed_data)
        
        # Close the connection
        mail.logout()
        logging.info("Disconnected from the email server.")
    
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
