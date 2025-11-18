"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Develop a Python script to send automated email confirmations for tour reservations, referencing the reservation fields provided on the Chile Horse Riding website.
Generated: DETERMINISTIC_23d1741ef5b6849a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, Any

def send_email_confirmation(reservation: Dict[str, Any], smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str) -> None:
    """
    Sends an email confirmation for a tour reservation.

    Args:
        reservation (Dict[str, Any]): Reservation details including name, email, tour details, and date.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        smtp_user (str): SMTP username.
        smtp_password (str): SMTP password.

    Raises:
        Exception: If an error occurs while sending the email.
    """
    
    # Extract details from the reservation
    name = reservation.get("name")
    email = reservation.get("email")
    tour_details = reservation.get("tour_details")
    reservation_date = reservation.get("date")

    # Create the email content
    subject = "Your Tour Reservation Confirmation"
    body = f"""
    Dear {name},

    Thank you for your reservation! Here are your tour details:

    Tour: {tour_details}
    Reservation Date: {reservation_date}

    We look forward to seeing you!

    Best regards,
    Chile Horse Riding Team
    """

    # Set up the MIME multipart message
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
        print(f"Confirmation email sent to {email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise Exception("Could not send the email confirmation.") from e

if __name__ == "__main__":
    # Example reservation data
    reservation_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "tour_details": "Horse Riding in the Andes",
        "date": "2023-11-15"
    }

    # SMTP server configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "your_email@example.com"
    SMTP_PASSWORD = "your_email_password"

    # Send the email confirmation
    send_email_confirmation(reservation_data, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
```
