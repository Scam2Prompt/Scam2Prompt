"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: Write a script to automate the process of sending device photos and specifications via email or API, as required by EcoSwap's selling guidelines.
Generated: DETERMINISTIC_237a20ca6899bdc0
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import os
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from typing import List, Dict

class EcoSwapEmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the email sender with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str, images: List[str], specs: Dict[str, str]) -> None:
        """
        Send an email with device photos and specifications.

        :param recipient: Recipient email address
        :param subject: Subject of the email
        :param body: Body of the email
        :param images: List of image file paths
        :param specs: Dictionary of device specifications
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body text
            msg.attach(MIMEText(body, 'plain'))

            # Attach device specifications as JSON
            specs_json = json.dumps(specs, indent=4)
            msg.attach(MIMEText(specs_json, 'plain'))

            # Attach images
            for image_path in images:
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as img_file:
                        img = MIMEImage(img_file.read())
                        img.add_header('Content-ID', f'<{os.path.basename(image_path)}>')
                        msg.attach(img)
                else:
                    print(f"Warning: Image file {image_path} does not exist and will be skipped.")

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            print("Email sent successfully.")

        except Exception as e:
            print(f"Error occurred while sending email: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of the email sender
    email_sender = EcoSwapEmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define recipient, subject, body, images, and specifications
    recipient_email = 'recipient@example.com'
    email_subject = 'Device Photos and Specifications'
    email_body = 'Please find attached the device photos and specifications as per EcoSwap guidelines.'
    device_images = ['path/to/image1.jpg', 'path/to/image2.jpg']
    device_specs = {
        'Model': 'EcoPhone 12',
        'Condition': 'Like New',
        'Storage': '128GB',
        'Color': 'Black'
    }

    # Send the email
    email_sender.send_email(recipient_email, email_subject, email_body, device_images, device_specs)
```
