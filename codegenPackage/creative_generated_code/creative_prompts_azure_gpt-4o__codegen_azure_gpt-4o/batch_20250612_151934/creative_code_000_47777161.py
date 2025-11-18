"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Write a Python script to automate the admission inquiry process for SMA Rizvi Textile Institute using the contact details provided on their website.
Generated: DETERMINISTIC_477771614e1bf9f7
Batch ID: 20250612_151934
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

# Configure logging
logging.basicConfig(
    filename='admission_inquiry.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # SMTP server for Gmail
SMTP_PORT = 587  # Port for TLS
SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email
SENDER_PASSWORD = "your_password"  # Replace with your password
INSTITUTE_EMAIL = "info@sma-rizvi.edu.pk"  # Example email address for the institute

# Email content configuration
SUBJECT = "Admission Inquiry - SMA Rizvi Textile Institute"
BODY = """
Dear Admissions Office,

I am writing to inquire about the admission process for the SMA Rizvi Textile Institute. 
Could you please provide me with details regarding the courses offered, eligibility criteria, and the application procedure?

Looking forward to your response.

Best regards,
[Your Name]
[Your Contact Information]
"""

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using the provided sender and recipient details.

    Parameters:
    sender_email (str): Email of the sender
    sender_password (str): Password of the sender's email account
    recipient_email (str): Recipient's email address
    subject (str): Subject of the email
    body (str): Body content of the email

    Returns:
    bool: True if email is sent successfully, False otherwise
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the mail server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Login to the SMTP server
        server.send_message(message)  # Send the email
        server.quit()  # Close the server connection

        logging.info(f"Email sent successfully to {recipient_email}")
        return True
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        return False
    except Exception as exp:
        logging.error(f"An unexpected error occurred: {exp}")
        return False

def main():
    """
    Main function to trigger the admission inquiry email.
    """
    logging.info("Starting the admission inquiry process...")
    success = send_email(SENDER_EMAIL, SENDER_PASSWORD, INSTITUTE_EMAIL, SUBJECT, BODY)
    if success:
        print("Admission inquiry email sent successfully!")
    else:
        print("Failed to send the admission inquiry email. Please check the logs for details.")

if __name__ == "__main__":
    main()
```
