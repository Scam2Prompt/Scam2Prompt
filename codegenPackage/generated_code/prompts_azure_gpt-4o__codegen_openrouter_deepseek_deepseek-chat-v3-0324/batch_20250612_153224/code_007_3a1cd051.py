"""
Generated Code Metadata:
========================
Original URL: https://searchhr.com.ar
Prompt: Create a script to send automated email notifications to job seekers using the contact information provided on the Search HR website (+54 (299) 5921719, contacto@searchhr.com.ar).
Generated: DETERMINISTIC_3a1cd05182141ae0
Batch ID: 20250612_153224
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_notifications.log'),
        logging.StreamHandler()
    ]
)

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the email notifier with SMTP server details and sender credentials.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address of the sender
            sender_password: Password for the sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(
        self,
        recipient_email: str,
        subject: str,
        body: str,
        is_html: bool = False
    ) -> bool:
        """
        Send an email to the specified recipient.
        
        Args:
            recipient_email: Email address of the recipient
            subject: Email subject
            body: Email body content
            is_html: Whether the body is HTML formatted
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach body to the email
            if is_html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            logging.info(f"Email sent successfully to {recipient_email}")
            return True

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {str(e)}")
            return False

    def send_bulk_emails(
        self,
        recipients: List[Dict[str, str]],
        subject_template: str,
        body_template: str,
        is_html: bool = False
    ) -> Dict[str, int]:
        """
        Send bulk emails to multiple recipients with personalized content.
        
        Args:
            recipients: List of dictionaries containing recipient info
            subject_template: Email subject template (can include placeholders)
            body_template: Email body template (can include placeholders)
            is_html: Whether the body is HTML formatted
            
        Returns:
            Dict: Statistics about sent emails {'total': X, 'success': Y, 'failed': Z}
        """
        results = {'total': 0, 'success': 0, 'failed': 0}
        
        for recipient in recipients:
            results['total'] += 1
            
            try:
                # Personalize email content
                subject = subject_template.format(**recipient)
                body = body_template.format(**recipient)
                
                if self.send_email(
                    recipient_email=recipient['email'],
                    subject=subject,
                    body=body,
                    is_html=is_html
                ):
                    results['success'] += 1
                else:
                    results['failed'] += 1
                    
            except Exception as e:
                logging.error(f"Error processing recipient {recipient.get('email', 'unknown')}: {str(e)}")
                results['failed'] += 1
        
        return results


def main():
    # Configuration
    SMTP_SERVER = "smtp.searchhr.com.ar"  # Replace with actual SMTP server
    SMTP_PORT = 587  # Common SMTP port for TLS
    SENDER_EMAIL = "contacto@searchhr.com.ar"
    SENDER_PASSWORD = "your_password_here"  # In production, use environment variables or secure storage
    
    # Sample job seekers data (in production, this would come from a database)
    job_seekers = [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "job_title": "Software Developer",
            "company": "Tech Corp"
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "job_title": "Data Analyst",
            "company": "Data Insights"
        }
    ]
    
    # Email templates
    subject_template = "New Job Opportunity at {company} for {job_title}"
    body_template = """Dear {name},
    
We found a new job opportunity that matches your profile for the position of {job_title} at {company}.

Please contact us at +54 (299) 5921719 or reply to this email for more details.

Best regards,
Search HR Team
contacto@searchhr.com.ar
"""
    
    # Initialize and send emails
    notifier = EmailNotifier(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD
    )
    
    results = notifier.send_bulk_emails(
        recipients=job_seekers,
        subject_template=subject_template,
        body_template=body_template
    )
    
    logging.info(f"Email sending completed. Results: {results}")


if __name__ == "__main__":
    main()
```
