"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: Write code to send notifications to users about their rewards progress and airdrop claims on the "Claim USDT Box" platform.
Generated: DETERMINISTIC_d2e913650ee3fac2
Batch ID: 20250612_151329
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

class NotificationService:
    """
    Service for sending notifications to users about rewards progress and airdrop claims.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the NotificationService with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, subject, body):
        """
        Sends a notification email to the recipient.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body content of the email
        :raises Exception: If there is an error during email sending
        """
        try:
            # Create the email
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = subject

            # Attach the email body
            message.attach(MIMEText(body, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)  # Log in to the server
                server.sendmail(self.sender_email, recipient_email, message.as_string())  # Send the email

            print(f"Notification sent to {recipient_email} successfully.")

        except Exception as e:
            print(f"Failed to send notification to {recipient_email}: {str(e)}")
            raise  # Re-raise the exception for further handling

# Example usage
if __name__ == "__main__":
    # SMTP server configuration (Replace with actual details)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_password"

    # Initialize the notification service
    notification_service = NotificationService(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # User details (Replace with actual details)
    RECIPIENT_EMAIL = "recipient_email@gmail.com"
    SUBJECT = "Your Rewards Progress and Airdrop Claims"
    BODY = """
    Hello,

    This is a reminder to check your rewards progress and claim your USDT Box airdrop on the Claim USDT Box platform.

    Visit the platform now to claim your rewards and view your progress.

    Best regards,
    Claim USDT Box Team
    """

    # Send the notification
    notification_service.send_notification(RECIPIENT_EMAIL, SUBJECT, BODY)
```
