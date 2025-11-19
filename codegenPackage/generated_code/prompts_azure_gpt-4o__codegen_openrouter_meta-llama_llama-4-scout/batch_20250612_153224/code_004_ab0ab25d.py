"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Write a script to send automated email inquiries to Micro Rent a Car's contact email (microtours14@gmail.com) for available vehicles in Lahore.
Generated: DETERMINISTIC_ab0ab25d4eb65b57
Batch ID: 20250612_153224
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
import ssl

def send_email_inquiry():
    # Define email configuration
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    recipient_email = "microtours14@gmail.com"
    subject = "Inquiry for Available Vehicles in Lahore"

    # Define email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Email body
    body = """
    Dear Micro Rent a Car Team,

    I am writing to inquire about the availability of vehicles for rent in Lahore.
    Could you please provide me with a list of available vehicles and their rental prices?

    Thank you for your time and assistance.

    Best regards,
    [Your Name]
    """
    message.attach(MIMEText(body, "plain"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Send email using SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Incorrect email or password")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_email_inquiry()
```
