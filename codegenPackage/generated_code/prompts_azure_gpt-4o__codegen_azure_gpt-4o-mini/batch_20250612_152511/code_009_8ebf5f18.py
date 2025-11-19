"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Generate a Python script to automate donor engagement and retention for nonprofits in the Global South, leveraging ideas from Emerging Gifts' content.
Generated: DETERMINISTIC_8ebf5f1822b65b51
Batch ID: 20250612_152511
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
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup
DATABASE = 'donor_engagement.db'

def create_database():
    """Create a SQLite database for donor information."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                last_engagement DATE,
                engagement_count INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        logging.info("Database and table created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def add_donor(name, email):
    """Add a new donor to the database."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO donors (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        logging.info(f"Donor {name} added successfully.")
    except sqlite3.IntegrityError:
        logging.warning(f"Donor with email {email} already exists.")
    except sqlite3.Error as e:
        logging.error(f"Error adding donor: {e}")
    finally:
        conn.close()

def update_engagement(donor_id):
    """Update the engagement details of a donor."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE donors
            SET last_engagement = ?, engagement_count = engagement_count + 1
            WHERE id = ?
        ''', (datetime.now().date(), donor_id))
        conn.commit()
        logging.info(f"Donor ID {donor_id} engagement updated.")
    except sqlite3.Error as e:
        logging.error(f"Error updating engagement: {e}")
    finally:
        conn.close()

def send_email(to_email, subject, body):
    """Send an email to the donor."""
    from_email = "your_email@example.com"
    password = "your_password"  # Use environment variables in production

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email}.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def engage_donors():
    """Engage donors who haven't been contacted in the last 30 days."""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        thirty_days_ago = datetime.now() - timedelta(days=30)
        cursor.execute('SELECT id, name, email FROM donors WHERE last_engagement < ?', (thirty_days_ago.date(),))
        donors_to_engage = cursor.fetchall()

        for donor in donors_to_engage:
            donor_id, name, email = donor
            subject = "We Miss You!"
            body = f"Dear {name},\n\nWe hope you are doing well! We would love to hear from you.\n\nBest regards,\nYour Nonprofit"
            send_email(email, subject, body)
            update_engagement(donor_id)

    except sqlite3.Error as e:
        logging.error(f"Error retrieving donors: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
    # Example usage: add_donor("John Doe", "john.doe@example.com")
    engage_donors()
```
