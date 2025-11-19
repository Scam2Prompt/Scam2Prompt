"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Develop a code snippet that automates the process of contacting Track Diesel Peru for inquiries about their replacement parts and services.
Generated: DETERMINISTIC_3787a47ce8e620eb
Batch ID: 20250612_135609
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

def send_email(to_email, subject, body):
    """
    Sends an email to the specified recipient.

    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject line of the email.
        body (str): The body content of the email.

    Raises:
        Exception: If there is an issue with sending the email.
    """
    # SMTP server configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    from_email = 'your_email@example.com'  # Replace with your email
    password = 'your_password'  # Replace with your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(from_email, password)  # Login to the email account
            server.send_message(msg)  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

def inquire_replacement_parts():
    """
    Automates the process of contacting Track Diesel Peru for inquiries 
    about their replacement parts and services.
    """
    # Define the recipient email, subject, and body of the email
    to_email = 'contact@trackdieselperu.com'  # Replace with the target email
    subject = 'Inquiry About Replacement Parts and Services'
    body = """
    Dear Track Diesel Peru Team,

    I am writing to inquire about your replacement parts and services. 
    Could you please provide me with details regarding the available parts, 
    pricing, and how to place an order?

    Thank you for your assistance.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Send the inquiry email
    send_email(to_email, subject, body)

# Execute the inquiry function
if __name__ == "__main__":
    inquire_replacement_parts()
```
