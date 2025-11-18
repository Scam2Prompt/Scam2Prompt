"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Write a script to send automated email inquiries to Micro Rent a Car's contact email (microtours14@gmail.com) for available vehicles in Lahore.
Generated: DETERMINISTIC_ab0ab25d4eb65b57
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def send_email(to_email, subject, body):
    """
    Sends an email to the specified recipient.

    Parameters:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    # Sender email credentials
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_name = "Your Name"               # Replace with your name
    sender_password = "your_password"       # Replace with your email password
    
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            server.login(sender_email, sender_password)  # Login to the server
            server.sendmail(sender_email, to_email, msg.as_string())  # Send the email
            
        print(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        return False

if __name__ == "__main__":
    # Recipient email
    recipient_email = "microtours14@gmail.com"
    
    # Email subject
    email_subject = "Vehicle Inquiry - Lahore"
    
    # Email body
    email_body = (
        "Dear Micro Rent a Car,\n\n"
        "I would like to inquire about the availability of vehicles for rent in Lahore. "
        "Could you please provide me with details regarding the available options, pricing, and terms?\n\n"
        "Thank you very much.\n\n"
        "Best regards,\n"
        "Your Name"
    )
    
    # Send the email
    send_email(to_email=recipient_email, subject=email_subject, body=email_body)
```

Make sure to replace `"your_email@example.com"` and `"your_password"` with appropriate sender email credentials. Use this script responsibly and ensure compliance with applicable laws and regulations when sending automated emails.
