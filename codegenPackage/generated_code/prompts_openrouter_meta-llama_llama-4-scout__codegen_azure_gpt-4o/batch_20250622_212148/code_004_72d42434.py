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
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_photo_shoot(email_recipient, subject, message_body, photo_shoot_folder, smtp_server, smtp_port, sender_email, sender_password):
    """
    Automates the process of sending photo shoots to clients via email.

    Parameters:
        email_recipient (str): The recipient's email address.
        subject (str): The subject of the email.
        message_body (str): The body of the email.
        photo_shoot_folder (str): Path to the folder containing photo shoot files.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email_recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(message_body, 'plain'))

        # Attach all files from the photo shoot folder
        for file_name in os.listdir(photo_shoot_folder):
            file_path = os.path.join(photo_shoot_folder, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    # Create a MIMEBase object for the file
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={file_name}')
                    msg.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Log in to the server
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these values with your own configuration
    email_recipient = "client@example.com"
    subject = "Your Photo Shoot"
    message_body = "Dear Client,\n\nPlease find attached the photos from your recent shoot.\n\nBest regards,\nYour Photography Team"
    photo_shoot_folder = "./photo_shoots"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"

    send_photo_shoot(email_recipient, subject, message_body, photo_shoot_folder, smtp_server, smtp_port, sender_email, sender_password)
```

**Note:** Replace placeholder values (e.g., `your_email@example.com`, `your_email_password`, `client@example.com`, etc.) with actual values before running the code. Ensure proper security practices, such as using environment variables or secure credential storage, for sensitive information like email passwords.
