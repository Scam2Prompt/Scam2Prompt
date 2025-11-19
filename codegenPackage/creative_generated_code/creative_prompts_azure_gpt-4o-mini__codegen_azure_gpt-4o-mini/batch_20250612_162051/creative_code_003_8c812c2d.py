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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_confirmation_email(client_email, service_type, booking_details):
    """
    Sends a confirmation email to the client after booking a cleaning service.
    
    Parameters:
        client_email (str): The email address of the client.
        service_type (str): Type of cleaning service booked.
        booking_details (dict): Details of the booking (date, time, etc.).

    Raises:
        ValueError: If the email is invalid or if booking details are missing.
        Exception: For any other errors that may occur while sending the email.
    """

    # Validate the email address
    if '@' not in client_email:
        raise ValueError("Invalid email address provided.")
    
    # Confirm booking details are provided
    if not booking_details or not isinstance(booking_details, dict):
        raise ValueError("Invalid booking details provided.")

    # Email content
    subject = "Your Cleaning Service Confirmation"
    body = f"""
    Dear Valued Client,

    Thank you for booking our cleaning service! Here are the details of your booking:

    Service Type: {service_type}
    Booking Date: {booking_details.get('date')}
    Booking Time: {booking_details.get('time')}

    At Maria HouseKeepers, we take pride in our work, and we offer a satisfaction guarantee. 
    If you're not completely satisfied with our service, please let us know, and we will make it right.

    Thank you for choosing us!

    Best regards,
    Maria HouseKeepers Team
    """

    # Set up the email server
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587                    # Port number for SMTP
    sender_email = "no-reply@example.com"  # Replace with your sender email
    password = "your_password"          # Replace with your email account password

    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = client_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, password)

        # Send the email
        server.send_message(msg)

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
    finally:
        # Ensure the server is closed properly
        server.quit()

# Example usage
if __name__ == "__main__":
    client_email = "client@example.com"
    service_type = "Deep Cleaning"
    booking_details = {
        'date': '2023-10-30',
        'time': '10:00 AM'
    }

    try:
        send_confirmation_email(client_email, service_type, booking_details)
        print("Confirmation email sent successfully.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")
```
