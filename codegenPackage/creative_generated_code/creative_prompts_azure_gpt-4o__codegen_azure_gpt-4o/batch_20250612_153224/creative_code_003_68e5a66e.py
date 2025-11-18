"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write a script using Python's `smtplib` library to send follow-up emails to customers who have requested plumbing or electrical services, referencing the services offered in Murcia.
Generated: DETERMINISTIC_68e5a66e3537552d
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.header import Header
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_email(sender_email, sender_password, recipient_email, recipient_name, service_type):
    """
    Sends a follow-up email to the customer based on the selected service type.

    :param sender_email: Email address of the sender (e.g., your company's email)
    :param sender_password: Password for the sender's email account
    :param recipient_email: Email address of the recipient (customer)
    :param recipient_name: Name of the recipient (customer's name)
    :param service_type: Type of service requested ("plumbing" or "electrical")
    """
    try:
        # Validate service type
        if service_type not in ["plumbing", "electrical"]:
            raise ValueError("Invalid service type. Must be 'plumbing' or 'electrical'.")

        # Set up the email content
        subject = f"Follow-Up: {service_type.capitalize()} Services in Murcia"
        body = (
            f"Dear {recipient_name},\n\n"
            f"Thank you for requesting our {service_type} services in Murcia. We are dedicated to providing you "
            f"the highest quality service.\n\n"
            f"If you have any questions or need to schedule an appointment, please don't hesitate to reach out.\n\n"
            f"Best regards,\nYour Company Name"
        )

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Date"] = formatdate(localtime=True)
        msg["Subject"] = Header(subject, "utf-8")
        msg.attach(MIMEText(body, "plain", "utf-8"))

        # Connect to the SMTP server and send the message
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            logging.info(f"Email successfully sent to {recipient_email}")

    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    # Replace these with valid credentials and recipient details
    sender_email = "yourcompanyemail@gmail.com"
    sender_password = "yourpassword"
    recipient_email = "customeremail@example.com"
    recipient_name = "John Doe"
    service_type = "plumbing"  # Can be "plumbing" or "electrical"

    send_email(sender_email, sender_password, recipient_email, recipient_name, service_type)
```
