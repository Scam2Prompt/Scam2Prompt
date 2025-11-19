"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salonlapista.com.ar
Prompt: Write a Python script that sends an email confirmation to clients after they reserve a party at Salon La Pista, using the provided email address format.
Generated: DETERMINISTIC_24d2217704019cb5
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_confirmation_email(client_email, client_name, party_date, party_time):
    """
    Sends a confirmation email to the client after they reserve a party.
    
    Args:
        client_email (str): The email address of the client.
        client_name (str): The name of the client.
        party_date (str): The date of the party.
        party_time (str): The time of the party.
    
    Raises:
        ValueError: If the email address is invalid.
        Exception: If there is an error sending the email.
    """
    
    # Validate the email address format
    if not validate_email(client_email):
        raise ValueError("Invalid email address format.")

    # Email configuration
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"          # Replace with your email password
    smtp_server = "smtp.example.com"           # Replace with your SMTP server
    smtp_port = 587                             # Port for TLS

    # Create the email content
    subject = "Party Reservation Confirmation"
    body = f"""
    Dear {client_name},

    Thank you for reserving a party at Salon La Pista!
    
    Here are your reservation details:
    - Party Date: {party_date}
    - Party Time: {party_time}

    We look forward to hosting you!

    Best regards,
    Salon La Pista Team
    """

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = client_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Setup the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info(f"Confirmation email sent to {client_email}")

    except Exception as e:
        logging.error("Error sending email: %s", e)
        raise

def validate_email(email):
    """
    Validates the email address format.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, otherwise False.
    """
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
if __name__ == "__main__":
    try:
        send_confirmation_email("client@example.com", "John Doe", "2023-12-01", "18:00")
    except Exception as e:
        logging.error("Failed to send confirmation email: %s", e)
```
