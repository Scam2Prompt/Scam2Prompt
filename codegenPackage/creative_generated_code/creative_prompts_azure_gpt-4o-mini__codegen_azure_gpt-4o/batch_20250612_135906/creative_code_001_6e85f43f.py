"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Write a Python script that sends an email to BCHDEkontakt@perrigo.com using SMTP, mimicking the communication methods mentioned in the Impressum of the Perrigo Claims site.
Generated: DETERMINISTIC_6e85f43f44a67818
Batch ID: 20250612_135906
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
import ssl

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.

    Args:
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email password.
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.

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

        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"  # Update if using a different SMTP server
        smtp_port = 587  # Port number for TLS
        context = ssl.create_default_context()

        # Connect to the server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the server
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send email
            print("Email sent successfully.")
    
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your email and password.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace with actual credentials and details
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_email_password"  # Replace with your email password
    recipient_email = "BCHDEkontakt@perrigo.com"  # Recipient's email address
    subject = "Subject of the Email"  # Email subject
    body = "This is the body of the email."  # Email body

    send_email(sender_email, sender_password, recipient_email, subject, body)
```

*Important Note*: Replace `your_email@gmail.com` and `your_email_password` with actual credentials. If you're using Gmail, you may need to enable "Less Secure Apps" or generate an App Password for access. Always store credentials securely and avoid hardcoding sensitive information in production environments.
