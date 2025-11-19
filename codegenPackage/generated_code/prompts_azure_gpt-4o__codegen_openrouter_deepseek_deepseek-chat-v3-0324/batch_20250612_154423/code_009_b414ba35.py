"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write a program to generate automated reminders for deadlines related to the ENADE exam and professor selection processes, using the timeline provided on the IGEOG website.
Generated: DETERMINISTIC_b414ba35c3947c8c
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional

# Configuration class for email settings and deadlines
class Config:
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    EMAIL_USER = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"
    FROM_EMAIL = "reminders@example.com"
    
    # Deadlines from IGEOG website (example dates - should be updated with actual dates)
    DEADLINES = {
        "ENADE": {
            "Registration Start": datetime.date(2023, 8, 1),
            "Registration End": datetime.date(2023, 8, 31),
            "Exam Date": datetime.date(2023, 11, 26),
            "Results Publication": datetime.date(2024, 1, 15)
        },
        "Professor Selection": {
            "Application Period": datetime.date(2023, 9, 1),
            "Document Submission": datetime.date(2023, 9, 15),
            "Interview Period": datetime.date(2023, 10, 1),
            "Final Results": datetime.date(2023, 10, 30)
        }
    }
    
    REMINDER_DAYS_BEFORE = [7, 3, 1]  # Days before deadline to send reminders

class DeadlineReminder:
    def __init__(self):
        self.today = datetime.date.today()
    
    def get_upcoming_deadlines(self) -> Dict[str, List[Dict[str, datetime.date]]]:
        """Get deadlines that are approaching based on REMINDER_DAYS_BEFORE"""
        upcoming = {"ENADE": [], "Professor Selection": []}
        
        for process, deadlines in Config.DEADLINES.items():
            for name, date in deadlines.items():
                days_until = (date - self.today).days
                if 0 < days_until <= max(Config.REMINDER_DAYS_BEFORE):
                    upcoming[process].append({
                        "name": name,
                        "date": date,
                        "days_until": days_until
                    })
        
        return upcoming
    
    def generate_email_content(self, process: str, deadline: Dict[str, datetime.date]) -> str:
        """Generate email content for the reminder"""
        deadline_name = deadline["name"]
        deadline_date = deadline["date"].strftime("%d/%m/%Y")
        days_until = deadline["days_until"]
        
        subject = f"Reminder: {process} - {deadline_name}"
        
        body = f"""
        <html>
            <body>
                <h2>{process} Deadline Reminder</h2>
                <p>
                    This is a reminder about the upcoming deadline for <strong>{deadline_name}</strong> 
                    in the {process} process.
                </p>
                <p>
                    <strong>Deadline:</strong> {deadline_date}<br>
                    <strong>Days remaining:</strong> {days_until}
                </p>
                <p>
                    Please make sure to complete all required actions before this date.
                </p>
                <p>
                    Best regards,<br>
                    IGEOG Reminder System
                </p>
            </body>
        </html>
        """
        
        return subject, body
    
    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        """Send reminder email to the recipient"""
        try:
            msg = MIMEMultipart()
            msg["From"] = Config.FROM_EMAIL
            msg["To"] = to_email
            msg["Subject"] = subject
            
            msg.attach(MIMEText(body, "html"))
            
            with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
                server.starttls()
                server.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def should_send_reminder(self, days_until: int) -> bool:
        """Check if a reminder should be sent today based on REMINDER_DAYS_BEFORE"""
        return days_until in Config.REMINDER_DAYS_BEFORE
    
    def send_reminders(self, recipient_emails: List[str]) -> None:
        """Main method to check deadlines and send reminders"""
        upcoming_deadlines = self.get_upcoming_deadlines()
        
        for process, deadlines in upcoming_deadlines.items():
            for deadline in deadlines:
                if self.should_send_reminder(deadline["days_until"]):
                    subject, body = self.generate_email_content(process, deadline)
                    for email in recipient_emails:
                        success = self.send_email(email, subject, body)
                        if success:
                            print(f"Reminder sent to {email} for {process} - {deadline['name']}")
                        else:
                            print(f"Failed to send reminder to {email}")

# Example usage
if __name__ == "__main__":
    # Replace with actual recipient emails
    recipients = ["professor1@example.com", "professor2@example.com", "student@example.com"]
    
    reminder = DeadlineReminder()
    reminder.send_reminders(recipients)
```
