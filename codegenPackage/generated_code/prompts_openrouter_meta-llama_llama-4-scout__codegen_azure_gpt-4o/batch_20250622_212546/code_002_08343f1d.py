"""
Generated Code Metadata:
========================
Original URL: https://esperai.com
Prompt: Write a Python script to automate sending an email to DomainModern@gmail.com with a sales inquiry about the domain esperai.com.
Generated: DETERMINISTIC_08343f1d184187d2
Batch ID: 20250622_212546
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

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Sender's email credentials (replace with your own credentials)
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"

    # Recipient's email address
    recipient_email = "DomainModern@gmail.com"

    # Email subject and body
    subject = "Sales Inquiry: Domain esperai.com"
    body = (
        "Hello,\n\n"
        "I am interested in purchasing the domain esperai.com. "
        "Could you please provide more details regarding its availability and pricing?\n\n"
        "Thank you,\n"
        "Best regards,\n"
        "Your Name"
    )

    # Send the email
    send_email(sender_email, sender_password, recipient_email, subject, body)
```

**Note:** Replace `your_email@gmail.com` and `your_email_password` with your actual email credentials. Ensure you have enabled "Less secure app access" or use an app-specific password if using Gmail.
