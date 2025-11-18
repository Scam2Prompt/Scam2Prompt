"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Write a script to automate email communication for a flip-flop manufacturing company, including templates for product inquiries, order confirmations, and technical support.
Generated: DETERMINISTIC_35741130c6f2c719
Batch ID: 20250612_152109
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

# Configuration for SMTP
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
SMTP_USERNAME = "your_email@example.com"  # Replace with your email address
SMTP_PASSWORD = "your_password"  # Replace with your email password

# Email templates
EMAIL_TEMPLATES = {
    "product_inquiry": """
Dear {recipient_name},

Thank you for your interest in our flip-flop products. Please let us know if you have any specific questions or if you'd like to receive further details about our offerings.

Best regards,
{sender_name}
Flip-Flop Manufacturing Team
""",
    "order_confirmation": """
Dear {recipient_name},

Your order has been successfully placed! Thank you for choosing our flip-flops. Your order details are as follows:
Order Number: {order_number}
Estimated Delivery Date: {delivery_date}

Please feel free to reach out to us for any inquiries regarding your order.

Best regards,
{sender_name}
Flip-Flop Manufacturing Team
""",
    "technical_support": """
Dear {recipient_name},

We received your technical support request regarding your flip-flops. Please provide additional details about your issue, or let us know how we can assist you further.

Best regards,
{sender_name}
Flip-Flop Manufacturing Team
"""
}

def send_email(recipient_email, subject, template_key, template_data):
    """
    Sends an email using the specified template and data.

    Args:
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        template_key (str): Key to identify the email template.
        template_data (dict): Data to populate the email template.
    """
    try:
        # Validate template key
        if template_key not in EMAIL_TEMPLATES:
            raise ValueError(f"Invalid template key: {template_key}")

        # Populate template with data
        template = EMAIL_TEMPLATES[template_key]
        email_body = template.format(**template_data)

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SMTP_USERNAME
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(email_body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Log in to SMTP server
            server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())  # Send email

        print(f"Email successfully sent to {recipient_email}")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define recipient and template data
    recipient_email = "customer@example.com"
    subject = "Order Confirmation"
    template_key = "order_confirmation"
    template_data = {
        "recipient_name": "John Doe",
        "order_number": "12345",
        "delivery_date": "2023-11-15",
        "sender_name": "Flip-Flop Manufacturing Team"
    }

    # Send the email
    send_email(recipient_email, subject, template_key, template_data)
```
