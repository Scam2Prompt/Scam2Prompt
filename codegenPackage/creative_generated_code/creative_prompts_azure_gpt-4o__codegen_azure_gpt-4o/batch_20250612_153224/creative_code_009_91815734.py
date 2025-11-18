"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Develop a system to notify students about upcoming cultural events and workshops via email, based on the community engagement focus of Escuela Preparatoria Oficial N.73.
Generated: DETERMINISTIC_9181573490f285e2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime, timedelta

# Database setup (Using SQLite for simplicity)
DB_NAME = 'events_notification.db'

def setup_database():
    """Initialize the database tables if they don't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Table to store student emails
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    
    # Table to store events
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    
    connection.commit()
    connection.close()

def add_student(name, email):
    """Add a student to the database."""
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"Error: Email '{email}' is already registered.")
    finally:
        connection.close()

def add_event(title, description, date):
    """Add an event to the database."""
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO events (title, description, date) VALUES (?, ?, ?)", (title, description, date))
        connection.commit()
    finally:
        connection.close()

def fetch_upcoming_events():
    """Fetch events occurring within the next 7 days."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    today = datetime.now()
    next_week = today + timedelta(days=7)
    cursor.execute("SELECT * FROM events WHERE date BETWEEN ? AND ?", (today.strftime('%Y-%m-%d'), next_week.strftime('%Y-%m-%d')))
    events = cursor.fetchall()
    connection.close()
    return events

def fetch_students():
    """Fetch all registered students."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    return students

def send_email(to_email, subject, body):
    """Send an email to the specified address."""
    try:
        # Email server configuration (replace with actual credentials)
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        sender_email = 'your-email@example.com'
        sender_password = 'your-password'
        
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect and send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

def notify_students_about_events():
    """Notify students about upcoming events via email."""
    students = fetch_students()
    events = fetch_upcoming_events()
    
    if not events:
        print("No upcoming events to notify.")
        return
    
    for student in students:
        student_name, student_email = student[1], student[2]
        event_details = "\n\n".join([f"{event[1]}: {event[2]} on {event[3]}" for event in events])
        email_body = f"Hello {student_name},\n\nHere are the upcoming cultural events and workshops:\n\n{event_details}\n\nBest regards,\nEscuela Preparatoria Oficial N.73"
        send_email(student_email, "Upcoming Events Notification", email_body)

# Main execution block
if __name__ == "__main__":
    setup_database()  # Ensure the database is set up
    
    # Example: Adding students and events (uncomment to use)
    # add_student("John Doe", "john.doe@example.com")
    # add_event("Cultural Dance Workshop", "Learn traditional dances from our experienced instructors.", "2023-10-15")
    
    notify_students_about_events()  # Notify students about upcoming events
```
