"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: Provide a Python script for scheduling marketing consultations via email or WhatsApp, inspired by the consultation scheduling feature on Tara Media Works' website.
Generated: DETERMINISTIC_760041ede52dcfa6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import json
import logging
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import pytz

# Configuration
CONFIG_FILE = 'config.json'
TIMEZONE = 'America/New_York'

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('consultation_scheduler.log'),
        logging.StreamHandler()
    ]
)

class ConsultationScheduler:
    def __init__(self):
        self.config = self._load_config()
        self.timezone = pytz.timezone(TIMEZONE)
        
    def _load_config(self):
        """Load configuration from JSON file"""
        try:
            with open(CONFIG_FILE) as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Configuration file {CONFIG_FILE} not found")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in configuration file {CONFIG_FILE}")
            raise

    def _validate_consultation_request(self, request):
        """Validate consultation request data"""
        required_fields = ['name', 'contact_method', 'contact_info', 'preferred_time']
        for field in required_fields:
            if field not in request or not request[field]:
                raise ValueError(f"Missing required field: {field}")
        
        if request['contact_method'] not in ['email', 'whatsapp']:
            raise ValueError("Invalid contact method. Must be 'email' or 'whatsapp'")
        
        try:
            datetime.strptime(request['preferred_time'], '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Invalid preferred_time format. Use 'YYYY-MM-DD HH:MM'")

    def _send_email(self, recipient, subject, body):
        """Send email using SMTP"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email']['sender']
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(
                self.config['email']['smtp_server'], 
                self.config['email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email']['username'],
                    self.config['email']['password']
                )
                server.send_message(msg)
            logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            raise

    def _send_whatsapp(self, recipient, message):
        """Send WhatsApp message using Twilio"""
        try:
            client = Client(
                self.config['whatsapp']['account_sid'],
                self.config['whatsapp']['auth_token']
            )
            
            message = client.messages.create(
                body=message,
                from_=f"whatsapp:{self.config['whatsapp']['twilio_number']}",
                to=f"whatsapp:{recipient}"
            )
            logging.info(f"WhatsApp message sent to {recipient}")
            return message.sid
        except Exception as e:
            logging.error(f"Failed to send WhatsApp message: {str(e)}")
            raise

    def _generate_confirmation_message(self, request):
        """Generate confirmation message based on request"""
        preferred_time = datetime.strptime(request['preferred_time'], '%Y-%m-%d %H:%M')
        localized_time = self.timezone.localize(preferred_time)
        
        return (
            f"Hi {request['name']},\n\n"
            f"Thank you for scheduling a marketing consultation with Tara Media Works!\n\n"
            f"Your consultation is scheduled for:\n"
            f"{localized_time.strftime('%A, %B %d, %Y at %I:%M %p')} {TIMEZONE}\n\n"
            f"We'll contact you via {request['contact_method']} at {request['contact_info']} "
            f"to confirm and provide meeting details.\n\n"
            f"Looking forward to our conversation!\n\n"
            f"Best regards,\n"
            f"The Tara Media Works Team"
        )

    def schedule_consultation(self, request):
        """Main method to schedule a consultation"""
        try:
            # Validate request
            self._validate_consultation_request(request)
            
            # Generate confirmation message
            message = self._generate_confirmation_message(request)
            
            # Send confirmation based on contact method
            if request['contact_method'] == 'email':
                subject = "Your Marketing Consultation Confirmation"
                self._send_email(request['contact_info'], subject, message)
            else:
                self._send_whatsapp(request['contact_info'], message)
            
            # Log successful scheduling
            logging.info(
                f"Consultation scheduled for {request['name']} at {request['preferred_time']}"
            )
            return True
        except Exception as e:
            logging.error(f"Failed to schedule consultation: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    scheduler = ConsultationScheduler()
    
    # Sample request
    consultation_request = {
        "name": "John Doe",
        "contact_method": "email",  # or "whatsapp"
        "contact_info": "john@example.com",  # or "+1234567890" for WhatsApp
        "preferred_time": "2023-12-15 14:30",
        "notes": "Interested in social media marketing"
    }
    
    success = scheduler.schedule_consultation(consultation_request)
    if success:
        print("Consultation scheduled successfully!")
    else:
        print("Failed to schedule consultation. Please check logs for details.")
```
