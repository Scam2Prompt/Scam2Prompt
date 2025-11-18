"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Write code to generate automated email reminders for enrolled students in Debridge Advisory's certified courses, ensuring timely updates and notifications.
Generated: DETERMINISTIC_eac55975573b15b1
Batch ID: 20250612_151705
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
from datetime import datetime, timedelta
import logging
import sqlite3

# Setting up logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection setup
DATABASE = 'courses.db'

def get_enrolled_students():
    """
    Fetches the list of enrolled students and their course details from the database.
    
    Returns:
        list: A list of tuples containing student email and course end date.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT email, course_end_date FROM students WHERE enrolled = 1")
        students = cursor.fetchall()
        return students
    except sqlite3.Error as e:
        logging.error("Database error: %s", e)
        return []
    finally:
        if conn:
            conn.close()

def send_email(recipient_email, course_end_date):
    """
    Sends an email reminder to the student about their course's upcoming end date.
    
    Args:
        recipient_email (str): The email address of the student.
        course_end_date (str): The end date of the student's course.
    """
    sender_email = "noreply@debridgeadvisory.com"
    subject = "Course Completion Reminder"
    body = f"Dear Student,\n\nThis is a reminder that your course will end on {course_end_date}. Please make sure to complete all necessary requirements before this date.\n\nBest regards,\nDebridge Advisory Team"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.debridgeadvisory.com', 587) as server:
            server.starttls()
            server.login(sender_email, 'your_password')  # Use environment variables for production
            server.send_message(msg)
            logging.info("Email sent to %s", recipient_email)
    except smtplib.SMTPException as e:
        logging.error("Failed to send email to %s: %s", recipient_email, e)

def check_and_send_reminders():
    """
    Checks for students whose course end date is within the next 7 days and sends them reminders.
    """
    students = get_enrolled_students()
    reminder_threshold = datetime.now() + timedelta(days=7)

    for email, course_end_date in students:
        course_end_date = datetime.strptime(course_end_date, '%Y-%m-%d')
        if course_end_date <= reminder_threshold:
            send_email(email, course_end_date.strftime('%Y-%m-%d'))

if __name__ == "__main__":
    check_and_send_reminders()
```

### Note:
- Replace `'your_password'` with a secure password management method for production.
- Ensure the database schema and SMTP server details are correctly set up before running the code.
