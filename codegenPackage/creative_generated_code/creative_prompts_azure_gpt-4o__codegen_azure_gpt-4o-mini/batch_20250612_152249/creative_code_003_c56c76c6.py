"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Create a script to send automated email notifications to participants of the "Patente d'Impresa" course, using the contact form fields provided on the website.
Generated: DETERMINISTIC_c56c76c67730fe8b
Batch ID: 20250612_152249
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

# Configuration for the email server
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
SENDER_EMAIL = 'your_email@example.com'
SUBJECT = "Automated Notification for Patente d'Impresa Course"

def send_email(recipient: str, message: str) -> None:
    """Sends an email to the specified recipient with the provided message.

    Args:
        recipient (str): The email address of the recipient.
        message (str): The body of the email message.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = SUBJECT

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

def notify_participants(participants: List[Dict[str, str]]) -> None:
    """Sends notifications to a list of participants.

    Args:
        participants (List[Dict[str, str]]): List of dictionaries containing participant details.
                                               Each dictionary should have 'email' and 'name' keys.
    """
    for participant in participants:
        email = participant.get('email')
        name = participant.get('name')

        if email:
            message = f"Dear {name},\n\nThank you for registering for the 'Patente d'Impresa' course. We look forward to seeing you!\n\nBest regards,\nThe Course Team"
            send_email(email, message)
        else:
            print(f"Participant {participant} does not have a valid email address.")

if __name__ == "__main__":
    # Example list of participants (simulate data retrieval from contact form)
    participants_list = [
        {'name': 'Mario Rossi', 'email': 'mario.rossi@example.com'},
        {'name': 'Luisa Bianchi', 'email': 'luisa.bianchi@example.com'},
        # Add more participants as needed
    ]

    # Notify all participants
    notify_participants(participants_list)
```
