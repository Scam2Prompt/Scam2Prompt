"""
Generated Code Metadata:
========================
Original URL: https://perrigo-claims.info
Prompt: Write a Python script that sends an email to BCHDEkontakt@perrigo.com using SMTP, mimicking the communication methods mentioned in the Impressum of the Perrigo Claims site.
Generated: DETERMINISTIC_6e85f43f44a67818
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.

    Parameters:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Set up the SMTP server with SSL
        smtp_server = "smtp.gmail.com"  # Replace with your SMTP server if different
        smtp_port = 465  # Port for SSL
        context = ssl.create_default_context()

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these with actual values
    sender_email = "your_email@gmail.com"  # Your email address
    sender_password = "your_password"      # Your email password (use app password if using Gmail)
    recipient_email = "BCHDEkontakt@perrigo.com"  # Recipient's email address
    subject = "Test Email"
    body = "This is a test email sent using Python."

    send_email(sender_email, sender_password, recipient_email, subject, body)
```

**Note:** Replace `your_email@gmail.com` and `your_password` with your actual email credentials. If using Gmail, you may need to enable "Less secure app access" or use an app password for authentication.
