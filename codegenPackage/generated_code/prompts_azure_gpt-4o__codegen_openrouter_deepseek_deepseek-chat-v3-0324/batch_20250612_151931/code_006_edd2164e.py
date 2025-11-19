"""
Generated Code Metadata:
========================
Original URL: https://cajicacompra.com
Prompt: Generate code to implement a notification system for judicial updates via email, similar to the "Correo para Notificaciones Judiciales" feature on Cajicá Compra.
Generated: DETERMINISTIC_edd2164e13c02aa1
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
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class JudicialNotificationSystem:
    """
    A system for sending judicial notifications via email.
    """
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_username = os.getenv('SMTP_USERNAME')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.admin_email = os.getenv('ADMIN_EMAIL')
        
        if not all([self.smtp_server, self.smtp_username, self.smtp_password, self.sender_email]):
            raise ValueError("Missing required SMTP configuration in environment variables")
    
    def _send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        is_html: bool = False
    ) -> bool:
        """
        Internal method to send an email.
        
        Args:
            recipient: Email address of the recipient
            subject: Email subject
            body: Email body content
            is_html: Whether the body is HTML formatted
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            if is_html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {recipient}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            self._notify_admin(f"Failed to send judicial notification to {recipient}")
            return False
    
    def _notify_admin(self, error_message: str) -> None:
        """
        Notify admin about system errors.
        
        Args:
            error_message: The error message to send to admin
        """
        try:
            subject = "Judicial Notification System Error"
            body = f"An error occurred in the Judicial Notification System:\n\n{error_message}"
            self._send_email(self.admin_email, subject, body)
        except Exception as e:
            logger.error(f"Failed to notify admin: {str(e)}")
    
    def send_judicial_notification(
        self,
        recipient_email: str,
        case_number: str,
        update_details: str,
        court_name: str,
        judge_name: Optional[str] = None,
        hearing_date: Optional[datetime] = None
    ) -> bool:
        """
        Send a judicial notification email to a recipient.
        
        Args:
            recipient_email: Email address of the recipient
            case_number: The case number/identifier
            update_details: Details of the judicial update
            court_name: Name of the court
            judge_name: Name of the judge (optional)
            hearing_date: Date of next hearing (optional)
            
        Returns:
            bool: True if notification was sent successfully, False otherwise
        """
        try:
            subject = f"Judicial Notification Update - Case {case_number}"
            
            # Format hearing date if provided
            hearing_date_str = ""
            if hearing_date:
                hearing_date_str = hearing_date.strftime("%B %d, %Y at %I:%M %p")
            
            # Create email body
            body = f"""
            <html>
                <body>
                    <h2>Judicial Notification Update</h2>
                    <p><strong>Case Number:</strong> {case_number}</p>
                    <p><strong>Court:</strong> {court_name}</p>
                    {f"<p><strong>Judge:</strong> {judge_name}</p>" if judge_name else ""}
                    {f"<p><strong>Next Hearing:</strong> {hearing_date_str}</p>" if hearing_date else ""}
                    <hr>
                    <h3>Update Details:</h3>
                    <p>{update_details}</p>
                    <hr>
                    <p>This is an automated notification. Please do not reply to this email.</p>
                </body>
            </html>
            """
            
            return self._send_email(recipient_email, subject, body, is_html=True)
            
        except Exception as e:
            logger.error(f"Error preparing judicial notification: {str(e)}")
            self._notify_admin(f"Error preparing judicial notification for case {case_number}")
            return False
    
    def batch_send_notifications(
        self,
        notifications: List[Dict]
    ) -> Dict[str, List[str]]:
        """
        Send multiple judicial notifications in batch.
        
        Args:
            notifications: List of dictionaries containing notification details
                Each dict should contain:
                - recipient_email
                - case_number
                - update_details
                - court_name
                - judge_name (optional)
                - hearing_date (optional)
                
        Returns:
            Dict: {
                'success': List of case numbers that were sent successfully,
                'failed': List of case numbers that failed to send
            }
        """
        results = {'success': [], 'failed': []}
        
        for notification in notifications:
            try:
                success = self.send_judicial_notification(
                    recipient_email=notification['recipient_email'],
                    case_number=notification['case_number'],
                    update_details=notification['update_details'],
                    court_name=notification['court_name'],
                    judge_name=notification.get('judge_name'),
                    hearing_date=notification.get('hearing_date')
                )
                
                if success:
                    results['success'].append(notification['case_number'])
                else:
                    results['failed'].append(notification['case_number'])
                    
            except KeyError as e:
                logger.error(f"Missing required field in notification: {str(e)}")
                results['failed'].append(notification.get('case_number', 'UNKNOWN'))
            except Exception as e:
                logger.error(f"Unexpected error processing notification: {str(e)}")
                results['failed'].append(notification.get('case_number', 'UNKNOWN'))
        
        return results


# Example usage
if __name__ == "__main__":
    try:
        notification_system = JudicialNotificationSystem()
        
        # Single notification example
        notification_system.send_judicial_notification(
            recipient_email="recipient@example.com",
            case_number="2023-001",
            update_details="The hearing scheduled for next week has been postponed.",
            court_name="Superior Court of Cundinamarca",
            judge_name="Hon. Judge Maria Rodriguez",
            hearing_date=datetime(2023, 12, 15, 10, 30)
        )
        
        # Batch notifications example
        notifications = [
            {
                'recipient_email': "user1@example.com",
                'case_number': "2023-002",
                'update_details': "New documents have been added to the case file.",
                'court_name': "District Court of Bogotá"
            },
            {
                'recipient_email': "user2@example.com",
                'case_number': "2023-003",
                'update_details': "The verdict has been announced.",
                'court_name': "Supreme Court",
                'judge_name': "Hon. Judge Carlos Mendez",
                'hearing_date': datetime(2023, 12, 20, 9, 0)
            }
        ]
        
        results = notification_system.batch_send_notifications(notifications)
        logger.info(f"Batch results: {results}")
        
    except Exception as e:
        logger.error(f"Error in notification system: {str(e)}")
```
