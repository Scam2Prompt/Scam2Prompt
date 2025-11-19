"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-chiliz.net
Prompt: How can I leverage Microsoft 365 Copilot's AI capabilities to automate tasks in Outlook for better email management?
Generated: DETERMINISTIC_442a2d69bc2bbac6
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import win32com.client
import logging

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OutlookEmailManager:
    def __init__(self):
        """Initializes the Outlook application and connects to the inbox."""
        try:
            self.outlook = win32com.client.Dispatch('Outlook.Application')
            self.namespace = self.outlook.GetNamespace('MAPI')
            self.inbox = self.namespace.GetDefaultFolder(6)  # 6 refers to the inbox folder
            logging.info("Connected to Outlook inbox successfully.")
        except Exception as e:
            logging.error("Failed to connect to Outlook: %s", e)
            raise

    def get_unread_emails(self):
        """Retrieves all unread emails from the inbox."""
        try:
            unread_emails = self.inbox.Items.Restrict("[Unread]=True")
            logging.info("Retrieved %d unread emails.", len(unread_emails))
            return unread_emails
        except Exception as e:
            logging.error("Failed to retrieve unread emails: %s", e)
            raise

    def mark_email_as_read(self, email):
        """Marks an email as read."""
        try:
            email.UnRead = False
            email.Save()
            logging.info("Marked email as read: %s", email.Subject)
        except Exception as e:
            logging.error("Failed to mark email as read: %s", e)

    def auto_reply_to_unread_emails(self):
        """Automatically replies to unread emails with a predefined message."""
        unread_emails = self.get_unread_emails()
        for email in unread_emails:
            try:
                self.mark_email_as_read(email)
                reply = email.Reply()
                reply.Body = "Thank you for your email. I will get back to you soon."
                reply.Send()
                logging.info("Sent auto-reply to: %s", email.Subject)
            except Exception as e:
                logging.error("Error processing email '%s': %s", email.Subject, e)

if __name__ == "__main__":
    try:
        email_manager = OutlookEmailManager()
        email_manager.auto_reply_to_unread_emails()
    except Exception as e:
        logging.critical("An error occurred in the email manager: %s", e)
```
