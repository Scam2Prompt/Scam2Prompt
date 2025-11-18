"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Create a Python script to send automated email notifications to users when their rental booking is confirmed, referencing the "Register" and "Login" features from the website.
Generated: DETERMINISTIC_f9214fcb135dfc7b
Batch ID: 20250612_151514
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
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("email_notifications.log"), logging.StreamHandler()]
)

# Email configuration (update with actual credentials and server information)
SMTP_SERVER = "smtp.example.com"         # Replace with your SMTP server
SMTP_PORT = 587                          # Common port for SMTP
EMAIL_ADDRESS = "your_email@example.com" # Replace with your email
EMAIL_PASSWORD = "your_password"         # Replace with your email password

def send_booking_confirmation_email(to_email, user_name, booking_details):
    """
    Send an email notification for booking confirmation.

    Args:
        to_email (str): Recipient's email address.
        user_name (str): Name of the user.
        booking_details (str): Details about the booking.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = formataddr(("Rental Service", EMAIL_ADDRESS))
        message['To'] = to_email
        message['Subject'] = "Booking Confirmation"

        # Email body
        email_body = f"""
        Hello {user_name},

        Your rental booking has been confirmed! Here are the details:
        {booking_details}

        Thank you for choosing our service.

        Best regards,
        The Rental Team
        """
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, message.as_string())
            logging.info(f"Booking confirmation email sent to {to_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email to {to_email}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Simulate registration and login process
    user_email = "user_email@example.com"  # Replace with recipient email
    user_name = "John Doe"                 # Replace with user's name
    booking_details = "Rental ID: 12345, Date: 2023-10-20, Location: Downtown"  # Replace with booking details

    logging.info("Registering user...")
    # Simulate user registration (dummy logic)
    # This part could include writing the user data to a database or performing validations
    
    logging.info("Logging in user...")
    # Simulate login (dummy logic)
    # This could involve checking the database for credentials
    
    logging.info("Sending booking confirmation email...")
    send_booking_confirmation_email(user_email, user_name, booking_details)
```
