"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Develop a script to maximize engagement for a grants program by automating outreach and tracking grantee experiences, referencing Gitcoin's framework.
Generated: DETERMINISTIC_f3482ec054fea8e1
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import sqlite3
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection function
def connect_db(db_name='grants_program.db'):
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_name)
        logging.info("Database connection established.")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection failed: {e}")
        return None

# Function to create a table for grantee information
def create_grantee_table(conn):
    """Create a table for storing grantee information if it doesn't exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grantees (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                outreach_date TEXT,
                feedback TEXT
            )
        ''')
        conn.commit()
        logging.info("Grantees table created or already exists.")
    except sqlite3.Error as e:
        logging.error(f"Failed to create table: {e}")

# Function to send outreach emails
def send_email(to_email, subject, message):
    """Send an email to the specified recipient."""
    try:
        from_email = "your_email@example.com"
        password = "your_email_password"
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email}.")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

# Function to add a grantee to the database
def add_grantee(conn, email, first_name, last_name):
    """Add a new grantee to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO grantees (email, first_name, last_name)
            VALUES (?, ?, ?)
        ''', (email, first_name, last_name))
        conn.commit()
        logging.info(f"Grantee {first_name} {last_name} added to the database.")
    except sqlite3.Error as e:
        logging.error(f"Failed to add grantee: {e}")

# Function to track feedback from grantees
def track_feedback(conn, grantee_id, feedback):
    """Update grantee feedback in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE grantees
            SET feedback = ?, outreach_date = ?
            WHERE id = ?
        ''', (feedback, datetime.now().isoformat(), grantee_id))
        conn.commit()
        logging.info(f"Feedback recorded for grantee ID {grantee_id}.")
    except sqlite3.Error as e:
        logging.error(f"Failed to record feedback: {e}")

# Main function to run the outreach program
def main():
    """Main function to execute the outreach program."""
    conn = connect_db()
    if conn is None:
        return

    create_grantee_table(conn)
    
    # Example of adding a grantee and sending an outreach email
    grantee_email = "grantee@example.com"
    add_grantee(conn, grantee_email, "John", "Doe")

    # Send outreach email
    email_subject = "Welcome to Our Grants Program"
    email_message = "Dear John Doe,\n\nThank you for joining our grants program! We look forward to supporting your project.\n\nBest regards,\nThe Grants Team"
    send_email(grantee_email, email_subject, email_message)

    # Example of tracking feedback
    track_feedback(conn, 1, "Excited to start the project!")

    # Close the database connection
    conn.close()
    logging.info("Database connection closed.")

if __name__ == "__main__":
    main()
```
