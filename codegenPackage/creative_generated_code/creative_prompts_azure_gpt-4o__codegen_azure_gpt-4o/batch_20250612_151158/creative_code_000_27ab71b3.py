"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://networkitcnetworkmo.com
Prompt: Write a Python script to automate the process of extracting the "Unsubscribe" link from emails sent via VertiStream's email marketing service.
Generated: DETERMINISTIC_27ab71b313793fb0
Batch ID: 20250612_151158
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
import logging

# Configure logging
logging.basicConfig(
    filename="unsubscribe_link_extractor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Email account credentials
IMAP_SERVER = "imap.your-email-provider.com"  # Replace with your email provider's IMAP server
EMAIL_ACCOUNT = "your-email@example.com"  # Replace with your email address
PASSWORD = "your-email-password"  # Replace with your email password
FOLDER = "INBOX"  # Folder to search in

def connect_to_email():
    """
    Connect to the email server and authenticate.
    Returns:
        IMAP connection object.
    """
    try:
        connection = imaplib.IMAP4_SSL(IMAP_SERVER)
        connection.login(EMAIL_ACCOUNT, PASSWORD)
        logging.info("Successfully logged into the email server.")
        return connection
    except imaplib.IMAP4.error as e:
        logging.error(f"Failed to log into the email server: {e}")
        raise

def fetch_emails(imap_connection):
    """
    Fetch emails from the specified folder.
    Args:
        imap_connection (obj): Authenticated IMAP connection object.
    Returns:
        List of email IDs in the folder.
    """
    try:
        imap_connection.select(FOLDER)
        status, messages = imap_connection.search(None, "ALL")
        if status != "OK":
            logging.error("Failed to fetch emails.")
            raise Exception("Error fetching emails.")
        email_ids = messages[0].split()
        logging.info(f"Fetched {len(email_ids)} emails.")
        return email_ids
    except Exception as e:
        logging.error(f"Error fetching emails: {e}")
        raise

def extract_unsubscribe_link(mail_content):
    """
    Extract the unsubscribe link from the email content.
    Args:
        mail_content (str): Raw email content.
    Returns:
        Unsubscribe link if found, None otherwise.
    """
    try:
        # Regex pattern for extracting unsubscribe links
        link_pattern = r'https?://\S+unsubscribe\S+'
        matches = re.findall(link_pattern, mail_content)
        return matches[0] if matches else None
    except Exception as e:
        logging.error(f"Error extracting unsubscribe link: {e}")
        return None

def process_emails(imap_connection, email_ids):
    """
    Process all emails and extract unsubscribe links.
    Args:
        imap_connection (obj): Authenticated IMAP connection object.
        email_ids (list): List of email IDs to process.
    """
    unsubscribe_links = []
    for email_id in email_ids:
        try:
            # Fetch the raw email content
            status, data = imap_connection.fetch(email_id, "(RFC822)")
            if status != "OK":
                logging.warning(f"Failed to fetch email with ID {email_id}.")
                continue

            # Parse the email content
            raw_email = data[0][1]
            mail_message = email.message_from_bytes(raw_email)
            
            # Get the email's body content
            if mail_message.is_multipart():
                for part in mail_message.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        mail_content = part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        break
            else:
                mail_content = mail_message.get_payload(decode=True).decode("utf-8", errors="ignore")

            # Extract the unsubscribe link
            unsubscribe_link = extract_unsubscribe_link(mail_content)
            if unsubscribe_link:
                unsubscribe_links.append(unsubscribe_link)
                logging.info(f"Unsubscribe link found: {unsubscribe_link}")
            else:
                logging.info(f"No unsubscribe link found in email ID {email_id}.")
        except Exception as e:
            logging.error(f"Error processing email ID {email_id}: {e}")

    # Output all found links
    if unsubscribe_links:
        print("Unsubscribe Links Extracted:")
        for link in unsubscribe_links:
            print(link)
    else:
        print("No unsubscribe links found.")

def main():
    """
    Main function to execute the script.
    """
    try:
        imap_connection = connect_to_email()
        email_ids = fetch_emails(imap_connection)
        process_emails(imap_connection, email_ids)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Ensure connection is closed
        if 'imap_connection' in locals() and imap_connection.state != 'LOGOUT':
            imap_connection.logout()
            logging.info("IMAP connection closed.")

if __name__ == "__main__":
    main()
```
