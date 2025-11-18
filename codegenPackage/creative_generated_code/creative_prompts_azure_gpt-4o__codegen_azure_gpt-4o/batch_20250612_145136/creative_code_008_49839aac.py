"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Write a Python script to send automated email reminders to students about upcoming class schedules for INESO's programs, including "Especialidad en Ortodoncia."
Generated: DETERMINISTIC_49839aac00a1ad17
Batch ID: 20250612_145136
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def send_email_reminder(student_email, student_name, class_name, class_date, smtp_config):
    """
    Sends an email reminder to a student about an upcoming class.

    Args:
        student_email (str): Email address of the student.
        student_name (str): Name of the student.
        class_name (str): Name of the class.
        class_date (datetime.date): Date of the class.
        smtp_config (dict): SMTP configuration containing 'host', 'port', 'username', and 'password'.

    Raises:
        Exception: If the email fails to send.
    """
    try:
        # Create the email content
        subject = f"Reminder: Upcoming Class - {class_name}"
        body = (
            f"Dear {student_name},\n\n"
            f"This is a friendly reminder that you have an upcoming class for INESO's program \"{class_name}\".\n"
            f"Date: {class_date.strftime('%A, %B %d, %Y')}\n\n"
            "Please ensure you are prepared and ready to participate.\n\n"
            "Best regards,\n"
            "INESO Team"
        )

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = smtp_config['username']
        msg['To'] = student_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_config['host'], smtp_config['port']) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_config['username'], smtp_config['password'])
            server.send_message(msg)
            logging.info(f"Email successfully sent to {student_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {student_email}: {e}")
        raise


def get_upcoming_classes():
    """
    Retrieves a list of upcoming classes and their details.

    Returns:
        list of dict: List of dictionaries containing class details.
    """
    # In a production system, this data might come from a database or API.
    return [
        {
            "student_email": "student1@example.com",
            "student_name": "John Doe",
            "class_name": "Especialidad en Ortodoncia",
            "class_date": datetime.date.today() + datetime.timedelta(days=3)
        },
        {
            "student_email": "student2@example.com",
            "student_name": "Jane Smith",
            "class_name": "Especialidad en Ortodoncia",
            "class_date": datetime.date.today() + datetime.timedelta(days=5)
        }
    ]


def main():
    """
    Main function to send email reminders to students about upcoming classes.
    """
    # SMTP configuration
    smtp_config = {
        "host": "smtp.example.com",  # Replace with your SMTP server host
        "port": 587,                # Replace with your SMTP server port
        "username": "your_email@example.com",  # Replace with your email address
        "password": "your_password"            # Replace with your email password
    }

    # Fetch upcoming classes
    upcoming_classes = get_upcoming_classes()

    # Send email reminders
    for cls in upcoming_classes:
        try:
            send_email_reminder(
                student_email=cls["student_email"],
                student_name=cls["student_name"],
                class_name=cls["class_name"],
                class_date=cls["class_date"],
                smtp_config=smtp_config
            )
        except Exception as e:
            logging.error(f"Error sending reminder for {cls['student_name']} ({cls['student_email']}): {e}")


if __name__ == "__main__":
    main()
```
