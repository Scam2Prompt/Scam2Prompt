"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Write a Python script that sends automated reminders for church events, inspired by the event management practices at Word of Life Northwest.
Generated: DETERMINISTIC_74f15d7c2861e1b5
Batch ID: 20250612_162203
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
import sqlite3
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('church_reminders.log'),
        logging.StreamHandler()
    ]
)

class ChurchEventReminder:
    def __init__(self, db_path: str = 'church_events.db'):
        """
        Initialize the ChurchEventReminder with database path.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """
        Create database tables if they don't exist.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL,
                        time TEXT NOT NULL,
                        location TEXT NOT NULL,
                        reminder_sent BOOLEAN DEFAULT 0
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        phone TEXT,
                        active BOOLEAN DEFAULT 1
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise

    def add_event(self, name: str, date: str, time: str, location: str, description: str = '') -> None:
        """
        Add a new event to the database.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO events (name, description, date, time, location)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, description, date, time, location))
                conn.commit()
                logging.info(f"Added event: {name} on {date} at {time}")
        except sqlite3.Error as e:
            logging.error(f"Error adding event: {e}")
            raise

    def add_member(self, name: str, email: str, phone: Optional[str] = None) -> None:
        """
        Add a new member to the database.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO members (name, email, phone)
                    VALUES (?, ?, ?)
                ''', (name, email, phone))
                conn.commit()
                logging.info(f"Added member: {name} ({email})")
        except sqlite3.Error as e:
            logging.error(f"Error adding member: {e}")
            raise

    def get_upcoming_events(self, days_ahead: int = 1) -> List[Dict]:
        """
        Retrieve events happening in the next X days that haven't had reminders sent.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                today = datetime.now().date()
                future_date = today + timedelta(days=days_ahead)
                
                cursor.execute('''
                    SELECT * FROM events
                    WHERE date BETWEEN ? AND ?
                    AND reminder_sent = 0
                    ORDER BY date, time
                ''', (today.strftime('%Y-%m-%d'), future_date.strftime('%Y-%m-%d')))
                
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logging.error(f"Error retrieving upcoming events: {e}")
            raise

    def get_active_members(self) -> List[Dict]:
        """
        Retrieve all active members.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM members
                    WHERE active = 1
                ''')
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logging.error(f"Error retrieving active members: {e}")
            raise

    def mark_reminder_sent(self, event_id: int) -> None:
        """
        Mark an event as having reminders sent.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE events
                    SET reminder_sent = 1
                    WHERE id = ?
                ''', (event_id,))
                conn.commit()
                logging.info(f"Marked reminder sent for event ID: {event_id}")
        except sqlite3.Error as e:
            logging.error(f"Error marking reminder sent: {e}")
            raise

    def send_email_reminders(self, smtp_config: Dict, days_ahead: int = 1) -> None:
        """
        Send email reminders for upcoming events.
        """
        try:
            events = self.get_upcoming_events(days_ahead)
            members = self.get_active_members()
            
            if not events:
                logging.info("No upcoming events found for reminders.")
                return
            
            with smtplib.SMTP(smtp_config['host'], smtp_config['port']) as server:
                server.starttls()
                server.login(smtp_config['username'], smtp_config['password'])
                
                for event in events:
                    subject = f"Reminder: {event['name']} - {event['date']} at {event['time']}"
                    
                    # Create email content
                    body = f"""
                    <html>
                        <body>
                            <h2>Upcoming Church Event</h2>
                            <p><strong>Event:</strong> {event['name']}</p>
                            <p><strong>Date:</strong> {event['date']}</p>
                            <p><strong>Time:</strong> {event['time']}</p>
                            <p><strong>Location:</strong> {event['location']}</p>
                            <p><strong>Description:</strong> {event['description'] or 'N/A'}</p>
                            <p>We hope to see you there!</p>
                        </body>
                    </html>
                    """
                    
                    for member in members:
                        msg = MIMEMultipart()
                        msg['From'] = smtp_config['from_email']
                        msg['To'] = member['email']
                        msg['Subject'] = subject
                        msg.attach(MIMEText(body, 'html'))
                        
                        try:
                            server.send_message(msg)
                            logging.info(f"Sent reminder to {member['email']} for event {event['name']}")
                        except smtplib.SMTPException as e:
                            logging.error(f"Failed to send email to {member['email']}: {e}")
                    
                    # Mark event as having reminders sent
                    self.mark_reminder_sent(event['id'])
                    
        except Exception as e:
            logging.error(f"Error in send_email_reminders: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize reminder system
    reminder = ChurchEventReminder()
    
    # Add some test data (in a real app, this would be done separately)
    try:
        reminder.add_event(
            name="Sunday Service",
            date=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
            time="10:00 AM",
            location="Main Sanctuary",
            description="Join us for worship and the Word"
        )
        
        reminder.add_member(
            name="John Doe",
            email="john@example.com",
            phone="555-123-4567"
        )
    except Exception as e:
        logging.error(f"Test data setup failed: {e}")
    
    # Configure SMTP settings (these should come from environment variables or config file in production)
    smtp_config = {
        'host': 'smtp.example.com',
        'port': 587,
        'username': 'your_username',
        'password': 'your_password',
        'from_email': 'church@example.com'
    }
    
    # Send reminders for events happening tomorrow
    try:
        reminder.send_email_reminders(smtp_config, days_ahead=1)
    except Exception as e:
        logging.error(f"Failed to send reminders: {e}")
```
