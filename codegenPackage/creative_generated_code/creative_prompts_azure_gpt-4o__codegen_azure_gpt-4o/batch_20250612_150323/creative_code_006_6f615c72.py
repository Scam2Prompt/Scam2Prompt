"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Write a script to automate sending booking confirmation emails for RIB rentals in Greece, including details like fleet name, rental dates, and departure location.
Generated: DETERMINISTIC_6f615c72a033d0cf
Batch ID: 20250612_150323
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# SMTP server configuration (example setup for Gmail's SMTP server)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-email@gmail.com"  # Replace with your email address
SMTP_PASSWORD = "your-email-password"  # Replace with your email password

# Function to send booking confirmation email
def send_booking_confirmation_email(to_email, fleet_name, rental_dates, departure_location):
    """
    Sends a booking confirmation email for RIB rentals.

    Args:
        to_email (str): Recipient's email address.
        fleet_name (str): Name of the fleet being rented.
        rental_dates (str): Rental dates in a readable format.
        departure_location (str): Departure location of the rental.
    """
    try:
        # Email subject and sender/receiver details
        subject = "Booking Confirmation for Your RIB Rental"
        sender_email = SMTP_USERNAME

        # Create the email content
        body = f"""
        Dear Customer,

        Thank you for booking with us! Here are your rental details:

        Fleet Name: {fleet_name}
        Rental Dates: {rental_dates}
        Departure Location: {departure_location}

        We look forward to serving you and hope you enjoy your experience.

        Best regards,
        RIB Rentals Greece Team
        """
        
        # Create a MIME email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            logging.info("Logged in to SMTP server successfully.")

            server.sendmail(sender_email, to_email, msg.as_string())
            logging.info(f"Booking confirmation email sent to {to_email} successfully.")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Example booking details
    recipient_email = "customer@example.com"  # Replace with the recipient's email address
    fleet = "Poseidon 500"
    dates = "April 1, 2024 - April 7, 2024"
    location = "Athens Marina"

    # Call the email sending function
    send_booking_confirmation_email(recipient_email, fleet, dates, location)
```
