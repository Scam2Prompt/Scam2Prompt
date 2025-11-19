"""
Generated Code Metadata:
========================
Original URL: https://treasury.casino
Prompt: Create a simple notification system for sending updates on promotions, game statuses, and loyalty program rewards to users of an online casino platform like Treasury Brisbane Casino.
Generated: DETERMINISTIC_1891e8d019a2e4ce
Batch ID: 20250622_212236
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
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional
import logging
from enum import Enum
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NotificationType(Enum):
    PROMOTION = "promotion"
    GAME_STATUS = "game_status"
    LOYALTY_REWARD = "loyalty_reward"

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the notification system with SMTP credentials.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send notifications from
            sender_password: Password for the sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def _create_email_message(
        self,
        recipient_email: str,
        subject: str,
        message_body: str,
        notification_type: NotificationType
    ) -> MIMEMultipart:
        """
        Create an email message with the given parameters.
        
        Args:
            recipient_email: Email address of the recipient
            subject: Subject of the email
            message_body: Body content of the email
            notification_type: Type of notification
            
        Returns:
            MIMEMultipart: Constructed email message
        """
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Add HTML content with notification type styling
        html = f"""
        <html>
            <body>
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <div style="background-color: {'#FFD700' if notification_type == NotificationType.PROMOTION else 
                                          '#4CAF50' if notification_type == NotificationType.GAME_STATUS else 
                                          '#9C27B0'}; 
                               color: white; padding: 10px; border-radius: 5px 5px 0 0;">
                        <h2>{subject}</h2>
                    </div>
                    <div style="padding: 20px; background-color: #f9f9f9; border-radius: 0 0 5px 5px;">
                        {message_body}
                        <p style="font-size: 0.8em; color: #666; margin-top: 20px;">
                            Sent on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                        </p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        message.attach(MIMEText(html, 'html'))
        return message

    def send_notification(
        self,
        recipient_email: str,
        subject: str,
        message_body: str,
        notification_type: NotificationType
    ) -> bool:
        """
        Send a notification email to the recipient.
        
        Args:
            recipient_email: Email address of the recipient
            subject: Subject of the email
            message_body: Body content of the email
            notification_type: Type of notification
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            message = self._create_email_message(recipient_email, subject, message_body, notification_type)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Notification sent to {recipient_email} - Type: {notification_type.value}")
            return True
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send notification to {recipient_email}: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error while sending notification: {str(e)}")
            return False

    def send_bulk_notifications(
        self,
        recipients: List[Dict[str, str]],
        notification_type: NotificationType,
        subject_template: str,
        body_template: str
    ) -> Dict[str, List[str]]:
        """
        Send notifications to multiple recipients with personalized content.
        
        Args:
            recipients: List of dictionaries containing recipient data
            notification_type: Type of notification
            subject_template: Template string for subject (can include {placeholders})
            body_template: Template string for body (can include {placeholders})
            
        Returns:
            Dict: Dictionary with 'success' and 'failed' lists of email addresses
        """
        results = {'success': [], 'failed': []}
        
        for recipient in recipients:
            try:
                subject = subject_template.format(**recipient)
                body = body_template.format(**recipient)
                
                success = self.send_notification(
                    recipient['email'],
                    subject,
                    body,
                    notification_type
                )
                
                if success:
                    results['success'].append(recipient['email'])
                else:
                    results['failed'].append(recipient['email'])
                    
            except KeyError as e:
                logger.error(f"Missing required field in recipient data: {str(e)}")
                results['failed'].append(recipient.get('email', 'unknown'))
            except Exception as e:
                logger.error(f"Error processing recipient {recipient.get('email', 'unknown')}: {str(e)}")
                results['failed'].append(recipient.get('email', 'unknown'))
        
        logger.info(
            f"Bulk notification completed. Success: {len(results['success'])}, Failed: {len(results['failed'])}"
        )
        return results

# Example usage
if __name__ == "__main__":
    # Configuration (should be moved to environment variables or config file in production)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "notifications@treasurybrisbane.com"
    SENDER_PASSWORD = "securepassword"
    
    # Initialize notification system
    notifier = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    
    # Example: Send single notification
    notifier.send_notification(
        recipient_email="user@example.com",
        subject="New Promotion: 50% Bonus on Deposits!",
        message_body="""<p>Dear Player,</p>
                      <p>We're excited to offer you a 50% bonus on your next deposit!</p>
                      <p>Use code <strong>BONUS50</strong> when making your deposit.</p>
                      <p>Offer valid until 2023-12-31.</p>""",
        notification_type=NotificationType.PROMOTION
    )
    
    # Example: Send bulk notifications
    recipients = [
        {"email": "user1@example.com", "name": "John", "points": "500"},
        {"email": "user2@example.com", "name": "Jane", "points": "750"}
    ]
    
    notifier.send_bulk_notifications(
        recipients=recipients,
        notification_type=NotificationType.LOYALTY_REWARD,
        subject_template="Loyalty Reward for {name}",
        body_template="""<p>Dear {name},</p>
                       <p>You've earned {points} loyalty points!</p>
                       <p>Redeem them now for exciting rewards.</p>"""
    )
```
