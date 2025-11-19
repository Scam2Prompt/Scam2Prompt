"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Write a Python script that sends an email notification to customers after their commercial cleaning service is completed, referencing the customer satisfaction guarantee from Star Cleaning Services.
Generated: DETERMINISTIC_709de250435ffa6b
Batch ID: 20250612_160703
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration constants
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

def send_email(customer_email, customer_name, service_date):
    """
    Sends an email notification to the customer after their cleaning service is completed.
    
    Parameters:
        customer_email (str): The customer's email address.
        customer_name (str): The customer's name.
        service_date (str): The date of the cleaning service.
    
    Returns:
        None
    """
    try:
        # Create the email message
        subject = "Thank You for Using Star Cleaning Services!"
        body = f"""
        Dear {customer_name},

        We hope you are satisfied with the cleaning service provided on {service_date}.
        At Star Cleaning Services, customer satisfaction is our top priority, and we stand by our guarantee to ensure high-quality service every time.

        If you have any feedback or concerns, please do not hesitate to reach out to us.

        Thank you for choosing Star Cleaning Services!
        Best regards,
        The Star Cleaning Services Team
        """

        # Create a MIMEText object for the email
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = customer_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, customer_email, message.as_string())
        logging.info(f"Email successfully sent to {customer_email}")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the server connection is closed
        server.quit()


# Example usage of the send_email function
if __name__ == "__main__":
    # Replace with actual customer details
    customer_email = "customer_email@example.com"
    customer_name = "John Doe"
    service_date = "2023-10-27"

    send_email(customer_email, customer_name, service_date)
```
