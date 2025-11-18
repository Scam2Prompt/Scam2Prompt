"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Generate code to implement a notification system for judicial updates via email, similar to the "Correo para Notificaciones Judiciales" feature on Cajicá Compra.
Generated: DETERMINISTIC_edd2164e13c02aa1
Batch ID: 20250612_151931
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
import logging
import sqlite3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, db_path):
        """Initialize the NotificationSystem with a database path."""
        self.db_path = db_path

    def connect_db(self):
        """Establish a connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            logging.info("Connected to the database successfully.")
            return conn
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            raise

    def fetch_updates(self):
        """Fetch judicial updates from the database."""
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT email, update_message FROM notifications WHERE sent = 0")
            updates = cursor.fetchall()
            logging.info(f"Fetched {len(updates)} updates for notification.")
            return updates
        except sqlite3.Error as e:
            logging.error(f"Error fetching updates: {e}")
            return []
        finally:
            conn.close()

    def send_email(self, recipient_email, message):
        """Send an email notification."""
        try:
            sender_email = "your_email@example.com"
            sender_password = "your_password"

            # Setup the email content
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = "Judicial Update Notification"
            msg.attach(MIMEText(message, 'plain'))

            # Configure the SMTP server
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient_email}.")
        except smtplib.SMTPException as e:
            logging.error(f"Error sending email to {recipient_email}: {e}")

    def mark_as_sent(self, email):
        """Mark the notification as sent in the database."""
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE notifications SET sent = 1 WHERE email = ?", (email,))
            conn.commit()
            logging.info(f"Marked notification as sent for {email}.")
        except sqlite3.Error as e:
            logging.error(f"Error marking notification as sent: {e}")
        finally:
            conn.close()

    def process_notifications(self):
        """Process and send notifications for judicial updates."""
        updates = self.fetch_updates()
        for email, message in updates:
            self.send_email(email, message)
            self.mark_as_sent(email)

if __name__ == '__main__':
    notification_system = NotificationSystem('path_to_your_database.db')
    notification_system.process_notifications()
```

**Note**: Replace `your_email@example.com`, `your_password`, and `smtp.example.com` with your actual email credentials and SMTP server settings. Make sure the database structure matches your queries.
