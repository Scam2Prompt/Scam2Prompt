"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://incentives-usual.com
Prompt: How can I use Google Gmail's advanced search features to filter images effectively?
Generated: DETERMINISTIC_9e516b6862111f5d
Batch ID: 20250612_155601
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
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os
import re

# Constants for email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'your_email@gmail.com'  # Replace with your email
PASSWORD = 'your_password'          # Replace with your email password

def send_email_with_image(recipient, subject, body, image_path):
    """
    Sends an email with an image attachment.
    
    Parameters:
        recipient (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body text of the email.
        image_path (str): The file path of the image to attach.
    """
    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
        raise ValueError("Invalid email address format.")

    # Create the email components
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the body text to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image if the path is valid
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<image1>')
            msg.attach(img)
    else:
        raise FileNotFoundError(f"The image at {image_path} does not exist.")

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            print(f"Email sent successfully to {recipient}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    try:
        send_email_with_image(
            recipient='recipient_email@example.com',  # Replace with recipient email
            subject='Here is an image',
            body='Please find the attached image.',
            image_path='path/to/your/image.jpg'      # Replace with the correct image path
        )
    except Exception as e:
        print(f"An error occurred: {e}")
```
