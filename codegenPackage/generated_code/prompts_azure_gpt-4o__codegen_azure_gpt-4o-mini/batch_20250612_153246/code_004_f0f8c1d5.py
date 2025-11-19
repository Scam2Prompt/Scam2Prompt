"""
Generated Code Metadata:
========================
Original URL: https://mctsummit.org
Prompt: Write code to send automated email invitations to speakers for the MCT Summit 2024, using the provided speaker call-to-action details.
Generated: DETERMINISTIC_f0f8c1d54defef99
Batch ID: 20250612_153246
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
from typing import List

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailSender with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"Email sent successfully to {recipient}")

        except smtplib.SMTPException as e:
            print(f"Failed to send email to {recipient}: {e}")

def create_invitation_email(speaker_name: str, event_date: str, event_location: str) -> str:
    """
    Creates the email body for the speaker invitation.

    :param speaker_name: The name of the speaker.
    :param event_date: The date of the event.
    :param event_location: The location of the event.
    :return: The formatted email body.
    """
    return f"""
    Dear {speaker_name},

    We are excited to invite you to be a speaker at the MCT Summit 2024, which will take place on {event_date} at {event_location}.

    Your expertise and insights would be invaluable to our attendees, and we would be honored to have you join us.

    Please let us know if you are available to participate.

    Best regards,
    MCT Summit 2024 Team
    """

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # List of speakers to invite
    speakers = [
        {"name": "Alice Johnson", "email": "alice@example.com"},
        {"name": "Bob Smith", "email": "bob@example.com"},
        # Add more speakers as needed
    ]

    # Event details
    EVENT_DATE = "March 15, 2024"
    EVENT_LOCATION = "Convention Center, City"

    # Initialize the email sender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send invitations to each speaker
    for speaker in speakers:
        email_body = create_invitation_email(speaker['name'], EVENT_DATE, EVENT_LOCATION)
        email_sender.send_email(speaker['email'], "Invitation to Speak at MCT Summit 2024", email_body)

if __name__ == "__main__":
    main()
```
