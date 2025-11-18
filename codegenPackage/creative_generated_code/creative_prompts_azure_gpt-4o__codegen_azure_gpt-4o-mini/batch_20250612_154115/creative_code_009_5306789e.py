"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Write a program to track and notify users about campaigns ending soon on the Oasys Games platform, using local time zones for notifications.
Generated: DETERMINISTIC_5306789edd643b34
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import pytz
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict

# Campaign class to hold campaign details
class Campaign:
    def __init__(self, name: str, end_time: str, user_emails: List[str]):
        """
        Initializes a Campaign object.

        :param name: The name of the campaign.
        :param end_time: The end time of the campaign in ISO format (UTC).
        :param user_emails: List of user emails to notify.
        """
        self.name = name
        self.end_time = datetime.datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        self.user_emails = user_emails

    def is_ending_soon(self, hours_threshold: int = 24) -> bool:
        """
        Checks if the campaign is ending within the specified threshold.

        :param hours_threshold: Number of hours to check against.
        :return: True if ending soon, False otherwise.
        """
        now = datetime.datetime.now(pytz.utc)
        time_difference = self.end_time - now
        return time_difference <= datetime.timedelta(hours=hours_threshold)


class CampaignNotifier:
    def __init__(self, campaigns: List[Campaign]):
        """
        Initializes the notifier with a list of campaigns.

        :param campaigns: List of Campaign objects.
        """
        self.campaigns = campaigns

    def notify_users(self):
        """Notifies users about campaigns ending soon."""
        for campaign in self.campaigns:
            if campaign.is_ending_soon():
                self.send_notifications(campaign)

    @staticmethod
    def send_notifications(campaign: Campaign):
        """
        Sends notification emails to users about the campaign.

        :param campaign: The Campaign object to notify about.
        """
        subject = f"Reminder: Campaign '{campaign.name}' Ending Soon!"
        body = f"The campaign '{campaign.name}' is ending soon on {campaign.end_time.strftime('%Y-%m-%d %H:%M:%S %Z')}."
        for email in campaign.user_emails:
            try:
                CampaignNotifier.send_email(email, subject, body)
                print(f"Notification sent to {email} for campaign '{campaign.name}'.")
            except Exception as e:
                print(f"Failed to send notification to {email}: {e}")

    @staticmethod
    def send_email(to_email: str, subject: str, body: str):
        """
        Sends an email notification.

        :param to_email: Recipient's email address.
        :param subject: Email subject.
        :param body: Email body content.
        """
        from_email = "your_email@example.com"
        password = "your_email_password"  # Use environment variables for production

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Use appropriate SMTP server
                server.starttls()
                server.login(from_email, password)
                server.send_message(msg)
        except Exception as e:
            raise RuntimeError(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    campaigns = [
        Campaign("Spring Sale", "2023-10-30T23:59:59Z", ["user1@example.com", "user2@example.com"]),
        Campaign("Halloween Event", "2023-10-31T23:59:59Z", ["user3@example.com"])
    ]

    notifier = CampaignNotifier(campaigns)
    notifier.notify_users()
```
