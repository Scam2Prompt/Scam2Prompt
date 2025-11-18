"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastfair.com
Prompt: Generate a Python script to subscribe users to the Études Newsletter and send them exclusive architectural design insights.
Generated: DETERMINISTIC_137f9e3747698736
Batch ID: 20250612_152527
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

# Database configuration
DB_FILE = 'subscribers.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Database error: {e}")
    return conn

def create_subscriber(conn, email):
    """Insert a new subscriber into the subscribers table."""
    sql = '''INSERT INTO subscribers(email) VALUES(?)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (email,))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(f"Error while inserting subscriber: {e}")
        return None

def send_email(to_email):
    """Send a welcome email to the subscriber."""
    from_email = "your_email@example.com"
    password = "your_password"  # Use environment variables or secret management in production.

    # Create the email content
    subject = "Welcome to the Études Newsletter!"
    body = "Thank you for subscribing! You'll receive exclusive architectural design insights soon."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Use your SMTP server
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """Main function to handle user subscription."""
    # Create a database connection
    conn = create_connection(DB_FILE)

    if conn is not None:
        # Create subscribers table if it does not exist
        conn.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        email = input("Enter your email to subscribe to the Études Newsletter: ").strip()

        # Check if email already exists
        cur = conn.cursor()
        cur.execute("SELECT * FROM subscribers WHERE email = ?", (email,))
        if cur.fetchone():
            print("This email is already subscribed.")
        else:
            # Add subscriber and send email
            if create_subscriber(conn, email):
                send_email(email)
            else:
                print("There was an error subscribing you. Please try again.")

        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
