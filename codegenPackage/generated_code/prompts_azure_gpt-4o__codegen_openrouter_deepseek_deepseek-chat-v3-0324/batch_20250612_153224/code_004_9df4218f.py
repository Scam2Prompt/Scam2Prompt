"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Design an SMS notification system for school administrators to send updates to parents, similar to the SMS module in Him Saral's software.
Generated: DETERMINISTIC_9df4218fe5ced7ee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from typing import List, Dict, Optional
from twilio.rest import Client
from dotenv import load_dotenv
from pydantic import BaseModel, validator

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Pydantic models for data validation
class ParentContact(BaseModel):
    name: str
    phone_number: str
    student_name: str
    student_class: str

    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.startswith('+'):
            raise ValueError('Phone number must include country code (e.g., +1)')
        if not v[1:].isdigit():
            raise ValueError('Phone number must contain only digits after country code')
        return v

class SMSMessage(BaseModel):
    sender_id: str
    message: str
    recipients: List[ParentContact]

    @validator('message')
    def validate_message_length(cls, v):
        if len(v) > 160:
            logger.warning('Message exceeds 160 characters and may be split into multiple SMS')
        return v

class SMSNotificationSystem:
    def __init__(self):
        self.twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
        
        if not all([self.twilio_account_sid, self.twilio_auth_token, self.twilio_phone_number]):
            raise ValueError("Twilio credentials not properly configured in environment variables")
        
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)
    
    def send_sms(self, sms_message: SMSMessage) -> Dict[str, List[Dict[str, str]]]:
        """
        Send SMS messages to multiple recipients.
        
        Args:
            sms_message: SMSMessage object containing message details and recipients
            
        Returns:
            Dictionary with 'success' and 'failed' lists containing status of each message
        """
        results = {'success': [], 'failed': []}
        
        for recipient in sms_message.recipients:
            try:
                message = self.client.messages.create(
                    body=f"Dear {recipient.name},\n{sms_message.message}\n- {sms_message.sender_id}",
                    from_=self.twilio_phone_number,
                    to=recipient.phone_number
                )
                results['success'].append({
                    'parent': recipient.name,
                    'student': recipient.student_name,
                    'phone': recipient.phone_number,
                    'message_id': message.sid
                })
                logger.info(f"SMS sent to {recipient.phone_number} for {recipient.student_name}")
            except Exception as e:
                results['failed'].append({
                    'parent': recipient.name,
                    'student': recipient.student_name,
                    'phone': recipient.phone_number,
                    'error': str(e)
                })
                logger.error(f"Failed to send SMS to {recipient.phone_number}: {str(e)}")
        
        return results

    def get_message_status(self, message_id: str) -> Optional[Dict[str, str]]:
        """
        Check the status of a sent SMS message.
        
        Args:
            message_id: Twilio message SID
            
        Returns:
            Dictionary with message status details or None if not found
        """
        try:
            message = self.client.messages(message_id).fetch()
            return {
                'status': message.status,
                'date_sent': str(message.date_sent),
                'to': message.to,
                'error_code': message.error_code,
                'error_message': message.error_message
            }
        except Exception as e:
            logger.error(f"Error fetching message status for {message_id}: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the SMS system
        sms_system = SMSNotificationSystem()
        
        # Example recipients
        recipients = [
            ParentContact(
                name="John Doe",
                phone_number="+1234567890",
                student_name="Alice Doe",
                student_class="5A"
            ),
            ParentContact(
                name="Jane Smith",
                phone_number="+1987654321",
                student_name="Bob Smith",
                student_class="3B"
            )
        ]
        
        # Create and send message
        message = SMSMessage(
            sender_id="School Admin",
            message="Parent-teacher meeting scheduled for Friday at 2 PM.",
            recipients=recipients
        )
        
        # Send SMS
        results = sms_system.send_sms(message)
        print("SMS sending results:", results)
        
        # Check status of first successful message (if any)
        if results['success']:
            first_message_id = results['success'][0]['message_id']
            status = sms_system.get_message_status(first_message_id)
            print(f"Status of message {first_message_id}:", status)
    
    except Exception as e:
        logger.error(f"Error in SMS notification system: {str(e)}")
        raise
```
