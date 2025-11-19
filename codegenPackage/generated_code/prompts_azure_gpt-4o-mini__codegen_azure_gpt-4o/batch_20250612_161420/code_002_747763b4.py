"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Create a notification for students about the importance of regular attendance in classes to avoid being marked as non-collegiate, as mentioned by the acting principal of Nazirpur Degree College.
Generated: DETERMINISTIC_747763b438776606
Batch ID: 20250612_161420
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

# Function to send email notifications to students
def send_attendance_notification(student_emails):
    """
    Sends an email notification to students about the importance of regular attendance.

    Args:
        student_emails (list): List of student email addresses.

    Returns:
        None
    """
    # Acting principal's message
    message_body = (
        "Dear Student,\n\n"
        "This is a reminder from the acting principal of Nazirpur Degree College about the importance of regular attendance. "
        "Students are advised to attend classes regularly to avoid being marked as non-collegiate. "
        "Your commitment to attending classes is crucial for your academic success.\n\n"
        "Thank you for your cooperation.\n\n"
        "Best regards,\n"
        "Nazirpur Degree College Administration"
    )

    # Email server configuration
    smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
    smtp_port = 587
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    # Loop through each student email and send the notification
    for email in student_emails:
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = "Important: Regular Attendance Reminder"
            msg.attach(MIMEText(message_body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
            
            print(f"Notification sent successfully to {email}")
        
        except Exception as e:
            # Log the error and continue with the next email
            print(f"Failed to send notification to {email}. Error: {e}")

# Example usage
if __name__ == "__main__":
    # List of student email addresses
    student_emails = [
        "student1@example.com",
        "student2@example.com",
        "student3@example.com"
    ]

    # Send notifications
    send_attendance_notification(student_emails)
```

**Note:** Replace `your_email@example.com` and `your_password` with valid credentials for the email account you want to use to send notifications. For production use, consider using environment variables or a secure secrets manager to store sensitive information like email credentials.
