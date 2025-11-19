"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write code to track court docket schedules and notify users of their case position for guardianship hearings, based on the Serve Utah process.
Generated: DETERMINISTIC_910b8aca49df7985
Batch ID: 20250612_154741
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

# Database setup
def initialize_database():
    """Initialize the SQLite database and create necessary tables."""
    conn = sqlite3.connect('docket_tracker.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cases (
            case_id TEXT PRIMARY KEY,
            case_name TEXT NOT NULL,
            hearing_date TEXT NOT NULL,
            hearing_time TEXT NOT NULL,
            court_room TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_cases (
            user_id INTEGER,
            case_id TEXT,
            notification_preference TEXT DEFAULT 'email',
            PRIMARY KEY (user_id, case_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (case_id) REFERENCES cases(case_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Case management
def add_case(case_id: str, case_name: str, hearing_date: str, hearing_time: str, court_room: str) -> bool:
    """Add a new case to the tracking system."""
    try:
        conn = sqlite3.connect('docket_tracker.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO cases (case_id, case_name, hearing_date, hearing_time, court_room)
            VALUES (?, ?, ?, ?, ?)
        ''', (case_id, case_name, hearing_date, hearing_time, court_room))
        
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def update_case_status(case_id: str, status: str) -> bool:
    """Update the status of a case."""
    try:
        conn = sqlite3.connect('docket_tracker.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE cases SET status = ? WHERE case_id = ?
        ''', (status, case_id))
        
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

# User management
def add_user(name: str, email: str, phone: Optional[str] = None) -> int:
    """Add a new user to the system."""
    try:
        conn = sqlite3.connect('docket_tracker.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO users (name, email, phone)
            VALUES (?, ?, ?)
        ''', (name, email, phone))
        
        user_id = cursor.lastrowid
        conn.commit()
        return user_id
    except sqlite3.IntegrityError:
        return -1
    finally:
        conn.close()

def assign_case_to_user(user_id: int, case_id: str, notification_preference: str = 'email') -> bool:
    """Assign a case to a user with notification preference."""
    try:
        conn = sqlite3.connect('docket_tracker.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO user_cases (user_id, case_id, notification_preference)
            VALUES (?, ?, ?)
        ''', (user_id, case_id, notification_preference))
        
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Notification system
class NotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, email: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
    
    def send_email_notification(self, to_email: str, subject: str, body: str) -> bool:
        """Send an email notification."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def send_sms_notification(self, phone_number: str, message: str) -> bool:
        """Placeholder for SMS notification functionality."""
        # In a real implementation, this would integrate with an SMS gateway
        print(f"SMS to {phone_number}: {message}")
        return True

# Docket tracking
def get_upcoming_hearings(days_ahead: int = 1) -> List[Dict]:
    """Get hearings scheduled for the next specified number of days."""
    conn = sqlite3.connect('docket_tracker.db')
    cursor = conn.cursor()
    
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=days_ahead)
    
    cursor.execute('''
        SELECT case_id, case_name, hearing_date, hearing_time, court_room, status
        FROM cases
        WHERE hearing_date BETWEEN ? AND ?
        ORDER BY hearing_date, hearing_time
    ''', (today.isoformat(), end_date.isoformat()))
    
    hearings = []
    for row in cursor.fetchall():
        hearings.append({
            'case_id': row[0],
            'case_name': row[1],
            'hearing_date': row[2],
            'hearing_time': row[3],
            'court_room': row[4],
            'status': row[5]
        })
    
    conn.close()
    return hearings

def notify_users_of_upcoming_hearings(notification_service: NotificationService, days_ahead: int = 1) -> int:
    """Notify users about their upcoming hearings."""
    hearings = get_upcoming_hearings(days_ahead)
    notified_count = 0
    
    conn = sqlite3.connect('docket_tracker.db')
    cursor = conn.cursor()
    
    for hearing in hearings:
        cursor.execute('''
            SELECT u.user_id, u.name, u.email, u.phone, uc.notification_preference
            FROM users u
            JOIN user_cases uc ON u.user_id = uc.user_id
            WHERE uc.case_id = ?
        ''', (hearing['case_id'],))
        
        for user in cursor.fetchall():
            user_id, name, email, phone, preference = user
            
            subject = f"Upcoming Hearing Reminder: {hearing['case_name']}"
            body = f"""
            Dear {name},
            
            This is a reminder about your upcoming guardianship hearing:
            
            Case: {hearing['case_name']}
            Date: {hearing['hearing_date']}
            Time: {hearing['hearing_time']}
            Court Room: {hearing['court_room']}
            Status: {hearing['status']}
            
            Please arrive at least 15 minutes early.
            """
            
            if preference == 'email' and email:
                if notification_service.send_email_notification(email, subject, body):
                    notified_count += 1
            elif preference == 'sms' and phone:
                if notification_service.send_sms_notification(phone, body):
                    notified_count += 1
    
    conn.close()
    return notified_count

# Main execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Example usage
    notification_service = NotificationService(
        smtp_server='smtp.example.com',
        smtp_port=587,
        email='notifications@example.com',
        password='securepassword'
    )
    
    # Add sample data
    add_case('GC-2023-001', 'Guardianship of Smith', '2023-12-15', '09:30', 'Room 101')
    user_id = add_user('John Doe', 'john.doe@example.com', '+15551234567')
    assign_case_to_user(user_id, 'GC-2023-001', 'email')
    
    # Run notifications
    notified = notify_users_of_upcoming_hearings(notification_service, 7)
    print(f"Sent notifications to {notified} users.")
```
