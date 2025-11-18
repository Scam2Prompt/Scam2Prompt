"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Develop a script to send automated email responses to business inquiries, using the contact details and services structure outlined by Remas Engineering Consultants.
Generated: DETERMINISTIC_407690d62a2e7db2
Batch ID: 20250612_153648
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

# Email settings
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password

# Function to send email
def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.
    
    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    """
    try:
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

# Services offered by Remas Engineering Consultants
SERVICES = {
    "structural_design": "We specialize in structural design services for residential, commercial, and industrial projects.",
    "civil_engineering": "Our civil engineering services include land development, site analysis, and stormwater management.",
    "project_management": "We provide project management services to ensure your projects are completed on time and within budget."
}

# Function to generate an email response based on inquiry
def generate_response(name, inquiry_type):
    """
    Generates an email response based on the type of inquiry.
    
    :param name: Name of the individual making the inquiry
    :param inquiry_type: Type of service inquired about (key in SERVICES dictionary)
    :return: Formatted email body as a string
    """
    if inquiry_type in SERVICES:
        return (f"Dear {name},\n\n"
                f"Thank you for reaching out to Remas Engineering Consultants.\n\n"
                f"{SERVICES[inquiry_type]}\n\n"
                f"If you have further questions, feel free to respond to this email.\n\n"
                f"Best regards,\n"
                f"Remas Engineering Consultants Team")
    else:
        return (f"Dear {name},\n\n"
                f"Thank you for your inquiry. Unfortunately, we could not identify the specific service you are looking for.\n"
                f"Please provide more details, and we will be happy to assist you.\n\n"
                f"Best regards,\n"
                f"Remas Engineering Consultants Team")

# Example usage
if __name__ == "__main__":
    # Replace with actual data from business inquiries
    inquiries = [
        {"name": "Alice", "email": "alice@example.com", "service": "structural_design"},
        {"name": "Bob", "email": "bob@example.com", "service": "civil_engineering"},
        {"name": "Charlie", "email": "charlie@example.com", "service": "unknown_service"}
    ]

    for inquiry in inquiries:
        # Prepare email details
        name = inquiry["name"]
        to_email = inquiry["email"]
        service = inquiry["service"]
        subject = "Response to Your Inquiry at Remas Engineering Consultants"
        body = generate_response(name, service)

        # Send the email
        send_email(to_email, subject, body)
```
