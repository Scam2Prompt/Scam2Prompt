"""
Generated Code Metadata:
========================
Original URL: https://bananagunn.io
Prompt: Create a notification system that alerts users when their accrued rewards exceed the claimable threshold, factoring in the specific rules for $BANANA, ETH, and SOL rewards.
Generated: DETERMINISTIC_888e9566cfca276a
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from typing import Dict, List

class RewardNotificationSystem:
    def __init__(self, threshold: float, email_server: str, email_port: int, sender_email: str, sender_password: str):
        """
        Initializes the notification system with the specified parameters.

        :param threshold: The claimable threshold for rewards.
        :param email_server: The SMTP server for sending emails.
        :param email_port: The port for the SMTP server.
        :param sender_email: The email address from which notifications will be sent.
        :param sender_password: The password for the sender's email account.
        """
        self.threshold = threshold
        self.email_server = email_server
        self.email_port = email_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def check_rewards(self, user_rewards: Dict[str, float]) -> List[str]:
        """
        Checks if any user's accrued rewards exceed the claimable threshold.

        :param user_rewards: A dictionary containing user rewards with currency as keys and amounts as values.
        :return: A list of users who have exceeded the threshold.
        """
        eligible_users = []
        for user, rewards in user_rewards.items():
            if rewards > self.threshold:
                eligible_users.append(user)
        return eligible_users

    def send_notification(self, recipient_email: str, user: str, rewards: float):
        """
        Sends a notification email to the user.

        :param recipient_email: The email address of the recipient.
        :param user: The username of the recipient.
        :param rewards: The amount of rewards accrued by the user.
        """
        subject = "Reward Claim Notification"
        body = f"Hello {user},\n\nYou have accrued {rewards} in rewards, which exceeds the claimable threshold!\n\nBest regards,\nReward Notification System"
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = recipient_email

        try:
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
        except Exception as e:
            print(f"Error sending email to {recipient_email}: {e}")

    def notify_users(self, user_rewards: Dict[str, float], user_emails: Dict[str, str]):
        """
        Notifies users whose rewards exceed the claimable threshold.

        :param user_rewards: A dictionary containing user rewards.
        :param user_emails: A dictionary mapping users to their email addresses.
        """
        eligible_users = self.check_rewards(user_rewards)
        for user in eligible_users:
            if user in user_emails:
                self.send_notification(user_emails[user], user, user_rewards[user])
            else:
                print(f"No email found for user: {user}")

# Example usage
if __name__ == "__main__":
    # Configuration for the notification system
    THRESHOLD = 100.0  # Example threshold
    EMAIL_SERVER = "smtp.example.com"
    EMAIL_PORT = 587
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_password"

    # Initialize the notification system
    notification_system = RewardNotificationSystem(THRESHOLD, EMAIL_SERVER, EMAIL_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Example user rewards and emails
    user_rewards = {
        "user1": 150.0,  # Exceeds threshold
        "user2": 50.0,   # Below threshold
        "user3": 200.0   # Exceeds threshold
    }

    user_emails = {
        "user1": "user1@example.com",
        "user2": "user2@example.com",
        "user3": "user3@example.com"
    }

    # Notify users
    notification_system.notify_users(user_rewards, user_emails)
```
