"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Write a code snippet that automates the process of scheduling a consultation with a family law attorney, similar to the services offered by Majeli Avocat in Nantes.
Generated: DETERMINISTIC_05d717cccd31b54a
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ConsultationScheduler:
    def __init__(self, attorney_email, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initializes the ConsultationScheduler with attorney's email and SMTP server details.
        
        :param attorney_email: Email address of the attorney
        :param smtp_server: SMTP server address for sending emails
        :param smtp_port: SMTP server port
        :param smtp_user: SMTP username
        :param smtp_password: SMTP password
        """
        self.attorney_email = attorney_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def schedule_consultation(self, client_email, consultation_date):
        """
        Schedules a consultation by sending an email to the attorney.
        
        :param client_email: Email address of the client
        :param consultation_date: Date and time for the consultation
        :raises ValueError: If the consultation date is in the past
        """
        if consultation_date < datetime.datetime.now():
            raise ValueError("Consultation date must be in the future.")

        subject = "New Consultation Request"
        body = f"Client Email: {client_email}\nConsultation Date: {consultation_date.strftime('%Y-%m-%d %H:%M:%S')}"

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = self.attorney_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
            print("Consultation scheduled successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Configuration for the attorney's email and SMTP server
    ATTORNEY_EMAIL = "attorney@example.com"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "your_email@example.com"
    SMTP_PASSWORD = "your_password"

    # Create an instance of the ConsultationScheduler
    scheduler = ConsultationScheduler(ATTORNEY_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Schedule a consultation
    client_email = "client@example.com"
    consultation_date = datetime.datetime(2023, 12, 1, 14, 0)  # Example date: December 1, 2023, at 2:00 PM

    try:
        scheduler.schedule_consultation(client_email, consultation_date)
    except ValueError as ve:
        print(f"Error: {ve}")
```
