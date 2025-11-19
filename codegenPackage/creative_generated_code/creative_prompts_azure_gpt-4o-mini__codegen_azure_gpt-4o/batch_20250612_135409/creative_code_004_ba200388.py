"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extenso-mayotte.fr
Prompt: What API can I use to notify users about website maintenance updates via email?
Generated: DETERMINISTIC_ba20038817d80db5
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the use of the SendGrid API to send email notifications 
to users about website maintenance updates. Ensure you have a SendGrid account 
and API key before using this script.
"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To

# Load environment variables (for best practices, store API keys securely)
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')  # Set your SendGrid API key in the environment variable
FROM_EMAIL = os.getenv('FROM_EMAIL')  # Sender's email address
TO_EMAILS = ["user1@example.com", "user2@example.com", "user3@example.com"]  # List of recipient email addresses

def send_maintenance_email(sender_email, recipient_emails, subject, content):
    """
    Send maintenance notification email using the SendGrid API.

    Args:
        sender_email (str): Email address of the sender.
        recipient_emails (list): List of recipient email addresses.
        subject (str): Subject of the email.
        content (str): Body content of the email.

    Returns:
        None
    """
    try:
        # Initialize SendGrid Mail object
        mail = Mail(
            from_email=Email(sender_email),
            to_emails=[To(email) for email in recipient_emails],
            subject=subject,
            plain_text_content=content
        )
        
        # Send the email using the SendGrid API client
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(mail)
        
        # Log response status for debugging
        print(f"Email sent successfully. Status code: {response.status_code}")
    
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred while sending email: {e}")

if __name__ == "__main__":
    """
    Main execution block. Update subject and content to match your email notification details.
    """
    # Customize your email subject and content
    email_subject = "Website Maintenance Notification"
    email_content = (
        "Dear user,\n\n"
        "We are performing scheduled maintenance on our website from 12:00 AM to 4:00 AM UTC.\n"
        "During this time, the website may be inaccessible.\n\n"
        "Thank you for your understanding.\n\n"
        "Best regards,\nThe Website Team"
    )

    # Send notification emails
    send_maintenance_email(FROM_EMAIL, TO_EMAILS, email_subject, email_content)
```
