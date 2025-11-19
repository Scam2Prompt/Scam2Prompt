"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Create a Python script to send automated email notifications to users when their rental booking is confirmed, referencing the "Register" and "Login" features from the website.
Generated: DETERMINISTIC_f9214fcb135dfc7b
Batch ID: 20250612_151514
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
from email.utils import formataddr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailNotifier with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param username: The username for the SMTP server
        :param password: The password for the SMTP server
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_confirmation_email(self, recipient_email, user_name, booking_details):
        """
        Sends a confirmation email to the user.

        :param recipient_email: The email address of the recipient
        :param user_name: The name of the user
        :param booking_details: Details of the booking
        """
        try:
            # Create the email content
            subject = "Your Rental Booking is Confirmed!"
            body = f"""
            Hi {user_name},

            Thank you for your booking! Here are your booking details:
            {booking_details}

            You can manage your bookings by logging into your account:
            - Register: [Your Register Link]
            - Login: [Your Login Link]

            Best regards,
            Your Rental Service Team
            """

            # Create a multipart email
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.username, self.username))
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient_email, msg.as_string())
                logging.info(f"Confirmation email sent to {recipient_email}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Sample data for sending an email
    recipient = 'user@example.com'
    user_name = 'John Doe'
    booking_details = 'Booking ID: 12345, Date: 2023-10-01, Location: City Center'

    # Send the confirmation email
    notifier.send_confirmation_email(recipient, user_name, booking_details)
```
