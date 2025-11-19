"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://333club.xyz
Prompt: Write a function that sends automated reminders for birthday packages at a club, ensuring it includes details about the exclusive lineups and events every Saturday.
Generated: DETERMINISTIC_b1433aeb3c6e6a10
Batch ID: 20250612_161259
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
from datetime import datetime
from typing import List, Dict

# Define custom exception for handling email errors
class EmailError(Exception):
    pass

def send_birthday_reminders(birthday_data: List[Dict[str, str]], smtp_server: str, port: int, sender_email: str, sender_password: str):
    """
    Sends automated birthday reminders for packages at a club.

    Parameters:
    - birthday_data (List[Dict[str, str]]): A list of dictionaries containing birthday information.
      Each dictionary should have 'name', 'email', and 'event_details' keys.
    - smtp_server (str): The SMTP server address.
    - port (int): The SMTP server port.
    - sender_email (str): The sender's email address.
    - sender_password (str): The sender's email password.
    
    Raises:
    - EmailError: If there is an issue sending the email.
    """

    # Current date to check for upcoming Saturdays
    today = datetime.now()
    current_weekday = today.weekday()  # Monday is 0 and Sunday is 6
    next_saturday = today + timedelta(days=(5 - current_weekday) % 7)

    # Prepare the email content
    for person in birthday_data:
        name = person.get('name')
        email = person.get('email')
        event_details = person.get('event_details', 'Join us for an unforgettable experience!')

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = email
        message['Subject'] = f"🎉 Birthday Reminder: Exclusive Events for You!"

        body = f"""\
        Hi {name},

        Happy Birthday! 🎂 We are excited to remind you of our exclusive birthday package at the club.

        This Saturday, we will have:
        {event_details}

        We look forward to celebrating with you!

        Best Wishes,
        The Club Team
        """

        message.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(sender_email, sender_password)
                server.send_message(message)
                print(f"Reminder sent to {name} at {email}")
        except Exception as e:
            raise EmailError(f"Failed to send email to {email}: {str(e)}")

# Example usage of the function (credentials and data should be replaced with actual values)
if __name__ == "__main__":
    birthday_list = [
        {"name": "John Doe", "email": "john@example.com", "event_details": "DJ Night, Drink Specials"},
        {"name": "Jane Smith", "email": "jane@example.com"},
    ]

    try:
        send_birthday_reminders(birthday_list, "smtp.example.com", 587, "your_email@example.com", "your_password")
    except EmailError as e:
        print(e)
```
