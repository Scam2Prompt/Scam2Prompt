"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Write code to send automated email invitations to speakers for the MCT Summit 2024, using the provided speaker call-to-action details.
Generated: DETERMINISTIC_f0f8c1d54defef99
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict
import logging

# Configure logging for debugging and tracking errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_addresses: List[str], subject: str, body: str, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
    """
    Sends an email to the specified addresses.
    
    Args:
        to_addresses (List[str]): List of recipient email addresses.
        subject (str): Subject of the email.
        body (str): Body content of the email.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP port number.
        username (str): Username for SMTP server authentication.
        password (str): Password for SMTP server authentication.

    Raises:
        Exception: Raises an exception if sending the email fails.
    """
    try:
        # Create the email container
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = ", ".join(to_addresses)
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(username, password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email
            logging.info(f"Email sent successfully to: {', '.join(to_addresses)}")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise

def create_invitation_email(speaker_details: Dict[str, str]) -> str:
    """
    Creates the email body for the speaker invitation.
    
    Args:
        speaker_details (Dict[str, str]): A dictionary containing speaker details.

    Returns:
        str: The formatted email body.
    """
    return (f"Dear {speaker_details['name']},\n\n"
            f"We are excited to invite you to be a speaker at the MCT Summit 2024. "
            f"This event will take place on {speaker_details['date']} at {speaker_details['location']}.\n\n"
            f"Details:\n"
            f"Topic: {speaker_details['topic']}\n"
            f"Duration: {speaker_details['duration']}\n\n"
            f"We hope you can join us for this exciting event!\n\n"
            f"Best regards,\n"
            f"MCT Summit Team")

def main() -> None:
    """
    Main function to send email invitations to speakers.
    """
    # Email configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    # List of speakers to invite
    speakers = [
        {"name": "Alice Johnson", "email": "alice@example.com", "date": "March 10, 2024", "location": "New York", "topic": "AI in Education", "duration": "30 minutes"},
        {"name": "Bob Smith", "email": "bob@example.com", "date": "March 10, 2024", "location": "New York", "topic": "Future of Technology", "duration": "45 minutes"}
    ]

    # Sending invitations
    for speaker in speakers:
        try:
            email_body = create_invitation_email(speaker)
            send_email([speaker["email"]], "Invitation to Speak at MCT Summit 2024", email_body, smtp_server, smtp_port, username, password)
        except Exception as e:
            logging.error(f"Error sending invitation to {speaker['name']}: {e}")

if __name__ == "__main__":
    main()
```
