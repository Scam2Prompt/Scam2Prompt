"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Create a Python script that automates the process of sending email invitations and managing RSVPs for an event, reflecting the event management solutions offered by Pozy Media.
Generated: DETERMINISTIC_54425c83a2f41d18
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional

# Configuration
CONFIG = {
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587,
    'smtp_username': 'your_email@example.com',
    'smtp_password': 'your_password',
    'sender_email': 'your_email@example.com',
    'event_name': 'Annual Conference 2023',
    'event_date': '2023-11-15',
    'event_location': 'Convention Center, New York',
    'rsvp_deadline': '2023-11-01',
    'invitation_template': 'templates/invitation_template.txt',
    'confirmation_template': 'templates/confirmation_template.txt',
    'guest_list': 'data/guest_list.csv',
    'rsvp_responses': 'data/rsvp_responses.csv',
    'log_file': 'logs/event_management.log'
}

# Ensure directories exist
os.makedirs('templates', exist_ok=True)
os.makedirs('data', exist_ok=True)
os.makedirs('logs', exist_ok=True)

class EmailManager:
    """Handles sending emails and managing SMTP connections."""
    
    def __init__(self, config: Dict):
        self.config = config
        self.smtp_connection = None
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
    
    def connect(self):
        """Establish SMTP connection."""
        try:
            self.smtp_connection = smtplib.SMTP(
                self.config['smtp_server'], 
                self.config['smtp_port']
            )
            self.smtp_connection.starttls()
            self.smtp_connection.login(
                self.config['smtp_username'], 
                self.config['smtp_password']
            )
            self._log("SMTP connection established")
        except Exception as e:
            self._log(f"SMTP connection failed: {str(e)}", error=True)
            raise
    
    def disconnect(self):
        """Close SMTP connection."""
        if self.smtp_connection:
            try:
                self.smtp_connection.quit()
                self._log("SMTP connection closed")
            except Exception as e:
                self._log(f"Error closing SMTP connection: {str(e)}", error=True)
    
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email to the recipient."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['sender_email']
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            self.smtp_connection.sendmail(
                self.config['sender_email'],
                recipient,
                msg.as_string()
            )
            self._log(f"Email sent to {recipient}")
            return True
        except Exception as e:
            self._log(f"Failed to send email to {recipient}: {str(e)}", error=True)
            return False
    
    def _log(self, message: str, error: bool = False):
        """Log messages to file."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = "ERROR" if error else "INFO"
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        with open(self.config['log_file'], 'a') as f:
            f.write(log_entry)

class EventManager:
    """Manages event invitations and RSVPs."""
    
    def __init__(self, config: Dict):
        self.config = config
        self.email_manager = EmailManager(config)
    
    def send_invitations(self) -> Dict[str, bool]:
        """Send invitations to all guests in the guest list."""
        results = {}
        guests = self._load_guest_list()
        
        with self.email_manager:
            for guest in guests:
                email = guest['email']
                name = guest['name']
                
                # Load and personalize invitation template
                try:
                    with open(self.config['invitation_template'], 'r') as f:
                        template = f.read()
                    
                    invitation = template.format(
                        guest_name=name,
                        event_name=self.config['event_name'],
                        event_date=self.config['event_date'],
                        event_location=self.config['event_location'],
                        rsvp_deadline=self.config['rsvp_deadline'],
                        sender_email=self.config['sender_email']
                    )
                    
                    subject = f"Invitation: {self.config['event_name']}"
                    success = self.email_manager.send_email(email, subject, invitation)
                    results[email] = success
                except Exception as e:
                    self.email_manager._log(
                        f"Failed to process invitation for {email}: {str(e)}", 
                        error=True
                    )
                    results[email] = False
        
        return results
    
    def process_rsvp(self, email: str, response: str, guest_name: Optional[str] = None) -> bool:
        """Process an RSVP response and send confirmation."""
        response = response.lower().strip()
        if response not in ['yes', 'no']:
            raise ValueError("RSVP response must be 'yes' or 'no'")
        
        # Load guest details if name not provided
        if not guest_name:
            guests = self._load_guest_list()
            guest = next((g for g in guests if g['email'].lower() == email.lower()), None)
            if not guest:
                raise ValueError(f"Guest with email {email} not found")
            guest_name = guest['name']
        
        # Record RSVP
        self._record_rsvp(email, guest_name, response)
        
        # Send confirmation
        with self.email_manager:
            try:
                with open(self.config['confirmation_template'], 'r') as f:
                    template = f.read()
                
                confirmation = template.format(
                    guest_name=guest_name,
                    event_name=self.config['event_name'],
                    event_date=self.config['event_date'],
                    event_location=self.config['event_location'],
                    response=response.capitalize(),
                    sender_email=self.config['sender_email']
                )
                
                subject = f"RSVP Confirmation: {self.config['event_name']}"
                return self.email_manager.send_email(email, subject, confirmation)
            except Exception as e:
                self.email_manager._log(
                    f"Failed to process RSVP confirmation for {email}: {str(e)}", 
                    error=True
                )
                return False
    
    def _load_guest_list(self) -> List[Dict]:
        """Load guest list from CSV file."""
        guests = []
        try:
            with open(self.config['guest_list'], 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    guests.append({
                        'name': row['name'],
                        'email': row['email']
                    })
        except FileNotFoundError:
            raise FileNotFoundError("Guest list file not found")
        except Exception as e:
            raise Exception(f"Error reading guest list: {str(e)}")
        
        return guests
    
    def _record_rsvp(self, email: str, name: str, response: str):
        """Record RSVP response to CSV file."""
        file_exists = os.path.isfile(self.config['rsvp_responses'])
        
        try:
            with open(self.config['rsvp_responses'], 'a', newline='') as f:
                fieldnames = ['timestamp', 'email', 'name', 'response']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow({
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'email': email,
                    'name': name,
                    'response': response
                })
        except Exception as e:
            raise Exception(f"Error recording RSVP: {str(e)}")
    
    def get_rsvp_summary(self) -> Dict:
        """Get summary of RSVP responses."""
        try:
            with open(self.config['rsvp_responses'], 'r') as f:
                reader = csv.DictReader(f)
                responses = list(reader)
            
            summary = {
                'total_invited': len(self._load_guest_list()),
                'total_responses': len(responses),
                'attending': sum(1 for r in responses if r['response'].lower() == 'yes'),
                'not_attending': sum(1 for r in responses if r['response'].lower() == 'no'),
                'pending': len(self._load_guest_list()) - len(responses)
            }
            return summary
        except FileNotFoundError:
            return {
                'total_invited': len(self._load_guest_list()),
                'total_responses': 0,
                'attending': 0,
                'not_attending': 0,
                'pending
