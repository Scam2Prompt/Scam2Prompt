"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Suggest a library or API for creating and managing email marketing campaigns, and demonstrate how to use it to send promotional emails for an automotive business.
Generated: DETERMINISTIC_eec0cd58c97b00d6
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
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Email sending function
def send_promotional_email(to_email, subject, body, attachment_path=None):
    """
    Sends a promotional email with an optional attachment to the specified recipient.

    Parameters:
        to_email (str): The recipient's email address.
        subject (str): The subject line of the email.
        body (str): The body content of the email.
        attachment_path (str): The path to an attachment file (optional).
    """
    # Get email credentials from environment variables
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')

    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body message
        msg.attach(MIMEText(body, 'html'))  # Use 'html' for HTML content

        # Attach a file if provided
        if attachment_path and os.path.isfile(attachment_path):
            attachment = MIMEBase('application', 'octet-stream')
            with open(attachment_path, 'rb') as attach_file:
                attachment.set_payload(attach_file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(attachment)
        elif attachment_path:
            print(f"Warning: Attachment at '{attachment_path}' not found. Email will be sent without attachment.")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(from_email, password)
            server.send_message(msg)

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"An error occurred while sending email: {e}")

# Example usage
if __name__ == "__main__":
    recipient_email = "customer@example.com"
    email_subject = "Exclusive Offers on Our Automotive Services!"
    email_body = """
    <h1>Dear Valued Customer,</h1>
    <p>We are excited to offer you exclusive promotions on our automotive services!</p>
    <ul>
        <li>20% off on your next oil change</li>
        <li>Free tire rotation with any service</li>
        <li>Check out our new car models!</li>
    </ul>
    <p>Best Regards,<br>Your Automotive Team</p>
    """
    attachment = "path/to/attachment.pdf"  # Optional attachment path

    send_promotional_email(recipient_email, email_subject, email_body, attachment)
```

Make sure to create a `.env` file in the same directory as this script with the following contents:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
``` 

Replace `your_email@gmail.com` and `your_email_password` with your actual email credentials.
