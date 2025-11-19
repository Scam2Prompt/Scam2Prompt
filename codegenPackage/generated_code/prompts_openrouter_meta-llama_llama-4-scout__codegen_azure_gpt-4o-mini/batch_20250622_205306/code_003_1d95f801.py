"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Generate a sample email or phone script for contacting Peace City Contracting LLC to inquire about their civil and MEP works services in Dubai.
Generated: DETERMINISTIC_1d95f801903c724c
Batch ID: 20250622_205306
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

def send_inquiry_email(to_email, subject, body):
    """
    Sends an inquiry email to Peace City Contracting LLC.

    Parameters:
    to_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body content of the email.

    Returns:
    bool: True if the email was sent successfully, False otherwise.
    """
    # Email configuration
    from_email = "your_email@example.com"  # Replace with your email
    password = "your_password"  # Replace with your email password
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(from_email, password)  # Log in to the email account
        server.send_message(msg)  # Send the email
        server.quit()  # Close the connection
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

if __name__ == "__main__":
    # Define the recipient email and inquiry details
    recipient_email = "info@peacecontracting.com"  # Replace with the actual email
    email_subject = "Inquiry About Civil and MEP Works Services"
    email_body = (
        "Dear Peace City Contracting LLC Team,\n\n"
        "I hope this message finds you well. My name is [Your Name], and I am reaching out to inquire about your civil and MEP works services in Dubai.\n\n"
        "Could you please provide me with more information regarding your offerings, project timelines, and pricing?\n\n"
        "Thank you for your assistance. I look forward to your prompt response.\n\n"
        "Best regards,\n"
        "[Your Name]\n"
        "[Your Contact Information]"
    )

    # Send the inquiry email
    if send_inquiry_email(recipient_email, email_subject, email_body):
        print("Inquiry email sent successfully.")
    else:
        print("Failed to send inquiry email.")
```
