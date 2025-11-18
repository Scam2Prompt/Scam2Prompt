"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Write a script to automate proactive follow-up calls to clients, gathering feedback and maintaining relationships, as described in ProSync's services.
Generated: DETERMINISTIC_40e56bea2803c09c
Batch ID: 20250612_152235
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
from datetime import datetime, timedelta
import logging
import sqlite3

# Set up logging for tracking the execution of the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database setup for clients
DATABASE_FILE = 'clients.db'

def setup_database():
    """Initializes the database to store client information."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                last_contact DATE,
                feedback TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    finally:
        conn.close()

def add_client(name, email):
    """Adds a new client to the database."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clients (name, email, last_contact) VALUES (?, ?, ?)',
                       (name, email, datetime.now().date()))
        conn.commit()
        logging.info(f"Added client: {name} ({email})")
    except sqlite3.Error as e:
        logging.error(f"Error adding client: {e}")
    finally:
        conn.close()

def fetch_clients_to_contact():
    """Fetches clients who haven't been contacted in the last 30 days."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        thirty_days_ago = datetime.now() - timedelta(days=30)
        cursor.execute('SELECT name, email FROM clients WHERE last_contact < ?', (thirty_days_ago.date(),))
        clients = cursor.fetchall()
        return clients
    except sqlite3.Error as e:
        logging.error(f"Database error when fetching clients: {e}")
        return []
    finally:
        conn.close()

def send_email(to_email, subject, body):
    """Sends an email to a specified recipient."""
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'youremail@domain.com'  # Change to your email
        msg['To'] = to_email
        
        with smtplib.SMTP('smtp.domain.com', 587) as server:  # Change to your SMTP server
            server.starttls()
            server.login('youremail@domain.com', 'yourpassword')  # Change to your email credentials
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

def update_last_contact(client_name):
    """Updates the last contact date for a client."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('UPDATE clients SET last_contact = ? WHERE name = ?',
                       (datetime.now().date(), client_name))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error updating last contact for {client_name}: {e}")
    finally:
        conn.close()

def automate_follow_up():
    """Automates the follow-up process with clients."""
    clients = fetch_clients_to_contact()
    for name, email in clients:
        subject = "We value your feedback!"
        body = f"Dear {name},\n\nWe would love to hear from you. Please share your thoughts with us!"
        send_email(email, subject, body)
        update_last_contact(name)

if __name__ == '__main__':
    setup_database()
    # Example client addition (uncomment to add clients)
    # add_client('John Doe', 'johndoe@example.com')
    
    automate_follow_up()
```
