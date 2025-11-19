"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Create a notification for students about the importance of regular attendance in classes to avoid being marked as non-collegiate, as mentioned by the acting principal of Nazirpur Degree College.
Generated: DETERMINISTIC_747763b438776606
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for sending notifications
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_attendance_notification(email_list, subject, message_body):
    """
    Sends a notification email to students regarding attendance.

    Args:
        email_list (list): List of email addresses for students.
        subject (str): Subject of the email.
        message_body (str): Content of the email message.

    Returns:
        None
    """
    # Email configuration
    sender_email = "official@nazirpurdc.edu"  # Replace with the official sender email
    sender_password = "YourPasswordHere"     # Replace with the sender email password
    smtp_server = "smtp.gmail.com"           # Replace with the SMTP server for your email provider
    smtp_port = 587                          # Port for the SMTP server
    
    try:
        # Set up the SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Authenticate the sender email
        
        # Loop through the list of student emails and send email notifications
        for recipient_email in email_list:
            # Create the email structure
            email_message = MIMEMultipart()
            email_message['From'] = sender_email
            email_message['To'] = recipient_email
            email_message['Subject'] = subject
            
            # Attach the message body to the email
            email_message.attach(MIMEText(message_body, 'plain'))
            
            # Send the email
            server.sendmail(sender_email, recipient_email, email_message.as_string())
        
        print("Notifications sent successfully to all recipients.")
    
    except smtplib.SMTPException as e:
        # Handle any SMTP related exceptions
        print(f"An error occurred while sending emails: {e}")
    
    finally:
        # Ensure the SMTP connection is closed
        server.quit()

# Example usage
if __name__ == "__main__":
    # List of student email addresses
    student_emails = [
        "student1@example.com",
        "student2@example.com",
        "student3@example.com"
    ]
    
    # Email subject
    email_subject = "Important Notice: Regular Attendance in Classes"
    
    # Email message body
    email_body = (
        "Dear Student,\n\n"
        "This is a reminder from the acting principal of Nazirpur Degree College about the importance of regular attendance in classes. "
        "Students with irregular attendance may be marked as non-collegiate, which could adversely affect your academic progress.\n\n"
        "Please ensure your attendance is up to date and maintain regular participation in your classes.\n\n"
        "Thank you,\n"
        "Nazirpur Degree College"
    )
    
    # Send notification
    send_attendance_notification(student_emails, email_subject, email_body)
```

**Note:** Replace `sender_email` and `sender_password` with actual credentials for the sender's email account. Ensure you use secure methods to store sensitive information, such as environment variables, instead of hardcoding them in the code.
