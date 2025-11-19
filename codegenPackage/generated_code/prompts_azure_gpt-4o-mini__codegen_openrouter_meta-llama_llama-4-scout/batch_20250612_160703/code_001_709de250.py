"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Write a Python script that sends an email notification to customers after their commercial cleaning service is completed, referencing the customer satisfaction guarantee from Star Cleaning Services.
Generated: DETERMINISTIC_709de250435ffa6b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email_notification(customer_name, customer_email, service_date):
    """
    Sends an email notification to customers after their commercial cleaning service is completed.

    Args:
        customer_name (str): The name of the customer.
        customer_email (str): The email address of the customer.
        service_date (str): The date the service was completed.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Email configuration
    sender_email = "starcleaningservices@example.com"
    sender_password = "password123"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Email content
    subject = "Commercial Cleaning Service Completed - Star Cleaning Services"
    body = f"""
    Dear {customer_name},

    We hope this email finds you well. Our team at Star Cleaning Services has completed your commercial cleaning service on {service_date}.

    At Star Cleaning Services, we stand behind our work and are committed to providing exceptional service. As a reminder, we offer a customer satisfaction guarantee. If you have any concerns or would like to provide feedback, please don't hesitate to reach out.

    Thank you for choosing Star Cleaning Services.

    Best regards,
    Star Cleaning Services
    """

    try:
        # Create a message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = customer_email
        message["Subject"] = subject

        # Attach the body to the message
        message.attach(MIMEText(body, "plain"))

        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, customer_email, text)
        server.quit()

        logging.info("Email sent successfully to %s", customer_email)
        return True

    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to authenticate with the SMTP server")
        return False

    except smtplib.SMTPException as e:
        logging.error("Error sending email: %s", e)
        return False

    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        return False


if __name__ == "__main__":
    customer_name = "John Doe"
    customer_email = "johndoe@example.com"
    service_date = "2024-09-16"

    send_email_notification(customer_name, customer_email, service_date)
```
