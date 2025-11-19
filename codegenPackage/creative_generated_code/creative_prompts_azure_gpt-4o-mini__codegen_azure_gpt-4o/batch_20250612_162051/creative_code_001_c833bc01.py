"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkawasiollague.cl
Prompt: Write a function that sends a confirmation email to guests after they reserve a room at a hostel, including details about safety protocols.
Generated: DETERMINISTIC_c833bc0133a9dc7e
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

def send_confirmation_email(guest_email, guest_name, reservation_details, hostel_safety_protocols):
    """
    Sends a confirmation email to a guest after they reserve a room at the hostel.
    
    Args:
        guest_email (str): Email address of the guest.
        guest_name (str): Name of the guest.
        reservation_details (str): Information about the guest's reservation.
        hostel_safety_protocols (str): Details of the hostel's safety protocols.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    try:
        # Email server configuration
        smtp_server = "smtp.gmail.com"  # Use your email provider's SMTP server address
        smtp_port = 587  # SMTP port number
        sender_email = "your_email@example.com"  # Replace with your email address
        sender_password = "your_password"  # Replace with your email account password

        # Create email content
        subject = "Room Reservation Confirmation"
        body = (f"Dear {guest_name},\n\n"
                "Thank you for reserving a room at our hostel. Below are the details of your reservation:\n\n"
                f"{reservation_details}\n\n"
                "For your safety and comfort, we follow these protocols:\n\n"
                f"{hostel_safety_protocols}\n\n"
                "We look forward to hosting you!\n\n"
                "Best regards,\n"
                "The Hostel Team")

        # Create MIME message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = guest_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the server
            server.sendmail(sender_email, guest_email, message.as_string())  # Send the email

        print(f"Confirmation email sent successfully to {guest_email}.")
        return True

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        return False

# Example usage
if __name__ == "__main__":
    guest_email = "guest@example.com"
    guest_name = "John Doe"
    reservation_details = "Room: Deluxe Suite, Check-in: Oct 15, Check-out: Oct 20"
    hostel_safety_protocols = "- Regular sanitization\n- Masks required in common areas\n- Contactless check-in and check-out"

    send_confirmation_email(guest_email, guest_name, reservation_details, hostel_safety_protocols)
```
