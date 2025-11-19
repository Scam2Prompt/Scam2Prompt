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
from datetime import datetime

class AppointmentEmailer:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the AppointmentEmailer with SMTP server details.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port for the SMTP server.
            username (str): The username for SMTP authentication.
            password (str): The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_confirmation_email(self, client_email, client_name, service_type, appointment_time):
        """
        Sends a confirmation email to the client after booking an appointment.

        Args:
            client_email (str): The email address of the client.
            client_name (str): The name of the client.
            service_type (str): The type of service booked.
            appointment_time (datetime): The date and time of the appointment.

        Raises:
            Exception: Raises an exception if an error occurs while sending the email.
        """
        try:
            # Create the email content
            subject = "Appointment Confirmation"
            body = f"""
            Dear {client_name},

            Thank you for booking an appointment at our art makeup salon!

            Service Type: {service_type}
            Appointment Time: {appointment_time.strftime('%Y-%m-%d %H:%M')}

            We look forward to seeing you!

            Best regards,
            Art Makeup Salon Team
            """

            # Set up the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = client_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            print("Confirmation email sent successfully.")

        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
            raise Exception("Failed to send confirmation email.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # SMTP server credentials
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of AppointmentEmailer
    emailer = AppointmentEmailer(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    
    # Client details
    client_email = 'client@example.com'
    client_name = 'John Doe'
    service_type = 'Full Makeup Session'
    appointment_time = datetime(2023, 10, 15, 14, 30)  # Example appointment time

    # Send the confirmation email
    emailer.send_confirmation_email(client_email, client_name, service_type, appointment_time)
```
