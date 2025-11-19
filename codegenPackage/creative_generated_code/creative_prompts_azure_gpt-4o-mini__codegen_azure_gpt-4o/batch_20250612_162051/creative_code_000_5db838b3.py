"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ibcaj.org
Prompt: Write a Python script to send an email invitation for the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan, including details about the event date, location, and entry fees.
Generated: DETERMINISTIC_5db838b3b331334e
Batch ID: 20250612_162051
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

def send_email_invitation(recipient_email):
    """
    Sends an email invitation for the Holy Saraswati Puja Celebration event.

    Args:
        recipient_email (str): The recipient's email address.
    """
    # Email account credentials (replace with your SMTP credentials)
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Event details
    event_title = "Holy Saraswati Puja Celebration"
    organizer = "India (Bengal) Cultural Association Japan"
    event_date = "Sunday, February 12, 2023"
    event_time = "10:00 AM to 5:00 PM"
    event_location = "Cultural Hall, Tokyo, Japan"
    entry_fee = "Free"

    # Compose the email subject and body
    subject = f"Invitation to {event_title}"
    body = f"""
    Dear Friend,

    You are cordially invited to join us for the {event_title}, organized by the {organizer}.

    Event Details:
    ----------------
    Date: {event_date}
    Time: {event_time}
    Location: {event_location}
    Entry Fee: {entry_fee}

    Please bring your family and friends along to celebrate this auspicious occasion with us.

    We look forward to seeing you there!

    Warm regards,
    {organizer}
    """
    
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure/encrypted
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Invitation email successfully sent to {recipient_email}")
    
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
if __name__ == "__main__":
    recipient = "recipient_email@example.com"  # Replace with the recipient's email
    send_email_invitation(recipient)
```

> **Note:** Replace `your_email@example.com` and `your_password` with valid sender credentials, and ensure that SMTP access is enabled for your email account. Use secure methods (e.g., environment variables or secrets management) to store sensitive information in production setups.
