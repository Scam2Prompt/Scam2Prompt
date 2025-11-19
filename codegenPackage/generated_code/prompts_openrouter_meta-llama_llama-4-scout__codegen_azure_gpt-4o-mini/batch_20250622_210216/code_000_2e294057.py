"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python script to automate the process of sending high-resolution images to clients via email, similar to how Simon Harris sends photos to his clients, with a focus on Perth real estate photography.
Generated: DETERMINISTIC_2e294057ece5eca8
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import List

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
USERNAME = 'your_email@example.com'  # Replace with your email
PASSWORD = 'your_password'  # Replace with your email password

def send_email_with_attachments(to_email: str, subject: str, body: str, attachments: List[Path]) -> None:
    """
    Sends an email with the specified subject and body to the given recipient,
    including any specified attachments.

    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body text of the email
    :param attachments: List of file paths to attach to the email
    """
    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach each file in the attachments list
    for file_path in attachments:
        try:
            # Check if the file exists
            if not file_path.is_file():
                print(f"Warning: {file_path} does not exist and will be skipped.")
                continue
            
            # Create a MIMEBase object for the attachment
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={file_path.name}')
                msg.attach(part)
        except Exception as e:
            print(f"Error attaching file {file_path}: {e}")

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the email server
            server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """
    Main function to execute the email sending process.
    """
    # Define recipient email, subject, body, and attachments
    recipient_email = 'client@example.com'  # Replace with the client's email
    email_subject = 'Your High-Resolution Real Estate Photos'
    email_body = 'Dear Client,\n\nPlease find attached the high-resolution images from your recent shoot.\n\nBest regards,\nYour Photography Service'
    
    # Specify the directory containing the images
    images_directory = Path('path/to/images')  # Replace with the path to your images
    attachments = [images_directory / img for img in os.listdir(images_directory) if img.endswith(('.jpg', '.jpeg', '.png'))]

    # Send the email with attachments
    send_email_with_attachments(recipient_email, email_subject, email_body, attachments)

if __name__ == '__main__':
    main()
```
