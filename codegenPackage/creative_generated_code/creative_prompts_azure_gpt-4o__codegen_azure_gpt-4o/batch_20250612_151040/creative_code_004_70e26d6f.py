"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Suggest a Python library for sending automated email confirmations after users book experimental electrostimulation training sessions, and write code to implement it.
Generated: DETERMINISTIC_70e26d6f8d86f2f2
Batch ID: 20250612_151040
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

# Configuration for the SMTP server
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Default SMTP port for TLS
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

def send_email_confirmation(to_email, user_name, session_details):
    """
    Sends an email confirmation for a booked session.

    Args:
        to_email (str): Recipient's email address.
        user_name (str): Name of the user booking the session.
        session_details (str): Details about the booked session.

    Returns:
        bool: True if email is sent successfully, False otherwise.
    """
    try:
        # Create a MIMEText object for the email
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Electrostimulation Training", EMAIL_ADDRESS))
        msg['To'] = to_email
        msg['Subject'] = "Session Booking Confirmation"

        # Email body content
        email_body = f"""
        Dear {user_name},

        Thank you for booking an experimental electrostimulation training session with us.

        Session Details:
        {session_details}

        If you have any questions, feel free to reach out.

        Best Regards,
        Electrostimulation Training Team
        """

        # Attach the email body to the message
        msg.attach(MIMEText(email_body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email server
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())  # Send the email

        print(f"Email successfully sent to {to_email}.")
        return True
    except Exception as e:
        # Log the error and return False
        print(f"Failed to send email to {to_email}. Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    recipient_email = "recipient_email@example.com"  # Replace with the recipient's email address
    recipient_name = "John Doe"  # Replace with the recipient's name
    session_info = "Date: 2023-10-15, Time: 10:00 AM, Location: Training Center A"  # Replace with session details
    
    send_email_confirmation(recipient_email, recipient_name, session_info)
```

**Note:** Replace `your_email@gmail.com` and `your_email_password` with your actual email credentials. Ensure you have enabled "Less Secure Apps" or an alternative method in your email provider, if necessary. Avoid hardcoding sensitive credentials in production; use environment variables or secure secrets management solutions instead.
