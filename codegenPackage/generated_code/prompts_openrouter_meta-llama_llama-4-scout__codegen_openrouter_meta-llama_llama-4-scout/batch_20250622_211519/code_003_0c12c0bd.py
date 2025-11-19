"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Create a code snippet that sends an HTML email with a custom subject and message body, using a sender email address and reply-to address, as described in the "Message Setup" section.
Generated: DETERMINISTIC_0c12c0bddcbbe1bf
Batch ID: 20250622_211519
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

def send_html_email(
    sender_email: str, 
    reply_to_email: str, 
    recipient_email: str, 
    subject: str, 
    html_message: str
):
    """
    Send an HTML email with a custom subject and message body.

    Args:
    - sender_email (str): The sender's email address.
    - reply_to_email (str): The reply-to email address.
    - recipient_email (str): The recipient's email address.
    - subject (str): The email subject.
    - html_message (str): The HTML message body.

    Raises:
    - Exception: If there's an error sending the email.
    """

    # Define the SMTP server settings
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = sender_email
    SMTP_PASSWORD = "your_smtp_password"  # Replace with your SMTP password

    try:
        # Create a message
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["Reply-To"] = reply_to_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the HTML message
        html_part = MIMEText(html_message, "html")
        message.attach(html_part)

        # Set up the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication error. Check your credentials.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    sender_email = "your_sender_email@example.com"
    reply_to_email = "your_reply_to_email@example.com"
    recipient_email = "recipient_email@example.com"
    subject = "Test HTML Email"
    html_message = """
    <html>
        <body>
            <h1>Hello,</h1>
            <p>This is a test HTML email.</p>
        </body>
    </html>
    """

    send_html_email(
        sender_email, 
        reply_to_email, 
        recipient_email, 
        subject, 
        html_message
    )
```
