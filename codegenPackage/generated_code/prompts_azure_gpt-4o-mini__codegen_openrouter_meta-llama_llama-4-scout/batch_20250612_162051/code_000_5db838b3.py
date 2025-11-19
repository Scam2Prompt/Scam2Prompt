"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: Write a Python script to send an email invitation for the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan, including details about the event date, location, and entry fees.
Generated: DETERMINISTIC_5db838b3b331334e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_invitation(
    sender_email: str, 
    sender_password: str, 
    recipient_email: str, 
    event_name: str, 
    event_date: str, 
    event_location: str, 
    entry_fees: str
):
    """
    Send an email invitation for the Holy Saraswati Puja Celebration.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address.
        event_name (str): The name of the event.
        event_date (str): The date of the event.
        event_location (str): The location of the event.
        entry_fees (str): The entry fees for the event.

    Returns:
        None
    """

    # Create a message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = f"Invitation: {event_name}"

    # Event details
    event_details = f"""
Dear Valued Members,

We are pleased to invite you to the Holy Saraswati Puja Celebration organized by the India (Bengal) Cultural Association Japan.

Event Name: {event_name}
Date: {event_date}
Location: {event_location}
Entry Fees: {entry_fees}

We look forward to seeing you there.

Best regards,
[Your Name]
India (Bengal) Cultural Association Japan
"""

    # Attach the event details to the message
    message.attach(MIMEText(event_details, 'plain'))

    try:
        # Set up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    recipient_email = "recipient-email@example.com"
    event_name = "Holy Saraswati Puja Celebration"
    event_date = "2024-02-14, 10:00 AM"
    event_location = "Tokyo, Japan"
    entry_fees = "Free for members, ¥500 for non-members"

    send_email_invitation(
        sender_email, 
        sender_password, 
        recipient_email, 
        event_name, 
        event_date, 
        event_location, 
        entry_fees
    )
```
