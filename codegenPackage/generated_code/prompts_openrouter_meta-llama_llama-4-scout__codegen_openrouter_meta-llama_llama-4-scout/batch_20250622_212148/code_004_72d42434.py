"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Write a code snippet in a programming language of your choice to automate the process of sending photo shoots to clients via email, inspired by Officine dell'Immagine's client services.
Generated: DETERMINISTIC_72d42434bd36b7aa
Batch ID: 20250622_212148
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
from email.mime.text import MIMEText
from email import encoders

def send_photo_shoot_via_email(client_email, photo_shoot_folder, smtp_server, smtp_port, sender_email, sender_password):
    """
    Send a photo shoot to a client via email.

    Args:
        client_email (str): The client's email address.
        photo_shoot_folder (str): The folder containing the photo shoot.
        smtp_server (str): The SMTP server to use.
        smtp_port (int): The SMTP port to use.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Check if the photo shoot folder exists
    if not os.path.exists(photo_shoot_folder):
        print(f"Error: Photo shoot folder '{photo_shoot_folder}' does not exist.")
        return False

    # Get a list of all files in the photo shoot folder
    files = [os.path.join(photo_shoot_folder, f) for f in os.listdir(photo_shoot_folder) if os.path.isfile(os.path.join(photo_shoot_folder, f))]

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = client_email
    msg['Subject'] = 'Your Photo Shoot'

    # Create the email body
    body = 'Dear valued client,<br><br>We are pleased to share your photo shoot with you.<br><br>Please find the photos attached to this email.<br><br>Best regards,<br>Your Photographer'
    msg.attach(MIMEText(body, 'html'))

    # Attach each file to the email
    for file in files:
        attachment = open(file, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file)}')
        msg.attach(part)

    # Set up the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    text = msg.as_string()
    try:
        server.sendmail(sender_email, client_email, text)
        print(f"Email sent to {client_email} successfully.")
        return True
    except Exception as e:
        print(f"Error sending email to {client_email}: {str(e)}")
        return False
    finally:
        server.quit()

if __name__ == "__main__":
    client_email = 'client@example.com'
    photo_shoot_folder = '/path/to/photo/shoot'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'sender@example.com'
    sender_password = 'password'

    send_photo_shoot_via_email(client_email, photo_shoot_folder, smtp_server, smtp_port, sender_email, sender_password)
```
