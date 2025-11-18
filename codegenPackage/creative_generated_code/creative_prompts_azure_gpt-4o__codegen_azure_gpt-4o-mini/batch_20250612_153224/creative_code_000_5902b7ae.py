"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Write a Python script to automate sending an email to Eric Navarro using the contact information provided on his website, ensuring the email includes an attachment of a voiceover script.
Generated: DETERMINISTIC_5902b7aeae0a243a
Batch ID: 20250612_153224
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
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# Configuration for email
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Commonly used port for SMTP
USERNAME = 'your_email@example.com'  # Your email address
PASSWORD = 'your_password'  # Your email password
RECIPIENT_EMAIL = 'eric.navarro@example.com'  # Eric Navarro's email address

def send_email(subject, body, attachment_path):
    """Sends an email with the specified subject, body, and attachment."""
    
    # Create the email container
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    # Attach the body text to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file if it exists
    if attachment_path and os.path.isfile(attachment_path):
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)
    else:
        raise FileNotFoundError(f"The attachment file {attachment_path} does not exist.")

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(USERNAME, PASSWORD)  # Log in to the server
            server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {RECIPIENT_EMAIL}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Define email content
    email_subject = "Voiceover Script Submission"
    email_body = "Hi Eric,\n\nPlease find attached the voiceover script as discussed.\n\nBest regards,\nYour Name"
    attachment_file_path = 'path/to/voiceover_script.pdf'  # Path to the attachment
    
    try:
        send_email(email_subject, email_body, attachment_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
``` 

Remember to replace the SMTP_SERVER, USERNAME, PASSWORD, and RECIPIENT_EMAIL with actual values. Also, provide the correct path to the attachment file.
