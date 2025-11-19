"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Write a Python script that automates the admission process for the IESTP PANGOA, including handling applications and notifying applicants.
Generated: DETERMINISTIC_a1569151dff0a546
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Configure logging for the application
logging.basicConfig(filename='admissions.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Application:
    """Class to represent a single application."""
    
    def __init__(self, name: str, email: str, program: str):
        self.name = name
        self.email = email
        self.program = program
        self.status = 'Received'  # Initial status

    def to_dict(self) -> Dict:
        """Convert application to dictionary."""
        return {
            'name': self.name,
            'email': self.email,
            'program': self.program,
            'status': self.status
        }

class Admissions:
    """Class to handle admissions processing."""
    
    def __init__(self, applications_file: str):
        self.applications_file = applications_file
        self.applications = self.load_applications()

    def load_applications(self) -> List[Application]:
        """Load applications from a JSON file."""
        try:
            with open(self.applications_file, 'r') as file:
                data = json.load(file)
                return [Application(**app) for app in data]
        except FileNotFoundError:
            logging.error("Applications file not found.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the applications file.")
            return []

    def save_applications(self):
        """Save applications to a JSON file."""
        try:
            with open(self.applications_file, 'w') as file:
                json.dump([app.to_dict() for app in self.applications], file, indent=4)
        except IOError as e:
            logging.error(f"Error saving applications: {e}")

    def notify_applicant(self, applicant: Application):
        """Send notification email to the applicant."""
        try:
            # Email configuration
            sender_email = "admissions@iestpangoa.edu"
            sender_password = "password"  # Use a secure method to handle passwords
            subject = "Application Status Update"
            body = f"Dear {applicant.name},\n\nYour application for the {applicant.program} program has been {applicant.status}.\n\nBest regards,\nAdmissions Office"

            # Create email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = applicant.email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)

            logging.info(f"Notification sent to {applicant.email} regarding {applicant.status}.")
        except Exception as e:
            logging.error(f"Failed to send email to {applicant.email}: {e}")

    def process_applications(self):
        """Process each application and send notifications."""
        for application in self.applications:
            # Here we can add logic to update application status
            application.status = 'Under Review'  # Example status update
            self.notify_applicant(application)

        # Save updated applications
        self.save_applications()

if __name__ == "__main__":
    admissions = Admissions('applications.json')
    admissions.process_applications()
```

Make sure to replace `sender_email` and `sender_password` with your actual email credentials, and consider using environment variables or secure vaults to manage sensitive information in a production setting.
