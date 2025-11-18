"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Write code to integrate a notification system for pre-professional practice opportunities, similar to the "Convenio para prácticas Pre-Profesionales" described on the Trentino website.
Generated: DETERMINISTIC_e26592d72d6b29da
Batch ID: 20250612_151445
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
from datetime import datetime

# Configuration for the notification system
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_email_password"    # Replace with your email password

DB_FILE = "opportunities.db"  # SQLite database file

def send_email_notification(to_email, subject, body):
    """
    Sends an email notification.
    Args:
        to_email (str): Recipient email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        # Add the email body
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def create_database():
    """
    Creates the SQLite database if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create a table for opportunities
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS opportunities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                deadline TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        print("Database created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

def add_opportunity(title, description, deadline):
    """
    Adds a new opportunity to the database.
    Args:
        title (str): Title of the opportunity.
        description (str): Description of the opportunity.
        deadline (str): Deadline for application (YYYY-MM-DD format).
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO opportunities (title, description, deadline, created_at)
            VALUES (?, ?, ?, ?)
        """, (title, description, deadline, created_at))
        conn.commit()
        conn.close()
        print(f"Opportunity '{title}' added to the database.")
    except sqlite3.Error as e:
        print(f"Error adding opportunity: {e}")

def notify_users(opportunity_title, opportunity_description, deadline, user_emails):
    """
    Sends notifications to users about a new opportunity.
    Args:
        opportunity_title (str): Title of the opportunity.
        opportunity_description (str): Description of the opportunity.
        deadline (str): Deadline for application.
        user_emails (list): List of email addresses to notify.
    """
    subject = f"New Opportunity: {opportunity_title}"
    body = f"""Hello,

We are excited to share a new pre-professional practice opportunity with you!

Title: {opportunity_title}
Description: {opportunity_description}
Deadline: {deadline}

Don't miss this chance!

Best regards,
Notification System
"""
    for email in user_emails:
        send_email_notification(email, subject, body)

# Example Usage
if __name__ == "__main__":
    # Step 1: Create the database
    create_database()

    # Step 2: Add a new opportunity
    add_opportunity(
        title="Software Engineering Internship",
        description="Work on exciting projects with a leading tech company.",
        deadline="2023-12-31"
    )

    # Step 3: Notify users about the opportunity
    user_emails = ["user1@example.com", "user2@example.com"]  # Replace with actual user emails
    notify_users(
        opportunity_title="Software Engineering Internship",
        opportunity_description="Work on exciting projects with a leading tech company.",
        deadline="2023-12-31",
        user_emails=user_emails
    )
```
