"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Create a Python script that automates the process of sending email invitations and managing RSVPs for an event, reflecting the event management solutions offered by Pozy Media.
Generated: DETERMINISTIC_54425c83a2f41d18
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_invitation_manager.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import os
from datetime import datetime
import json

# Event Invitation Manager Class
class EventInvitationManager:
    def __init__(self, event_name, event_date, event_time, sender_email, sender_password):
        """
        Initialize the Event Invitation Manager.

        Args:
        - event_name (str): The name of the event.
        - event_date (str): The date of the event.
        - event_time (str): The time of the event.
        - sender_email (str): The email of the sender.
        - sender_password (str): The password of the sender's email account.
        """
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.rsvps = {}

    def send_invitation(self, recipient_email, recipient_name):
        """
        Send an email invitation to a recipient.

        Args:
        - recipient_email (str): The email of the recipient.
        - recipient_name (str): The name of the recipient.
        """
        try:
            # Create a secure SSL context
            context = ssl.create_default_context()

            # Set up the SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                # Log in to the sender's email account
                server.login(self.sender_email, self.sender_password)

                # Create the email message
                message = MIMEMultipart()
                message["From"] = self.sender_email
                message["To"] = recipient_email
                message["Subject"] = f"Invitation to {self.event_name}"

                # Create the email body
                body = f"""
                Dear {recipient_name},

                You are cordially invited to {self.event_name} on {self.event_date} at {self.event_time}.

                Please RSVP by replying to this email.

                Best regards,
                [Your Name]
                """
                message.attach(MIMEText(body, "plain"))

                # Send the email
                server.sendmail(self.sender_email, recipient_email, message.as_string())

            print(f"Invitation sent to {recipient_email}")

        except Exception as e:
            print(f"Error sending invitation to {recipient_email}: {str(e)}")

    def manage_rsvp(self, recipient_email, rsvp_status):
        """
        Manage an RSVP for a recipient.

        Args:
        - recipient_email (str): The email of the recipient.
        - rsvp_status (str): The RSVP status ("yes" or "no").
        """
        if recipient_email in self.rsvps:
            self.rsvps[recipient_email] = rsvp_status
        else:
            self.rsvps[recipient_email] = rsvp_status

        print(f"RSVP for {recipient_email} updated to {rsvp_status}")

    def save_rsvps(self, filename):
        """
        Save the RSVPs to a JSON file.

        Args:
        - filename (str): The name of the file to save the RSVPs to.
        """
        with open(filename, "w") as file:
            json.dump(self.rsvps, file)

        print(f"RSVPs saved to {filename}")

    def load_rsvps(self, filename):
        """
        Load the RSVPs from a JSON file.

        Args:
        - filename (str): The name of the file to load the RSVPs from.
        """
        try:
            with open(filename, "r") as file:
                self.rsvps = json.load(file)

            print(f"RSVPs loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found")

def main():
    # Event details
    event_name = "Event Name"
    event_date = "2024-09-17"
    event_time = "14:00"

    # Sender's email details
    sender_email = "sender@example.com"
    sender_password = "password"

    # Create an Event Invitation Manager
    manager = EventInvitationManager(event_name, event_date, event_time, sender_email, sender_password)

    # Send invitations
    recipients = [
        {"email": "recipient1@example.com", "name": "Recipient 1"},
        {"email": "recipient2@example.com", "name": "Recipient 2"},
    ]

    for recipient in recipients:
        manager.send_invitation(recipient["email"], recipient["name"])

    # Manage RSVPs
    manager.manage_rsvp("recipient1@example.com", "yes")
    manager.manage_rsvp("recipient2@example.com", "no")

    # Save RSVPs
    manager.save_rsvps("rsvps.json")

    # Load RSVPs
    manager.load_rsvps("rsvps.json")

if __name__ == "__main__":
    main()
```
