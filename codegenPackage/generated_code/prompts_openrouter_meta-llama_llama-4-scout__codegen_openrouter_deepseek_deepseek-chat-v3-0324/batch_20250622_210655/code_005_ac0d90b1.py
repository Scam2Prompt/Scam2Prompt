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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime, timedelta
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='client_messaging.log'
)

class ClientMessenger:
    def __init__(self):
        self.db_path = 'consultation_requests.db'
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.email_address = os.getenv('EMAIL_ADDRESS')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.initialize_database()

    def initialize_database(self):
        """Initialize the SQLite database if it doesn't exist."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS consultation_requests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        client_email TEXT NOT NULL,
                        request_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        message_sent BOOLEAN DEFAULT 0,
                        sent_time TIMESTAMP
                    )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise

    def get_pending_requests(self):
        """Fetch consultation requests from the last 24 hours that haven't been processed."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
                cursor.execute('''
                    SELECT id, client_email, request_time
                    FROM consultation_requests
                    WHERE request_time >= ? AND message_sent = 0
                ''', (twenty_four_hours_ago,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error fetching pending requests: {e}")
            raise

    def send_email(self, to_email, subject, body):
        """Send an email to the specified recipient."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.send_message(msg)
            
            logging.info(f"Email sent to {to_email}")
            return True
        except smtplib.SMTPException as e:
            logging.error(f"Error sending email to {to_email}: {e}")
            return False
        except Exception as e:
            logging.error(f"Unexpected error sending email: {e}")
            return False

    def mark_as_sent(self, request_id):
        """Mark a consultation request as processed."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE consultation_requests
                    SET message_sent = 1, sent_time = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (request_id,))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error marking request {request_id} as sent: {e}")
            raise

    def process_requests(self):
        """Process all pending consultation requests."""
        pending_requests = self.get_pending_requests()
        if not pending_requests:
            logging.info("No pending requests to process.")
            return

        for request in pending_requests:
            request_id, client_email, request_time = request
            subject = "Thank you for your consultation request"
            body = f"""Dear Client,

Thank you for your consultation request received on {request_time}.
We will get back to you shortly with more information.

Best regards,
Your Service Team
"""

            if self.send_email(client_email, subject, body):
                self.mark_as_sent(request_id)
                logging.info(f"Processed request ID {request_id} for {client_email}")
            else:
                logging.error(f"Failed to process request ID {request_id} for {client_email}")

if __name__ == "__main__":
    try:
        messenger = ClientMessenger()
        messenger.process_requests()
    except Exception as e:
        logging.error(f"Fatal error in main execution: {e}")
```
