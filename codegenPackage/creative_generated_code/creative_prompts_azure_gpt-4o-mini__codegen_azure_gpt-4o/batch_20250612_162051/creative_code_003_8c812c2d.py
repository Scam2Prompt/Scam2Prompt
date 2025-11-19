"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Develop a code snippet that sends a confirmation email to clients after they book a cleaning service, ensuring it includes details about the service type and satisfaction guarantee, as highlighted by Maria HouseKeepers.
Generated: DETERMINISTIC_8c812c2dd3da4f40
Batch ID: 20250612_162051
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

def send_confirmation_email(client_email, client_name, service_type):
    """
    Sends a confirmation email to the client after booking a cleaning service.

    Args:
        client_email (str): Email address of the client.
        client_name (str): Name of the client.
        service_type (str): Type of cleaning service booked.

    Returns:
        bool: True if email is sent successfully, False otherwise.
    """
    # Email server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "mariahousekeepers@example.com"  # Replace with actual sender email
    sender_password = "yourpassword"                # Replace with the actual password

    try:
        # Create email message
        subject = "Confirmation of Your Cleaning Service Booking"
        body = f"""
        Dear {client_name},

        Thank you for booking a cleaning service with Maria HouseKeepers!

        Service Type: {service_type}

        Your satisfaction is our top priority. If you have any questions or concerns,
        please don't hesitate to contact us.

        Best regards,
        Maria HouseKeepers Team
        """

        # Create MIME message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = client_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Log in to the server
            server.sendmail(sender_email, client_email, message.as_string())  # Send the email

        return True  # Email sent successfully

    except Exception as e:
        # Log the error and return False
        print(f"Error sending email: {e}")
        return False


# Example usage
if __name__ == "__main__":
    client_email = "client@example.com"
    client_name = "John Doe"
    service_type = "Deep Cleaning"
    
    success = send_confirmation_email(client_email, client_name, service_type)
    if success:
        print(f"Confirmation email successfully sent to {client_email}.")
    else:
        print("Failed to send confirmation email.")
```

> **Note:** Replace `sender_email` and `sender_password` with valid credentials for the email account you want to use. Ensure sensitive credentials are not hardcoded in production; use environment variables or a secrets manager instead.
