"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hfm88.com
Prompt: Develop a function to track international money transfers and notify users when funds are successfully delivered, inspired by HFM's fast delivery model.
Generated: DETERMINISTIC_6a7db7c24a7ba9ee
Batch ID: 20250612_154111
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


class MoneyTransferSystem:
    def __init__(self):
        # Initialize system with an empty transaction log
        self.transaction_log = []

    def send_money(self, sender, receiver, amount, currency, email):
        """
        Handles the money transfer process and notifies the user upon successful delivery.

        Args:
            sender (str): Name of the sender.
            receiver (str): Name of the receiver.
            amount (float): Amount to transfer.
            currency (str): Currency type (e.g., USD, EUR, GBP).
            email (str): User's email address for notifications.

        Returns:
            dict: Details of the completed transaction.
        """
        try:
            # Validate input data
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if not isinstance(currency, str) or len(currency) != 3:
                raise ValueError("Currency must be a 3-letter ISO code (e.g., USD).")

            # Simulate the delivery of funds
            transaction_id = len(self.transaction_log) + 1
            timestamp = datetime.now()
            transaction_details = {
                "transaction_id": transaction_id,
                "sender": sender,
                "receiver": receiver,
                "amount": amount,
                "currency": currency,
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Delivered",
            }
            self.transaction_log.append(transaction_details)

            # Notify user of successful delivery
            self._send_notification(email, transaction_details)

            return transaction_details
        except Exception as e:
            # Handle any unexpected errors
            print(f"Error occurred during the transfer: {e}")
            raise

    def _send_notification(self, email, transaction_details):
        """
        Sends a notification to the user's email about the successful transaction.

        Args:
            email (str): User's email address.
            transaction_details (dict): Details of the completed transaction.
        """
        try:
            # Create the email content
            subject = "Money Transfer Notification: Funds Delivered Successfully"
            body = (
                f"Dear User,\n\n"
                f"Your money transfer has been successfully delivered.\n\n"
                f"Transaction Details:\n"
                f"Sender: {transaction_details['sender']}\n"
                f"Receiver: {transaction_details['receiver']}\n"
                f"Amount: {transaction_details['amount']} {transaction_details['currency']}\n"
                f"Transaction ID: {transaction_details['transaction_id']}\n"
                f"Timestamp: {transaction_details['timestamp']}\n\n"
                f"Thank you for using our service!\n"
            )

            # Configure email settings
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = "noreply@moneytransfersystem.com"
            msg["To"] = email

            # Simulate sending the email (replace with actual SMTP server settings in production)
            smtp_server = "smtp.example.com"  # Replace with your SMTP server
            smtp_port = 587  # Common port for SMTP
            smtp_username = "your_smtp_username"  # Replace with your username
            smtp_password = "your_smtp_password"  # Replace with your password

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(msg["From"], [msg["To"]], msg.as_string())

            print(f"Notification sent successfully to {email}")
        except Exception as e:
            # Handle any email sending errors
            print(f"Error occurred while sending notification: {e}")
            raise


# Example Usage
if __name__ == "__main__":
    mts = MoneyTransferSystem()
    try:
        transaction = mts.send_money(
            sender="John Doe",
            receiver="Jane Smith",
            amount=1500.0,
            currency="USD",
            email="johndoe@example.com"
        )
        print("Transaction completed successfully:", transaction)
    except Exception as e:
        print(f"Failed to complete transaction: {e}")
```
