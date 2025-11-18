"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Write a script to automate subscription-based updates for clients, similar to the newsletter system mentioned on Finance Investment Limited's webpage.
Generated: DETERMINISTIC_fe43f014c6b25161
Batch ID: 20250612_154631
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
from sqlite3 import Error

# Constants for email settings
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Port for SMTP
USERNAME = 'your-email@example.com'  # Replace with your email
PASSWORD = 'your-password'  # Replace with your password

# Database configuration
DATABASE = 'subscriptions.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create the subscriptions table if it doesn't exist."""
    try:
        sql_create_subscriptions_table = """ CREATE TABLE IF NOT EXISTS subscriptions (
                                                id integer PRIMARY KEY,
                                                email text NOT NULL UNIQUE
                                            ); """
        cursor = conn.cursor()
        cursor.execute(sql_create_subscriptions_table)
    except Error as e:
        print(f"Error creating table: {e}")

def add_subscription(conn, email):
    """Add a new email subscription to the database."""
    try:
        sql_insert_subscription = """ INSERT INTO subscriptions(email) VALUES(?) """
        cursor = conn.cursor()
        cursor.execute(sql_insert_subscription, (email,))
        conn.commit()
    except Error as e:
        print(f"Error adding subscription: {e}")

def send_email(to_email, subject, message):
    """Send an email using SMTP."""
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_updates(conn):
    """Send updates to all subscribed clients."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM subscriptions")
        emails = cursor.fetchall()

        for email_tuple in emails:
            email = email_tuple[0]
            send_email(email, "Your Monthly Update", "Here are the updates for this month...")
    except Error as e:
        print(f"Error retrieving subscriptions: {e}")

def main():
    """Main function to automate subscription updates."""
    # Create a database connection
    conn = create_connection(DATABASE)
    
    if conn:
        create_table(conn)
        
        # Example: Add a subscription (replace with actual email input)
        add_subscription(conn, "client@example.com")
        
        # Send updates to all subscribers
        send_updates(conn)

        # Close the database connection
        conn.close()

if __name__ == '__main__':
    main()
```
