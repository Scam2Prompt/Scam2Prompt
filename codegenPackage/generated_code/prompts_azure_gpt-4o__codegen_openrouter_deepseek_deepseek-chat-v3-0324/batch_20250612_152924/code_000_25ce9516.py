"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write Python code to automate the creation of email invitations for an event, incorporating branding elements and distribution timelines as described by Pozy Media's event marketing services.
Generated: DETERMINISTIC_25ce95161291e903
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
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
import csv
import os
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_invitations.log'),
        logging.StreamHandler()
    ]
)

class EmailInvitationAutomator:
    """
    Automates the creation and sending of branded email invitations for events.
    Handles email templates, branding elements, and distribution timelines.
    """
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        logo_path: Optional[str] = None,
        brand_color: str = "#2A5CAA",
        company_name: str = "Pozy Media"
    ):
        """
        Initialize the email invitation automator.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Email account password
            logo_path: Path to company logo image (optional)
            brand_color: Primary brand color in HEX format
            company_name: Name of the company/organization
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.logo_path = logo_path
        self.brand_color = brand_color
        self.company_name = company_name
        self.email_template = self._load_default_template()
        
        # Validate SMTP connection
        self._test_smtp_connection()
    
    def _test_smtp_connection(self) -> None:
        """Test the SMTP server connection."""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
            logging.info("SMTP connection test successful")
        except Exception as e:
            logging.error(f"SMTP connection failed: {str(e)}")
            raise
    
    def _load_default_template(self) -> str:
        """Load the default HTML email template."""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Event Invitation</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ color: {self.brand_color}; text-align: center; }}
                .logo {{ max-width: 200px; max-height: 100px; }}
                .event-details {{ background-color: #f9f9f9; padding: 15px; border-radius: 5px; }}
                .footer {{ margin-top: 20px; font-size: 12px; color: #777; text-align: center; }}
                .button {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: {self.brand_color};
                    color: white !important;
                    text-decoration: none;
                    border-radius: 5px;
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {{logo}}
                <h1 class="header">You're Invited!</h1>
                <p>Dear {{recipient_name}},</p>
                <p>We're excited to invite you to our upcoming event:</p>
                
                <div class="event-details">
                    <h2>{{event_name}}</h2>
                    <p><strong>Date:</strong> {{event_date}}</p>
                    <p><strong>Time:</strong> {{event_time}}</p>
                    <p><strong>Location:</strong> {{event_location}}</p>
                    <p>{{event_description}}</p>
                </div>
                
                <p>Please RSVP by clicking the button below:</p>
                <a href="{{rsvp_link}}" class="button">RSVP Now</a>
                
                <div class="footer">
                    <p>This invitation was sent by {self.company_name}.</p>
                    <p>If you received this email by mistake, please ignore it.</p>
                </div>
            </div>
        </body>
        </html>
        """
    
    def _process_template(
        self,
        recipient_name: str,
        event_name: str,
        event_date: str,
        event_time: str,
        event_location: str,
        event_description: str,
        rsvp_link: str
    ) -> str:
        """
        Populate the email template with event-specific details.
        
        Args:
            recipient_name: Name of the recipient
            event_name: Name of the event
            event_date: Date of the event
            event_time: Time of the event
            event_location: Location of the event
            event_description: Description of the event
            rsvp_link: URL for RSVP
            
        Returns:
            Processed HTML email content
        """
        logo_html = ""
        if self.logo_path and os.path.exists(self.logo_path):
            logo_html = f'<img src="cid:logo" class="logo" alt="{self.company_name} Logo">'
        
        return self.email_template.format(
            logo=logo_html,
            recipient_name=recipient_name,
            event_name=event_name,
            event_date=event_date,
            event_time=event_time,
            event_location=event_location,
            event_description=event_description,
            rsvp_link=rsvp_link
        )
    
    def send_invitation(
        self,
        recipient_email: str,
        recipient_name: str,
        event_name: str,
        event_date: str,
        event_time: str,
        event_location: str,
        event_description: str,
        rsvp_link: str,
        subject: str = "You're Invited!"
    ) -> bool:
        """
        Send a single email invitation.
        
        Args:
            recipient_email: Email address of the recipient
            recipient_name: Name of the recipient
            event_name: Name of the event
            event_date: Date of the event
            event_time: Time of the event
            event_location: Location of the event
            event_description: Description of the event
            rsvp_link: URL for RSVP
            subject: Email subject line
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        try:
            # Create message container
            msg = MIMEMultipart('related')
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Create the HTML body
            html_content = self._process_template(
                recipient_name=recipient_name,
                event_name=event_name,
                event_date=event_date,
                event_time=event_time,
                event_location=event_location,
                event_description=event_description,
                rsvp_link=rsvp_link
            )
            
            # Attach HTML content
            msg.attach(MIMEText(html_content, 'html'))
            
            # Attach logo if available
            if self.logo_path and os.path.exists(self.logo_path):
                with open(self.logo_path, 'rb') as img_file:
                    img = MIMEImage(img_file.read())
                    img.add_header('Content-ID', '<logo>')
                    msg.attach(img)
            
            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            logging.info(f"Invitation sent to {recipient_email}")
            return True
            
        except Exception as e:
            logging.error(f"Failed to send invitation to {recipient_email}: {str(e)}")
            return False
    
    def send_bulk_invitations(
        self,
        recipients_csv: str,
        event_name: str,
        event_date: str,
        event_time: str,
        event_location: str,
        event_description: str,
        rsvp_link: str,
        subject: str = "You're Invited!",
        send_delay_minutes: int = 0,
        batch_size: int = 50
    ) -> Dict[str, int]:
        """
        Send invitations to multiple recipients from a CSV file.
        
        Args:
            recipients_csv: Path to CSV file with recipient data
            event_name: Name of the event
            event_date: Date of the event
            event_time: Time of the event
            event_location: Location of the event
            event_description: Description of the event
            rsvp_link: URL for RSVP
            subject: Email subject line
