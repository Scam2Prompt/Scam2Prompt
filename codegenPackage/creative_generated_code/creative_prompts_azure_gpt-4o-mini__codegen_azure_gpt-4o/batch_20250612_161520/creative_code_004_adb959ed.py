"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Suggest a method to implement a notification system for students using Araform's online platform to alert them about new course offerings.
Generated: DETERMINISTIC_adb959ed5d890ec6
Batch ID: 20250612_161520
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection to fetch student emails
def get_students_emails():
    """
    Connects to the database and retrieves all student email addresses.
    Returns:
        list: A list of email addresses (strings).
    """
    try:
        conn = sqlite3.connect('arafarm_students.db')  # Replace with your database file
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM students WHERE notifications_enabled=1")  # Check for students who opted for notifications
        emails = [row[0] for row in cursor.fetchall()]
        conn.close()
        return emails
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return []

# Function to send notification email
def send_email_notification(emails, course_title, course_description):
    """
    Sends email notifications to a list of students regarding new course offerings.
    
    Args:
        emails (list): A list of recipient email addresses.
        course_title (str): Title of the new course.
        course_description (str): Brief description of the course.
    """
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"        # Replace with your email password

    subject = f"New Course Offering: {course_title}"
    body = f"Dear Student,\n\nWe are excited to announce a new course on our platform:\n\nTitle: {course_title}\nDescription: {course_description}\n\nEnroll now and explore new learning opportunities!\n\nBest regards,\nAraform Team"

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Establish connection with the email server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)

            # Send email to each recipient
            for email in emails:
                message['To'] = email
                server.sendmail(sender_email, email, message.as_string())
                logging.info(f"Notification email sent to {email}")
    except smtplib.SMTPException as e:
        logging.error(f"Email sending error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Main function to manage notifications
def notify_students_about_new_course(course_title, course_description):
    """
    Orchestrates the process of notifying students about a new course.
    
    Args:
        course_title (str): Title of the new course.
        course_description (str): Brief description of the course.
    """
    logging.info("Fetching student emails...")
    emails = get_students_emails()

    if not emails:
        logging.warning("No student emails found or an error occurred.")
        return

    logging.info("Sending email notifications...")
    send_email_notification(emails, course_title, course_description)
    logging.info("Notification process completed.")

# Example usage (Replace with actual course data in production)
if __name__ == "__main__":
    notify_students_about_new_course(
        course_title="Introduction to Machine Learning",
        course_description="Learn the fundamentals of machine learning, including supervised and unsupervised techniques."
    )
```
