"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Create a Python script that automates the process of sending email invitations and managing RSVPs for an event, reflecting the event management solutions offered by Pozy Media.
Generated: DETERMINISTIC_54425c83a2f41d18
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import os

# Configuration for SMTP server (replace with actual values)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_email_password"

# Event details
EVENT_NAME = "Pozy Media Event"
EVENT_DATE = "2023-12-15"
EVENT_TIME = "6:00 PM"
EVENT_LOCATION = "123 Main Street, Cityville"
RSVP_DEADLINE = "2023-12-10"
RSVP_EMAIL = "rsvp@example.com"

# File paths
INVITEES_FILE = "invitees.csv"
RSVP_FILE = "rsvp.csv"

def send_email(to_email, subject, body):
    """
    Sends an email using SMTP server.

    :param to_email: Recipient email address
    :param subject: Email subject
    :param body: Email body
    """
    try:
        # Create MIMEText message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)  # Secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def generate_email_body(name):
    """
    Generates the email body for the invitation.

    :param name: Recipient's name
    :return: Email body as string
    """
    return f"""Dear {name},

You are cordially invited to attend the {EVENT_NAME}!

Event Details:
Date: {EVENT_DATE}
Time: {EVENT_TIME}
Location: {EVENT_LOCATION}

Please RSVP by {RSVP_DEADLINE} to confirm your attendance by replying to this email at {RSVP_EMAIL}.

We look forward to seeing you there!

Best regards,
Pozy Media Team
"""

def send_invitations():
    """
    Reads invitees from a CSV file and sends email invitations.
    """
    try:
        if not os.path.exists(INVITEES_FILE):
            print(f"Invitees file '{INVITEES_FILE}' not found.")
            return
        
        with open(INVITEES_FILE, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row.get("Name")
                email = row.get("Email")
                if name and email:
                    email_body = generate_email_body(name)
                    send_email(email, subject=f"Invitation to {EVENT_NAME}", body=email_body)
                else:
                    print(f"Invalid entry in CSV: {row}")
    except Exception as e:
        print(f"Error while sending invitations: {e}")

def log_rsvp(name, email, response):
    """
    Logs RSVP responses to a CSV file.

    :param name: Name of the respondent
    :param email: Email of the respondent
    :param response: Response ('Accepted' or 'Declined')
    """
    try:
        is_new_file = not os.path.exists(RSVP_FILE)
        with open(RSVP_FILE, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            # Write header if it's a new file
            if is_new_file:
                csv_writer.writerow(["Name", "Email", "Response"])
            csv_writer.writerow([name, email, response])
        print(f"RSVP logged for {name} ({email}): {response}")
    except Exception as e:
        print(f"Error while logging RSVP: {e}")

def main():
    """
    Main function to automate email invitations and manage RSVPs.
    """
    print("Starting Pozy Media Event Management System...")
    send_invitations()
    # Simulating RSVP logging
    log_rsvp(name="John Doe", email="john.doe@example.com", response="Accepted")
    log_rsvp(name="Jane Smith", email="jane.smith@example.com", response="Declined")
    print("Event management tasks completed.")

if __name__ == "__main__":
    main()
```
