"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherealspamassagetherapist.com
Prompt: Develop a script that sends a confirmation email to clients who book a myofascial release session at Ethereal Spa.
Generated: DETERMINISTIC_aa0b03077b415f4a
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to send a confirmation email to clients who book a myofascial release session at Ethereal Spa.
This script uses the built-in smtplib library for sending emails.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirmation_email(client_email, client_name, booking_date_time):
    """
    Sends a confirmation email to the client after booking a session.
    
    Args:
        client_email (str): Email address of the client.
        client_name (str): Full name of the client.
        booking_date_time (str): Scheduled date and time of the session.
    
    Returns:
        None
    """
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'  # Replace with your email
    sender_password = 'your_password'  # Replace with your email password (or use app-specific password)

    try:
        # Create the email content
        subject = "Ethereal Spa - Booking Confirmation"
        body = f"""
        Dear {client_name},

        Thank you for booking a myofascial release session at Ethereal Spa. 
        Here are your session details:

        Date and Time: {booking_date_time}

        Please arrive 10 minutes early to ensure a smooth check-in process.

        We look forward to seeing you!

        Best regards,
        Ethereal Spa Team
        """

        # Create MIME email object
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = client_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Login to SMTP server
            server.sendmail(sender_email, client_email, email_message.as_string())  # Send email

        print(f"Confirmation email sent successfully to {client_email}.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email. SMTP error occurred: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Replace these details with actual client information
    client_email = "client@example.com"
    client_name = "Jane Doe"
    booking_date_time = "2023-11-01 3:00 PM"

    send_confirmation_email(client_email, client_name, booking_date_time)
```

**Note**: 
- Replace `your_email@gmail.com` and `your_password` with actual credentials. If using Gmail, ensure less secure app access is enabled or use an app password.
- Use environment variables or a secure vault for storing credentials in production environments to ensure security.
