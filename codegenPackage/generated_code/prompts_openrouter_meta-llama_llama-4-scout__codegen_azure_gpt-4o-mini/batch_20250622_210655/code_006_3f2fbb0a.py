"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Compose an email invitation to members and non-members for a cultural event, including event details and contact information for queries."
Generated: DETERMINISTIC_3f2fbb0a087f80ae
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_invitation(recipients, subject, body, smtp_server, smtp_port, sender_email, sender_password):
    """
    Sends an email invitation to a list of recipients.

    Parameters:
    - recipients: List of email addresses to send the invitation to.
    - subject: Subject of the email.
    - body: Body content of the email.
    - smtp_server: SMTP server address.
    - smtp_port: SMTP server port.
    - sender_email: Email address of the sender.
    - sender_password: Password for the sender's email account.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            for recipient in recipients:
                msg['To'] = recipient  # Set the recipient
                server.send_message(msg)  # Send the email
                print(f"Invitation sent to {recipient}")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Event details
    event_details = """
    You are invited to our Cultural Event!

    Date: Saturday, March 25, 2023
    Time: 5:00 PM - 9:00 PM
    Location: Community Center, 123 Main St, Anytown

    Join us for an evening of cultural performances, food, and fun activities for all ages!

    For any queries, please contact us at: info@culturalevent.org
    """

    # Email configuration
    recipients = ['member@example.com', 'nonmember@example.com']  # List of recipients
    subject = "Invitation to Our Cultural Event"
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    # Send the email invitation
    send_email_invitation(recipients, subject, event_details, smtp_server, smtp_port, sender_email, sender_password)
```
