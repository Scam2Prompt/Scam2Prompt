"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cometrecords.co.uk
Prompt: Create a script to automate the submission of demo tracks to Comet Records via their email (demo@cometrecord.co.uk), ensuring proper formatting and metadata inclusion.
Generated: DETERMINISTIC_8d910bb38e9cee05
Batch ID: 20250612_153246
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
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to send demo track via email
def send_demo_track(email_sender, email_password, demo_file_path, recipient_email='demo@cometrecord.co.uk'):
    """
    Sends a demo track to the specified recipient email.

    Parameters:
    email_sender (str): The sender's email address.
    email_password (str): The password for the sender's email account.
    demo_file_path (str): The path to the demo file to be sent.
    recipient_email (str): The email address of the recipient. Default is Comet Records demo email.

    Raises:
    ValueError: If the demo file path does not exist or is not a file.
    Exception: If email sending fails.
    """
    
    # Check if demo file exists
    if not os.path.isfile(demo_file_path):
        raise ValueError(f"The file {demo_file_path} does not exist or is not a valid file.")
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = recipient_email
    msg['Subject'] = "Demo Submission"
    
    # Email body
    body = """\
    Dear Comet Records Team,

    Please find attached my demo track for your consideration.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """
    msg.attach(MIMEText(body, 'plain'))

    # Attach the demo file
    with open(demo_file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(demo_file_path)}')
        msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(email_sender, email_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            print("Demo track sent successfully.")
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")

# Example usage (uncomment and fill in your details)
# send_demo_track('your_email@gmail.com', 'your_password', 'path_to_your_demo.mp3')
```
