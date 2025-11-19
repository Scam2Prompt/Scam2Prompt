"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Write a Python script that sends a confirmation email to clients after they book an appointment at an art makeup salon, ensuring it includes details like service type and appointment time.
Generated: DETERMINISTIC_722ec34015acb65f
Batch ID: 20250612_163406
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = 'your-email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your-email-password'  # Replace with your email password

def send_confirmation_email(client_name, client_email, service_type, appointment_time):
    """
    Sends a confirmation email to a client after booking an appointment.

    Args:
        client_name (str): Name of the client.
        client_email (str): Email address of the client.
        service_type (str): Type of service booked.
        appointment_time (str): Appointment date and time.
    """
    try:
        # Create the email
        subject = "Appointment Confirmation - Art Makeup Salon"
        body = f"""
        Dear {client_name},
        
        Thank you for booking an appointment at our Art Makeup Salon. Here are your appointment details:

        Service Type: {service_type}
        Appointment Time: {appointment_time}

        We look forward to seeing you!

        Best regards,
        Art Makeup Salon Team
        """

        # Set up MIME structure
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Art Makeup Salon", EMAIL_ADDRESS))
        msg['To'] = client_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, client_email, msg.as_string())
            logging.info(f"Confirmation email sent successfully to {client_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Example data
    client_name = "Jane Doe"
    client_email = "jane.doe@example.com"
    service_type = "Eyebrow Shaping"
    appointment_time = "2023-10-15 3:00 PM"

    # Send confirmation email
    send_confirmation_email(client_name, client_email, service_type, appointment_time)
```

Make sure to replace placeholders like `SMTP_SERVER`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` with your actual values before running the code.
