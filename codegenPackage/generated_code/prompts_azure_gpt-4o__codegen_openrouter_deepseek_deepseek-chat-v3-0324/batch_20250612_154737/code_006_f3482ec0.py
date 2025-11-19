"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Develop a script to maximize engagement for a grants program by automating outreach and tracking grantee experiences, referencing Gitcoin's framework.
Generated: DETERMINISTIC_f3482ec054fea8e1
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('grant_engagement.log'),
        logging.StreamHandler()
    ]
)

class Grantee:
    """Class to represent a grantee and their engagement data."""
    
    def __init__(self, name: str, email: str, grant_amount: float, project: str):
        self.name = name
        self.email = email
        self.grant_amount = grant_amount
        self.project = project
        self.engagement_score = 0
        self.last_contact = None
        self.responses = []
    
    def update_engagement(self, score: int, response: Optional[str] = None):
        """Update the engagement score and record response."""
        self.engagement_score += score
        self.last_contact = datetime.now()
        if response:
            self.responses.append(response)
    
    def to_dict(self) -> Dict:
        """Convert grantee data to dictionary for CSV export."""
        return {
            'name': self.name,
            'email': self.email,
            'grant_amount': self.grant_amount,
            'project': self.project,
            'engagement_score': self.engagement_score,
            'last_contact': self.last_contact.strftime('%Y-%m-%d %H:%M:%S') if self.last_contact else None,
            'responses': '|'.join(self.responses) if self.responses else None
        }

class GrantEngagementTracker:
    """Main class to handle grantee engagement tracking and outreach."""
    
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.grantees: List[Grantee] = []
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        
        # Load existing data if available
        self._load_grantees()
    
    def _load_grantees(self):
        """Load grantees from CSV if file exists."""
        try:
            if os.path.exists('grantees.csv'):
                with open('grantees.csv', 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        grantee = Grantee(
                            row['name'],
                            row['email'],
                            float(row['grant_amount']),
                            row['project']
                        )
                        grantee.engagement_score = int(row['engagement_score'])
                        if row['last_contact']:
                            grantee.last_contact = datetime.strptime(row['last_contact'], '%Y-%m-%d %H:%M:%S')
                        if row['responses']:
                            grantee.responses = row['responses'].split('|')
                        self.grantees.append(grantee)
                logging.info(f"Loaded {len(self.grantees)} grantees from file")
        except Exception as e:
            logging.error(f"Error loading grantees: {e}")
    
    def _save_grantees(self):
        """Save current grantees to CSV."""
        try:
            with open('grantees.csv', 'w', newline='') as f:
                if not self.grantees:
                    return
                
                fieldnames = self.grantees[0].to_dict().keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for grantee in self.grantees:
                    writer.writerow(grantee.to_dict())
            logging.info("Saved grantees to file")
        except Exception as e:
            logging.error(f"Error saving grantees: {e}")
    
    def add_grantee(self, name: str, email: str, grant_amount: float, project: str):
        """Add a new grantee to the tracker."""
        try:
            grantee = Grantee(name, email, grant_amount, project)
            self.grantees.append(grantee)
            self._save_grantees()
            logging.info(f"Added new grantee: {name}")
        except Exception as e:
            logging.error(f"Error adding grantee: {e}")
    
    def send_outreach_email(self, grantee: Grantee, template: str) -> bool:
        """Send an outreach email to a grantee."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = grantee.email
            msg['Subject'] = "Follow-up on Your Grant Project"
            
            # Personalize the template
            body = template.format(
                name=grantee.name,
                project=grantee.project,
                amount=grantee.grant_amount
            )
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            grantee.update_engagement(5)  # Basic engagement score for outreach
            self._save_grantees()
            logging.info(f"Sent email to {grantee.name}")
            return True
        except Exception as e:
            logging.error(f"Error sending email to {grantee.name}: {e}")
            return False
    
    def batch_outreach(self, template: str, days_since_last_contact: int = 30):
        """Send outreach emails to grantees who haven't been contacted recently."""
        try:
            count = 0
            for grantee in self.grantees:
                if (grantee.last_contact is None or 
                    (datetime.now() - grantee.last_contact).days >= days_since_last_contact):
                    if self.send_outreach_email(grantee, template):
                        count += 1
            logging.info(f"Sent {count} outreach emails")
            return count
        except Exception as e:
            logging.error(f"Error in batch outreach: {e}")
            return 0
    
    def generate_engagement_report(self) -> str:
        """Generate a report of grantee engagement."""
        try:
            if not self.grantees:
                return "No grantees to report on"
            
            report = []
            report.append("Grantee Engagement Report")
            report.append("=" * 40)
            report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report.append("")
            
            # Sort by engagement score (descending)
            sorted_grantees = sorted(self.grantees, key=lambda x: x.engagement_score, reverse=True)
            
            for i, grantee in enumerate(sorted_grantees, 1):
                report.append(
                    f"{i}. {grantee.name} ({grantee.project}) - "
                    f"Score: {grantee.engagement_score} - "
                    f"Last Contact: {grantee.last_contact.strftime('%Y-%m-%d') if grantee.last_contact else 'Never'}"
                )
            
            report.append("")
            report.append(f"Total Grantees: {len(self.grantees)}")
            report.append(f"Average Engagement Score: {sum(g.engagement_score for g in self.grantees)/len(self.grantees):.1f}")
            
            return "\n".join(report)
        except Exception as e:
            logging.error(f"Error generating engagement report: {e}")
            return f"Error generating report: {e}"

# Example usage
if __name__ == "__main__":
    # Configuration - should be loaded from environment variables in production
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "grants@example.org"
    SENDER_PASSWORD = "securepassword"
    
    # Email template
    EMAIL_TEMPLATE = """Hello {name},

We're following up regarding your grant for {project} (amount: ${amount}). 

We'd love to hear about your progress and any challenges you're facing. Please reply to this email with any updates or if you need additional support.

Best regards,
The Grants Team
"""
    
    # Initialize tracker
    tracker = GrantEngagementTracker(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    
    # Add some example grantees (in real usage, this would come from a database or CSV)
    tracker.add_grantee("Alice Smith", "alice@example.com", 5000, "Open Source Sustainability")
    tracker.add_grantee("Bob Johnson", "bob@example.com", 7500, "Decentralized Identity")
    
    # Perform outreach
    tracker.batch_outreach(EMAIL_TEMPLATE)
    
    # Generate and print report
    print(tracker.generate_engagement_report())
```
