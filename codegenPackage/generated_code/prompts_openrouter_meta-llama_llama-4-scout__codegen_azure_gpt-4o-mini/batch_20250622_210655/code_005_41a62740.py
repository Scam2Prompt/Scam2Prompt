"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Create a sample email template for sending booking confirmations and reminders to customers for a cleaning services company like Maria HouseKeepers.
Generated: DETERMINISTIC_41a62740e1bc99e3
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailService with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_addresses: List[str], subject: str, body: str) -> None:
        """
        Sends an email to the specified addresses.

        :param to_addresses: List of recipient email addresses.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ", ".join(to_addresses)
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'html'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

def create_booking_confirmation_email(customer_name: str, booking_date: str, service_details: str) -> str:
    """
    Creates a booking confirmation email template.

    :param customer_name: Name of the customer.
    :param booking_date: Date of the booking.
    :param service_details: Details of the cleaning service booked.
    :return: Formatted email body as a string.
    """
    return f"""
    <html>
        <body>
            <h2>Booking Confirmation</h2>
            <p>Dear {customer_name},</p>
            <p>Thank you for choosing Maria HouseKeepers!</p>
            <p>Your booking has been confirmed for <strong>{booking_date}</strong>.</p>
            <p>Service Details:</p>
            <p>{service_details}</p>
            <p>We look forward to serving you!</p>
            <p>Best regards,<br>Maria HouseKeepers Team</p>
        </body>
    </html>
    """

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of EmailService
    email_service = EmailService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Prepare email details
    customer_name = "John Doe"
    booking_date = "2023-10-15"
    service_details = "Deep cleaning of 3-bedroom apartment."
    to_addresses = ["customer@example.com"]

    # Create email body
    email_body = create_booking_confirmation_email(customer_name, booking_date, service_details)

    # Send the email
    email_service.send_email(to_addresses, "Booking Confirmation - Maria HouseKeepers", email_body)
```
