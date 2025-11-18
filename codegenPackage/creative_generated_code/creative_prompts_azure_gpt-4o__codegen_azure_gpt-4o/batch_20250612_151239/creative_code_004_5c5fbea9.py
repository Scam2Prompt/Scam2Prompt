"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.kesug.com
Prompt: Write a Python script to send automated emails using a hosting service that supports multiple email accounts and Python apps, such as iFastNet.
Generated: DETERMINISTIC_5c5fbea9180c4edc
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl

# Configuration for the SMTP server
SMTP_SERVER = "smtp.ifastnet.com"  # Replace with actual SMTP server address
SMTP_PORT = 587  # Typical port for TLS
USERNAME = "your_email@ifastnet.com"  # Replace with your email address
PASSWORD = "your_password"  # Replace with your email password

def send_email(sender_email, recipient_email, subject, body, attachment_path=None):
    """
    Sends an email using the specified SMTP server.
    
    Args:
        sender_email (str): The email address of the sender.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email, plain text.
        attachment_path (str, optional): Path to a file to attach to the email. Defaults to None.
    
    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    try:
        # Create a multipart email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, "plain"))
        
        # Attach a file if specified
        if attachment_path:
            try:
                with open(attachment_path, "rb") as attachment_file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={attachment_path.split('/')[-1]}"
                )
                message.attach(part)
            except FileNotFoundError:
                print(f"Error: File not found at {attachment_path}")
                return False
        
        # Connect to SMTP server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)  # Start TLS encryption
            server.login(USERNAME, PASSWORD)  # Login to the SMTP server
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        print("Email sent successfully.")
        return True
    
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Replace the following placeholders with actual values
    sender = "your_email@ifastnet.com"
    recipient = "recipient_email@example.com"
    email_subject = "Automated Email Subject"
    email_body = "This is an automated email sent using Python."
    attachment_file_path = "/path/to/your/attachment.txt"  # Optional, set to None if no attachment
    
    # Call the function to send email
    send_email(sender, recipient, email_subject, email_body, attachment_file_path)
```
