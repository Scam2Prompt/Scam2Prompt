"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Write a Python script that automates the process of sending reminders for new makeup classes and live sessions to members of a beauty school like Ju Ensina.
Generated: DETERMINISTIC_36bc695179243eac
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import sqlite3
from typing import List, Dict
import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reminder_logs.log'),
        logging.StreamHandler()
    ]
)

# Load environment variables
load_dotenv()

class DatabaseManager:
    """Handles database operations for member and class data."""
    
    def __init__(self, db_path: str = 'beauty_school.db'):
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self):
        """Initialize database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create members table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    subscription_date TEXT NOT NULL,
                    active INTEGER DEFAULT 1
                )
            ''')
            
            # Create classes table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS classes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    instructor TEXT NOT NULL,
                    schedule_time TEXT NOT NULL,
                    class_type TEXT NOT NULL,  -- 'makeup' or 'live_session'
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create sent_reminders table to track sent reminders
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sent_reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    class_id INTEGER NOT NULL,
                    sent_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (member_id) REFERENCES members(id),
                    FOREIGN KEY (class_id) REFERENCES classes(id)
                )
            ''')
            
            conn.commit()
    
    def get_active_members(self) -> List[Dict]:
        """Retrieve all active members from the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM members WHERE active = 1')
            return [dict(row) for row in cursor.fetchall()]
    
    def get_upcoming_classes(self, days_ahead: int = 7) -> List[Dict]:
        """Retrieve upcoming classes within the specified days."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            end_date = (datetime.now() + timedelta(days=days_ahead)).strftime('%Y-%m-%d %H:%M:%S')
            
            cursor.execute('''
                SELECT * FROM classes 
                WHERE schedule_time BETWEEN ? AND ?
                ORDER BY schedule_time ASC
            ''', (start_date, end_date))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def is_reminder_sent(self, member_id: int, class_id: int) -> bool:
        """Check if a reminder has already been sent for this member and class."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT 1 FROM sent_reminders 
                WHERE member_id = ? AND class_id = ?
                LIMIT 1
            ''', (member_id, class_id))
            return cursor.fetchone() is not None
    
    def mark_reminder_sent(self, member_id: int, class_id: int) -> None:
        """Record that a reminder has been sent."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO sent_reminders (member_id, class_id)
                VALUES (?, ?)
            ''', (member_id, class_id))
            conn.commit()

class EmailSender:
    """Handles sending email reminders."""
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_username = os.getenv('SMTP_USERNAME')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.sender_email = os.getenv('SENDER_EMAIL')
    
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email to the specified recipient."""
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient
            message['Subject'] = subject
            
            message.attach(MIMEText(body, 'html'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(message)
            
            return True
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {str(e)}")
            return False

class ReminderGenerator:
    """Generates reminder content for classes."""
    
    @staticmethod
    def generate_class_reminder(member_name: str, class_info: Dict) -> Dict[str, str]:
        """Generate email subject and body for a class reminder."""
        class_type = "Makeup Class" if class_info['class_type'] == 'makeup' else "Live Session"
        schedule_time = datetime.strptime(class_info['schedule_time'], '%Y-%m-%d %H:%M:%S')
        
        subject = f"Reminder: Upcoming {class_type} - {class_info['title']}"
        
        body = f"""
        <html>
            <body>
                <p>Dear {member_name},</p>
                <p>This is a friendly reminder about your upcoming {class_type}:</p>
                <h3>{class_info['title']}</h3>
                <p><strong>Instructor:</strong> {class_info['instructor']}</p>
                <p><strong>Date & Time:</strong> {schedule_time.strftime('%A, %B %d, %Y at %I:%M %p')}</p>
                <p><strong>Description:</strong> {class_info['description']}</p>
                <p>We look forward to seeing you there!</p>
                <p>Best regards,<br>The Ju Ensina Team</p>
            </body>
        </html>
        """
        
        return {'subject': subject, 'body': body}

class ReminderService:
    """Main service that orchestrates the reminder process."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.email_sender = EmailSender()
    
    def send_reminders(self) -> None:
        """Send reminders for upcoming classes to active members."""
        try:
            members = self.db.get_active_members()
            upcoming_classes = self.db.get_upcoming_classes()
            
            if not upcoming_classes:
                logging.info("No upcoming classes found in the next 7 days.")
                return
            
            for member in members:
                for class_info in upcoming_classes:
                    if not self.db.is_reminder_sent(member['id'], class_info['id']):
                        reminder = ReminderGenerator.generate_class_reminder(
                            member['name'], class_info
                        )
                        
                        if self.email_sender.send_email(
                            member['email'],
                            reminder['subject'],
                            reminder['body']
                        ):
                            self.db.mark_reminder_sent(member['id'], class_info['id'])
                            logging.info(
                                f"Sent reminder to {member['email']} for class {class_info['title']}"
                            )
                        else:
                            logging.warning(
                                f"Failed to send reminder to {member['email']} for class {class_info['title']}"
                            )
            
            logging.info("Reminder sending process completed.")
        except Exception as e:
            logging.error(f"Error in reminder process: {str(e)}", exc_info=True)

if __name__ == "__main__":
    reminder_service = ReminderService()
    reminder_service.send_reminders()
```
