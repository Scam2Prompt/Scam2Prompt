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
from typing import Dict, Any

def send_confirmation_email(guest_email: str, guest_name: str, room_details: Dict[str, Any], safety_protocols: str) -> None:
    """
    Sends a confirmation email to a guest after they reserve a room at a hostel.

    Parameters:
    - guest_email (str): The email address of the guest.
    - guest_name (str): The name of the guest.
    - room_details (dict): A dictionary containing details about the reserved room (e.g. room number, check-in/out dates).
    - safety_protocols (str): A string containing the safety protocols in place at the hostel.

    Raises:
    - ValueError: If the guest's email is invalid.
    - Exception: For general errors during the email sending process.
    """

    # Validate the guest's email address
    if '@' not in guest_email or '.' not in guest_email.split('@')[-1]:
        raise ValueError("Invalid email address provided.")

    # Prepare the email content
    subject = "Your Reservation Confirmation"
    body = f"Dear {guest_name},\n\n"
    body += "Thank you for choosing our hostel! Here are your reservation details:\n\n"
    body += f"Room Number: {room_details.get('room_number')}\n"
    body += f"Check-in Date: {room_details.get('check_in')}\n"
    body += f"Check-out Date: {room_details.get('check_out')}\n\n"
    body += "Safety Protocols:\n"
    body += f"{safety_protocols}\n\n"
    body += "We look forward to welcoming you!\n\nBest regards,\nThe Hostel Team"

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = 'hostel@example.com'
    msg['To'] = guest_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email using SMTP
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login('your_username', 'your_password')  # Replace with your SMTP username and password
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print("Confirmation email sent successfully.")
    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    try:
        send_confirmation_email(
            guest_email="guest@example.com",
            guest_name="John Doe",
            room_details={
                "room_number": 101,
                "check_in": "2023-10-01",
                "check_out": "2023-10-07"
            },
            safety_protocols="Masks are required in common areas. Please maintain social distancing."
        )
    except Exception as e:
        print(f"An error occurred: {e}")
```
