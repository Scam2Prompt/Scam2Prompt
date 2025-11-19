"""
Generated Code Metadata:
========================
Original URL: https://vivadainfotech.com
Prompt: Write a script to automate the creation of email marketing campaigns for hospitals, using Vivada Infotech's SKLS method for customer retention.
Generated: DETERMINISTIC_2d88574ee559430f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='email_campaign.log'
)

class EmailCampaign:
    """
    A class to automate email marketing campaigns using Vivada Infotech's SKLS method.
    SKLS stands for:
    - Segment
    - Knowledge
    - Loyalty
    - Service
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the EmailCampaign with SMTP server details.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipients = []
        
    def load_recipients(self, csv_file: str) -> None:
        """
        Load recipient data from a CSV file.
        
        Args:
            csv_file: Path to CSV file containing recipient data
        """
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.recipients = [row for row in reader]
            logging.info(f"Successfully loaded {len(self.recipients)} recipients from {csv_file}")
        except Exception as e:
            logging.error(f"Error loading recipients: {str(e)}")
            raise
            
    def segment_recipients(self) -> Dict[str, List[Dict]]:
        """
        Segment recipients based on SKLS method.
        
        Returns:
            Dictionary with segmented recipients
        """
        segments = {
            'new_patients': [],
            'regular_patients': [],
            'loyal_patients': [],
            'inactive_patients': []
        }
        
        for recipient in self.recipients:
            last_visit = datetime.datetime.strptime(recipient['last_visit'], '%Y-%m-%d').date()
            days_since_last_visit = (datetime.date.today() - last_visit).days
            
            if days_since_last_visit < 30:
                segments['new_patients'].append(recipient)
            elif 30 <= days_since_last_visit < 90:
                segments['regular_patients'].append(recipient)
            elif 90 <= days_since_last_visit < 180:
                segments['loyal_patients'].append(recipient)
            else:
                segments['inactive_patients'].append(recipient)
                
        logging.info("Recipients segmented successfully")
        return segments
    
    def generate_email_content(self, segment: str, recipient: Dict) -> str:
        """
        Generate personalized email content based on segment.
        
        Args:
            segment: Recipient segment
            recipient: Recipient data
            
        Returns:
            Personalized email content
        """
        templates = {
            'new_patients': f"""
            <html>
                <body>
                    <p>Dear {recipient['name']},</p>
                    <p>Thank you for choosing our hospital for your recent visit!</p>
                    <p>We'd love to hear about your experience and how we can serve you better.</p>
                    <p>As a new patient, we're offering you a special discount on your next visit.</p>
                    <p>Best regards,<br>The Hospital Team</p>
                </body>
            </html>
            """,
            'regular_patients': f"""
            <html>
                <body>
                    <p>Dear {recipient['name']},</p>
                    <p>We appreciate your continued trust in our hospital services.</p>
                    <p>Did you know we now offer telemedicine consultations? Book your next appointment online!</p>
                    <p>Best regards,<br>The Hospital Team</p>
                </body>
            </html>
            """,
            'loyal_patients': f"""
            <html>
                <body>
                    <p>Dear {recipient['name']},</p>
                    <p>We miss seeing you at our hospital!</p>
                    <p>As a valued patient, we're offering you a complimentary health check-up this month.</p>
                    <p>Best regards,<br>The Hospital Team</p>
                </body>
            </html>
            """,
            'inactive_patients': f"""
            <html>
                <body>
                    <p>Dear {recipient['name']},</p>
                    <p>It's been a while since we've seen you, and we hope you're doing well.</p>
                    <p>We've made several improvements to our services and would love for you to experience them.</p>
                    <p>Best regards,<br>The Hospital Team</p>
                </body>
            </html>
            """
        }
        
        return templates.get(segment, "")
    
    def send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        """
        Send an email to a single recipient.
        
        Args:
            recipient_email: Email address of recipient
            subject: Email subject
            body: Email body content
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                
            logging.info(f"Email sent successfully to {recipient_email}")
            return True
        except Exception as e:
            logging.error(f"Error sending email to {recipient_email}: {str(e)}")
            return False
            
    def run_campaign(self, segments: Dict[str, List[Dict]]) -> None:
        """
        Run the email campaign for all segments.
        
        Args:
            segments: Dictionary of segmented recipients
        """
        subjects = {
            'new_patients': "Welcome to Our Hospital - Special Offer Inside!",
            'regular_patients': "Enhancing Your Healthcare Experience",
            'loyal_patients': "We Miss You - Complimentary Health Check-Up",
            'inactive_patients': "We've Improved - Come See What's New"
        }
        
        for segment_name, recipients in segments.items():
            for recipient in recipients:
                email_content = self.generate_email_content(segment_name, recipient)
                subject = subjects.get(segment_name, "Important Message from Our Hospital")
                
                if not self.send_email(recipient['email'], subject, email_content):
                    logging.warning(f"Failed to send email to {recipient['email']}")
                    
        logging.info("Email campaign completed")

def main():
    try:
        # Initialize campaign with SMTP details
        campaign = EmailCampaign(
            smtp_server='smtp.example.com',
            smtp_port=587,
            sender_email='marketing@hospital.com',
            sender_password='securepassword'
        )
        
        # Load recipients from CSV
        campaign.load_recipients('recipients.csv')
        
        # Segment recipients
        segments = campaign.segment_recipients()
        
        # Run campaign
        campaign.run_campaign(segments)
        
    except Exception as e:
        logging.error(f"Campaign failed: {str(e)}")

if __name__ == "__main__":
    main()
```
