"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Write a Python script to automate the process of sending messages to clients within 24 hours of receiving a consultation request."
Generated: DETERMINISTIC_ac0d90b1a9caba0f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import time
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

# Database setup
DATABASE = 'consultation_requests.db'

def create_database():
    """Create a SQLite database to store consultation requests."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_email TEXT NOT NULL,
            request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def send_email(to_email, subject, body):
    """Send an email to the specified recipient."""
    from_email = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def check_and_send_messages():
    """Check for consultation requests and send messages within 24 hours."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Get the current time and the time 24 hours ago
    now = datetime.now()
    twenty_four_hours_ago = now - timedelta(days=1)

    # Query for requests made in the last 24 hours
    cursor.execute('''
        SELECT client_email FROM requests
        WHERE request_time >= ?
    ''', (twenty_four_hours_ago,))

    # Fetch all matching requests
    requests = cursor.fetchall()

    for request in requests:
        client_email = request[0]
        subject = "Thank you for your consultation request"
        body = "We have received your consultation request and will get back to you shortly."
        send_email(client_email, subject, body)

    conn.close()

def main():
    """Main function to run the script."""
    create_database()
    
    # Simulate adding a consultation request (for testing purposes)
    # In a real application, this would be done through a web form or API
    # Uncomment the following lines to add a test request
    # conn = sqlite3.connect(DATABASE)
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO requests (client_email) VALUES (?)", ('client@example.com',))
    # conn.commit()
    # conn.close()

    # Run the message check every hour
    while True:
        check_and_send_messages()
        time.sleep(3600)  # Sleep for 1 hour

if __name__ == "__main__":
    main()
```
