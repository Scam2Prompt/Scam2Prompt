"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genteparaservir.org
Prompt: Write a Python script that sends a prayer request to the Gente Para Servir contact email, incorporating the community support features highlighted on their site.
Generated: DETERMINISTIC_7f70601006cb4f0e
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with the SMTP server
SMTP_PORT = 587  # Common SMTP port for TLS
SENDER_EMAIL = 'your_email@example.com'  # Replace with your email
SENDER_PASSWORD = 'your_password'  # Replace with your email password
RECIPIENT_EMAIL = 'contact@gentepaservir.org'  # Gente Para Servir contact email

def send_prayer_request(name, message):
    """
    Sends a prayer request email to the designated recipient.

    Args:
        name (str): The name of the person sending the request.
        message (str): The content of the prayer request.

    Raises:
        Exception: Raises an exception if sending the email fails.
    """
    # Create the email message
    email_message = MIMEMultipart()
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = RECIPIENT_EMAIL
    email_message['Subject'] = 'Prayer Request from {}'.format(name)

    # Format the email body
    body = f"Name: {name}\n\nPrayer Request:\n{message}"
    email_message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the email account
            server.send_message(email_message)  # Send the email
            print("Prayer request sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise  # Re-raise the exception for further handling if necessary


if __name__ == '__main__':
    # Example usage
    try:
        user_name = input("Enter your name: ")
        prayer_message = input("Enter your prayer request: ")
        send_prayer_request(user_name, prayer_message)
    except Exception as e:
        print(f"Failed to send prayer request: {e}")
```
