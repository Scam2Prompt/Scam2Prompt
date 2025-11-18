"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Generate code to automate email notifications for donors and volunteers, referencing Youngistaan Foundation's "Donate Now" and "Join Now" functionalities.
Generated: DETERMINISTIC_a49c082ccc2a2dac
Batch ID: 20250612_153246
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
from typing import List, Dict

# Email configuration constants
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@example.com'
SMTP_PASSWORD = 'your-email-password'

# Email content templates
EMAIL_TEMPLATES = {
    "donor": {
        "subject": "Thank you for your generous donation!",
        "body": """Dear {name},

Thank you for your support of the Youngistaan Foundation. Your contribution helps us make a difference in the lives of those we serve.

If you'd like to learn more about our projects, please visit our website.

Best regards,
Youngistaan Foundation"""
    },
    "volunteer": {
        "subject": "Welcome to the Youngistaan Foundation!",
        "body": """Dear {name},

Thank you for joining us as a volunteer! We are excited to have you on board.

Please check your email regularly for updates on upcoming events and how you can contribute.

Best regards,
Youngistaan Foundation"""
    }
}


def send_email(recipient: str, name: str, category: str) -> None:
    """
    Sends an email notification to the donor or volunteer.

    :param recipient: Email address of the recipient
    :param name: Name of the recipient
    :param category: Type of notification ('donor' or 'volunteer')
    :raises ValueError: If the category is invalid
    :raises Exception: For any other errors encountered during sending
    """
    if category not in EMAIL_TEMPLATES:
        raise ValueError("Invalid category. Must be 'donor' or 'volunteer'.")

    # Prepare the email
    subject = EMAIL_TEMPLATES[category]['subject']
    body = EMAIL_TEMPLATES[category]['body'].format(name=name)

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Sending the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, recipient, msg.as_string())
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")


def notify_donors_and_volunteers(donors: List[Dict], volunteers: List[Dict]) -> None:
    """
    Sends notifications to donors and volunteers.

    :param donors: List of dictionaries containing donor information
    :param volunteers: List of dictionaries containing volunteer information
    """
    # Notify donors
    for donor in donors:
        try:
            send_email(donor['email'], donor['name'], 'donor')
        except Exception as e:
            print(f"Error sending email to donor {donor['name']}: {e}")

    # Notify volunteers
    for volunteer in volunteers:
        try:
            send_email(volunteer['email'], volunteer['name'], 'volunteer')
        except Exception as e:
            print(f"Error sending email to volunteer {volunteer['name']}: {e}")


# Example usage
if __name__ == "__main__":
    donors_list = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'}
    ]
    
    volunteers_list = [
        {'name': 'Charlie', 'email': 'charlie@example.com'},
        {'name': 'Diana', 'email': 'diana@example.com'}
    ]

    notify_donors_and_volunteers(donors_list, volunteers_list)
```
