"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a module to manage pre-admission processes for schools, automating tasks such as application tracking, inspired by Him Saral's Pre Admission module.
Generated: DETERMINISTIC_85cd17596cd25085
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pre-Admission Management Module for Schools

This module automates the pre-admission process including application tracking,
status updates, and communication with applicants.

Features:
- Application submission and tracking
- Status updates (Pending, Reviewed, Accepted, Rejected)
- Automated notifications
- Reporting and analytics
"""

import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
from dataclasses import dataclass, field

# Constants
APPLICATIONS_FILE = "applications.json"
CONFIG_FILE = "config.json"

class ApplicationStatus(Enum):
    """Enum representing possible application statuses."""
    PENDING = auto()
    REVIEWED = auto()
    ACCEPTED = auto()
    REJECTED = auto()

@dataclass
class Applicant:
    """Data class representing an applicant."""
    id: str
    name: str
    email: str
    phone: str
    address: str
    birth_date: str
    applied_date: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    status: ApplicationStatus = ApplicationStatus.PENDING
    notes: str = ""
    documents: List[str] = field(default_factory=list)

class PreAdmissionManager:
    """Main class for managing pre-admission processes."""
    
    def __init__(self):
        """Initialize the manager with loaded applications and configuration."""
        self.applications: Dict[str, Applicant] = {}
        self.config = self._load_config()
        self._load_applications()
    
    def _load_config(self) -> Dict:
        """Load configuration from file."""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            return {
                "smtp_server": "",
                "smtp_port": 587,
                "email": "",
                "password": "",
                "notification_templates": {
                    "submission": "Thank you for your application.",
                    "status_update": "Your application status has been updated."
                }
            }
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}
    
    def _save_config(self) -> bool:
        """Save configuration to file."""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def _load_applications(self) -> None:
        """Load applications from storage file."""
        try:
            if os.path.exists(APPLICATIONS_FILE):
                with open(APPLICATIONS_FILE, 'r') as f:
                    data = json.load(f)
                    for app_id, app_data in data.items():
                        app_data['status'] = ApplicationStatus[app_data['status']]
                        self.applications[app_id] = Applicant(**app_data)
        except Exception as e:
            print(f"Error loading applications: {e}")
    
    def _save_applications(self) -> bool:
        """Save applications to storage file."""
        try:
            apps_to_save = {}
            for app_id, applicant in self.applications.items():
                app_dict = applicant.__dict__.copy()
                app_dict['status'] = applicant.status.name
                apps_to_save[app_id] = app_dict
            
            with open(APPLICATIONS_FILE, 'w') as f:
                json.dump(apps_to_save, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving applications: {e}")
            return False
    
    def submit_application(self, applicant_data: Dict) -> Optional[Applicant]:
        """Submit a new application."""
        try:
            if not all(key in applicant_data for key in ['name', 'email', 'phone', 'address', 'birth_date']):
                raise ValueError("Missing required applicant information")
            
            app_id = f"APP-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
            applicant = Applicant(id=app_id, **applicant_data)
            self.applications[app_id] = applicant
            self._save_applications()
            self._send_notification(applicant.email, "submission")
            return applicant
        except Exception as e:
            print(f"Error submitting application: {e}")
            return None
    
    def update_application_status(self, app_id: str, status: ApplicationStatus, notes: str = "") -> bool:
        """Update the status of an application."""
        try:
            if app_id not in self.applications:
                raise ValueError("Application not found")
            
            applicant = self.applications[app_id]
            applicant.status = status
            applicant.notes = notes
            self._save_applications()
            self._send_notification(applicant.email, "status_update")
            return True
        except Exception as e:
            print(f"Error updating application status: {e}")
            return False
    
    def get_application(self, app_id: str) -> Optional[Applicant]:
        """Retrieve an application by ID."""
        return self.applications.get(app_id)
    
    def list_applications(self, status: Optional[ApplicationStatus] = None) -> List[Applicant]:
        """List all applications, optionally filtered by status."""
        if status:
            return [app for app in self.applications.values() if app.status == status]
        return list(self.applications.values())
    
    def _send_notification(self, recipient: str, template_type: str) -> bool:
        """Send email notification to applicant."""
        try:
            if not self.config.get('smtp_server') or not self.config.get('email'):
                return False
            
            msg = MIMEMultipart()
            msg['From'] = self.config['email']
            msg['To'] = recipient
            msg['Subject'] = "Application Status Update"
            
            template = self.config['notification_templates'].get(template_type, "")
            msg.attach(MIMEText(template, 'plain'))
            
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['email'], self.config['password'])
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending notification: {e}")
            return False
    
    def generate_report(self) -> Dict:
        """Generate a report of application statistics."""
        report = {
            "total_applications": len(self.applications),
            "status_counts": {
                status.name: 0 for status in ApplicationStatus
            },
            "last_updated": datetime.datetime.now().isoformat()
        }
        
        for app in self.applications.values():
            report["status_counts"][app.status.name] += 1
        
        return report
    
    def configure_smtp(self, server: str, port: int, email: str, password: str) -> bool:
        """Configure SMTP settings for email notifications."""
        try:
            self.config.update({
                "smtp_server": server,
                "smtp_port": port,
                "email": email,
                "password": password
            })
            return self._save_config()
        except Exception as e:
            print(f"Error configuring SMTP: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = PreAdmissionManager()
    
    # Example: Submit an application
    new_applicant = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "birth_date": "2000-01-01"
    }
    
    application = manager.submit_application(new_applicant)
    if application:
        print(f"Application submitted with ID: {application.id}")
    
    # Example: Update status
    if application:
        manager.update_application_status(application.id, ApplicationStatus.REVIEWED, "Under review")
    
    # Example: Generate report
    print(manager.generate_report())
```
