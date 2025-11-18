"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taylorswiftmerchstore.net
Prompt: Develop a Python script to automate sending promotional emails for Taylor Swift Midnights Hoodies using the SendGrid API.
Generated: DETERMINISTIC_8484510fd83ce136
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sendgrid
from sendgrid.helpers.mail import Mail
from sendgrid.exceptions import SendGridException

# Load environment variables for sensitive information
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')

# Ensure necessary environment variables are set
if not SENDGRID_API_KEY or not SENDER_EMAIL:
    raise ValueError("Please set SENDGRID_API_KEY and SENDER_EMAIL in environment variables.")

def send_promotional_email(recipient_email, recipient_name):
    """
    Sends a promotional email about Taylor Swift Midnights Hoodies to the provided email address.

    Args:
        recipient_email (str): The email address of the recipient.
        recipient_name (str): The name of the recipient.

    Raises:
        ValueError: If recipient_email or recipient_name are not valid.
        SendGridException: If there is an error sending the email.
    """
    # Validate input parameters
    if not recipient_email or not isinstance(recipient_email, str):
        raise ValueError("Invalid recipient email address.")
    if not recipient_name or not isinstance(recipient_name, str):
        raise ValueError("Invalid recipient name.")

    # Create the email content
    subject = "Get Your Taylor Swift Midnights Hoodie!"
    content = f"Hello {recipient_name},\n\n" \
              "We're excited to announce our exclusive Taylor Swift Midnights Hoodies!\n" \
              "Grab yours now and show your love for Taylor!\n\n" \
              "Best,\nYour Promo Team"

    # Create a Mail object
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=content
    )

    # Initialize SendGrid client
    sg_client = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    try:
        # Send the email
        response = sg_client.send(message)
        print(f"Email sent to {recipient_email} with status code {response.status_code}")
    except SendGridException as e:
        print(f"Error sending email to {recipient_email}: {e.message}")
        raise

def main():
    # List of recipients (can be replaced with a database or external file)
    recipients = [
        {"email": "example1@mail.com", "name": "Alice"},
        {"email": "example2@mail.com", "name": "Bob"},
        # Add more recipients as needed
    ]

    # Send promotional emails
    for recipient in recipients:
        try:
            send_promotional_email(recipient['email'], recipient['name'])
        except Exception as e:
            print(f"Failed to send email to {recipient['name']}: {e}")

if __name__ == "__main__":
    main()
```
