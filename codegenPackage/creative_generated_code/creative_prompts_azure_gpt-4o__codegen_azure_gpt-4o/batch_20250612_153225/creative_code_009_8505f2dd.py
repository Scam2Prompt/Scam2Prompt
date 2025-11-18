"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Write a Python script to send automated email responses to inquiries received via the contact form on the website, using the email address "contact@maraboutreconnu.com."
Generated: DETERMINISTIC_8505f2dd783354f2
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for email setup
SMTP_SERVER = 'smtp.gmail.com'  # Update this if using a different SMTP server
SMTP_PORT = 587                 # Port for TLS
EMAIL_ADDRESS = 'contact@maraboutreconnu.com'  # Sender email address
EMAIL_PASSWORD = 'your_password_here'          # Replace with the actual password or use environment variables for security

def send_email(to_address, subject, message_body):
    """
    Sends an automated email response.

    Args:
        to_address (str): Recipient's email address.
        subject (str): Subject of the email.
        message_body (str): Body of the email.

    Returns:
        bool: True if email was sent successfully, False otherwise.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Initiate TLS encryption
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the SMTP server
        
        # Send the email
        server.send_message(msg)
        logging.info(f"Email sent successfully to {to_address}")
        
        # Quit the server
        server.quit()
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {to_address}: {e}")
        return False

def main():
    """
    Main function to send automated email responses.
    """
    # Example inquiry
    inquiries = [
        {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'Hello, I am interested in learning more about your services.'
        },
        # Add more inquiries as needed
    ]

    # Define the automated response message
    response_message = (
        "Dear {name},\n\n"
        "Thank you for contacting us! We have received your inquiry and will get back to you shortly.\n\n"
        "Best regards,\n"
        "Marabout Reconnu Team"
    )

    # Process each inquiry
    for inquiry in inquiries:
        recipient_email = inquiry['email']
        recipient_name = inquiry['name']
        subject = "Thank you for your inquiry"

        # Personalize the message
        personalized_message = response_message.format(name=recipient_name)
        
        # Send the email
        send_email(recipient_email, subject, personalized_message)

if __name__ == '__main__':
    main()
```

> **Note**: Replace `your_password_here` with your actual email password or consider using environment variables and secure methods like OAuth2 for better security.
