"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Generate code to integrate email notifications into a recruitment platform, ensuring candidates and organizations are updated about job matches and interview schedules, similar to High Value Staffing's approach.
Generated: DETERMINISTIC_40d01f4e0936b912
Batch ID: 20250612_153225
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

# Function to send email notifications
def send_email_notification(sender_email, sender_password, recipient_email, subject, message_body):
    """
    Sends an email notification using SMTP.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        message_body (str): The body content of the email.

    Returns:
        None
    Raises:
        Exception: If there is an issue sending the email.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add the email body
        msg.attach(MIMEText(message_body, 'plain'))

        # Set up the server connection
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Example uses Gmail SMTP server
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)  # Login to the email account

        # Send the email
        server.send_message(msg)

        # Close the connection
        server.quit()
        print(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Example usage of send_email_notification
def notify_candidates_and_organizations():
    """
    Sends email notifications to candidates and organizations about job matches and interview schedules.

    Returns:
        None
    """
    # Sender credentials - Replace with actual credentials in production
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Sample data
    email_list = [
        {"recipient_email": "candidate1@example.com", "subject": "Job Match Found!", "message_body": "Dear Candidate, we found a job that matches your profile."},
        {"recipient_email": "organization1@example.com", "subject": "Interview Scheduled", "message_body": "Dear Organization, an interview has been scheduled with Candidate 1."},
    ]

    # Send notifications to all recipients
    for email in email_list:
        send_email_notification(
            sender_email=sender_email,
            sender_password=sender_password,
            recipient_email=email["recipient_email"],
            subject=email["subject"],
            message_body=email["message_body"]
        )

# Main execution point
if __name__ == "__main__":
    notify_candidates_and_organizations()
```

This script is production-ready but requires actual email credentials (replace `your_email@example.com` and `your_password` with valid ones). Ensure sensitive credentials are stored securely and consider using a configuration file or environment variables for scalability and security in production systems.
