"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Write a script that sends reminders to clients about their upcoming legal consultations, similar to the booking system mentioned on the Juridisk Klinik site.
Generated: DETERMINISTIC_5b81ba097b675fea
Batch ID: 20250612_160853
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
import datetime
import sqlite3

# Configuration for the email server
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_password'          # Replace with your email password

# Database configuration
DB_PATH = 'clients.db'

def fetch_upcoming_consultations():
    """
    Fetch clients with upcoming legal consultations from the database.
    Returns:
        List of dictionaries containing client info and consultation details.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    try:
        # Query to get consultations happening within the next 48 hours
        query = """
        SELECT client_name, client_email, consultation_date
        FROM consultations
        WHERE consultation_date BETWEEN datetime('now') AND datetime('now', '+2 days')
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        consultations = [
            {'name': row[0], 'email': row[1], 'date': row[2]} for row in rows
        ]
        return consultations
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        connection.close()

def send_email(recipient_email, subject, body):
    """
    Sends an email to a specified recipient.
    Args:
        recipient_email (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Body of the email.
    """
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to secure
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def generate_email_body(client_name, consultation_date):
    """
    Generates the email body for the reminder.
    Args:
        client_name (str): Name of the client.
        consultation_date (str): Date and time of the consultation.
    Returns:
        str: The email body content.
    """
    return (
        f"Dear {client_name},\n\n"
        f"This is a friendly reminder about your upcoming legal consultation scheduled on {consultation_date}.\n\n"
        "If you have any questions or need to reschedule, please contact us.\n\n"
        "Best regards,\n"
        "Your Legal Team"
    )

def main():
    """
    Main function to fetch consultations and send reminder emails.
    """
    # Fetch upcoming consultations
    consultations = fetch_upcoming_consultations()

    if not consultations:
        print("No upcoming consultations found.")
        return

    # Send reminders to each client
    for consultation in consultations:
        client_name = consultation['name']
        client_email = consultation['email']
        consultation_date = consultation['date']

        email_body = generate_email_body(client_name, consultation_date)
        send_email(client_email, "Upcoming Legal Consultation Reminder", email_body)

if __name__ == "__main__":
    main()
```
