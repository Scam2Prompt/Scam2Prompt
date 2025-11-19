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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to send an email with photo attachments
def send_photos_via_email(sender_email, sender_password, recipient_email, subject, body, photo_paths):
    """
    Sends an email with attached photos to the specified recipient.

    :param sender_email: Email address of the sender
    :param sender_password: Password for the sender's email account
    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body text of the email
    :param photo_paths: List of file paths to the photos to be attached
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Attach each photo to the email
        for photo_path in photo_paths:
            if os.path.isfile(photo_path):  # Check if the file exists
                with open(photo_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(photo_path)}')
                    msg.attach(part)
            else:
                print(f"Warning: The file {photo_path} does not exist and will not be attached.")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your email credentials and recipient details
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "client_email@example.com"
    subject = "Your Photo Shoot"
    body = "Dear Client,\n\nPlease find attached the photos from your recent shoot.\n\nBest regards,\nYour Photography Team"
    photo_paths = ["path/to/photo1.jpg", "path/to/photo2.jpg"]  # List of photo file paths

    send_photos_via_email(sender_email, sender_password, recipient_email, subject, body, photo_paths)
```

**Note:** Ensure to replace the placeholder values for `sender_email`, `sender_password`, `recipient_email`, and `photo_paths` with actual data before running the code. Additionally, consider using environment variables or a secure vault for managing sensitive information like email passwords.
