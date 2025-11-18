"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Write a script to automate the creation of email marketing campaigns for hospitals, using Vivada Infotech's SKLS method for customer retention.
Generated: DETERMINISTIC_2d88574ee559430f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict

class EmailCampaign:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the EmailCampaign with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        
    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        """Send an email to a specified recipient."""
        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'html'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
            return True
            
        except Exception as e:
            print(f"Failed to send email to {to_email}: {str(e)}")
            return False

class MarketingCampaign:
    def __init__(self, email_campaign: EmailCampaign):
        """Initialize the MarketingCampaign with an EmailCampaign instance."""
        self.email_campaign = email_campaign
    
    def create_campaign(self, target_audience: List[Dict[str, str]], subject: str, body_template: str) -> None:
        """Create and send an email campaign to the target audience."""
        for recipient in target_audience:
            to_email = recipient.get('email')
            if to_email:
                # Personalize the email body
                body = body_template.format(name=recipient.get('name', 'Valued Customer'))
                
                # Send the email
                if self.email_campaign.send_email(to_email, subject, body):
                    print(f"Email sent successfully to {to_email}")
                else:
                    print(f"Email failed to send to {to_email}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'user@example.com'
    PASSWORD = 'securepassword'
    
    # Create an instance of EmailCampaign
    email_campaign = EmailCampaign(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    
    # Create an instance of MarketingCampaign
    marketing_campaign = MarketingCampaign(email_campaign)
    
    # Define the target audience
    target_audience = [
        {'name': 'John Doe', 'email': 'john.doe@example.com'},
        {'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    ]
    
    # Define the email subject and body template
    SUBJECT = "Important Health Updates"
    BODY_TEMPLATE = """
    <html>
        <body>
            <p>Dear {name},</p>
            <p>We hope you are doing well! Here are some important updates regarding your health.</p>
            <p>Thank you,</p>
            <p>Your Healthcare Team</p>
        </body>
    </html>
    """
    
    # Create and send the campaign
    marketing_campaign.create_campaign(target_audience, SUBJECT, BODY_TEMPLATE)
```
