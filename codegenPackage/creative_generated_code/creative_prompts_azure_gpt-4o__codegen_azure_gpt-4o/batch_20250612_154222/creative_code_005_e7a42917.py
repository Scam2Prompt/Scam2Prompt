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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.charset import Charset, add_charset

# Set up encoding/charset options (based on LuFix.to Sender v1.0 specifications)
# Assuming charset is UTF-8 and encoding method is quoted-printable
add_charset("utf-8", Charset.QP, Charset.QP, "utf-8")

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    """
    Sends an email with an attachment, using UTF-8 charset and quoted-printable encoding.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        attachment_path (str): The file path of the attachment.

    Raises:
        Exception: Raises an exception if the email fails to send.
    """
    try:
        # Create the email message container (multipart)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add the email body with UTF-8 charset
        body_part = MIMEText(body, _charset="utf-8")
        msg.attach(body_part)

        # Attach file
        if attachment_path:
            try:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={attachment_path.split('/')[-1]}",
                    )
                    msg.attach(part)
            except FileNotFoundError:
                print(f"Error: File not found at {attachment_path}")
                return

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace with appropriate SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Error: Failed to send email. {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. {e}")


# Example usage:
if __name__ == "__main__":
    # Replace with your email credentials and email details
    sender = "youremail@example.com"
    password = "yourpassword"
    recipient = "recipient@example.com"
    email_subject = "Test Email with Attachment"
    email_body = "This is a test email with an attachment."
    file_path = "path/to/your/file.txt"  # Update with the actual file path

    send_email_with_attachment(sender, password, recipient, email_subject, email_body, file_path)
```
