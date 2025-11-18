"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Write code to send automated email notifications to property owners with updates on their rental income, similar to Inmobiliaria Capri's owner services.
Generated: DETERMINISTIC_a875cbbedf4d3a7c
Batch ID: 20250612_152924
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
from typing import List, Dict

class EmailNotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the email notification service.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The port to use for the SMTP server.
            username (str): The username for the email account.
            password (str): The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        """Send an email notification.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject of the email.
            body (str): The body content of the email.

        Raises:
            Exception: If there is an error sending the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"Email sent successfully to {to_email}")
        except Exception as e:
            print(f"Failed to send email to {to_email}: {e}")

    def notify_property_owners(self, owners: List[Dict[str, str]]) -> None:
        """Notify property owners about their rental income updates.

        Args:
            owners (List[Dict[str, str]]): A list of property owners with their email and income update details.
        """
        for owner in owners:
            email = owner.get("email")
            rental_income = owner.get("rental_income")
            property_name = owner.get("property_name")

            if email and rental_income is not None:
                subject = f"Rental Income Update for {property_name}"
                body = (
                    f"Dear Property Owner,\n\n"
                    f"We are pleased to inform you that your rental income for the property '{property_name}' "
                    f"is now updated to: ${rental_income:.2f}.\n\n"
                    f"Thank you for choosing our services!\n\n"
                    f"Best regards,\n"
                    f"Inmobiliaria Capri"
                )
                self.send_email(email, subject, body)
            else:
                print(f"Missing email or rental income for owner: {owner}")

# Example usage
if __name__ == "__main__":
    service = EmailNotificationService(
        smtp_server='smtp.example.com',
        smtp_port=587,
        username='your_email@example.com',
        password='your_password'
    )

    property_owners = [
        {"email": "owner1@example.com", "rental_income": 1200.50, "property_name": "Ocean View Apartment"},
        {"email": "owner2@example.com", "rental_income": 950.75, "property_name": "Downtown Studio"},
        {"email": "owner3@example.com", "rental_income": 1500.00, "property_name": "Suburban House"},
    ]

    service.notify_property_owners(property_owners)
```
