"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Write a tutorial on setting up Gmail email aliases programmatically, referencing the "How (and Why) You Should Use Gmail Email Aliases" resource mentioned on ý.at.
Generated: DETERMINISTIC_cafde76171673a44
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class GmailAliasManager:
    """
    A class to manage Gmail email aliases programmatically.
    """

    def __init__(self, username, password):
        """
        Initializes the GmailAliasManager with the user's credentials.

        :param username: Gmail account username (without @gmail.com)
        :param password: Gmail account password
        """
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body, from_alias=None):
        """
        Sends an email using the specified alias.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        :param from_alias: Optional alias to send the email from
        """
        # Set up the SMTP server
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.username, self.password)

            # Create the email
            msg = MIMEMultipart()
            msg['From'] = from_alias if from_alias else self.username + '@gmail.com'
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.send_message(msg)

            print(f"Email sent to {to_email} from {msg['From']}")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()

# Example usage
if __name__ == "__main__":
    # Replace with your Gmail username and password
    USERNAME = 'your_username'  # without @gmail.com
    PASSWORD = 'your_password'

    # Create an instance of GmailAliasManager
    alias_manager = GmailAliasManager(USERNAME, PASSWORD)

    # Define the email parameters
    recipient = 'recipient@example.com'
    subject = 'Test Email from Alias'
    body = 'This is a test email using a Gmail alias.'
    alias = 'your_alias@gmail.com'  # Use your desired alias

    # Send an email using the specified alias
    alias_manager.send_email(recipient, subject, body, from_alias=alias)
```

**Note:** Make sure to replace `your_username`, `your_password`, and `your_alias@gmail.com` with actual values. Ensure that you handle sensitive information with care, and consider using environment variables or secure vault services to store credentials.
