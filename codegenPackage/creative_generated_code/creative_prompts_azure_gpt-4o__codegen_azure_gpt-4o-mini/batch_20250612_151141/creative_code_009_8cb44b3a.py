"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Create a notification system that alerts users when their accrued rewards exceed the minimum thresholds for claiming ($BANANA, $ETH, or $SOL).
Generated: DETERMINISTIC_8cb44b3ab0abf763
Batch ID: 20250612_151141
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
from dataclasses import dataclass
from typing import Dict

@dataclass
class User:
    email: str
    rewards: Dict[str, float]  # Maps currency to accrued rewards

class NotificationSystem:
    def __init__(self, threshold: Dict[str, float], smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.threshold = threshold
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def check_rewards(self, user: User):
        """
        Check if the user's accrued rewards exceed the minimum thresholds.
        If they do, send a notification email.
        """
        for currency, amount in user.rewards.items():
            if amount >= self.threshold.get(currency, 0):
                self.send_notification(user.email, currency, amount)

    def send_notification(self, recipient_email: str, currency: str, amount: float):
        """
        Send an email notification to the user about their accrued rewards.
        """
        subject = f"Reward Notification: {currency} Threshold Exceeded"
        body = f"Congratulations! Your accrued {currency} rewards have reached {amount:.2f}, which exceeds the minimum threshold."
        
        # Create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email

        try:
            # Set up the SMTP server and send the email
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                print(f"Notification sent to {recipient_email} for {currency}")
        except Exception as e:
            print(f"Error sending email: {e}")

# Example of usage
if __name__ == "__main__":
    # Define thresholds for notification
    reward_thresholds = {
        '$BANANA': 100.0,
        '$ETH': 0.5,
        '$SOL': 1.0
    }

    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 465
    SENDER_EMAIL = 'your-email@example.com'
    SENDER_PASSWORD = 'your-password'

    # Create the Notification System
    notification_system = NotificationSystem(reward_thresholds, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Create a sample user with rewards
    user = User(email='user@example.com', rewards={'$BANANA': 150.0, '$ETH': 0.3, '$SOL': 1.5})

    # Check the user's rewards and send notifications if applicable
    notification_system.check_rewards(user)
```
