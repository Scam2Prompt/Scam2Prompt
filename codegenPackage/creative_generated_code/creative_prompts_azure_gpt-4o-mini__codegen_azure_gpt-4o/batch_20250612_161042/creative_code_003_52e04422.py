"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Create a function that sends email notifications to users who RSVP for events like those listed on the Celestia website.
Generated: DETERMINISTIC_52e04422de10c735
Batch ID: 20250612_161042
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email_notifications(event_name: str, rsvp_users: List[Dict[str, str]], sender_email: str, sender_password: str, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587) -> None:
    """
    Sends email notifications to users who RSVP'd for an event.

    Parameters:
      - event_name (str): Name of the event.
      - rsvp_users (List[Dict[str, str]]): List of dictionaries containing user details. Each dictionary should contain "name" and "email".
      - sender_email (str): Email address of the sender.
      - sender_password (str): Password for the sender email.
      - smtp_server (str): SMTP server to use for sending emails. Default is "smtp.gmail.com".
      - smtp_port (int): Port to use for the SMTP server. Default is 587.

    Returns:
      None.

    Raises:
      Exception: If there is an error in sending the email.
    """
    try:
        # Connect to the SMTP server
        logging.info("Connecting to the SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        logging.info("Successfully connected to the SMTP server.")

        # Send an email to each RSVP user
        for user in rsvp_users:
            try:
                recipient_name = user.get('name', 'User')
                recipient_email = user.get('email')
                
                if not recipient_email:
                    logging.warning(f"Missing email for user {recipient_name}. Skipping...")
                    continue

                # Create the email content
                subject = f"Reminder: Upcoming Event - {event_name}"
                body = f"Hello {recipient_name},\n\nThank you for RSVPing to the event '{event_name}'. We look forward to seeing you there!\n\nBest regards,\nCelestia Team"

                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = recipient_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))

                # Send the email
                logging.info(f"Sending email to {recipient_name} at {recipient_email}...")
                server.sendmail(sender_email, recipient_email, message.as_string())
                logging.info(f"Email successfully sent to {recipient_name}.")

            except Exception as e:
                logging.error(f"Failed to send email to {recipient_name} at {recipient_email}. Error: {e}")

        # Close the connection to the server
        server.quit()
        logging.info("Disconnected from the SMTP server.")

    except Exception as e:
        logging.error(f"Failed to send email notifications. Error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    event_name = "Celestia Stargazing Night"
    rsvp_users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": ""}  # Missing email example
    ]
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    try:
        send_email_notifications(event_name, rsvp_users, sender_email, sender_password)
    except Exception as e:
        logging.error(f"An error occurred while sending notifications: {e}")
```
