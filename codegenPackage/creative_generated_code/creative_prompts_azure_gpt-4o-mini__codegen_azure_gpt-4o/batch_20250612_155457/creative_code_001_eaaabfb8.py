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

# Set up logging for debugging and error tracking
logging.basicConfig(
    filename='subscription_email.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_subscription_email(user_email, user_name):
    """
    Sends a subscription email to the provided user_email address.

    Args:
        user_email (str): The recipient's email address.
        user_name (str): The name of the recipient.

    Raises:
        Exception: Raises an exception in case of an error during email sending.
    """
    try:
        # Email configuration (replace <PLACEHOLDER> values with actual credentials)
        sender_email = "your_email@example.com"  # Sender's email address
        sender_password = "your_password"  # Sender's email password
        smtp_server = "smtp.example.com"  # SMTP server address
        smtp_port = 587  # SMTP server port (TLS)

        # Subject and email message
        subject = "Welcome to Sensible Optimism!"
        body = f"""
        Hi {user_name},

        Thank you for subscribing to Sensible Optimism! We're thrilled to have you with us.
        
        Stay tuned for updates, inspiration, and insights!

        Best regards,
        The Sensible Optimism Team
        """

        # Create a MIMEText email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = user_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.send_message(message)  # Send the email

        # Log success
        logging.info(f"Subscription email successfully sent to {user_email}")
        print(f"Subscription email successfully sent to {user_email}")

    except Exception as e:
        # Log and re-raise the exception
        logging.error(f"Failed to send subscription email to {user_email}: {str(e)}")
        print(f"Failed to send subscription email to {user_email}. Check logs for details.")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        # Replace these with actual user details
        user_email = "recipient@example.com"
        user_name = "John Doe"

        send_subscription_email(user_email, user_name)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
