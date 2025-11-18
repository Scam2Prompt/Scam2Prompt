"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptominnerfx.com
Prompt: Develop a script to automate notifications for successful withdrawals, similar to the notification system described on Cryptominnerfx.
Generated: DETERMINISTIC_b8442b6d1714c6bc
Batch ID: 20250612_150135
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WithdrawalNotifier:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the WithdrawalNotifier with SMTP server details.

        Parameters:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port.
            sender_email (str): The email address used to send notifications.
            sender_password (str): The password for the sender's email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, amount, transaction_id):
        """
        Sends a notification email for a successful withdrawal.

        Parameters:
            recipient_email (str): The email address to send the notification to.
            amount (float): The amount withdrawn.
            transaction_id (str): The unique identifier for the transaction.
        """
        subject = "Withdrawal Successful"
        body = (f"Dear User,\n\n"
                f"Your withdrawal of ${amount:.2f} has been processed successfully.\n"
                f"Transaction ID: {transaction_id}\n"
                f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                "Thank you for using our service!\n"
                "Best regards,\nCryptominnerfx Team")

        # Create MIMEText object
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.sender_email, self.sender_password)  # Login to the email account
                server.sendmail(self.sender_email, recipient_email, msg.as_string())  # Send email
                logging.info(f"Notification sent to {recipient_email} for transaction {transaction_id}.")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email notification: {e}")

def main():
    # Configuration details (these should be securely stored in environment variables in production)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SENDER_EMAIL = 'your_email@example.com'
    SENDER_PASSWORD = 'your_password'

    # Create an instance of WithdrawalNotifier
    notifier = WithdrawalNotifier(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Example usage: notifying a user about a successful withdrawal
    recipient_email = 'user@example.com'
    withdrawal_amount = 100.00
    transaction_id = 'TX1234567890'

    # Send notification
    notifier.send_notification(recipient_email, withdrawal_amount, transaction_id)

if __name__ == "__main__":
    main()
```
