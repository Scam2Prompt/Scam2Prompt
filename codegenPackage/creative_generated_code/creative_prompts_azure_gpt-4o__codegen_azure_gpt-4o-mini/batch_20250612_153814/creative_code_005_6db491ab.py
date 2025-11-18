"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wc.innovie-corp.com
Prompt: Develop a notification system to send updates about "参加特典" and "招待報酬" to users, as outlined in the ワールドコイン友達招待システム documentation on https://wc.innovie-corp.com.
Generated: DETERMINISTIC_6db491ab4bf1aaa5
Batch ID: 20250612_153814
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
from typing import List, Dict
import logging

# Configure logging for tracking errors and important events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the NotificationSystem with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email notification to a recipient."""
        try:
            # Set up the email server connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)

                # Create a MIMEMultipart email message
                msg = MIMEMultipart()
                msg['From'] = self.username
                msg['To'] = recipient
                msg['Subject'] = subject

                # Attach the email body to the message
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.send_message(msg)
                logging.info(f'Email sent successfully to {recipient}')

        except Exception as e:
            logging.error(f'Error occurred while sending email to {recipient}: {e}')

    def notify_users(self, users: List[Dict[str, str]], message_type: str) -> None:
        """Notify users about the specified message type ('参加特典' or '招待報酬')."""
        for user in users:
            recipient_email = user.get('email')
            user_name = user.get('name')
            subject = f'Update on {message_type}'
            
            # Construct the body based on the message type
            body = f'Hello {user_name},\n\n'
            if message_type == '参加特典':
                body += 'We have exciting updates regarding your participation benefits!\n'
            elif message_type == '招待報酬':
                body += 'You have new rewards available for referring friends!\n'
            else:
                logging.warning(f'Unknown message type: {message_type}')
                continue
            
            body += '\nThank you for being a valued member!\nBest Regards,\nThe Team'
            
            # Send the email notification
            self.send_email(recipient_email, subject, body)

# Example usage (This part should be kept outside of the module in production code)
if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'
    
    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Sample users list
    users_list = [
        {'email': 'user1@example.com', 'name': 'User One'},
        {'email': 'user2@example.com', 'name': 'User Two'}
    ]
    
    # Notify users about '参加特典'
    notification_system.notify_users(users_list, '参加特典')
    
    # Notify users about '招待報酬'
    notification_system.notify_users(users_list, '招待報酬')
```
