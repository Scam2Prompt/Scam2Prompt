"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write code to automate the scheduling of RM’s Food ATM timings and locations, ensuring updates are sent to registered users via email or SMS.
Generated: DETERMINISTIC_c9884e8fe7b6d9f1
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import sqlite3
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pytz
from twilio.rest import Client

# Configuration
DATABASE_FILE = "food_atm.db"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASSWORD = "your_password"
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"
TIMEZONE = "America/New_York"

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("food_atm_scheduler.log"),
        logging.StreamHandler()
    ]
)

class FoodATMScheduler:
    def __init__(self):
        self.db_conn = sqlite3.connect(DATABASE_FILE)
        self._init_db()
        self.twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def _init_db(self):
        """Initialize database tables if they don't exist."""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                notification_preference TEXT CHECK(notification_preference IN ('email', 'sms', 'both')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS locations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                capacity INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id INTEGER NOT NULL,
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP NOT NULL,
                available_slots INTEGER NOT NULL,
                FOREIGN KEY(location_id) REFERENCES locations(id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                schedule_id INTEGER NOT NULL,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(schedule_id) REFERENCES schedules(id)
            )
        """)
        self.db_conn.commit()

    def add_user(self, name: str, email: Optional[str], phone: Optional[str], 
                 notification_preference: str) -> int:
        """Add a new user to the database."""
        if not email and not phone:
            raise ValueError("At least one of email or phone must be provided")
        
        if notification_preference not in ['email', 'sms', 'both']:
            raise ValueError("Invalid notification preference")
        
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, phone, notification_preference)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, notification_preference))
        self.db_conn.commit()
        return cursor.lastrowid

    def add_location(self, name: str, address: str, capacity: int) -> int:
        """Add a new location to the database."""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO locations (name, address, capacity)
            VALUES (?, ?, ?)
        """, (name, address, capacity))
        self.db_conn.commit()
        return cursor.lastrowid

    def add_schedule(self, location_id: int, start_time: datetime, 
                    end_time: datetime, available_slots: int) -> int:
        """Add a new schedule to the database."""
        if start_time >= end_time:
            raise ValueError("End time must be after start time")
        
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO schedules (location_id, start_time, end_time, available_slots)
            VALUES (?, ?, ?, ?)
        """, (location_id, start_time, end_time, available_slots))
        self.db_conn.commit()
        return cursor.lastrowid

    def get_upcoming_schedules(self, days_ahead: int = 7) -> List[Dict]:
        """Get schedules for the next specified number of days."""
        now = datetime.now(pytz.timezone(TIMEZONE))
        end_date = now + timedelta(days=days_ahead)
        
        cursor = self.db_conn.cursor()
        cursor.execute("""
            SELECT s.id, l.name, l.address, s.start_time, s.end_time, s.available_slots
            FROM schedules s
            JOIN locations l ON s.location_id = l.id
            WHERE s.start_time BETWEEN ? AND ?
            ORDER BY s.start_time
        """, (now, end_date))
        
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def get_users_to_notify(self) -> List[Dict]:
        """Get users who should receive notifications."""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            SELECT u.id, u.name, u.email, u.phone, u.notification_preference
            FROM users u
            WHERE u.email IS NOT NULL OR u.phone IS NOT NULL
        """)
        
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def send_email_notification(self, email: str, subject: str, message: str) -> bool:
        """Send an email notification."""
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                email_message = f"Subject: {subject}\n\n{message}"
                server.sendmail(SMTP_USER, email, email_message)
            return True
        except Exception as e:
            logging.error(f"Failed to send email to {email}: {str(e)}")
            return False

    def send_sms_notification(self, phone: str, message: str) -> bool:
        """Send an SMS notification."""
        try:
            self.twilio_client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=phone
            )
            return True
        except Exception as e:
            logging.error(f"Failed to send SMS to {phone}: {str(e)}")
            return False

    def create_notification_message(self, schedule: Dict) -> str:
        """Create a notification message for a schedule."""
        start_time = datetime.strptime(schedule['start_time'], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(schedule['end_time'], "%Y-%m-%d %H:%M:%S")
        
        return (
            f"Food ATM Schedule Update:\n"
            f"Location: {schedule['name']}\n"
            f"Address: {schedule['address']}\n"
            f"Time: {start_time.strftime('%A, %B %d, %Y %I:%M %p')} to "
            f"{end_time.strftime('%I:%M %p')}\n"
            f"Available slots: {schedule['available_slots']}"
        )

    def send_notifications(self):
        """Send notifications for upcoming schedules."""
        upcoming_schedules = self.get_upcoming_schedules()
        if not upcoming_schedules:
            logging.info("No upcoming schedules found")
            return
        
        users = self.get_users_to_notify()
        if not users:
            logging.info("No users to notify")
            return
        
        for schedule in upcoming_schedules:
            message = self.create_notification_message(schedule)
            subject = f"Food ATM Schedule Update: {schedule['name']}"
            
            for user in users:
                try:
                    notification_sent = False
                    
                    if user['notification_preference'] in ['email', 'both'] and user['email']:
                        if self.send_email_notification(user['email'], subject, message):
                            notification_sent = True
                    
                    if user['notification_preference'] in ['sms', 'both'] and user['phone']:
                        if self.send_sms_notification(user['phone'], message):
                            notification_sent = True
                    
                    if notification_sent:
                        self._record_notification(user['id'], schedule['id'])
                        logging.info(f"Notification sent to user {user['id']} for schedule {schedule['id']}")
                
                except Exception as e:
                    logging.error(f"Error sending notification to user {user['id']}: {str(e)}")

    def _record_notification(self, user_id: int, schedule_id: int):
        """Record
