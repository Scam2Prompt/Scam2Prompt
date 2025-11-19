"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Create a script to automate email reminders for clients of a holistic health clinic, notifying them of upcoming appointments for therapies like postpartum massage or Hijama.
Generated: DETERMINISTIC_2d74757726a8cb9f
Batch ID: 20250612_153246
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
import datetime
import sqlite3
from typing import List, Dict
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('appointment_reminders.log'),
        logging.StreamHandler()
    ]
)

class EmailReminderSystem:
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.smtp_username = os.getenv('SMTP_USERNAME')
        self.smtp_password = os.getenv('SMTP_PASSWORD')
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.db_path = os.getenv('DB_PATH', 'clinic_appointments.db')
        
        # Validate required environment variables
        if not all([self.smtp_server, self.smtp_username, self.smtp_password, self.sender_email]):
            raise ValueError("Missing required environment variables for email configuration")

    def get_upcoming_appointments(self, days_ahead: int = 1) -> List[Dict]:
        """Retrieve appointments scheduled for the next X days from the database."""
        appointments = []
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            start_date = datetime.datetime.now()
            end_date = start_date + datetime.timedelta(days=days_ahead)
            
            query = """
                SELECT 
                    a.appointment_id, 
                    c.client_id, 
                    c.first_name, 
                    c.last_name, 
                    c.email, 
                    a.appointment_time, 
                    t.therapy_name
                FROM 
                    appointments a
                JOIN 
                    clients c ON a.client_id = c.client_id
                JOIN 
                    therapies t ON a.therapy_id = t.therapy_id
                WHERE 
                    a.appointment_time BETWEEN ? AND ?
                    AND a.status = 'confirmed'
                    AND a.reminder_sent = 0
            """
            cursor.execute(query, (start_date, end_date))
            
            for row in cursor.fetchall():
                appointments.append({
                    'appointment_id': row[0],
                    'client_id': row[1],
                    'first_name': row[2],
                    'last_name': row[3],
                    'email': row[4],
                    'appointment_time': row[5],
                    'therapy_name': row[6]
                })
                
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        finally:
            if conn:
                conn.close()
                
        return appointments

    def send_reminder_email(self, recipient: Dict) -> bool:
        """Send an email reminder for a specific appointment."""
        try:
            # Format appointment time
            appointment_time = datetime.datetime.strptime(
                recipient['appointment_time'], '%Y-%m-%d %H:%M:%S'
            )
            formatted_time = appointment_time.strftime('%A, %B %d at %I:%M %p')
            
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient['email']
            msg['Subject'] = f"Reminder: Upcoming {recipient['therapy_name']} Appointment"
            
            # Email body
            body = f"""
            Dear {recipient['first_name']},
            
            This is a friendly reminder about your upcoming {recipient['therapy_name']} appointment:
            
            Date/Time: {formatted_time}
            
            Location: Holistic Health Clinic
            123 Wellness Way
            Healing City, HC 12345
            
            Please arrive 10 minutes early to complete any necessary paperwork.
            
            If you need to reschedule or cancel, please contact us at least 24 hours in advance.
            
            We look forward to seeing you!
            
            Warm regards,
            The Holistic Health Clinic Team
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
                
            logging.info(f"Sent reminder to {recipient['email']} for appointment ID {recipient['appointment_id']}")
            return True
            
        except Exception as e:
            logging.error(f"Failed to send email to {recipient['email']}: {e}")
            return False

    def mark_reminder_sent(self, appointment_id: int) -> None:
        """Update database to mark reminder as sent."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE appointments SET reminder_sent = 1 WHERE appointment_id = ?",
                (appointment_id,)
            )
            conn.commit()
            
        except sqlite3.Error as e:
            logging.error(f"Failed to update appointment {appointment_id}: {e}")
            conn.rollback()
        finally:
            if conn:
                conn.close()

    def process_reminders(self) -> None:
        """Main method to process and send all reminders."""
        try:
            appointments = self.get_upcoming_appointments(days_ahead=2)
            
            if not appointments:
                logging.info("No upcoming appointments found requiring reminders.")
                return
                
            logging.info(f"Found {len(appointments)} appointments requiring reminders.")
            
            for appointment in appointments:
                if self.send_reminder_email(appointment):
                    self.mark_reminder_sent(appointment['appointment_id'])
                    
        except Exception as e:
            logging.error(f"Error processing reminders: {e}")

if __name__ == "__main__":
    try:
        reminder_system = EmailReminderSystem()
        reminder_system.process_reminders()
    except Exception as e:
        logging.error(f"Failed to initialize reminder system: {e}")
```
