"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Write code to generate automated email confirmations for Whirlpool appliance repair appointments, including details like appliance type (e.g., neveras, lavadoras) and technician visit date.
Generated: DETERMINISTIC_4e957c85c5ad7b73
Batch ID: 20250612_152511
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
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_confirmation_email(self, recipient_email, appliance_type, technician_name, visit_date):
        """
        Send confirmation email for appliance repair appointment.

        :param recipient_email: str, the recipient's email address
        :param appliance_type: str, type of appliance (e.g., 'neveras', 'lavadoras')
        :param technician_name: str, name of the technician
        :param visit_date: datetime, date and time of the technician's visit
        """
        # Create the email content
        subject = "Confirmation of Your Appliance Repair Appointment"
        body = f"""
        Dear Customer,

        This is a confirmation for your appliance repair appointment.

        Appliance Type: {appliance_type}
        Technician Name: {technician_name}
        Visit Date: {visit_date.strftime('%Y-%m-%d %H:%M')}

        Thank you for choosing our service!

        Best Regards,
        Whirlpool Service Team
        """

        # Setup the email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Use TLS for security
                server.login(self.username, self.password)
                server.send_message(msg)
                print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Create an instance of AppointmentEmailer
    emailer = AppointmentEmailer(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define appointment details
    recipient = "customer@example.com"
    appliance = "neveras"  # e.g., refrigerator
    technician = "John Doe"
    visit = datetime(2023, 10, 30, 14, 30)  # Scheduled visit date and time

    # Send the confirmation email
    emailer.send_confirmation_email(recipient, appliance, technician, visit)
```
