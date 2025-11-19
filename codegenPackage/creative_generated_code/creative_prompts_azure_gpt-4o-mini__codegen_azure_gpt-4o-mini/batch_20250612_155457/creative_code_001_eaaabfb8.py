"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sensibleoptimism.com
Prompt: Write a Python script that sends a subscription email to a user, inspired by the subscription feature on the Sensible Optimism website.
Generated: DETERMINISTIC_eaaabfb85c546b8b
Batch ID: 20250612_155457
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
logging.basicConfig(level=logging.INFO)

def send_subscription_email(user_email: str, user_name: str) -> bool:
    """
    Sends a subscription email to the user.

    Parameters:
    user_email (str): The email address of the user.
    user_name (str): The name of the user.

    Returns:
    bool: True if the email was sent successfully, False otherwise.
    """

    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = "Welcome to Sensible Optimism!"
    
    # Construct the email content
    body = f"Hi {user_name},\n\nThank you for subscribing to Sensible Optimism! We're excited to have you on board.\n\nBest regards,\nThe Sensible Optimism Team"
    
    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email server
            server.send_message(msg)  # Send the email
            logging.info(f"Subscription email sent to {user_email}")
            return True
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {user_email}: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    user_email = "new_user@example.com"
    user_name = "New User"
    
    success = send_subscription_email(user_email, user_name)
    
    if success:
        print("Email sent successfully.")
    else:
        print("Email sending failed.")
```

**Note:** Please replace `your_email@example.com`, `your_password`, and `smtp.example.com` with your actual email address, password, and SMTP server information for the script to work properly.
