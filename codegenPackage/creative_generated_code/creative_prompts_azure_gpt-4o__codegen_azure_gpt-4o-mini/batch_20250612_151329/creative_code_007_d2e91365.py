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
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the NotificationService with SMTP configuration.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email username for authentication
        :param password: Email password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_notification(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification to a user.

        :param recipient: Email address of the recipient
        :param subject: Subject line of the email
        :param body: Body content of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f'Notification sent to {recipient}')
        except Exception as e:
            logging.error(f'Failed to send notification to {recipient}: {str(e)}')

def compose_reward_progress_message(user_name: str, progress_percentage: float) -> str:
    """
    Compose a message about the user's rewards progress.

    :param user_name: The name of the user
    :param progress_percentage: Progress percentage of the rewards
    :return: Formatted message string
    """
    return f"Hello {user_name},\n\nYour current rewards progress is at {progress_percentage}%.\nKeep it up!"

def compose_airdrop_claim_message(user_name: str) -> str:
    """
    Compose a message about the airdrop claims.

    :param user_name: The name of the user
    :return: Formatted message string
    """
    return f"Hello {user_name},\n\nDon't forget to claim your USDT from the Airdrop! Visit our platform for more details."

def main(users: List[dict]):
    """
    Main function to send notifications to users about rewards and airdrop claims.

    :param users: List of users containing their email and progress info
    """
    # SMTP configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_email_password'

    # Initialize the notification service
    notification_service = NotificationService(smtp_server, smtp_port, username, password)

    for user in users:
        user_name = user.get('name')
        user_email = user.get('email')
        user_progress = user.get('progress')
        
        # Send rewards progress notification
        rewards_message = compose_reward_progress_message(user_name, user_progress)
        notification_service.send_notification(user_email, 'Your Rewards Progress', rewards_message)
        
        # Send airdrop claim notification
        airdrop_message = compose_airdrop_claim_message(user_name)
        notification_service.send_notification(user_email, 'Claim Your USDT Airdrop', airdrop_message)

if __name__ == "__main__":
    # Example user list for demonstration
    users_info = [
        {'name': 'Alice', 'email': 'alice@example.com', 'progress': 75},
        {'name': 'Bob', 'email': 'bob@example.com', 'progress': 50}
    ]
    
    # Run the main function to send notifications
    main(users_info)
```
