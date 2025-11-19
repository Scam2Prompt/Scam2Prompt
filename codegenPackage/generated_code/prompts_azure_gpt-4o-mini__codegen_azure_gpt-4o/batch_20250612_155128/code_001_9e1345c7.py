"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Write a Python script to automate sending service estimates for concrete cleaning and fleet washing, inspired by Klean-Pro Utah's service model.
Generated: DETERMINISTIC_9e1345c7417bb3a8
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for email configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Service estimate template
SERVICE_ESTIMATE_TEMPLATE = """
Dear {customer_name},

Thank you for considering our services at Klean-Pro Utah. Below is the estimate for your requested service:

Service Type: {service_type}
Estimated Cost: ${estimated_cost}
Details: {service_details}

If you have any questions or would like to proceed, please reply to this email or call us at (123) 456-7890.

Best regards,
Klean-Pro Utah Team
"""

def send_service_estimate(customer_email, customer_name, service_type, estimated_cost, service_details):
    """
    Sends a service estimate email to the customer.

    Args:
        customer_email (str): The customer's email address.
        customer_name (str): The customer's name.
        service_type (str): The type of service (e.g., Concrete Cleaning, Fleet Washing).
        estimated_cost (float): The estimated cost of the service.
        service_details (str): Additional details about the service.
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = customer_email
        message["Subject"] = f"Service Estimate for {service_type}"

        # Format the email body using the template
        email_body = SERVICE_ESTIMATE_TEMPLATE.format(
            customer_name=customer_name,
            service_type=service_type,
            estimated_cost=estimated_cost,
            service_details=service_details
        )
        message.attach(MIMEText(email_body, "plain"))

        # Connect to the SMTP server and send the email
        logging.info("Connecting to SMTP server...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            logging.info(f"Service estimate sent to {customer_email}")

    except Exception as e:
        logging.error(f"Failed to send service estimate: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual customer details
    customer_email = "customer@example.com"
    customer_name = "John Doe"
    service_type = "Concrete Cleaning"
    estimated_cost = 250.00
    service_details = "Includes cleaning of driveway and patio."

    send_service_estimate(customer_email, customer_name, service_type, estimated_cost, service_details)
```
