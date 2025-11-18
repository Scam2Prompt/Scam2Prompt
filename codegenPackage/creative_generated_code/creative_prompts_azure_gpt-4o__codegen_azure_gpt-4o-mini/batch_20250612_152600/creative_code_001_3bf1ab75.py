"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimism.rs
Prompt: Generate code using Python's `smtplib` library to send an email inquiry to "info@domainnames.rs" about purchasing the domain "optimism.rs."
Generated: DETERMINISTIC_3bf1ab7529cec606
Batch ID: 20250612_152600
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

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.

    :param sender_email: The email address of the sender.
    :param sender_password: The password for the sender's email.
    :param recipient_email: The email address of the recipient.
    :param subject: The subject of the email.
    :param body: The body content of the email.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Create a secure SSL context
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define email credentials and message details
    SENDER_EMAIL = 'your_email@gmail.com'
    SENDER_PASSWORD = 'your_password'
    RECIPIENT_EMAIL = 'info@domainnames.rs'
    SUBJECT = 'Inquiry about domain purchase'
    BODY = 'Hello,\n\nI would like to inquire about purchasing the domain "optimism.rs".\n\nThank you.\nBest regards,\nYour Name'

    # Send the email inquiry
    send_email(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, SUBJECT, BODY)
```
