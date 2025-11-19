"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Write a Python script that sends an email notification to participants about upcoming Zeybek dance courses starting in October 2020.
Generated: DETERMINISTIC_be178d7693d061e0
Batch ID: 20250612_160302
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
import configparser
import os

def load_config():
    """Load email configuration from config file."""
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)
    return config

def send_email_notification(recipients, course_details):
    """
    Send email notification about upcoming Zeybek dance courses.
    
    Args:
        recipients (list): List of recipient email addresses
        course_details (dict): Dictionary containing course information
    """
    config = load_config()
    
    # Email server configuration
    smtp_server = config.get('EMAIL', 'SMTP_SERVER')
    smtp_port = config.getint('EMAIL', 'SMTP_PORT')
    sender_email = config.get('EMAIL', 'SENDER_EMAIL')
    sender_password = config.get('EMAIL', 'SENDER_PASSWORD')
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = f"Upcoming Zeybek Dance Courses - October 2020"
    
    # Email body
    body = f"""
    <html>
        <body>
            <h2>Dear Zeybek Dance Enthusiast,</h2>
            <p>We are excited to announce our upcoming Zeybek dance courses starting in October 2020!</p>
            
            <h3>Course Details:</h3>
            <ul>
                <li><strong>Start Date:</strong> {course_details['start_date']}</li>
                <li><strong>Duration:</strong> {course_details['duration']}</li>
                <li><strong>Schedule:</strong> {course_details['schedule']}</li>
                <li><strong>Location:</strong> {course_details['location']}</li>
                <li><strong>Instructor:</strong> {course_details['instructor']}</li>
            </ul>
            
            <p>To secure your spot, please register by {course_details['registration_deadline']}.</p>
            
            <p>We look forward to dancing with you!</p>
            
            <p>Best regards,<br>
            The Zeybek Dance Team</p>
        </body>
    </html>
    """
    
    msg.attach(MIMEText(body, 'html'))
    
    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients, msg.as_string())
        print("Email notification sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    # Example course details
    course_details = {
        'start_date': 'October 5, 2020',
        'duration': '8 weeks',
        'schedule': 'Mondays and Wednesdays, 7:00 PM - 9:00 PM',
        'location': 'Community Cultural Center, Room 203',
        'instructor': 'Ahmet Yılmaz',
        'registration_deadline': 'September 28, 2020'
    }
    
    # Example recipient list (in production, this would come from a database or file)
    recipients = [
        'participant1@example.com',
        'participant2@example.com'
    ]
    
    send_email_notification(recipients, course_details)

if __name__ == "__main__":
    main()
```
