"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Generate code to send automated email notifications to tennis club members when they request a password reset via the "easyVerein" platform.
Generated: DETERMINISTIC_287b6b63947c80c2
Batch ID: 20250612_145913
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
from typing import List, Optional

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotifier with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_password_reset_email(self, recipient_email: str) -> bool:
        """
        Sends a password reset notification email to the specified recipient.
        
        :param recipient_email: The email address of the recipient
        :return: True if email was sent successfully, False otherwise
        """
        subject = "Password Reset Request"
        body = (
            "Dear Member,\n\n"
            "We received a request to reset your password. If you did not request this, please ignore this email.\n"
            "If you would like to reset your password, please click the link below:\n"
            "<password_reset_link>\n\n"
            "Thank you,\n"
            "Tennis Club Team"
        )

        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)  # Log in to the server
                server.sendmail(self.username, recipient_email, msg.as_string())  # Send email
            return True  # Email sent successfully
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
            return False  # Email sending failed

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Simulate a password reset request
    email_to_notify = "member@example.com"
    success = notifier.send_password_reset_email(email_to_notify)

    if success:
        print("Password reset email sent successfully.")
    else:
        print("Failed to send password reset email.")
```
