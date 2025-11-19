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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import sqlite3
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DATABASE = 'grants_program.db'

def create_database():
    """Create a SQLite database to track grantee experiences."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grantees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                outreach_date TEXT,
                feedback TEXT
            )
        ''')
        conn.commit()
        logging.info("Database created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def send_email(to_email, subject, body):
    """Send an email to the specified recipient."""
    try:
        from_email = "your_email@example.com"
        password = "your_email_password"  # Use environment variables in production

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email}.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def add_grantee(name, email):
    """Add a new grantee to the database."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO grantees (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        logging.info(f"Grantee {name} added successfully.")
    except sqlite3.IntegrityError:
        logging.warning(f"Grantee with email {email} already exists.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def outreach_grantees():
    """Perform outreach to all grantees."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT name, email FROM grantees')
        grantees = cursor.fetchall()

        for name, email in grantees:
            subject = "Welcome to the Grants Program!"
            body = f"Dear {name},\n\nThank you for being a part of our grants program. We look forward to your contributions!\n\nBest regards,\nGrants Team"
            send_email(email, subject, body)
            cursor.execute('UPDATE grantees SET outreach_date = ? WHERE email = ?', (datetime.now().isoformat(), email))

        conn.commit()
        logging.info("Outreach completed for all grantees.")
    except sqlite3.Error as e:
        logging.error(f"Database error during outreach: {e}")
    finally:
        conn.close()

def collect_feedback(email, feedback):
    """Collect feedback from a grantee."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('UPDATE grantees SET feedback = ? WHERE email = ?', (feedback, email))
        conn.commit()
        logging.info(f"Feedback collected from {email}.")
    except sqlite3.Error as e:
        logging.error(f"Database error while collecting feedback: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
    # Example usage
    add_grantee("Alice Smith", "alice@example.com")
    add_grantee("Bob Johnson", "bob@example.com")
    outreach_grantees()
    collect_feedback("alice@example.com", "Great program, looking forward to more!")
```
