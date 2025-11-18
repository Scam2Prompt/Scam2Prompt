"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://247signalfxtrade.com
Prompt: Write Python code to send automatic notifications for successful withdrawals, as described in the FAQ section of 247signalfxtrade.
Generated: DETERMINISTIC_2d63a8239337f0e8
Batch ID: 20250612_154542
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
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WithdrawalNotifier:
    def __init__(self, smtp_server, smtp_port, email_user, email_password):
        """
        Initialize the WithdrawalNotifier with SMTP server details.
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param email_user: Email address to send notifications from
        :param email_password: Password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_notification(self, recipient_email, withdrawal_amount):
        """
        Send a notification email for a successful withdrawal.
        :param recipient_email: Email address of the recipient
        :param withdrawal_amount: Amount withdrawn
        """
        try:
            # Create the email content
            subject = "Withdrawal Successful"
            body = (f"Dear User,\n\n"
                    f"We are pleased to inform you that your withdrawal of ${withdrawal_amount:.2f} was successful.\n"
                    f"Date of withdrawal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                    "Thank you for using our services!\n\n"
                    "Best regards,\n"
                    "247SignalfxTrade Team")
            
            # Prepare the email
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.email_user, self.email_password)
                server.send_message(msg)
                logging.info(f"Notification sent to {recipient_email} for withdrawal of ${withdrawal_amount:.2f}.")
        
        except Exception as e:
            logging.error(f"Failed to send notification: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    EMAIL_USER = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"

    # Create an instance of WithdrawalNotifier
    notifier = WithdrawalNotifier(SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD)

    # Example recipient and withdrawal amount
    recipient = "recipient@example.com"
    withdrawal_amount = 150.00

    # Send notification
    notifier.send_notification(recipient, withdrawal_amount)
```

Make sure to replace the SMTP server details and credentials with actual values before running the code.
