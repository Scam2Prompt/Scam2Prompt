"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Write a function to send automated email notifications to members about upcoming basketball events, inspired by the announcements on the "Grad košarke" website.
Generated: DETERMINISTIC_c7b10cf8523e4cce
Batch ID: 20250612_152739
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
from email.utils import formataddr

def send_email_notification(member_email, member_name, event_details):
    """
    Sends an automated email notification to a member about an upcoming basketball event.

    Args:
        member_email (str): The recipient's email address.
        member_name (str): The recipient's name.
        event_details (dict): A dictionary containing event details such as title, date, time, and location.
                              Example: {"title": "Basketball Tournament", "date": "2023-11-04", "time": "18:00", "location": "Local Arena"}
    Returns:
        None
    """
    try:
        # Email server configuration
        smtp_server = "smtp.example.com"  # Replace with your SMTP server
        smtp_port = 587                  # Common port for SMTP (may vary depending on your server)
        sender_email = "your_email@example.com"  # Replace with your email address
        sender_name = "Basketball Event Notifications"
        sender_password = "your_password"  # Replace with your email account password

        # Create the email content
        subject = f"Upcoming Basketball Event: {event_details['title']}"
        body = (
            f"Hello {member_name},\n\n"
            f"We're excited to announce an upcoming basketball event:\n\n"
            f"Event: {event_details['title']}\n"
            f"Date: {event_details['date']}\n"
            f"Time: {event_details['time']}\n"
            f"Location: {event_details['location']}\n\n"
            f"Don't miss out! We look forward to seeing you there.\n\n"
            f"Best regards,\nGrad Košarke Team"
        )

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = member_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable encryption for secure transmission
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, member_email, msg.as_string())

        print(f"Email sent successfully to {member_email}")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {str(e)}")
    except KeyError as e:
        print(f"Missing event detail key: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    member_email = "member@example.com"
    member_name = "John Doe"
    event_details = {
        "title": "Basketball Tournament",
        "date": "2023-11-04",
        "time": "18:00",
        "location": "Local Arena"
    }
    send_email_notification(member_email, member_name, event_details)
```
