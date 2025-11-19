"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Generate a code snippet for a conference registration system that includes features like abstract submission, registration, and invitation letter generation, inspired by Conferences Global's conference management process.
Generated: DETERMINISTIC_bdc37122d7035757
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import uuid

# Constants
CONFIG_FILE = "config.json"
TEMPLATES_DIR = "templates"
REGISTRATIONS_DB = "registrations.json"
ABSTRACTS_DB = "abstracts.json"

# Data Models
@dataclass
class Attendee:
    id: str
    name: str
    email: str
    affiliation: str
    registration_date: str
    registration_type: str  # e.g., "regular", "student", "speaker"
    paid: bool = False

@dataclass
class Abstract:
    id: str
    author_id: str
    title: str
    content: str
    submission_date: str
    status: str = "pending"  # "pending", "accepted", "rejected"

class ConferenceRegistrationSystem:
    def __init__(self):
        self._load_config()
        self._setup_templates()
        self._load_databases()

    def _load_config(self):
        """Load system configuration from file."""
        try:
            with open(CONFIG_FILE, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise Exception("Configuration file not found")
        except json.JSONDecodeError:
            raise Exception("Invalid configuration file")

    def _setup_templates(self):
        """Initialize template environment."""
        if not os.path.exists(TEMPLATES_DIR):
            os.makedirs(TEMPLATES_DIR)
        self.env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    def _load_databases(self):
        """Load or initialize registration and abstract databases."""
        for db_file in [REGISTRATIONS_DB, ABSTRACTS_DB]:
            if not os.path.exists(db_file):
                with open(db_file, 'w') as f:
                    json.dump([], f)

    def register_attendee(self, name: str, email: str, affiliation: str, registration_type: str) -> str:
        """Register a new attendee."""
        attendee_id = str(uuid.uuid4())
        new_attendee = Attendee(
            id=attendee_id,
            name=name,
            email=email,
            affiliation=affiliation,
            registration_date=datetime.now().isoformat(),
            registration_type=registration_type
        )

        try:
            with open(REGISTRATIONS_DB, 'r+') as f:
                attendees = json.load(f)
                attendees.append(asdict(new_attendee))
                f.seek(0)
                json.dump(attendees, f, indent=2)
            return attendee_id
        except Exception as e:
            raise Exception(f"Failed to register attendee: {str(e)}")

    def submit_abstract(self, author_id: str, title: str, content: str) -> str:
        """Submit a new abstract."""
        abstract_id = str(uuid.uuid4())
        new_abstract = Abstract(
            id=abstract_id,
            author_id=author_id,
            title=title,
            content=content,
            submission_date=datetime.now().isoformat()
        )

        try:
            with open(ABSTRACTS_DB, 'r+') as f:
                abstracts = json.load(f)
                abstracts.append(asdict(new_abstract))
                f.seek(0)
                json.dump(abstracts, f, indent=2)
            return abstract_id
        except Exception as e:
            raise Exception(f"Failed to submit abstract: {str(e)}")

    def generate_invitation_letter(self, attendee_id: str) -> str:
        """Generate an invitation letter for an attendee."""
        try:
            with open(REGISTRATIONS_DB, 'r') as f:
                attendees = json.load(f)
                attendee = next((a for a in attendees if a['id'] == attendee_id), None)
                if not attendee:
                    raise Exception("Attendee not found")

            template = self.env.get_template("invitation_letter.html")
            letter = template.render(
                attendee=attendee,
                conference=self.config['conference'],
                date=datetime.now().strftime("%B %d, %Y")
            )
            return letter
        except Exception as e:
            raise Exception(f"Failed to generate invitation letter: {str(e)}")

    def send_invitation_email(self, attendee_id: str) -> bool:
        """Send invitation email with attached letter."""
        try:
            letter = self.generate_invitation_letter(attendee_id)
            
            with open(REGISTRATIONS_DB, 'r') as f:
                attendees = json.load(f)
                attendee = next((a for a in attendees if a['id'] == attendee_id), None)
                if not attendee:
                    raise Exception("Attendee not found")

            msg = MIMEMultipart()
            msg['From'] = self.config['email']['sender']
            msg['To'] = attendee['email']
            msg['Subject'] = f"Invitation to {self.config['conference']['name']}"

            body = MIMEText(letter, 'html')
            msg.attach(body)

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
            
            return True
        except Exception as e:
            raise Exception(f"Failed to send invitation email: {str(e)}")

    def get_attendee(self, attendee_id: str) -> Optional[Dict]:
        """Retrieve attendee information."""
        try:
            with open(REGISTRATIONS_DB, 'r') as f:
                attendees = json.load(f)
                return next((a for a in attendees if a['id'] == attendee_id), None)
        except Exception as e:
            raise Exception(f"Failed to retrieve attendee: {str(e)}")

    def get_abstract(self, abstract_id: str) -> Optional[Dict]:
        """Retrieve abstract information."""
        try:
            with open(ABSTRACTS_DB, 'r') as f:
                abstracts = json.load(f)
                return next((a for a in abstracts if a['id'] == abstract_id), None)
        except Exception as e:
            raise Exception(f"Failed to retrieve abstract: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        system = ConferenceRegistrationSystem()
        
        # Register attendee
        attendee_id = system.register_attendee(
            name="John Doe",
            email="john@example.com",
            affiliation="University of Example",
            registration_type="regular"
        )
        print(f"Registered attendee with ID: {attendee_id}")

        # Submit abstract
        abstract_id = system.submit_abstract(
            author_id=attendee_id,
            title="Advanced Conference Systems",
            content="A study of modern conference management systems..."
        )
        print(f"Submitted abstract with ID: {abstract_id}")

        # Generate invitation letter
        letter = system.generate_invitation_letter(attendee_id)
        print("Generated invitation letter")

        # Send invitation email
        if system.send_invitation_email(attendee_id):
            print("Invitation email sent successfully")

    except Exception as e:
        print(f"Error: {str(e)}")
```
