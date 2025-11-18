"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Write a program to send automated email notifications using the contact email (radio.ummfm@gmail.com) for updates about UMM FM's events and broadcasts.
Generated: DETERMINISTIC_a234a7599c4d5159
Batch ID: 20250612_153225
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
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "radio.ummfm@gmail.com"  # Sender's email
EMAIL_PASSWORD = "your_password_here"   # Sender's email password (use environment variables in production)

def send_email(to_email, subject, body):
    """
    Sends an email using the specified parameters.

    :param to_email: Recipient's email address
    :param subject: Subject line of the email
    :param body: Body content of the email
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        logging.info(f"Connecting to SMTP server: {SMTP_SERVER}")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS for security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send the email
        logging.info(f"Sending email to {to_email}")
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

        # Close the connection to the server
        server.quit()
        logging.info(f"Email successfully sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
        raise

def main():
    """
    Main function to send automated email notifications.
    """
    # Example email list
    email_list = [
        "listener1@example.com",
        "listener2@example.com",
        "listener3@example.com",
    ]
    
    # Email content
    subject = "UMM FM Updates: Upcoming Events and Broadcasts"
    body = (
        "Hello,\n\n"
        "We are excited to share updates about upcoming events and broadcasts at UMM FM.\n"
        "Stay tuned for more information and check our website for details.\n\n"
        "Best regards,\n"
        "UMM FM Team"
    )

    # Send emails to all recipients in the list
    for email in email_list:
        try:
            send_email(email, subject, body)
        except Exception as e:
            logging.error(f"Error occurred while sending email to {email}: {e}")

if __name__ == "__main__":
    """
    Entry point for the program.
    """
    main()
```

**Note:** Replace `your_password_here` with the actual password for the email account, or better yet, use environment variables to store sensitive credentials securely.
