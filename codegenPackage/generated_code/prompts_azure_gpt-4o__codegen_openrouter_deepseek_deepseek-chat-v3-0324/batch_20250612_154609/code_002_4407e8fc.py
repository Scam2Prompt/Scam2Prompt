"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Generate code to automate event scheduling and notifications for a public policy conference hosted by an organization like IACI.
Generated: DETERMINISTIC_4407e8fc2513d244
Batch ID: 20250612_154609
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
import sqlite3
from typing import List, Dict, Optional

# Database setup and management
class DatabaseManager:
    def __init__(self, db_name: str = "conference_scheduler.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary tables for events and attendees."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                start_time DATETIME NOT NULL,
                end_time DATETIME NOT NULL,
                location TEXT NOT NULL,
                max_attendees INTEGER,
                current_attendees INTEGER DEFAULT 0
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (event_id) REFERENCES events (id)
            )
        """)
        self.conn.commit()

    def add_event(self, title: str, description: str, start_time: datetime.datetime,
                  end_time: datetime.datetime, location: str, max_attendees: Optional[int] = None) -> int:
        """Add a new event to the database."""
        if start_time >= end_time:
            raise ValueError("End time must be after start time")

        self.cursor.execute("""
            INSERT INTO events (title, description, start_time, end_time, location, max_attendees)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, description, start_time, end_time, location, max_attendees))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_event(self, event_id: int) -> Dict:
        """Retrieve an event by its ID."""
        self.cursor.execute("SELECT * FROM events WHERE id = ?", (event_id,))
        event = self.cursor.fetchone()
        if not event:
            raise ValueError("Event not found")
        return {
            "id": event[0],
            "title": event[1],
            "description": event[2],
            "start_time": event[3],
            "end_time": event[4],
            "location": event[5],
            "max_attendees": event[6],
            "current_attendees": event[7]
        }

    def register_attendee(self, event_id: int, name: str, email: str) -> bool:
        """Register an attendee for an event."""
        event = self.get_event(event_id)
        
        # Check if event is full
        if event["max_attendees"] and event["current_attendees"] >= event["max_attendees"]:
            return False

        self.cursor.execute("""
            INSERT INTO attendees (event_id, name, email)
            VALUES (?, ?, ?)
        """, (event_id, name, email))

        # Update attendee count
        self.cursor.execute("""
            UPDATE events
            SET current_attendees = current_attendees + 1
            WHERE id = ?
        """, (event_id,))
        self.conn.commit()
        return True

    def get_event_attendees(self, event_id: int) -> List[Dict]:
        """Get all attendees for a specific event."""
        self.cursor.execute("""
            SELECT name, email, registration_date
            FROM attendees
            WHERE event_id = ?
            ORDER BY registration_date
        """, (event_id,))
        return [{"name": row[0], "email": row[1], "registration_date": row[2]} for row in self.cursor.fetchall()]

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Email notification system
class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """Initialize the email notifier with SMTP credentials."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email to the specified recipient."""
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

# Conference scheduler main class
class ConferenceScheduler:
    def __init__(self, db_manager: DatabaseManager, email_notifier: EmailNotifier):
        """Initialize the conference scheduler with database and email components."""
        self.db = db_manager
        self.notifier = email_notifier

    def schedule_event(self, title: str, description: str, start_time: datetime.datetime,
                      end_time: datetime.datetime, location: str, max_attendees: Optional[int] = None) -> int:
        """Schedule a new conference event."""
        try:
            event_id = self.db.add_event(title, description, start_time, end_time, location, max_attendees)
            return event_id
        except ValueError as e:
            print(f"Error scheduling event: {e}")
            raise

    def register_for_event(self, event_id: int, name: str, email: str) -> bool:
        """Register an attendee for an event and send confirmation email."""
        try:
            success = self.db.register_attendee(event_id, name, email)
            if success:
                event = self.db.get_event(event_id)
                subject = f"Registration Confirmation: {event['title']}"
                body = f"""Dear {name},
                
Thank you for registering for {event['title']}.
Event Details:
- Date: {event['start_time']} to {event['end_time']}
- Location: {event['location']}

We look forward to seeing you there!

Best regards,
IACI Conference Team
"""
                self.notifier.send_email(email, subject, body)
            return success
        except Exception as e:
            print(f"Error during registration: {e}")
            return False

    def send_reminders(self, hours_before: int = 24) -> int:
        """Send reminder emails for upcoming events."""
        now = datetime.datetime.now()
        reminder_time = now + datetime.timedelta(hours=hours_before)
        
        self.db.cursor.execute("""
            SELECT id, title, start_time, location
            FROM events
            WHERE start_time BETWEEN ? AND ?
        """, (now, reminder_time))
        
        events = self.db.cursor.fetchall()
        sent_count = 0

        for event in events:
            event_id, title, start_time, location = event
            attendees = self.db.get_event_attendees(event_id)
            
            for attendee in attendees:
                subject = f"Reminder: {title} starts soon"
                body = f"""Dear {attendee['name']},
                
This is a reminder that {title} is scheduled for:
- Time: {start_time}
- Location: {location}

Don't forget to attend!

Best regards,
IACI Conference Team
"""
                if self.notifier.send_email(attendee['email'], subject, body):
                    sent_count += 1

        return sent_count

# Example usage
if __name__ == "__main__":
    # Initialize components
    db = DatabaseManager()
    notifier = EmailNotifier(
        smtp_server="smtp.example.com",
        smtp_port=587,
        sender_email="conference@iaci.example",
        sender_password="securepassword"
    )
    scheduler = ConferenceScheduler(db, notifier)

    # Schedule an event
    try:
        event_id = scheduler.schedule_event(
            title="Public Policy Forum 2023",
            description="Annual conference on public policy challenges",
            start_time=datetime.datetime(2023, 11, 15, 9, 0),
            end_time=datetime.datetime(2023, 11, 16, 17, 0),
            location="Washington DC Convention Center",
            max_attendees=200
        )
        print(f"Event scheduled with ID: {event_id}")
    except Exception as e:
        print(f"Failed to schedule event: {e}")

    # Register attendees
    attendees = [
        ("John Doe", "john.doe@example.com"),
        ("Jane Smith", "jane.smith@example.com")
    ]
