"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farazhaidermusic.com
Prompt: Develop a function that sends an email update about Faraz Haider's new album releases to a list of subscribers using a mailing library.
Generated: DETERMINISTIC_18eaf1dd3df179d6
Batch ID: 20250612_162050
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
from typing import List

def send_email_update(subscribers: List[str], album_name: str, release_date: str):
    """
    Sends an email update about Faraz Haider's new album releases to a list of subscribers.
    
    Args:
        subscribers (List[str]): A list of email addresses to send the update to.
        album_name (str): The name of the new album.
        release_date (str): The release date of the new album.

    Raises:
        Exception: Raises an exception if the email fails to send due to SMTP errors.
    """
    
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    subject = f"New Album Release: {album_name}"
    
    # Create the email body
    body = f"Hello,\n\nWe are excited to announce the release of Faraz Haider's new album '{album_name}' on {release_date}.\n\nBest Regards,\nThe Music Team"
    
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = subject

    # Attach the email body to the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server connection
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Log in to the email account
            
            # Send the email to each subscriber
            for subscriber in subscribers:
                message['To'] = subscriber
                server.send_message(message)
                print(f"Email sent to: {subscriber}")
                
    except smtplib.SMTPException as e:
        # Handle SMTP exceptions
        print(f"Error occurred while sending email: {e}")
        raise Exception("Failed to send emails due to SMTP error.") from e

# Example usage (commented out for production use)
# subscribers_list = ["subscriber1@example.com", "subscriber2@example.com"]
# send_email_update(subscribers_list, "New Horizons", "2023-12-15")
```
