"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Create a code snippet that automates the enrollment process for a training program like those offered by SMART Training Resources.
Generated: DETERMINISTIC_51e1d403625aee7f
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional

class EnrollmentAutomation:
    """
    Automates the enrollment process for a training program.
    Handles participant registration, confirmation emails, and CSV exports.
    """

    def __init__(self, smtp_server: str, smtp_port: int, email: str, password: str):
        """
        Initialize with SMTP server details for email notifications.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        self.participants = []

    def register_participant(self, name: str, email: str, course: str, **kwargs) -> Dict:
        """
        Register a new participant with their details.
        Returns the participant record.
        """
        participant = {
            'name': name,
            'email': email,
            'course': course,
            'status': 'registered',
            **kwargs
        }
        self.participants.append(participant)
        return participant

    def send_confirmation_email(self, participant: Dict) -> bool:
        """
        Send a confirmation email to the registered participant.
        Returns True if successful.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = participant['email']
            msg['Subject'] = f"Confirmation: Enrollment in {participant['course']}"

            body = f"""
            Dear {participant['name']},

            Thank you for enrolling in {participant['course']}.
            
            Your registration is confirmed. We'll send further details shortly.

            Regards,
            SMART Training Resources
            """
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            participant['status'] = 'confirmed'
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            participant['status'] = 'error'
            return False

    def export_to_csv(self, filename: str) -> bool:
        """
        Export participant data to a CSV file.
        Returns True if successful.
        """
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = list(self.participants[0].keys()) if self.participants else []
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.participants)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False

    def process_enrollment(self, name: str, email: str, course: str, **kwargs) -> bool:
        """
        Complete enrollment process: register, send email, and update status.
        Returns True if all steps successful.
        """
        participant = self.register_participant(name, email, course, **kwargs)
        email_sent = self.send_confirmation_email(participant)
        return email_sent
```
