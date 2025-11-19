"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://handyfix.co.nz
Prompt: Write a Python script that sends an email request to Handyfix for a handyman job, using the provided contact details and service requirements.
Generated: DETERMINISTIC_86fab430257aa604
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, body, smtp_server, smtp_port, from_email, password):
    """
    Sends an email using the provided SMTP details.

    Parameters:
    - to_email (str): Recipient email address.
    - subject (str): Subject of the email.
    - body (str): Email body content.
    - smtp_server (str): SMTP server hostname.
    - smtp_port (int): SMTP server port.
    - from_email (str): Sender's email address.
    - password (str): Sender's email password.

    Returns:
    - None
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.set_content(body)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure (TLS)
            server.login(from_email, password)  # Authenticate with the server
            server.send_message(msg)  # Send the email
            print("Email successfully sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Handyfix contact details
    handyfix_email = "contact@handyfix.com"
    
    # Email details
    subject = "Request for Handyman Service"
    body = (
        "Dear Handyfix,\n\n"
        "I would like to request a handyman service. Below are my details and requirements:\n\n"
        "Name: John Doe\n"
        "Phone: 123-456-7890\n"
        "Address: 123 Main Street, Springfield\n"
        "Service Required: Plumbing repair in the kitchen.\n"
        "Preferred Date and Time: 15th October 2023, 10:00 AM\n\n"
        "Please let me know if this can be scheduled.\n\n"
        "Best regards,\n"
        "John Doe"
    )
    
    # Sender email credentials
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"        # Replace with your email password
    
    # SMTP server configuration (example for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Send the email
    send_email(handyfix_email, subject, body, smtp_server, smtp_port, sender_email, sender_password)
```
