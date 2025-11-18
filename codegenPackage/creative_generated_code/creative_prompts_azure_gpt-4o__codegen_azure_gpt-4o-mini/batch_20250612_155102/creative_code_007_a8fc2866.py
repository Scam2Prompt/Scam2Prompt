"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardedcoin.com
Prompt: Create a script to automate the process of sending transaction screenshots and payment details via email for Guarded Ethereum ©️ cash-out services.
Generated: DETERMINISTIC_a8fc2866ff05a0fd
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def send_email(sender_email, sender_password, recipient_email, subject, body, image_paths):
    """
    Sends an email with transaction details and screenshots attached.

    :param sender_email: Email address of the sender
    :param sender_password: Password for the sender email account
    :param recipient_email: Email address of the recipient
    :param subject: Subject line of the email
    :param body: Body content of the email
    :param image_paths: List of file paths to images (screenshots)
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach each image as a separate MIMEImage object
        for image_path in image_paths:
            try:
                with open(image_path, 'rb') as image_file:
                    img = MIMEImage(image_file.read())
                    img.add_header('Content-Disposition', f'attachment; filename={Path(image_path).name}')
                    msg.attach(img)
                    logging.info(f'Attached image: {image_path}')
            except FileNotFoundError:
                logging.error(f'Image file not found: {image_path}')
                continue
            except Exception as e:
                logging.error(f'Error attaching image {image_path}: {e}')
                continue

        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Use TLS for security
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info('Email sent successfully.')

    except Exception as e:
        logging.error(f'Failed to send email: {e}')

if __name__ == "__main__":
    # User-defined parameters
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')  # Email must be set in environment
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')  # Password must be set in environment
    RECIPIENT_EMAIL = 'recipient@example.com'  # Change to the actual recipient
    SUBJECT = 'Guarded Ethereum Cash-Out Transaction'
    BODY = 'Attached are the transaction screenshots and payment details.'

    # List of paths to transaction screenshots
    IMAGE_PATHS = [
        'path/to/screenshot1.png',
        'path/to/screenshot2.png'
    ]

    # Call the function to send the email
    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, BODY, IMAGE_PATHS)
```

**Note**: Make sure to replace `recipient@example.com` and the image paths with actual values before running the code. Additionally, set the environment variables `SENDER_EMAIL` and `SENDER_PASSWORD` for authentication.
