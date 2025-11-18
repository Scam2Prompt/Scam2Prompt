"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Develop a script to send automated follow-up emails to clients who inquire about plots or villas, based on the contact form structure provided by Corfu Coastal Collection.
Generated: DETERMINISTIC_8fde13102169cca8
Batch ID: 20250612_153224
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
from datetime import datetime, timedelta
import sqlite3

# Configuration - Update these values with your email settings
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
FOLLOW_UP_INTERVAL_DAYS = 3  # Number of days after inquiry to send the follow-up email

# Database file path
DATABASE_PATH = "inquiries.db"

# Email content templates
FOLLOW_UP_SUBJECT = "Thank You for Your Inquiry - Corfu Coastal Collection"
FOLLOW_UP_BODY = """
Dear {first_name} {last_name},

Thank you for reaching out to Corfu Coastal Collection regarding plots or villas. 
We hope you found the information useful. If you have further questions or need assistance, feel free to contact us.

Warm regards,
Corfu Coastal Collection Team
"""

def send_email(to_email, subject, body):
    """
    Sends an email using SMTP.
    :param to_email: Recipient email address.
    :param subject: Email subject.
    :param body: Email body content.
    """
    try:
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def get_pending_follow_ups():
    """
    Retrieves inquiries that are due for follow-up emails.
    :return: List of records with client details.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        # Select inquiries where the follow-up date is today or earlier
        query = f"""
        SELECT id, first_name, last_name, email, inquiry_date 
        FROM inquiries 
        WHERE follow_up_sent = 0 AND inquiry_date <= ?
        """
        follow_up_date = datetime.now() - timedelta(days=FOLLOW_UP_INTERVAL_DAYS)
        cursor.execute(query, (follow_up_date.strftime('%Y-%m-%d'),))
        pending_inquiries = cursor.fetchall()
        conn.close()
        return pending_inquiries
    except Exception as e:
        print(f"Error fetching pending follow-ups: {e}")
        return []

def mark_follow_up_sent(inquiry_id):
    """
    Marks an inquiry as having received a follow-up email.
    :param inquiry_id: ID of the inquiry to update.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        query = "UPDATE inquiries SET follow_up_sent = 1 WHERE id = ?"
        cursor.execute(query, (inquiry_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error marking follow-up as sent for inquiry ID {inquiry_id}: {e}")

def main():
    """
    Main script logic to process and send follow-up emails.
    """
    print("Starting follow-up email processing...")
    pending_inquiries = get_pending_follow_ups()
    if not pending_inquiries:
        print("No pending follow-up emails to process.")
        return

    for inquiry in pending_inquiries:
        inquiry_id, first_name, last_name, email, inquiry_date = inquiry
        # Customize email body with user details
        email_body = FOLLOW_UP_BODY.format(first_name=first_name, last_name=last_name)
        send_email(email, FOLLOW_UP_SUBJECT, email_body)
        mark_follow_up_sent(inquiry_id)

    print("Follow-up email processing completed.")

if __name__ == "__main__":
    main()
```

**Notes about the code:**
1. Ensure the `inquiries.db` database and `inquiries` table exist with columns: `id`, `first_name`, `last_name`, `email`, `inquiry_date`, and `follow_up_sent`.
2. Replace placeholders (`SMTP_SERVER`, `EMAIL_ADDRESS`, etc.) with actual values for your email configuration.
3. This script assumes SQLite for database management; adapt it if using another DBMS.
