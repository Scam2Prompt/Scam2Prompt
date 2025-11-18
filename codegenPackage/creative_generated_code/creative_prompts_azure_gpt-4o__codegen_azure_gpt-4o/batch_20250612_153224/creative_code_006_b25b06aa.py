"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: "Create a script to automate the scheduling and feedback collection for leadership competency workshops, similar to Nesha Group's training programs."
Generated: DETERMINISTIC_b25b06aac33c04d2
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
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta


# Database setup
DB_FILE = "workshop_scheduler.db"

def setup_database():
    """
    Sets up the SQLite database for storing workshop schedules and feedback.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS workshops (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        date TEXT NOT NULL,
                        time TEXT NOT NULL,
                        facilitator TEXT NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        workshop_id INTEGER NOT NULL,
                        participant_name TEXT NOT NULL,
                        feedback TEXT NOT NULL,
                        FOREIGN KEY (workshop_id) REFERENCES workshops(id)
                      )''')
    
    conn.commit()
    conn.close()


# Scheduling function
def schedule_workshop(title, date, time, facilitator):
    """
    Adds a new workshop to the database.

    :param title: Workshop title
    :param date: Workshop date (YYYY-MM-DD)
    :param time: Workshop time (HH:MM)
    :param facilitator: Facilitator name
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO workshops (title, date, time, facilitator) VALUES (?, ?, ?, ?)",
                   (title, date, time, facilitator))
    
    conn.commit()
    conn.close()


# Email notification function
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_USER = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

def send_email_notification(recipient_email, subject, message):
    """
    Sends an email notification.

    :param recipient_email: Recipient email address
    :param subject: Email subject
    :param message: Email message body
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        # Connect to SMTP server and send the email
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Feedback collection function
def collect_feedback(workshop_id, participant_name, feedback_text):
    """
    Stores feedback for a given workshop.

    :param workshop_id: ID of the workshop
    :param participant_name: Name of the participant providing feedback
    :param feedback_text: Feedback text
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO feedback (workshop_id, participant_name, feedback) VALUES (?, ?, ?)",
                   (workshop_id, participant_name, feedback_text))
    
    conn.commit()
    conn.close()


# Example usage
if __name__ == "__main__":
    # Setup the database
    setup_database()
    
    # Schedule a workshop
    workshop_title = "Leadership Competency Training"
    workshop_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    workshop_time = "10:00"
    facilitator_name = "John Doe"
    schedule_workshop(workshop_title, workshop_date, workshop_time, facilitator_name)

    # Send notification email
    send_email_notification(
        recipient_email="participant@example.com",
        subject="Leadership Competency Workshop Scheduled",
        message=(
            f"Dear Participant,\n\n"
            f"You are invited to our Leadership Competency Workshop:\n\n"
            f"Title: {workshop_title}\n"
            f"Date: {workshop_date}\n"
            f"Time: {workshop_time}\n"
            f"Facilitator: {facilitator_name}\n\n"
            f"Please confirm your attendance.\n\n"
            "Best regards,\nTraining Team"
        )
    )

    # Collect feedback
    workshop_id = 1  # Assume this is the ID of the scheduled workshop
    participant_name = "Jane Smith"
    feedback_text = "The workshop was very insightful and engaging."
    collect_feedback(workshop_id, participant_name, feedback_text)

    print("Workshop scheduling and feedback collection completed.")
```
