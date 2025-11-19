"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Write code to implement a notification system for informing users about updates to the privacy policy, including push notifications and email alerts, as described by STELLAR TECHNOLOGY LIMITED.
Generated: DETERMINISTIC_69c5ec9e7df7be59
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional
import logging
from push_notifications.models import APNSDevice, GCMDevice

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotificationSystem:
    """
    A system for sending privacy policy update notifications via email and push notifications.
    """
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.example.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_username = os.getenv('SMTP_USERNAME')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.from_email = os.getenv('FROM_EMAIL', 'notifications@stellartechnology.com')
        
    def send_email_notification(self, recipients: List[str], policy_version: str, update_date: str) -> bool:
        """
        Send email notification about privacy policy update.
        
        Args:
            recipients: List of email addresses to notify
            policy_version: New version of the privacy policy
            update_date: Date when policy was updated
            
        Returns:
            bool: True if emails were sent successfully, False otherwise
        """
        if not recipients:
            logger.warning("No recipients provided for email notification")
            return False
            
        subject = f"STELLAR TECHNOLOGY LIMITED - Privacy Policy Update (v{policy_version})"
        
        # HTML email template
        html = f"""
        <html>
            <body>
                <h2>Privacy Policy Update Notification</h2>
                <p>Dear User,</p>
                <p>We wanted to inform you that STELLAR TECHNOLOGY LIMITED has updated its Privacy Policy (version {policy_version}) on {update_date}.</p>
                <p>Please review the updated policy at your earliest convenience.</p>
                <p>If you have any questions, please contact our support team.</p>
                <br>
                <p>Best regards,</p>
                <p>The STELLAR TECHNOLOGY LIMITED Team</p>
            </body>
        </html>
        """
        
        try:
            # Create message container
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_email
            msg['To'] = ', '.join(recipients)
            
            # Attach HTML version
            msg.attach(MIMEText(html, 'html'))
            
            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            logger.info(f"Successfully sent email notifications to {len(recipients)} recipients")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email notifications: {str(e)}")
            return False
    
    def send_push_notification(self, user_ids: List[int], policy_version: str) -> Dict[str, int]:
        """
        Send push notifications about privacy policy update.
        
        Args:
            user_ids: List of user IDs to notify
            policy_version: New version of the privacy policy
            
        Returns:
            Dict: {'success': count of successful notifications, 'failure': count of failed notifications}
        """
        if not user_ids:
            logger.warning("No user IDs provided for push notification")
            return {'success': 0, 'failure': 0}
            
        results = {'success': 0, 'failure': 0}
        message = f"STELLAR TECHNOLOGY LIMITED has updated its Privacy Policy to version {policy_version}. Please review it."
        
        try:
            # Get all registered devices for these users
            apns_devices = APNSDevice.objects.filter(user_id__in=user_ids)
            gcm_devices = GCMDevice.objects.filter(user_id__in=user_ids)
            
            # Send to iOS devices
            for device in apns_devices:
                try:
                    device.send_message(message, badge=1)
                    results['success'] += 1
                except Exception as e:
                    logger.error(f"Failed to send APNS notification to user {device.user_id}: {str(e)}")
                    results['failure'] += 1
            
            # Send to Android devices
            for device in gcm_devices:
                try:
                    device.send_message(message)
                    results['success'] += 1
                except Exception as e:
                    logger.error(f"Failed to send GCM notification to user {device.user_id}: {str(e)}")
                    results['failure'] += 1
                    
            logger.info(f"Push notification results: {results}")
            return results
            
        except Exception as e:
            logger.error(f"Error in push notification system: {str(e)}")
            return {'success': 0, 'failure': len(user_ids)}
    
    def notify_users(self, email_recipients: List[str], push_user_ids: List[int], policy_version: str) -> Dict[str, Dict]:
        """
        Main method to notify users about privacy policy update.
        
        Args:
            email_recipients: List of email addresses to notify
            push_user_ids: List of user IDs to send push notifications to
            policy_version: New version of the privacy policy
            
        Returns:
            Dict: Results from both notification methods
        """
        update_date = datetime.now().strftime('%Y-%m-%d')
        
        email_result = self.send_email_notification(email_recipients, policy_version, update_date)
        push_result = self.send_push_notification(push_user_ids, policy_version)
        
        return {
            'email': {'success': email_result, 'recipients': len(email_recipients)},
            'push': push_result
        }


# Example usage
if __name__ == "__main__":
    notification_system = NotificationSystem()
    
    # Example data
    email_recipients = ["user1@example.com", "user2@example.com"]
    push_user_ids = [101, 102, 103]
    policy_version = "2.1"
    
    # Send notifications
    results = notification_system.notify_users(email_recipients, push_user_ids, policy_version)
    print("Notification results:", results)
```
