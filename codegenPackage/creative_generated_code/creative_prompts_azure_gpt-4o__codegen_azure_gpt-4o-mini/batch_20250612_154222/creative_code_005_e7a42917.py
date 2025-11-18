"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audifree.duckdns.org
Prompt: Create a Python program that attaches files to emails and sets the encoding/charset options based on the specifications provided on the LuFix.to Sender v1.0 webpage.
Generated: DETERMINISTIC_e7a42917b5a3bc7b
Batch ID: 20250612_154222
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
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(smtp_server, smtp_port, username, password, to_email, subject, body, attachment_paths, charset='utf-8'):
    """
    Sends an email with attachment(s) to the specified recipient using the provided SMTP server.
    
    :param smtp_server: SMTP server address
    :param smtp_port: SMTP server port
    :param username: SMTP username
    :param password: SMTP password
    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    :param attachment_paths: List of file paths to attach
    :param charset: Character set for the email body
    """
    # Create a multipart email message
    msg = MIMEMultipart()
    
    # Set email headers
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the email body with the specified charset
    msg.attach(MIMEText(body, 'plain', charset))
    
    # Attach files
    for file_path in attachment_paths:
        try:
            # Check if the file exists
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"The file '{file_path}' does not exist.")
            
            # Create a MIMEBase object and attach the file
            with open(file_path, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                msg.attach(part)
        
        except Exception as e:
            print(f"Error attaching file '{file_path}': {e}")

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")
    
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

# Example usage:
if __name__ == "__main__":
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"
    TO_EMAIL = "recipient@example.com"
    SUBJECT = "Test Email with Attachments"
    BODY = "Please find the attached files."
    ATTACHMENTS = ["path/to/file1.txt", "path/to/file2.jpg"]

    send_email_with_attachment(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD, TO_EMAIL, SUBJECT, BODY, ATTACHMENTS)
```
