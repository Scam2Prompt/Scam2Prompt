"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Create a Python script to send automated email reminders to registered attendees of FestiVin Caraquet seminars, including details about time, location, and featured wines.
Generated: DETERMINISTIC_8314bfcf4b48d004
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
from email.utils import formataddr

# Configuration settings
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Seminar details
SEMINAR_DETAILS = {
    "title": "FestiVin Caraquet: Wines of the World",
    "date": "2023-11-12",
    "time": "18:00",
    "location": "Caraquet Cultural Center, Room A",
    "featured_wines": ["Chardonnay", "Pinot Noir", "Riesling"],
}

# List of attendees (replace with your actual attendees list)
ATTENDEES = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
]

def send_email(to_name, to_email):
    """
    Sends an automated email reminder to the specified recipient.

    :param to_name: Name of the recipient
    :param to_email: Email address of the recipient
    """
    try:
        # Create the email message
        subject = f"Reminder: {SEMINAR_DETAILS['title']}"
        body = f"""
        Hi {to_name},

        This is a friendly reminder that you are registered for the seminar "{SEMINAR_DETAILS['title']}."

        Here are the details:
        - Date: {SEMINAR_DETAILS['date']}
        - Time: {SEMINAR_DETAILS['time']}
        - Location: {SEMINAR_DETAILS['location']}
        - Featured Wines: {', '.join(SEMINAR_DETAILS['featured_wines'])}

        We look forward to seeing you there!

        Best regards,
        FestiVin Caraquet Team
        """

        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = formataddr(("FestiVin Caraquet", EMAIL_ADDRESS))
        msg['To'] = formataddr((to_name, to_email))
        msg['Subject'] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())  # Send email

        print(f"Email successfully sent to {to_name} at {to_email}.")
    except Exception as e:
        print(f"Failed to send email to {to_name} at {to_email}. Error: {e}")

def main():
    """
    Main function to send email reminders to all attendees.
    """
    for attendee in ATTENDEES:
        send_email(attendee["name"], attendee["email"])

if __name__ == "__main__":
    main()
```
