"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Develop a script that automates the process of sending follow-up emails to clients who have undergone hair transplant procedures at AuQual Hair Services.
Generated: DETERMINISTIC_75d22547a161cd7d
Batch ID: 20250612_162051
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

# Configuration for email server
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
FROM_EMAIL = 'your_email@example.com'

# Database configuration
DATABASE_FILE = 'clients.db'

def create_database():
    """Creates a SQLite database if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            procedure_date DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_clients_due_for_follow_up():
    """Fetches clients who are due for a follow-up email."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Calculate the date 30 days after the procedure
    follow_up_date = datetime.now() - timedelta(days=30)
    
    cursor.execute('''
        SELECT name, email FROM clients 
        WHERE procedure_date <= ?
    ''', (follow_up_date,))
    
    clients = cursor.fetchall()
    conn.close()
    return clients

def send_email(to_email, client_name):
    """Sends a follow-up email to the specified client."""
    subject = "Follow-Up on Your Hair Transplant Procedure"
    body = f"Dear {client_name},\n\nWe hope you are doing well after your hair transplant procedure.\nPlease let us know if you have any questions or concerns.\n\nBest regards,\nAuQual Hair Services"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {client_name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {client_name} at {to_email}: {e}")

def main():
    """Main function to execute the email follow-up process."""
    create_database()
    clients_due = get_clients_due_for_follow_up()
    
    if not clients_due:
        print("No clients are due for follow-up.")
        return
    
    for client in clients_due:
        client_name, client_email = client
        send_email(client_email, client_name)

if __name__ == "__main__":
    main()
```
