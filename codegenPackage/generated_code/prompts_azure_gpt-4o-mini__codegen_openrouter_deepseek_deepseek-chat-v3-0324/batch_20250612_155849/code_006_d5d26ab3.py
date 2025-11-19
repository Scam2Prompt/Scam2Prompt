"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: How can I program a smart home system to alert family members in case of a medical emergency, such as a fall detection?
Generated: DETERMINISTIC_d5d26ab3b88761ad
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import requests
from twilio.rest import Client
from datetime import datetime
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmergencyAlertSystem:
    """
    A smart home system to alert family members in case of medical emergencies.
    Supports SMS, voice calls, and email notifications.
    """
    
    def __init__(
        self,
        twilio_account_sid: Optional[str] = None,
        twilio_auth_token: Optional[str] = None,
        twilio_phone_number: Optional[str] = None,
        smtp_server: Optional[str] = None,
        smtp_port: Optional[int] = None,
        email_username: Optional[str] = None,
        email_password: Optional[str] = None
    ):
        """
        Initialize the emergency alert system with notification services.
        """
        self.twilio_client = None
        if twilio_account_sid and twilio_auth_token:
            self.twilio_client = Client(twilio_account_sid, twilio_auth_token)
        self.twilio_phone_number = twilio_phone_number
        
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_username = email_username
        self.email_password = email_password
        
        # Emergency contacts
        self.emergency_contacts = {
            'sms': [],
            'call': [],
            'email': []
        }
    
    def add_emergency_contact(
        self,
        contact_type: str,
        contact_info: str,
        name: Optional[str] = None
    ) -> bool:
        """
        Add an emergency contact for notifications.
        
        Args:
            contact_type: 'sms', 'call', or 'email'
            contact_info: Phone number or email address
            name: Optional contact name
            
        Returns:
            bool: True if contact was added successfully
        """
        if contact_type not in self.emergency_contacts:
            logger.error(f"Invalid contact type: {contact_type}")
            return False
            
        self.emergency_contacts[contact_type].append({
            'info': contact_info,
            'name': name
        })
        logger.info(f"Added {contact_type} contact: {contact_info}")
        return True
    
    def send_sms_alert(self, message: str) -> bool:
        """
        Send SMS alerts to all registered SMS contacts.
        
        Args:
            message: The alert message to send
            
        Returns:
            bool: True if all messages were sent successfully
        """
        if not self.twilio_client or not self.twilio_phone_number:
            logger.error("Twilio not configured for SMS alerts")
            return False
            
        if not self.emergency_contacts['sms']:
            logger.warning("No SMS contacts configured")
            return False
            
        success = True
        for contact in self.emergency_contacts['sms']:
            try:
                self.twilio_client.messages.create(
                    body=message,
                    from_=self.twilio_phone_number,
                    to=contact['info']
                )
                logger.info(f"SMS sent to {contact['info']}")
            except Exception as e:
                logger.error(f"Failed to send SMS to {contact['info']}: {str(e)}")
                success = False
                
        return success
    
    def make_emergency_call(self, message: str) -> bool:
        """
        Make voice calls to all registered call contacts.
        
        Args:
            message: The message to speak during the call
            
        Returns:
            bool: True if all calls were initiated successfully
        """
        if not self.twilio_client or not self.twilio_phone_number:
            logger.error("Twilio not configured for voice calls")
            return False
            
        if not self.emergency_contacts['call']:
            logger.warning("No call contacts configured")
            return False
            
        success = True
        for contact in self.emergency_contacts['call']:
            try:
                call = self.twilio_client.calls.create(
                    twiml=f'<Response><Say>{message}</Say></Response>',
                    from_=self.twilio_phone_number,
                    to=contact['info']
                )
                logger.info(f"Call initiated to {contact['info']}, SID: {call.sid}")
            except Exception as e:
                logger.error(f"Failed to call {contact['info']}: {str(e)}")
                success = False
                
        return success
    
    def send_email_alert(self, subject: str, message: str) -> bool:
        """
        Send email alerts to all registered email contacts.
        
        Args:
            subject: Email subject
            message: Email body
            
        Returns:
            bool: True if all emails were sent successfully
        """
        if not all([self.smtp_server, self.smtp_port, self.email_username, self.email_password]):
            logger.error("Email not configured properly")
            return False
            
        if not self.emergency_contacts['email']:
            logger.warning("No email contacts configured")
            return False
            
        success = True
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_username, self.email_password)
                
                for contact in self.emergency_contacts['email']:
                    email_message = (
                        f"Subject: {subject}\n"
                        f"To: {contact['info']}\n"
                        f"\n{message}"
                    )
                    try:
                        server.sendmail(
                            self.email_username,
                            contact['info'],
                            email_message
                        )
                        logger.info(f"Email sent to {contact['info']}")
                    except Exception as e:
                        logger.error(f"Failed to send email to {contact['info']}: {str(e)}")
                        success = False
        except Exception as e:
            logger.error(f"SMTP connection failed: {str(e)}")
            success = False
            
        return success
    
    def trigger_emergency_alerts(self, emergency_type: str, location: str = "unknown") -> bool:
        """
        Trigger all emergency alerts for a detected emergency.
        
        Args:
            emergency_type: Type of emergency (e.g., "fall")
            location: Optional location information
            
        Returns:
            bool: True if all alerts were triggered successfully
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject = f"EMERGENCY ALERT: {emergency_type.upper()} detected"
        message = (
            f"EMERGENCY ALERT\n"
            f"Type: {emergency_type}\n"
            f"Time: {timestamp}\n"
            f"Location: {location}\n"
            f"\nImmediate attention required!"
        )
        
        sms_success = self.send_sms_alert(message)
        call_success = self.make_emergency_call(message)
        email_success = self.send_email_alert(subject, message)
        
        return all([sms_success, call_success, email_success])

# Example usage
if __name__ == "__main__":
    # Initialize with your credentials
    alert_system = EmergencyAlertSystem(
        twilio_account_sid="your_twilio_account_sid",
        twilio_auth_token="your_twilio_auth_token",
        twilio_phone_number="+1234567890",
        smtp_server="smtp.example.com",
        smtp_port=587,
        email_username="your_email@example.com",
        email_password="your_email_password"
    )
    
    # Add emergency contacts
    alert_system.add_emergency_contact("sms", "+15551234567", "John Doe")
    alert_system.add_emergency_contact("call", "+15557654321", "Jane Smith")
    alert_system.add_emergency_contact("email", "family@example.com", "Family Group")
    
    # Simulate fall detection
    alert_system.trigger_emergency_alerts("fall", "Living Room")
```
