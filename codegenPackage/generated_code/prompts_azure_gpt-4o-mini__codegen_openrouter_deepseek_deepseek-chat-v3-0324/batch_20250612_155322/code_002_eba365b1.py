"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Generate a code snippet that sends an email notification to clients when their PPI claim status changes, inspired by the customer service practices of Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_eba365b105825f19
Batch ID: 20250612_155322
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
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmailNotifier:
    """
    Handles sending email notifications to clients about PPI claim status changes.
    """
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        use_tls: bool = True
    ):
        """
        Initialize the email notifier with SMTP server details.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for sender email
            use_tls: Whether to use TLS encryption
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.use_tls = use_tls
        
    def send_status_update(
        self,
        recipient_email: str,
        client_name: str,
        claim_reference: str,
        old_status: str,
        new_status: str,
        additional_info: Optional[str] = None
    ) -> bool:
        """
        Send an email notification about PPI claim status change.
        
        Args:
            recipient_email: Client's email address
            client_name: Client's full name
            claim_reference: PPI claim reference number
            old_status: Previous claim status
            new_status: New claim status
            additional_info: Optional additional information
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"Update on your PPI Claim - Reference: {claim_reference}"
            
            # Create email body
            body = f"""
            Dear {client_name},
            
            We're writing to inform you about a change in the status of your PPI claim.
            
            Claim Reference: {claim_reference}
            Previous Status: {old_status}
            New Status: {new_status}
            """
            
            if additional_info:
                body += f"\nAdditional Information: {additional_info}\n"
                
            body += """
            If you have any questions about this update, please don't hesitate to contact us.
            
            Kind regards,
            Financial Recovery Solutions Ltd Customer Service Team
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                
            logger.info(f"Successfully sent status update email to {recipient_email}")
            return True
            
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send email to {recipient_email}: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error when sending email: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Configuration - these should come from environment variables or config in production
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "notifications@frsolutions.com"
    SENDER_PASSWORD = "securepassword"
    
    notifier = EmailNotifier(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD
    )
    
    # Example client data
    success = notifier.send_status_update(
        recipient_email="client@example.com",
        client_name="John Doe",
        claim_reference="PPI-2023-12345",
        old_status="Under Review",
        new_status="Approved",
        additional_info="Your claim has been approved and payment will be processed within 14 days."
    )
    
    if success:
        print("Email notification sent successfully")
    else:
        print("Failed to send email notification")
```
